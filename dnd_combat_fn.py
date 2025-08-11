import copy
from dnd_python_classes import Player, Monster, Announcer
import dnd_spells
import dnd_tools
import math
import random
import re

SQUARE_SIZE = 5
SIZE_ORDER = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
MOVE_OPTIONS = {
    "W": (0, 1),   # Up
    "S": (0, -1),  # Down
    "A": (-1, 0),  # Left
    "D": (1, 0),   # Right
}


def dice(sides):
    return random.randint(1, sides)

def roll(dice_roll):
    if isinstance(dice_roll, str) and dice_roll.strip().isdigit():
        dice_roll = f"{dice_roll.strip()}d1"
    else:
        dice_roll = dice_roll.replace(" ", "") #removes spaces, makes parsing easier
    pattern = r"(\d+)d(\d+)([+-]\d+)?"
    match = re.match(pattern, dice_roll)

    num_dice = int(match.group(1))
    dice_type = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    total = sum(dice(dice_type) for _ in range(num_dice)) + modifier
    return total

def crit(dice_roll, announcer):
    if isinstance(dice_roll, str) and dice_roll.strip().isdigit():
        dice_roll = f"{dice_roll.strip()}d1"
    else:
        dice_roll = dice_roll.replace(" ", "") #removes spaces, makes parsing easier
    pattern = r"(\d+)d(\d+)([+-]\d+)?"
    match = re.match(pattern, dice_roll)

    num_dice = int(match.group(1))
    dice_type = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    damage_dice_roll = dice(dice_type)
    total = sum(int(dice_type) for _ in range(num_dice)) + modifier + damage_dice_roll
    print(f"Full Powered Die: {int(dice_type)*num_dice}, Modifier: {modifier}, Exta Damage Dice: {damage_dice_roll}")
    return total

def nat1(attacker, target, announcer, attack_data, current_turn, weapon_name = None):
    announcer.announce("critical_fail")
    critcard = random.randint(1, 8)
    print(f"Critcard was {critcard}") #debug
    if ((critcard == 1) and (attacker.nat1choice == True)):
    #This is meant to be the Crit Card system, but for now, just a damage die will be removed
        # Use Damage Components if available
        attack_data = attack_data.get('Effect', attack_data)
        damage_components = attack_data.get("Damage Components")
        if damage_components:
            # Picking a random component to fumble with
            fumble_component = random.choice(damage_components)
            dice_str = fumble_component.get("Dice", "0")
            damage_type = fumble_component.get("Type", "Unknown")
            dmg = roll(dice_str)
            print(f"{attacker.name} accidentally hits itself for {dmg} {damage_type} damage!")
            attacker.take_damage(dmg, damage_type, announcer)
        else:
            # Fallback to old logic
            dice_str = attack_data.get("Damage", "1")
            damage_type = attack_data.get("Damage Type", "Bludgeoning")

            # Handle scaling for players
            if isinstance(attacker, Player):
                scaling = attack_data.get("Effect", {}).get("Scaling", {})
                dice_str = scaling.get(str(attacker.level), dice_str)

            dice_str = dice_str.replace(" ", "")
            match = re.match(r"(\d+)d(\d+)([+-]\d+)?", dice_str)
            if match:
                dice_type = int(match.group(2))
                dmg = dice(dice_type)
            else:
                dmg = 1  # Fallback

            print(f"{attacker.name} hits itself for {dmg} {damage_type} damage!")
            attacker.take_damage(dmg, damage_type, announcer)

        # 🎯 Apply any Active Effects to the attacker
        if "Active Effects" in attack_data:
            for effect in attack_data["Active Effects"]:
                effect_data = effect["Effect"]
                if "Conditions" in effect_data:
                    condition = effect_data["Conditions"]
                    if "Booming Blade" in condition["Name"]:
                        condition_to_apply = {
                            "Name": f"{condition["Name"]} (Movement)",
                            "Damage": condition["MovementScaling"].get(str(attacker.level), 0), #Fix this, needs to have the max_level instead of attacker.level
                            "Trigger": condition.get("Trigger", "Move"),
                            "Source": attacker,
                            "Expires": "StartOfSourceTurn",
                            "Duration": condition.get("Duration", 1),
                            "Applied": current_turn,
                        }
                        attacker.conditions.append(condition_to_apply)
                        print(f"{attacker.name} is affected by {condition_to_apply['Name']}!")    
    elif ((critcard == 2) or (critcard == 3)):
        if weapon_name:
            print(f"{attacker.name} missed and dropped their weapon.")
            attacker.disarmed = True
            attacker.disarmed_item = None

            for e in attacker.equipment:
                if e["Name"] == weapon_name:
                    attacker.mainhand = None
                    attacker.disarmed_item = e
                    attacker.equipment.remove(e)
                    break
        else:
            print(f"{attacker.name} is lucky — no weapon to drop!")
        
    elif ((critcard == 5) or (critcard == 6)):
        print(f"{attacker.name} missed and opened themselves up to an opportunity attack from {target.name}, if they are within range.")
        opportunity_attack(target, attacker, announcer, current_turn)

    elif critcard == 7:
        print(f"{attacker.name} missed and falls prone.")
        condition_to_apply = {
            "Name": "Prone",
            "Source": attacker,
            "Target": attacker,
            "Expires": "Stand",
            "Applied": current_turn,
        }
        attacker.conditions.append(condition_to_apply)         

def apply_damage(target, announcer, spell, caster, half=False):
    scaling_raw = spell.get("Effect", {}).get("Scaling", {})
    scaling = {int(k): v for k, v in scaling_raw.items()}
    caster_level = caster.level  # Or caster.spellcasting_level
    max_level = max([lvl for lvl in scaling if lvl <= caster_level], default=None)

    if max_level:
        if "Toll the Dead" in spell['Name']:
            if target.currenthitpoints < target.hitpoints:
                #hurt_scaling = spell.get("Effect", {}).get("HurtScaling", {})
                #print(f"The target is hurt, meaning scaling changes, it is now: \n-{'\n-'.join(f'{hsk}:{hsv}' for hsk, hsv in hurt_scaling.items())}") #debug
                damage_roll = spell['Effect']['HurtScaling'][str(max_level)]
                #print(f"Dice roll is now {damage_roll}") #debug
            else:
                damage_roll = spell['Effect']['Scaling'][str(max_level)]
        else:
            damage_roll = spell['Effect']['Scaling'][str(max_level)]
        dmg = roll(damage_roll)
        if half:
            damage_roll = damage_roll // 2
        damage_type = spell["Effect"]["Damage Type"]
        print(f"{target.name} takes {dmg} {damage_type} damage.")
        target.take_damage(dmg, damage_type, announcer)

def process_spell_effects(target, spell, caster, current_turn):
    spell_ae = spell.get("Active Effects", [])
    #print(f"After attacking while the weapon is shillelagh'd, in process_spell_effects, our active effect is {spell_ae}")
    if "Chill Touch" in spell['Name']:
        target.no_healing = True
        condition_to_apply = {
            "Name": "Chill Touch (can't regain hp)",
            "Source": caster,
            "Target": target,
            "Applied": current_turn,
            "Expires": "StartOfSourceNextTurn"
        }
        target.conditions.append(condition_to_apply)
        print(f"{target.name} can't regain hp until the end of {caster.name}'s next turn")
        if "Undead" in target.type:
            target.disadvantage_against[caster.name] = True
            condition_to_apply = {
                "Name": f"Chill Touch (Undead - Disadvantage on attack rolls against {caster.name})",
                "Source": caster,
                "Target": target,
                "Applied": current_turn,
                "Expires": "EndOfSourceNextTurn"
            }   
            target.conditions.append(condition_to_apply)
            print(f"{target.name} has disadvantage on attack rolls against {caster.name} until the end of {caster.name}'s next turn.")           
    
    #Firebolt ignites anything flammable that isnt worn/carried

    if "Frostbite" in spell['Name']:
        print(f"{target.name} has disadvantage on next weapon attack roll until the end of its next turn.")
        target.disadvantage = True
        condition_to_apply = {
            "Name": "Disadvantage on next weapon attack roll",
            "Source": caster,
            "Target": target,
            "Expires": "EndOfTargetTurn",
            "Applied": current_turn,            
        }
        target.conditions.append(condition_to_apply)    

    if any("Green-Flame Blade" in spell.get('Name') for spell in spell_ae):
        print(f"Fire jumps off the weapon and hits an enemy within 5ft of {target.name}.")
        print("More happens at higher levels.")

    if "Lightning Lure" in spell['Name']:
        print(f"{target.name} will be pulled up to 10ft towards you in a straight line")
        #When a map is implemented, this effect will be coded
    
    if "Infestation" in spell['Name']:
        print(f"{target.name} is infested, and will be forced to move 5ft, unwillingly, in a random cardinal direction.")
        #When a map is implemented, this effect will be coded, roll a d4 and they move 5ft North(1), South(2), East(3), or West(4)
        #ONLY if it can move, and it has 5ft of proper movement; if way is blocked then no movement
    
    if "Mind Sliver" in spell['Name']:
        print(f"{target.name} has to subtract a d4 from its next saving throw it makes before the end of my next turn.")
        condition_to_apply = {
            "Name": "Mind Sliver (D4 from NEXT Saving Throw)",
            "Source": caster,
            "Target": target,
            "Expires": "EndOfSourceNextTurn",
            "Applied": current_turn,
        }
        target.conditions.append(condition_to_apply)

    if "Ray of Frost" in spell['Name']:
        print(f"{target.name}'s speed is reduced by 10ft until start of my next turn.")
        target.speed['Walk'] -= 10
        condition_to_apply = {
            "Name": "Ray of Frost (speed reduction)",
            "Source": caster,
            "Target": target,
            "Expires": "StartOfSourceNextTurn",
            "Applied": current_turn,
        }
        target.conditions.append(condition_to_apply)
    
    if "Sapping Sting" in spell['Name']:
        #This spell, and several others, will not be available until all wizard sublasses are coded in, only available to Chron... and Grav... subclasses
        print(f"{target.name} is knocked prone.")
        condition_to_apply = {
            "Name": "Prone",
            "Source": caster,
            "Target": target,
            "Expires": "Stand",
            "Applied": current_turn,
        }
        target.conditions.append(condition_to_apply) 

    if "Shocking Grasp" in spell['Name']:
        print(f"{target.name} can't take reactions until the start of its next turn.")
        condition_to_apply = {
            "Name": "Shocking Grasp (can't take reactions)",
            "Source": caster,
            "Target": target,
            "Expires": "StartOfTargetTurn",
            "Applied": current_turn,
        }
        target.conditions.append(condition_to_apply) 

    if "Thorn Whip" in spell['Name']:
        if SIZE_ORDER.index(target.size) <= SIZE_ORDER.index("Large"):
            print(f"{target.name} is caught by the Thorn Whip and is pulled up to 10ft closer.")
            #When a map is implemented, this effect will be coded
    
    if "Vicious Mockery" in spell['Name']:
        print(f"{target.name} has disadvantage on the next attack roll before the end of its turn.")
        target.disadvantage = True
        condition_to_apply = {
            "Name": "Vicious Mockery (disadvantage)",
            "Source": caster,
            "Target": target,
            "Expires": "EndOfTargetTurn",
            "Applied": current_turn,
        }
        target.conditions.append(condition_to_apply)         

    

def apply_special_effects(caster, target, spell):
    extra = spell.get("ExtraEffect")
    if extra:
        print(f"Extra Effect: {extra}")
        # Optional: parse or queue this for a future effect system        
         
def cleanup_expired_effects(creature, current_round): #Put this at the end of the creature's turn
    for effect in creature.conditions[:]:
        if effect.get("Duration_rounds") is not None:
            if current_round >= effect["Applied_on_round"] + effect["Duration_rounds"]:
                if effect["Type"] == "Resistance":
                    for dmg_type in effect["Resistances"]:
                        creature.resistances.remove(dmg_type)
                    print(f"{creature.name}'s resistance to {', '.join(effect['Resistances'])} has ended.")
                creature.conditions.remove(effect)       

def advance_turn(combat_state):
    combat_state["Turn_index"] = (combat_state["Turn_index"] + 1) % len(combat_state["Participants"])

    # If we wrapped around to the first participant again, a round has passed
    if combat_state["Turn_index"] == 0:
        combat_state["Global_turn_counter"] += 1       

def cast_spell(caster, target, announcer, current_turn, home_team, opponent_team, init_tracker, spl_key):
    if spl_key == "Breath Weapon":
        spell = caster.actions[spl_key]
    else:
        spell = caster.spelllist[spl_key]
    print(f"Spell is {spell}") #debug
    save_type = spell.get("Save")
    flavor = spell.get("Flavor")
    if save_type:
        save_dc_mod = spell['Modifier']
        if spl_key == "Breath Weapon":
            save_dc = 8 + math.floor((caster.ability_scores[save_dc_mod] - 10)/2) + caster.profbonus
        else:
            save_dc = 10 + math.floor((caster.ability_scores[save_dc_mod] - 10)/2) + caster.profbonus

        dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0),target.saving_throws[f"{save_type} ST"])    
        if any("Mind Sliver" in c.get("Name") for c in target.conditions):
            print(f"Unfortunately {target.name} has Mind Sliver, therefore they have to subtract a d4 from their roll, or from {dice_roll}.")
            deduction = dice(4)
            dice_roll -= deduction
            print(f"The roll is now {dice_roll}")
        print(f"{target.name} rolls a {dice_roll} {save_type} save vs DC {save_dc}")

        if dice_roll >= save_dc:
            if spell.get('Level', None) == 0:
                print(f"{target.name} saves!")
                return #just ends
            else:
                print(f"{target.name} Saved, but still takes half damage!")
                apply_damage(target, announcer, spell, caster, half=True)
        else:
            print(f"{target.name} fails the save!")
            apply_damage(target, announcer, spell, caster)
            process_spell_effects(target, spell, caster, current_turn)
    elif flavor:
        print(f"This spell, {spell['Name']}, is a flavor spell.")             
    elif spell['Effect']['Type'] == 'Player Buff':
        if 'Resistance' in spell['Effect']: #if a spell gives you resistances, I feel like this is a very niche case
            resistances = spell["Effect"]["Resistance"]
            target.resistances += resistances
            for res in resistances:
                target.conditions.append({
                    "Name": f"Resistance to {res}",
                    "Type": "Resistance",
                    "Source": caster,
                    "Target": target,
                    "Expires": "EndOfSourceNextTurn",
                    "Applied": current_turn,
                })
            print(f"{target.name} gains resistance to {', '.join(spell['Effect']['Resistance'])} until the end of their next turn.")       

        elif "Guidance" in spell['Name']:
            print(f"{spell['Name']} is being cast on {target.name}")
            print(f"Until concentration is broken or this is used, {target.name} can add a d4 to any ability check (not attack rolls or saves).")
            condition_to_apply = {
                "Name": "Guidance (d4 to ability check)",
                "Type": "Buff",
                "Source": caster,
                "Target": target,
                "Expires": "OneMinute",
                "Applied": current_turn
            }
            target.conditions.append(condition_to_apply)
            print(f"{caster.name} has given {target.name} guidance!")
        elif "Resistance" in spell['Name']:
            print(f"{spell['Name']} is being cast on {target.name}")
            print(f"Until concentration is broken or this is used, {target.name} can add a d4 to any saving throw (not attack rolls or ability checks).")
            condition_to_apply = {
                "Name": "Resistance (d4 to saving throw)",
                "Type": "Buff",
                "Source": caster,
                "Target": target,
                "Expires": "OneMinute",
                "Applied": current_turn
            }
            target.conditions.append(condition_to_apply) 
        elif "Spare the Dying" in spell['Name']:
            if target.type not in ["Construct", "Undead"]:
                for c in target.conditions:
                    if c['Name'] == "Unconscious":
                        print(f"{target.name} is stable!")
                        target.conditions.remove(c)
        elif "True Strike" in spell['Name']:
            caster.advantage_against[target.name] = True
            print(f"As long as you maintain concentration, you have advantage against {target.name} until the end of your next turn.")
            condition_to_apply = {
                "Name": f"True Strike (advantage against {target.name})",
                "Source": caster,
                "Target": target,
                "Expires": "EndOfSourceNextTurn",
                "Applied": current_turn
            }
            caster.conditions.append(condition_to_apply) 

    elif spell['Effect']['Type'] == 'Weapon Buff':
        attacks = list(caster.attacksspellcasting.keys())
        #print(f"Current atks before buffing: {attacks}") #debug
        if "Shillelagh" in spell['Name']:
            attacks_shill = []
            for atk in attacks:
                if ("Club" in atk) or ("Quarterstaff" in atk):
                    attacks_shill.append(atk)
            #print(f"Done adding attacks, we have: {attacks_shill}") #debug
            if attacks_shill != []:
                while True:
                    try:
                        print("0 - Random")
                        for idx, wa in enumerate(attacks_shill, 1):
                            print(f"{idx} - {wa}")
                        choice = int(input(f"Choose which weapon to cast {spell['Name']} on. "))
                        if choice == 0:
                            selected_weapon_name = random.choice(attacks_shill)
                        elif 1 <= choice <= len(attacks_shill):
                            selected_weapon_name = attacks_shill[choice - 1]
                        else:
                            print("Invalid choice, please choose a valid option.")
                            continue

                        selected_weapon = caster.attacksspellcasting[selected_weapon_name]
                        #print(f"Selected weapon is: \n{selected_weapon}") debug
                        if not selected_weapon.get('Attack Bonus'):
                            selected_weapon['Attack Bonus'] = selected_weapon['Damage Bonus'] + (caster.profbonus if selected_weapon['Proficient'] == True else 0)                
                    
                        # Ensure Active Effects list exists
                        if "Active Effects" not in selected_weapon:
                            selected_weapon["Active Effects"] = []

                        # Add the spell's weapon buff effect
                        selected_weapon["Active Effects"].append({
                            "Type": "Condition",
                            "Name": f"{spell['Name']} (Modify)",
                            "Effect": spell.get("Effect", {}),
                            "Expires": spell.get("Effect", {}).get("Conditions", {}).get("Expires", "StartOfSourceTurn"),
                            "Applied": current_turn,
                            "Source": caster
                        })
                        print(f"After applying {spell['Name']}, our weapon looks like: \n{selected_weapon}") #debug
                        selected_weapon["Old Damage"] = selected_weapon["Damage"]
                        parts = selected_weapon["Damage"].split('d', 1)
                        parts[1] = 8
                        selected_weapon["Damage"] = f"{str(parts[0])+'d'+str(parts[1])}"
                        selected_weapon["Old Attack Bonus"] = selected_weapon["Attack Bonus"] #This is a problem
                        selected_weapon["Attack Bonus"] = selected_weapon["Spell Mod"]
                        selected_weapon["Old Damage Bonus"] = selected_weapon["Damage Bonus"]
                        selected_weapon["Damage Bonus"] = selected_weapon["Spell Mod"]
                        if "Magical" not in selected_weapon["Properties"]:
                            selected_weapon["Properties"].append('Magical')
                        #print(f"{spell['Name']} has been applied to {selected_weapon_name}.")
                        #print(f"Weapon after applying: {selected_weapon}")
                        break  # ✅ Break AFTER applying the effect
                    except ValueError:
                        print("Invalid input. Please enter a number.")
        else:
            all_valid_weapons = set(
                list(dnd_tools.simple_weapons.keys()) +
                list(dnd_tools.martial_weapons.keys()) +
                list(dnd_tools.firearms.keys())
            )
            attacks_melee = []
            for atk in attacks:
                attack_data = caster.attacksspellcasting[atk]
                attack_type = attack_data.get("Attack Type", '')
                if attack_type == "Melee Weapon":
                    attacks_melee.append(atk)
            weaponattacks = [atk for atk in attacks_melee if atk in all_valid_weapons]
            while True:
                try:
                    print("0 - Random")
                    for idx, wa in enumerate(weaponattacks, 1):
                        print(f"{idx} - {wa}")
                    choice = int(input(f"Choose which weapon to cast {spell['Name']} on. "))
                    if choice == 0:
                        selected_weapon_name = random.choice(weaponattacks)
                    elif 1 <= choice <= len(weaponattacks):
                        selected_weapon_name = weaponattacks[choice - 1]
                    else:
                        print("Invalid choice, please choose a valid option.")
                        continue

                    selected_weapon = caster.attacksspellcasting[selected_weapon_name]
                    if not selected_weapon.get('Attack Bonus'):
                        selected_weapon['Attack Bonus'] = selected_weapon['Damage Bonus'] + (caster.profbonus if selected_weapon['Proficient'] == True else 0)

                    # Ensure Active Effects list exists
                    if "Active Effects" not in selected_weapon:
                        selected_weapon["Active Effects"] = []

                    # Add the spell's weapon buff effect
                    if "Booming Blade" in spell['Name']:
                        selected_weapon["Active Effects"].append({
                            "Type": "Condition",
                            "Name": f"{spell['Name']} (Movement)",
                            "Effect": spell.get("Effect", {}),
                            "Duration": spell.get("Effect", {}).get("Duration", 1),
                            "Expires": spell.get("Effect", {}).get("Expires", "StartOfSourceTurn"),
                            "Applied": current_turn,
                            "Source": caster
                        })

                        print(f"{spell['Name']} has been applied to {selected_weapon_name}.")
                        break  # ✅ Break AFTER applying the effect
                    elif "Green-Flame Blade" in spell['Name']:
                        selected_weapon["Active Effects"].append({
                            "Type": "Condition",
                            "Name": f"{spell['Name']}",
                            "Effect": spell.get("Effect", {}),
                            "Expires": spell.get("Effect", {}).get("Expires", "StartOfSourceTurn"),
                            "Applied": current_turn,
                            "Source": caster
                        })
                        print(f"{spell['Name']} has been applied to {selected_weapon_name}.")
                        break  # ✅ Break AFTER applying the effect                    
                except ValueError:
                    print("Invalid input. Please enter a number.")
        perform_attack(caster, target, announcer, current_turn, home_team, opponent_team, init_tracker, WeaponorSpell="Weapon", attack_key = selected_weapon_name)
    elif spell['Effect']['Type'] == 'Self Buff':
        print("You channel primal magic to cause your teeth or fingernails to sharpen, ready to deliver a corrosive attack.")
        scaling = spell.get("Effect", {}).get("Scaling", {})
        int_level_scaling = {int(k): v for k, v in scaling.items()}
        max_level = max([k for k in int_level_scaling if k <= caster.level], default=None)
        modifier = spell.get('Modifier')
        hit_mod = math.floor((caster.ability_scores[modifier] - 10)/2) + caster.profbonus
        caster.attacksspellcasting["Primal Savagery"] = {
            'Name' : "Primal Savagery",
            'Attack Bonus': hit_mod,
            'Attack Type': 'Melee Spell Attack',
            'Damage' : f"{scaling[str(max_level)]}",
            'Damage Type' : "Acid",
        }        
        perform_attack(caster, target, announcer, current_turn, home_team, opponent_team, init_tracker, WeaponorSpell="Weapon", attack_key = "Primal Savagery")
        print("Your teeth or fingernails return to normal after the attack.")
        del caster.attacksspellcasting["Primal Savagery"]
    else:
        #No save, like most cantrips or magic missile
        perform_attack(caster, target, announcer, current_turn, home_team, opponent_team, init_tracker, WeaponorSpell="Spell", attack_key = spl_key)
    apply_special_effects(caster, target, spell)

def apply_weapon_buff_damage(target, announcer, condition, caster):
    scaling = condition.get("Scaling", {})
    caster_level = caster.level
    max_level = max([lvl for lvl in scaling if lvl <= caster_level], default=None)

    if max_level:
        damage_roll = dice(scaling[max_level])
        damage_type = condition.get("Damage Type", "force")  # fallback
        print(f"{target.name} takes {damage_roll} {damage_type} damage from {condition['Name']}.")
        target.take_damage(damage_roll, damage_type, announcer)

def cast_weapon_buff_spells(caster, spell, combat_state):
    attacks = list(caster.attacksspellcasting.keys())
    all_valid_weapons = set(dnd_tools.simple_weapons + dnd_tools.martial_weapons + dnd_tools.firearms)
    weaponattacks = [atk for atk in attacks if atk in all_valid_weapons] #Fix this, should all include the attack details
    for weapon in weaponattacks:
        weapon_name = weapon["Name"]
        print(f"Weapon is {weapon_name}")
    if not weaponattacks:
        print("No valid weapons to cast this spell on!")
        return
    
    while True:
        try:
            print("0 - Random")
            for idx, wa in enumerate(weaponattacks, 1):
                print(f"{idx} - {wa}")
            choice = int(input(f"Choose which weapon to cast {spell['Name']} on: "))
            if choice == 0:
                selected_weapon_name = random.choice(weaponattacks)
            elif 1 <= choice <= len(weaponattacks):
                selected_weapon_name = weaponattacks[choice - 1]
            else:
                print("Invalid choice, please choose a valid option.")
                continue

            selected_weapon = caster.attacksspellcasting[selected_weapon_name]

            # Add Active Effects list if not already present
            if "Active Effects" not in selected_weapon:
                selected_weapon["Active Effects"] = []

            # Add the spell effect to the weapon
            weapon_effect = {
                "Type": "Condition",
                "Name": spell["Name"],
                "Source": caster,
                "Effect": spell.get("Effect", {}),
                "Duration": spell.get("Effect", {}).get("Duration", 1),
                "Expires": spell.get("Effect", {}).get("Expires", "AfterHit"),
            }
            print(f"Information on {selected_weapon_name} is {selected_weapon['Active Effects']}")


            selected_weapon["Active Effects"].append(weapon_effect)

            print(f"{spell['Name']} has been cast on {selected_weapon_name}!")
            return selected_weapon_name  # Return the name to be used in perform_attack

        except ValueError:
            print("Invalid input, please enter a number.")

def apply_weapon_buff_damage(target, announcer, condition, caster):
    scaling = condition.get("MovementScaling", {})
    caster_level = caster.level
    max_level = max([lvl for lvl in scaling if lvl <= caster_level], default=None)

    if max_level:
        damage_roll = dice(scaling[max_level])
        damage_type = condition.get("Damage Type", "force")  # fallback
        print(f"{target.name} takes {damage_roll} {damage_type} damage from {condition['Name']}.")
        target.take_damage(damage_roll, damage_type, announcer)

def snap_to_grid(value, grid_size=5):
    return round(value / grid_size) * grid_size

#Collision Check
def is_square_occupied(grid_x, grid_y, all_combatants, creature_attempting=None):
    tiny_occupants = 0

    for c in all_combatants:
        occupied = occupied_squares(c)
        if (grid_x, grid_y) in occupied:
            if c.size == "Tiny":
                tiny_occupants += 1
            else:
                # If any non-Tiny is already there, it's fully occupied
                return True

    # If a Tiny creature is trying to move here
    if creature_attempting and creature_attempting.size == "Tiny":
        return tiny_occupants >= 4  # max 4 tiny creatures
    else:
        # If anything is here (Tiny or not), non-Tiny can't enter
        return tiny_occupants > 0

def occupied_squares(creature):
    x, y = creature.position
    return get_occupied_squares(x, y, creature.size)    

def random_location_within_speed(center, speed, grid_size=5):
    angle = random.uniform(0, 2 * math.pi)
    radius = random.uniform(0, speed)
    dx = radius * math.cos(angle)
    dy = radius * math.sin(angle)
    
    new_x = snap_to_grid(center[0] + dx, grid_size)
    new_y = snap_to_grid(center[1] + dy, grid_size)
    return (new_x, new_y)       

def perform_attack(attacker, target, announcer, current_turn, home_team, opponent_team, init_tracker, WeaponorSpell = None, attack_key = None):
    if WeaponorSpell == "Weapon":
        if isinstance(attacker, Player):
            if attack_key == None:
                print(f"Choose an attack to use against {target.name}")
                atk_key = pick_weapon(attacker)
            else:
                atk_key = attack_key
        else:
            atk_key = attack_key #check this
            print(f"Attack key is {atk_key}") 
        attack_data = attacker.attacksspellcasting[atk_key]
        weapon_attack(attacker, atk_key, target, announcer, current_turn, home_team, opponent_team, init_tracker, attack_data = attack_data)
        
    if WeaponorSpell == "Spell":
        spell_attack(attacker, attack_key, target, announcer, current_turn, home_team, opponent_team, init_tracker)

def pick_weapon(attacker):
    attacks = list(attacker.attacksspellcasting.keys())
    weaponattacks = [atk for atk in attacks if atk in (dnd_tools.simple_weapons or dnd_tools.martial_weapons or dnd_tools.firearms)]
    while True:
        try:
            print("0 - Random Attack")
            for idx, key in enumerate(weaponattacks, 1):
                atk = attacker.attacksspellcasting[key]
                if atk['Proficient'] == True :
                    atk['Attack Bonus'] = atk['Damage Bonus'] + attacker.profbonus
                else:
                    atk['Attack Bonus'] = atk['Damage Bonus']
                print(f"{idx} - {atk['Name']} ({atk['Attack Bonus']} to hit) | {atk['Damage']} {atk['Damage Type']} ({'Proficient' if atk['Proficient'] else 'Not Proficient'})")
            atk_choice = int(input("Choose an attack. "))
            if atk_choice == 0:
                atk_key = random.choice(weaponattacks)
                break
            elif 1 <= atk_choice <= len(weaponattacks):
                atk_key = weaponattacks[atk_choice - 1]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input, try again.")
    return atk_key


def weapon_attack(attacker, atk_key, target, announcer, current_turn, home_team, opponent_team, init_tracker, attack_data = None):   
    if isinstance(attacker, Player):
        if attack_data is None:
            attack_data = attacker.attacksspellcasting[atk_key]
        hit_mod = attack_data.get('Attack Bonus', 0)
        attack_roll1 = dice(20)
        attack_roll2 = dice(20)
        if ((attacker.advantage == True) and (attacker.disadvantage == False)) or (attacker.advantage_against.get(f'{target.name}') == True):
            attack_roll = max(attack_roll1, attack_roll2)
            print(f"{attacker.name} has advantage, atk was {attack_roll1} before, now it is {attack_roll}!")
        elif ((attacker.disadvantage == True) and (attacker.advantage == False)) or (attacker.disadvantage_against.get(f'{target.name}') == True):
            attack_roll = min(attack_roll1, attack_roll2)
            print(f"{attacker.name} has disadvantage, atk was {attack_roll1} before, now it is {attack_roll}.")
        else:
            print(f"{attacker.name} rolls normally.")
            attack_roll = attack_roll1            
        to_hit_roll = attack_roll + hit_mod
        print(f"To hit, you got a {attack_roll} + {hit_mod}, for a total of {to_hit_roll}, against {target.name}'s AC of {target.armor_class}")

        if attack_roll == 1:
            print("Natural 1! You fumble!")
            nat1(attacker, target, announcer, attack_data, current_turn, weapon_name=atk_key)
        elif attack_roll == 20:
            print("Crit! Auto-hit, rolling crit damage...")
            dmg = crit(attack_data['Damage'], announcer)
            damage_type = attack_data['Damage Type']
            attack_data_str = "\n".join(f"{key}: {value}" for key, value in attack_data.items())
            if "Active Effects" in attack_data:
                apply_weapon_condition(attacker, attack_data, target, current_turn)            
            print(f"{attacker.name} crits {target.name} with {attack_data['Name']}, dealing {dmg} {damage_type} damage!")
            target.take_damage(dmg, damage_type, announcer)
            process_effects(attack_data, attacker, target, current_turn)   
        elif attack_roll + hit_mod >= target.armor_class:
            dmg = roll(attack_data['Damage'])
            damage_type = attack_data['Damage Type']
            attack_data_str = "\n".join(f"{key}: {value}" for key, value in attack_data.items())
            if "Active Effects" in attack_data:
                apply_weapon_condition(attacker, attack_data, target, current_turn)               
            print(f"{attacker.name} hits {target.name} with {attack_data['Name']}, dealing {dmg} {damage_type} damage, weapon_attack the first time!")
            target.take_damage(dmg, damage_type, announcer)
            process_effects(attack_data, attacker, target, current_turn)   
        else:
            print(f"{attacker.name} missed {target.name}")        
    else: #The only other one is Monster for now
        if atk_key == "Multiattack":            
            multi = attacker.actions[atk_key]
            sequence = multi.get("Sequence", [])
            # If the sequence is a list of sequences (random pick)
            if sequence and isinstance(sequence[0], list):
                sequence = random.choice(sequence)

            print(f"Sequence is: {sequence}")
            for sub_action in sequence:  # List like ["Bite", "Claw"]
                print(f"{attacker.name} uses {sub_action} as part of Multiattack!")
                # 🐊 Giant Crocodile special case: skip Tail if target is Grappled by this crocodile
                if sub_action == "Tail" and "Giant Crocodile" in attacker.name:
                    if any(c.get("Name", "").startswith("Grappled") and c.get("Source") == attacker for c in target.conditions):
                        print(f"{attacker.name} has already grappled {target.name}; skipping Tail attack.")
                        continue
                # Trex special case: skip Tail if target is Grappled by this crocodile
                if sub_action == "Tail" and "Tyrannosaurus Rex" in attacker.name:
                    if any(c.get("Name", "").startswith("Grappled") and c.get("Source") == attacker for c in target.conditions):
                        print(f"{attacker.name} has already grappled {target.name}; skipping Tail attack.")
                        continue                    
                # Giant Shark special case: if target hp is not max, Bite gets advantage
                if sub_action == "Bite" and "Giant Shark" in attacker.name:
                    if target.currenthitpoints != target.hitpoints:
                        attacker.advantage = True

                attack_data = attacker.actions["Multiattack"]["Attacks"][sub_action]
                if attack_data['Attack Type'] == "Saving Throw":
                    attack_effect = attack_data.get("Effect", {})
                    save_type = attack_effect.get("Save Type")
                    save_dc = attack_effect.get("Save DC")
                    dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
                    print(f"{target.name} rolls a {dice_roll} {save_type} save vs DC {save_dc}")            

                    if dice_roll >= save_dc:
                        print(f"{target.name} saves!")
                        continue #just ends
                    else:
                        print(f"{target.name} fails the save!")
                        if attack_data.get('Damage') is not None:
                            dmg_dice = attack_data['Damage']
                            dmg_dice = dmg_dice.replace(" ", "")
                            dmg = roll(dmg_dice)
                            damage_type = attack_data['Damage Type']
                            target.take_damage(dmg, damage_type, announcer)
                        if "Effect" in attack_data:
                            process_effects(attack_data, attacker, target, current_turn)
                else:
                    attack_data = attacker.actions["Multiattack"]["Attacks"][sub_action]
                    print(f"({attacker.name}) is attacking ({target.name}) with {sub_action}")
                    attack_roll1 = dice(20)
                    attack_roll2 = dice(20)
                    if ((attacker.advantage == True) and (attacker.disadvantage == False)) or (attacker.advantage_against.get(f'{target.name}') == True):
                        attack_roll = max(attack_roll1, attack_roll2)
                        print(f"{attacker.name} has advantage, atk was {attack_roll1} before, now it is {attack_roll}!")
                    elif ((attacker.disadvantage == True) and (attacker.advantage == False)) or (attacker.disadvantage_against.get(f'{target.name}') == True):
                        attack_roll = min(attack_roll1, attack_roll2)
                        print(f"{attacker.name} has disadvantage, atk was {attack_roll1} before, now it is {attack_roll}.")
                    else:
                        print(f"{attacker.name} rolls normally.")
                        attack_roll = attack_roll1     
                    hit_mod = attack_data.get('Attack Bonus', 0)
                    to_hit_roll = attack_roll + hit_mod
                    damage_components = attack_data.get("Damage Components")
                    print(f"To hit, you got a {attack_roll} + {hit_mod}, for a total of {to_hit_roll}, against {target.name}'s AC of {target.armor_class}")
                    #print(f"Attack Data is {attack_data}")

                    if attack_roll == 1:
                        print("Natural 1! You fumble!")
                        nat1(attacker, target, announcer, attack_data, current_turn, weapon_name=atk_key)
                    elif attack_roll == 20:
                        print("Crit! Auto-hit, rolling crit damage...")
                        if damage_components:
                            for comp in damage_components:
                                dice_str = comp.get("Dice", "0")
                                if dice_str.strip().isdigit():
                                    dice_str = f"{dice_str.strip()}d1"
                                dice_mod = comp.get("Modifier", "0")
                                dice_str = dice_str+"+"+dice_mod
                                damage_type = comp.get("Type", "Unknown")
                                dmg = crit(dice_str, announcer)
                                print(f"{attacker.name} crits {target.name} for {dmg} {damage_type} damage!")
                                target.take_damage(dmg, damage_type, announcer)                                       
                        else:                    
                            dmg_dice = attack_data['Damage']
                            if "Conditional Extra" in attack_data:
                                conditional = attack_data.get("Conditional Extra", {})
                                req_cond = conditional.get("Condition")
                                if any(c.get("Name") == req_cond for c in target.conditions):
                                    print(f"{target.name} is taking extra damage because they are {req_cond}")
                                dmg_dice = conditional["Damage"]
                            dmg = crit(dmg_dice, announcer)
                            damage_type = attack_data['Damage Type']
                            print(f"{attacker.name} crits {target.name} with {sub_action}, dealing {dmg} {damage_type} damage!")
                            target.take_damage(dmg, damage_type, announcer)
                        process_effects(attack_data, attacker, target, current_turn)   
                    elif attack_roll + hit_mod >= target.armor_class:
                        if damage_components:
                            for comp in damage_components:
                                dice_str = comp.get("Dice", "0")
                                if dice_str.strip().isdigit():
                                    dice_str = f"{dice_str.strip()}d1"                                
                                dice_mod = comp.get("Modifier", "0")
                                dice_str = dice_str+"+"+dice_mod                            
                                damage_type = comp.get("Type", "Unknown")
                                dmg = roll(dice_str)
                                print(f"{attacker.name} hits {target.name} for {dmg} {damage_type} damage!")
                                target.take_damage(dmg, damage_type, announcer)                              
                        else:                           
                            dmg_dice = attack_data['Damage']
                            if "Conditional Extra" in attack_data:
                                conditional = attack_data.get("Conditional Extra", {})
                                req_cond = conditional.get("Condition")
                                if any(c.get("Name") == req_cond for c in target.conditions):
                                    print(f"{target.name} is taking extra damage because they are {req_cond}")
                                dmg_dice = conditional["Damage"]
                            dmg = roll(dmg_dice)
                            damage_type = attack_data['Damage Type']
                            print(f"{attacker.name} hits {target.name} with {sub_action}, dealing {dmg} {damage_type} damage!")
                            target.take_damage(dmg, damage_type, announcer)
                        process_effects(attack_data, attacker, target, current_turn)   
                    else:
                        print(f"{attacker.name} missed {target.name}")  
                if target.currenthitpoints <= 0 or any(c.get("Name") == "Unconscious" for c in target.conditions):
                    #Need new targets
                    valid_targets = [
                        t for t in opponent_team
                        if t != target
                        and t.currenthitpoints > 0
                        and not any(c.get("Name") == "Unconscious" for c in t.conditions) 
                        and distance(target.position, t.position) <= 5 #5 is temporary, until map mechanics are more explored
                    ]
                    if not valid_targets:
                        print(f"No valid targets within range. {attacker.name} skips this attack.")
                        continue  # skip this sub-action

                    # Choose a new target from valid ones
                    target = choose_target(attacker, attack_data, valid_targets)                    
                #Here! I need to insert a check for if the target is dead, check for a different target in range, and continue, else break out of this
        else:
            print("This is a singular attack.")
            attack_data = attacker.actions[atk_key]
            if attack_data['Attack Type'] == "Saving Throw":
                save_type = attack_data.get("Save Type")
                save_dc = attack_data.get("Save DC")
                dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
                print(f"{target.name} rolls a {dice_roll} {save_type} save vs DC {save_dc}")            

                if dice_roll >= save_dc:
                    print(f"{target.name} saves!")
                    return #just ends
                else:
                    print(f"{target.name} fails the save!")
                    dmg_dice = attack_data['Damage']
                    dmg_dice = dmg_dice.replace(" ", "")
                    dmg = roll(dmg_dice)
                    damage_type = attack_data['Damage Type']
                    target.take_damage(dmg, damage_type, announcer)
                    if "Effect" in attack_data:
                        process_effects(attack_data, attacker, target, current_turn)
            else:
                # Hunter Shark special case: if target hp is not max, Bite gets advantage
                if ((attack_data['Name'] == "Bite" and "Hunter Shark" in attacker.name) or
                    (attack_data['Name'] == "Bite" and "Piranha" in attacker.name) or
                    (attack_data['Name'] == "Bites" and "Swarm of Piranhas" in attacker.name)):
                    if target.currenthitpoints != target.hitpoints:
                        attacker.advantage = True    
                hit_mod = attack_data.get('Attack Bonus', 0)
                attack_roll1 = dice(20)
                attack_roll2 = dice(20)
                if ((attacker.advantage == True) and (attacker.disadvantage == False)) or (attacker.advantage_against.get(f'{target.name}') == True):
                    attack_roll = max(attack_roll1, attack_roll2)
                    print(f"{attacker.name} has advantage, atk was {attack_roll1} before, now it is {attack_roll}!")
                elif ((attacker.disadvantage == True) and (attacker.advantage == False)) or (attacker.disadvantage_against.get(f'{target.name}') == True):
                    attack_roll = min(attack_roll1, attack_roll2)
                    print(f"{attacker.name} has disadvantage, atk was {attack_roll1} before, now it is {attack_roll}.")
                else:
                    print(f"{attacker.name} rolls normally.")
                    attack_roll = attack_roll1     
                to_hit_roll = attack_roll + hit_mod
                damage_components = attack_data.get("Damage Components")
                print(f"To hit, you got a {attack_roll} + {hit_mod}, for a total of {to_hit_roll}, against {target.name}'s AC of {target.armor_class}")

                if attack_roll == 1:
                    print("Natural 1! You fumble!")
                    nat1(attacker, target, announcer, attack_data, current_turn)
                elif attack_roll == 20:
                    print("Crit! Auto-hit, rolling crit damage...")
                    if damage_components:
                        for i, comp in enumerate(damage_components):
                            dice_str = comp.get("Dice", "0")
                            if dice_str.strip().isdigit():
                                dice_str = f"{dice_str.strip()}d1"                            
                            dice_mod = comp.get("Modifier", "0")
                            dice_str = dice_str+"+"+dice_mod  
                            if "Swarm of Venomous Snakes" in attacker.name:
                                if any(c.get("Name") == "Bloodied" for c in attacker.conditions):
                                    if i == 0:
                                        dice_str = attack_data['Bloodied Damage']
                                    print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dice_str}")
                            damage_type = comp.get("Type", "Unknown")
                            dmg = crit(dice_str, announcer)
                            print(f"{attacker.name} crits {target.name} for {dmg} {damage_type} damage!")
                            target.take_damage(dmg, damage_type, announcer)                                       
                    else:
                        dmg_dice = attack_data['Damage']
                        if "Conditional Extra" in attack_data:
                            conditional = attack_data.get("Conditional Extra", {})
                            req_cond = conditional.get("Condition")
                            if any(c.get("Name") == req_cond for c in target.conditions):
                                print(f"{target.name} is taking extra damage because they are {req_cond}")
                                dmg_dice = conditional["Damage"]
                            elif any(c.get("Name") == req_cond for c in attacker.conditions):
                                if "Swarm of" in attacker.name:
                                    dmg_dice = conditional["Damage"]
                                    print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dmg_dice}")
                        dmg = crit(dmg_dice, announcer)
                        damage_type = attack_data['Damage Type']
                        print(f"{attacker.name} crits {target.name} with {atk_key}, dealing {dmg} {damage_type} damage!")
                        target.take_damage(dmg, damage_type, announcer)
                    process_effects(attack_data, attacker, target, current_turn)   
                elif attack_roll + hit_mod >= target.armor_class:
                    if damage_components:
                        for i, comp in enumerate(damage_components):
                            dice_str = comp.get("Dice", "0")
                            if dice_str.strip().isdigit():
                                dice_str = f"{dice_str.strip()}d1"                            
                            dice_mod = comp.get("Modifier", "0")
                            dice_str = dice_str+"+"+dice_mod     
                            if "Swarm of Venomous Snakes" in attacker.name:
                                if any(c.get("Name") == "Bloodied" for c in attacker.conditions):
                                    if i == 0:
                                        dice_str = attack_data['Bloodied Damage']
                                    print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dice_str}")                                                   
                            damage_type = comp.get("Type", "Unknown")
                            dmg = roll(dice_str)
                            print(f"{attacker.name} hits {target.name} for {dmg} {damage_type} damage!")
                            target.take_damage(dmg, damage_type, announcer)                              
                    else:                    
                        dmg_dice = attack_data['Damage']
                        if "Conditional Extra" in attack_data:
                            conditional = attack_data.get("Conditional Extra", {})
                            req_cond = conditional.get("Condition")
                            if any(c.get("Name") == req_cond for c in target.conditions):
                                print(f"{target.name} is taking extra damage because they are {req_cond}")
                                dmg_dice = conditional["Damage"]
                            elif any(c.get("Name") == req_cond for c in attacker.conditions):
                                if "Swarm of" in attacker.name:
                                    dmg_dice = conditional["Damage"]
                                    print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dmg_dice}")                                
                        dmg = roll(dmg_dice)
                        damage_type = attack_data['Damage Type']
                        print(f"{attacker.name} hits {target.name} with {atk_key}, dealing {dmg} {damage_type} damage, weapon_attack the second time!")
                        target.take_damage(dmg, damage_type, announcer)
                    process_effects(attack_data, attacker, target, current_turn)   
                else:
                    print(f"{attacker.name} missed {target.name}")      

def spell_attack(attacker, spell, target, announcer, current_turn, home_team, opponent_team, init_tracker):
    spell_data = attacker.attacksspellcasting[spell]
    print(f"Spell Data is {spell_data}") #debug
    roll_scaling = spell_data.get("Effect", {}).get("Rolls", {})
    caster_level = attacker.level
    num_rolls = max([v for k, v in roll_scaling.items() if int(k) <= caster_level], default=1)
    print(f"num_rolls is {num_rolls}") #debug
    for _ in range(int(num_rolls)):
        hit_mod = spell_data.get('Attack Bonus', 0)
        attack_roll1 = dice(20)
        attack_roll2 = dice(20)
        if ((attacker.advantage == True) and (attacker.disadvantage == False)) or (attacker.advantage_against.get(f'{target.name}') == True):
            attack_roll = max(attack_roll1, attack_roll2)
            print(f"{attacker.name} has advantage, atk was {attack_roll1} before, now it is {attack_roll}!")
        elif ((attacker.disadvantage == True) and (attacker.advantage == False)) or (attacker.disadvantage_against.get(f'{target.name}') == True):
            attack_roll = min(attack_roll1, attack_roll2)
            print(f"{attacker.name} has disadvantage, atk was {attack_roll1} before, now it is {attack_roll}.")
        else:
            print(f"{attacker.name} rolls normally.")
            attack_roll = attack_roll1     
        to_hit_roll = attack_roll + hit_mod
        print(f"To hit, you got a {attack_roll} + {hit_mod}, for a total of {to_hit_roll}, against {target.name}'s AC of {target.armor_class}")

        if attack_roll == 1:
            print("Natural 1! You fumble!")
            nat1(attacker, target, announcer, spell_data, current_turn)
        elif attack_roll == 20:
            #print(f"Spell Data is {spell_data}") debug
            if "Eldritch Blast" in spell_data['Name']:
                dice_roll = spell_data.get("Effect", {}).get("Damage")                
            else:            
                scaling = spell_data.get("Effect", {}).get("Scaling", {})
                caster_level = attacker.level
                max_level = max([lvl for lvl in scaling if int(lvl) <= caster_level], default=None)
                dice_roll = spell_data['Effect']['Scaling'][str(max_level)]
            if "Mod" in dice_roll:
                spell_mod = spell_data.get('Modifier')
                mod = math.floor((attacker.ability_scores[spell_mod] - 10)/2)
                #print(f"Mod is {mod}") #debug
                new_dice_roll = dice_roll.replace("Mod", str(mod))
                #print(f"Now Dice Roll for {spell_data['Name']} is {new_dice_roll}") #debug
                dmg = crit(new_dice_roll, announcer)
            else:
                dmg = roll(dice_roll)           
            damage_type = spell_data['Effect']['Damage Type']
            print(f"{attacker.name} crits {target.name} with {spell_data['Name']}, dealing {dmg} {damage_type} damage!")
            target.take_damage(dmg, damage_type, announcer)
            process_effects(spell_data, attacker, target, current_turn)
        elif attack_roll + hit_mod >= target.armor_class:
            if "Eldritch Blast" in spell_data['Name']:
                dice_roll = spell_data.get("Effect", {}).get("Damage")                
            else:
                scaling = spell_data.get("Effect", {}).get("Scaling", {})
                caster_level = attacker.level
                max_level = max([lvl for lvl in scaling if int(lvl) <= caster_level], default=None)
                dice_roll = spell_data['Effect']['Scaling'][str(max_level)]
            #print(f"So Dice Roll for {spell_data['Name']} is {dice_roll}") #debug
            if "Mod" in dice_roll:
                spell_mod = spell_data.get('Modifier')
                mod = math.floor((attacker.ability_scores[spell_mod] - 10)/2)
                #print(f"Mod is {mod}") #debug
                new_dice_roll = dice_roll.replace("Mod", str(mod))
                #print(f"Now Dice Roll for {spell_data['Name']} is {new_dice_roll}") #debug
                dmg = roll(new_dice_roll)
            else:
                dmg = roll(dice_roll)
            damage_type = spell_data['Effect']['Damage Type']
            print(f"{attacker.name} hits {target.name} with {spell_data['Name']}, dealing {dmg} {damage_type} damage!")
            target.take_damage(dmg, damage_type, announcer)
            process_effects(spell_data, attacker, target, current_turn)
        else:
            print(f"{attacker.name}'s spell misses {target.name}!")

def apply_weapon_condition(attacker, attack_data, target, current_turn):
    for effect in attack_data["Active Effects"][:]:  # Copy to avoid iteration errors
        if effect["Type"] == "Condition":
            effect_data = effect["Effect"]
            #print(f"Effect Data is {effect_data}") #debug
            if "Damage" in effect_data:
                scaling = attack_data.get("Effect", {}).get("Scaling", {})
                caster_level = attacker.level  # Or caster.spellcasting_level
                max_level = max([lvl for lvl in scaling if lvl <= caster_level], default=None)                        
                extra_damage = dice(effect_data["Scaling"][str(max_level)])
                damage += extra_damage
                print(f"{effect['Name']} adds {extra_damage} extra {effect_data.get('Damage Type', 'force')} damage!")

            # 🌩️ Apply condition to target, e.g., Booming Blade
            if "Conditions" in effect_data:
                condition = effect_data["Conditions"]
                scaling = condition.get("MovementScaling", {})
                caster_level = attacker.level
                max_level = max([lvl for lvl in scaling if int(lvl) <= caster_level], default=None)    
                if "Booming Blade" in condition['Name']:
                    condition_to_apply = {
                        "Name": f"{condition['Name']} (Movement)",  # e.g., "Booming Blade"
                        "Damage": condition["MovementScaling"][str(max_level)],
                        "Trigger": condition.get("Trigger", "Move"),
                        "Source": attacker,
                        "Expires": "StartOfSourceNextTurn",
                        "Duration": condition.get("Duration", 1),
                        "Applied": current_turn,
                    }
                    print(f"Condition applying: {condition_to_apply}")
                    target.conditions.append(condition_to_apply)
                    print(f"{target.name} is affected by {condition_to_apply['Name']}!")

            if effect["Expires"] == "AfterHit":
                attack_data["Active Effects"].remove(effect)  

def process_effects(attack, attacker, target, current_turn):
    print(f"Attack name is {attack['Name']} and attacker name is {attacker.name}, this is in process_effects") #debug
    attack_ae = attack.get("Active Effects", [])
    #print(f"Full info on attack: {attack}") #debug
    if ((attack['Name'] == "Tail" and "Ankylosaurus" in attacker.name)
        or (attack['Name'] == "Claw" and "Brown Bear" in attacker.name)
        or (attack['Name'] == "Bite" and "Dire Wolf" in attacker.name)
        or (attack['Name'] == "Tail" and "Giant Crocodile" in attacker.name)
        or (attack['Name'] == "Bite" and "Mastiff" in attacker.name)
        or (attack['Name'] == "Rend" and "Tiger" in attacker.name)
        or (attack['Name'] == "Bite" and (("Wolf" in attacker.name) and not ("Winter Wolf" in attacker.name)))
        or (attack['Name'] == "Tail" and "Tyrannosaurus Rex" in attacker.name)):
        attack_effect = attack.get("Effect", "").lower()
        if "knocked prone" in attack_effect:
            if SIZE_ORDER.index(target.size) <= SIZE_ORDER.index(attack['Target Size']):
                if not any(cond.get("Name") == "Prone" for cond in target.conditions):
                    condition_to_apply = {
                        "Name": "Prone",  # e.g., "Booming Blade"
                        "Source": attacker,
                        "Expires": "Stand",
                    }
                    target.conditions.append(condition_to_apply)
                    print(f"{target.name} is knocked Prone by {attacker.name}'s {attack['Name']} attack!")
    if ((attack['Name'] == "Constrict" and "Constrictor Snake" in attacker.name) or 
        (attack['Name'] == "Claw" and "Giant Crab" in attacker.name) or
        (attack['Name'] == "Bite" and "Giant Frog" in attacker.name) or
        (attack['Name'] == "Claw" and "Giant Scorpion" in attacker.name) or
        (attack['Name'] == "Tentacle" and "Giant Squid" in attacker.name) or
        (attack['Name'] == "Bite" and "Giant Toad" in attacker.name)):
        attack_effect = attack.get("Effect", {})
        if SIZE_ORDER.index(target.size) <= SIZE_ORDER.index(attack['Target Size']):
            if not any(cond.get("Name") == "Grappled" for cond in target.conditions):
                condition_to_apply = {
                    "Name": attack_effect["Name"],
                    "Source": attacker,
                    "Escape Modifier": attack_effect["Escape Modifier"],
                    "Escape DC": attack_effect["Escape DC"],
                    "Expires": "Escape"
                }
                target.conditions.append(condition_to_apply)
                attacker.grappling.append(target)
                print(f"{attacker.name} grapples {target.name}!")
    if ((attack['Name'] == "Bite" and "Crocodile" in attacker.name) or
        (attack['Name'] == "Tentacles" and "Giant Octopus" in attacker.name) or
        (attack['Name'] == "Bite" and "Tyrannosaurus Rex" in attacker.name)):
        attack_effect = attack.get("Effect", {})
        if SIZE_ORDER.index(target.size) <= SIZE_ORDER.index(attack['Target Size']):
            if not any(cond.get("Name", "").startswith("Grappled") for cond in target.conditions):
                condition_to_apply = {
                    "Name": attack_effect["Name"],
                    "Source": attacker,
                    "Escape Modifier": attack_effect["Escape Modifier"],
                    "Escape DC": attack_effect["Escape DC"],
                    "Expires": "Escape"
                }
                target.conditions.append(condition_to_apply)   
                attacker.grappling.append(target)
                print(f"{attacker.name} attacks {target.name} with {attack['Name']}, grappling and restraining them!")      
    if ((attack['Name'] == "Bite" and "Death Dog" in attacker.name) or
        (attack['Name'] == "Roar" and "Lion" in attacker.name)):
        attack_effect = attack.get("Effect", {})
        save_dc = attack_effect['Save DC']
        save_type = attack_effect['Save Type']
        print(f"{target.name} needs to roll a DC {save_dc} {save_type} Save.")
        dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
        print(f"{target.name} rolled a {dice_roll} against the save DC!")
        if dice_roll >= save_dc:
            print(f"{target.name} saved!")
        else:
            if "Death Dog" in attacker.name:
                if not any(cond.get("Name") == "Poisoned" for cond in target.conditions):
                    lower_amount = roll(attack_effect['Condition Dice'])
                    print(f"{target.name} is already poisoned, HP max lowers by {lower_amount}.")
                    target.hitpointstemp -= lower_amount
                else:
                    print(f"{target.name} is now poisoned.")
                    condition_to_apply = {
                        "Name" : "Poisoned",
                        "Target": target,
                        "Source": attacker,
                        "Save Type": attack_effect["Save Type"],
                        "Save DC": attack_effect["Save DC"],
                        "Expires": "StartofDay"                    
                    }
                    target.conditions.append(condition_to_apply)
            elif "Lion" in attacker.name:
                if not any(cond.get("Name") == "Frightened" for cond in target.conditions):
                    print(f"{target.name} is now frightened.")
                    condition_to_apply = {
                        "Name" : "Frightened",
                        "Target": target,
                        "Source": attacker,
                        "Save Type": attack_effect["Save Type"],
                        "Save DC": attack_effect["Save DC"],
                        "Expires": "StartOfSourceNextTurn"                    
                    }                
                    target.conditions.append(condition_to_apply)
    if ((attack['Name'] == "Bite" and "Diseased Giant Rat" in attacker.name) or
    (attack['Name'] == "Bite" and "Winter Wolf" in attacker.name) or
    (attack['Name'] == "Bite" and "Worg" in attacker.name)):
        attack_effect = attack.get("Effect", {})
        save_dc = attack_effect['Save DC']
        save_type = attack_effect['Save Type']
        effect_name = attack_effect['Name']
        print(f"{target.name} needs to roll a DC {save_dc} {save_type} Save.")
        dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
        print(f"{target.name} rolled a {dice_roll} against the save DC!")
        if not any(cond.get("Name") == effect_name for cond in target.conditions):
            if dice_roll >= save_dc:
                print(f"{target.name} saved!")
            else:
                if effect_name == "Prone":
                    print(f"{target.name} is now Prone.")
                    condition_to_apply = {
                        "Name" : "Prone",
                        "Target": target,
                        "Source": attacker,
                        "Expires": "Stand"   
                    }
                elif effect_name == "Diseased":
                    print(f"{target.name} is now Diseased.")
                    condition_to_apply = {
                        "Name" : "Disease",
                        "Target": target,
                        "Source": attacker,
                        "Expires": "Cured"   
                    }
    if ((attack['Name'] == 'Bite' and "Giant Centipede" in attacker.name) or
        (attack['Name'] == "Gouge" and "Giant Vulture" in attacker.name)):
        if not any(cond.get("Name") == "Poisoned" for cond in target.conditions):
            condition_to_apply = {
                "Name": "Poisoned",
                "Target": target,
                "Source": attacker,
                "Applied": current_turn,
                "Expires": "EndOfTargetTurn"
            }
            target.conditions.append(condition_to_apply)
            print(f"{target.name} has been Poisoned by {attacker.name}")

    if attack['Name'] == "Bite" and "Phase Spider" in attacker.name:
        if "Conditional Extra" in attack:
            conditional = attack.get("Conditional Extra", {})
            req_cond = conditional.get("Condition")
            for c in target.conditions[:]:
                if c.get("Name") == req_cond:
                    target.conditions.remove(c)
                    condition_to_apply1 = {
                        "Name": "Stable",
                        "Target": target
                    }
                    condition_to_apply2 = {
                        "Name": "Poisoned",
                        "Target": target,
                        "Source": attacker,
                        "Expires": "OneHour",
                    }
                    condition_to_apply3 = {
                        "Name": "Paralyzed",
                        "Target": target,
                        "Source": attacker,
                    }
                    target.conditions.append(condition_to_apply1)
                    target.conditions.append(condition_to_apply2)
                    target.conditions.append(condition_to_apply3)
    
    if any("Green-Flame Blade" in effect.get('Name') for effect in attack_ae):
        print("This attack has Green-Flame Blade and therefore has a spell effect.")
        process_spell_effects(target, attack, attacker, current_turn)

    if attack.get("Attack Type") == "Spell":
        print(f"This attack, {attack['Name']}, is a spell.")
        process_spell_effects(target, attack, attacker, current_turn)

def perform_swallow(attacker, target, announcer, turn_number):
    for cond in target.conditions:
        if cond['Name'] == "Grappled" and cond['Source'] == attacker:
            target.conditions.remove(cond)
            attacker.grappling.remove(target)
            target.conditions.append({"Name": "Swallowed", "Target": target, "Source": attacker, "Expires": "UntilReleased", "TurnSwallowed": turn_number})
            attacker.has_swallowed = True
            target.swallowed_by = attacker.name
            print(f"{attacker.name} has swallowed {target.name}!")
            condition_to_apply1 = {
                "Name": "Blinded",
                "Source": attacker
            }
            print(f"{target.name} is Blinded after being swallowed.")
            condition_to_apply2 = {
                "Name": "Restrained",
                "Source": attacker
            }
            print(f"{target.name} is Restrained after being swallowed.")
            condition_to_apply3 = {
                "Name": "Total Cover",
                "Target": target,
                "Source": attacker,
                "Description": "The target has total cover, meaning their AC is infinite."
            }
            print(f"{target.name} has Total Cover after being swallowed.")
            target.conditions.append(condition_to_apply1)
            target.conditions.append(condition_to_apply2)
            target.conditions.append(condition_to_apply3)   

def remove_condition(target, cond_name):
    target.conditions = [cond for cond in target.conditions if cond.get("Name") != cond_name]      

def random_grid_offset_within_speed(speed_in_feet):
    """Choose a valid grid offset (dx, dy) such that distance moved is ≤ speed"""
    max_squares = speed_in_feet // SQUARE_SIZE
    options = []
    for dx in range(-max_squares, max_squares + 1):
        for dy in range(-max_squares, max_squares + 1):
            if abs(dx) + abs(dy) <= max_squares:  # simple movement cost (Manhattan)
                options.append((dx, dy))
    return random.choice(options) if options else (0, 0)  

def move_creature(creature, announcer, home_team, opponent_team, current_turn, double): #Eventually this should include the terrain type
    old_position = creature.position
    all_combatants = home_team + opponent_team
    if creature in home_team:
        opposing_team = opponent_team
    if creature in opponent_team:
        opposing_team = home_team    
    base_speed = max(creature.speed.values())
    speed_keys = list(creature.speed.keys())
    speed_keys_str = ", ".join(sp for sp in speed_keys)
    print(f"Your base speed is {base_speed}ft of movement, split however you wish between {speed_keys_str}.")
    base_speed = max(creature.speed.values())

    #Get current position
    grid_x, grid_y = to_grid_coords(*creature.position)

    #Random Move within range
    options = get_movement_options(creature, announcer, home_team, opponent_team, double)
    selection_label = None
    while True:
        try:
            for i, (opt, opt_n) in enumerate(options):
                print(f"{i} - {opt} ({opt_n})")
            choice = int(input("Where would you like to move? "))
            if choice == 0:
                new_grid_x, new_grid_y = options[0][0]
                selection_label = options[0][1]
                break
            elif 1 <= choice <= len(options):
                new_grid_x, new_grid_y = options[choice][0]
                selection_label = options[choice][1]
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Enter a valid number.")
    
    while True:
        try:
            print("0 - Random Speed")
            for i, idx in enumerate(speed_keys, 1):
                print(f"{i} - {idx}")
            choice = int(input("Which speed will you use to move to that location? "))
            if choice == 0:
                movement_type = random.choice(speed_keys)
                break
            elif 1 <= choice <= len(speed_keys):
                movement_type = speed_keys[choice-1]
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Enter a valid number.")

    new_position = to_map_coords(new_grid_x, new_grid_y)        

    if (new_position != old_position) and not is_square_occupied(new_grid_x, new_grid_y, all_combatants, creature):
        for enemy in opposing_team:
            if f"Adjacent to {enemy.name}" not in selection_label:            
                trait_list = list(creature.traits.keys())
                immune = check_opportunity_attack(creature, movement_type, trait_list)
                if not immune: #These ignore opportunity attacks
                    print(f"{enemy.name} gets to make an opportunity attack!")
                    opportunity_attack(creature, enemy, announcer, current_turn)
                    print(f"After opportunity attack, conditions: {', '.join(c.get('Name') for c in creature.conditions)}")
                    if (c.get('Name') in ('Grappled','Prone') for c in creature.conditions):
                        print(f"{enemy.name} stopped {creature.name} with their attack.")
                        creature.position = old_position  
                        creature.moved = False          
                    else:
                        creature.moved = True
                        creature.position = new_position
                        print(f"{creature.name} moved from: \n{old_position} (grid: {grid_x}, {grid_y}) to:\n{new_position} (grid: {new_grid_x}, {new_grid_y})")

        # Check for Booming Blade
        for condition in creature.conditions[:]:  # copy to allow safe removal
            if condition["Name"] == "Booming Blade" and condition.get("Trigger") == "Move":
                damage = condition.get("Damage", {})
                num_dice = damage.get("NumDice", 1)
                die_size = damage.get("Dice", 8)
                damage_type = damage.get("Type", "Thunder")

                full_dmg = sum(dice(die_size) for _ in range(num_dice))
                print(f"{creature.name} takes {full_dmg} {damage_type} damage from Booming Blade!")

                # You can apply this damage to monster.hp here if you want
                creature.take_damage(full_dmg, damage_type, announcer)

                # Remove the condition
                creature.conditions.remove(condition)  


def take_turn(creature, announcer, current_turn, player_list, home_team, opponent_team, init_tracker):

    # Handle condition durations and expirations

    # Action economy options
    available_actions = list(creature.actions.keys())
    available_movement = True  # You can move unless you Dash as an Action first
    
    all_combatants = home_team + opponent_team

    while available_actions or available_movement:
        print("\nChoose your action:")
        options = []
        #Add all available actions
        if available_actions:
            for act in available_actions:
                act_data = creature.actions.get(act, {})
                versatile = act_data.get("Properties", {}).get("Versatile")
                weapon = act_data.get('Weapon Type')
                #print(f"For {act}, weapon data is {weapon}") #debug
                if act == "Breath Weapon":
                    if act_data["Current Uses"] > 0:
                        options.append(("Action", act))
                elif act == "Spellcasting":                    
                    spell_mod = act_data.get("Modifier", "WIS")
                    for cast_type in ["At Will", "1/Day", "3/Day", "Spells"]:
                        for spell_name in act_data.get(cast_type, []):
                            spell_data = dnd_spells.spells.get(spell_name, {}).copy()
                            if not spell_data:
                                continue
                            label_suffix = "" if cast_type == "At Will" else f" ({cast_type})"
                            spell_data["Name"] += label_suffix
                            spell_data["Original Name"] = spell_name
                            spell_data["Spell Source"] = "Monster"
                            spell_data["Frequency"] = cast_type
                            spell_data["Modifier"] = spell_mod
                            # Add spell to creature.actions if not present
                            if spell_data["Name"] not in creature.actions:
                                creature.actions[spell_data["Name"]] = spell_data
                                available_actions.append(spell_data["Name"])  # ← Add the spell for future iterations
                elif versatile:
                    options.append(("Action", f"{act} (1H)"))
                    options.append(("Action", f"{act} (2H)"))
                elif weapon:                    
                    options.append(("Action", act)) 
                    options.append(("Action", f"Throw {act}"))
                else:
                    options.append(("Action", act))                
        #Add Movement
        if available_movement:
            options.append(("Move", None))
        
        if available_actions and available_movement:
            options.append(("Action", "Dash"))
        
        #Eventually add hide, disengage, etc

        if creature.disarmed:
            if "Attack Type" in creature.disarmed_item and "Weapon" in creature.disarmed_item["Attack Type"]:
                weapon_name = creature.disarmed_item["Name"]
                if available_actions:
                    options.append(("Action", f"Pick up {weapon_name} and Attack"))
                if available_movement:
                    options.append((f"Pick up {weapon_name} and Move", "Pickup&Move"))
            elif "shield" in creature.disarmed_item["Name"].lower():
                shield_name = creature.disarmed_item["Name"]
                if available_actions:
                    options.append(("Action", f"Pick up {shield_name}"))

        #Add End Turn
        options.append(("End Turn", None))

        #Print the Menu
        for idx, (label, act) in enumerate(options, 1):
            #print(f"Label is {label}") #debug
            #print(f"Act is {act}") #debug
            throw_act = None
            if act is not None and "Throw" in act:
                throw_act = act
                act = act[6:]
                #print(f"After getting rid of 'Throw ', act is {act}") #debug
            display_text = f"{act} (Action)" if label == "Action" else label
            verse = ""
            if (act is not None) and ((act.endswith(" (1H)")) or (act.endswith(" (2H)"))):
                verse = act[-5:]        # Get ' (1H)' or ' (2H)'
                act = act[:-5]          # Remove the suffix to get the base weapon name  
            #print(f"Act COULD be different, it is now {act}") #debug
            if act in available_actions and act != "Multiattack":        
                act_data = creature.actions[act]
                #print(f"Action data is {act_data}") #debug
                #print(f"Atk name is {act_data['Name']}") #debug
                atk_ogname = act_data.get("Original Name", act_data["Name"])
                effect = act_data.get("Effect", {})
                if not isinstance(effect, dict):
                    effect = {}
                scaling = effect.get("Scaling", {})
                num_rolls = effect.get("Rolls", {})
                int_roll_scaling = {int(k): v for k, v in num_rolls.items()}
                max_roll = max([k for k in int_roll_scaling if k <= creature.level], default=None)
                int_level_scaling = {int(k): v for k, v in scaling.items()}
                max_level = max([k for k in int_level_scaling if k <= creature.level], default=None)
                proficient = act_data.get("Proficient")
                if act == "Breath Weapon":
                    save_dc_mod = act_data['Modifier']
                    save_dc = 8 + math.floor((creature.ability_scores[save_dc_mod] - 10)/2) + creature.profbonus                

                if isinstance(creature, Monster):
                    proficient = ''
                elif proficient == True:
                    proficient = "(Proficient)"
                else:
                    proficient = "(Not Proficient)"                 
                if atk_ogname in dnd_spells.spells:
                    atk_bonus = act_data.get("Attack Bonus", None)
                    if atk_bonus is not None:
                        #print(f"This action is: {act_data['Name']}") #debug
                        #print(f"Num rolls is: {num_rolls}") #debug
                        #print(f"Max roll is: {max_roll}") #debug
                        #print(f"Creature level is {creature.level}, type: {type(creature.level)}") #debug
                        #print("Eligible Rolls:", [int(roll) for roll in scaling if int(roll) <= creature.level]) #debug
                        #print(f"Scaling is {scaling}") #debug
                        #print(f"Max Level is {max_level}") #debug

                        if "Eldritch Blast" in act_data['Name']:
                            display_text = f"{act_data['Name']} ({'+' if atk_bonus>=0 else ''}{atk_bonus} to hit) | {num_rolls[str(max_roll)]} x {act_data['Effect']['Damage']} {act_data['Effect']['Damage Type']}"
                        else:
                            if "Magic Stone" in act_data['Name']:
                                spell_mod = act_data.get('Modifier')
                                mod = math.floor((creature.ability_scores[spell_mod] - 10)/2)
                                dmg = scaling[str(max_level)]
                                new_dmg = dmg.replace("Mod", str(mod))
                                display_text = f"{act_data['Name']} ({'+' if atk_bonus>=0 else ''}{atk_bonus} to hit) | {new_dmg} {act_data['Effect']['Damage Type']}"
                            else:
                                if "Save" in act_data.keys():
                                    if "Toll the Dead" in act_data['Name']:
                                        display_text = f"{act_data['Name']} ({act_data['Save']} Save) | {scaling[str(max_level)]} + {act_data['Effect']['Damage Type']}"
                                    else:
                                        display_text = f"{act_data['Name']} ({act_data['Save']} Save) | {scaling[str(max_level)]} {act_data['Effect']['Damage Type']}"
                                else:
                                    display_text = f"{act_data['Name']} ({'+' if atk_bonus>=0 else ''}{atk_bonus} to hit) | {scaling[str(max_level)]} {act_data['Effect']['Damage Type']}"
                    else:
                        display_text = f"{act_data['Name']}"
                elif act == "Breath Weapon":
                    display_text = f"{act_data['Name']} (DC {save_dc} {act_data['Save']} Save) | {scaling[str(max_level)]} {act_data['Effect']['Damage Type']} ({act_data["Current Uses"]} Uses)"
                elif act == "Unarmed Strike: Grapple":
                    grapple_dc_mod = act_data['Modifier']
                    grapple_dc = 8 + math.floor((creature.ability_scores[grapple_dc_mod] - 10)/2) + creature.profbonus
                    display_text = f"{act_data['Name']} (DC {grapple_dc} '{act_data['Save']}' Save) | Grappled"
                elif act == "Unarmed Strike: Shove":
                    shove_dc_mod = act_data['Modifier']
                    shove_dc = 8 + math.floor((creature.ability_scores[grapple_dc_mod] - 10)/2) + creature.profbonus
                    display_text = f"{act_data['Name']} (DC {grapple_dc} '{act_data['Save']}' Save) | Push 5FT or Prone"
                elif verse == " (1H)":
                    display_text = f"{act_data['Name']} ({'+' if act_data.get('Attack Bonus', 0)>=0 else ''}{act_data.get('Attack Bonus', 0)} to hit) | {act_data['Damage']} {act_data['Damage Type']} {proficient}"
                elif verse == " (2H)":
                    verse_dmg = act_data.get("Properties", {}).get("Versatile", "???")
                    if creature.offhand:
                        display_text = f"{act_data['Name']} ({'+' if act_data.get('Attack Bonus', 0) >= 0 else ''}{act_data.get('Attack Bonus', 0)} to hit) | {verse_dmg} {act_data['Damage Type']} {proficient}, using as a 2H, but to do this you would drop {creature.offhand['Name']}"
                    else:
                        display_text = f"{act_data['Name']} ({'+' if act_data.get('Attack Bonus', 0) >= 0 else ''}{act_data.get('Attack Bonus', 0)} to hit) | {verse_dmg} {act_data['Damage Type']} {proficient}, using as a 2H"
                else:      
                    if throw_act:
                        if act_data.get('Properties', {}).get('Type', '') == "Thrown":
                            display_text = f"(Throw) {act_data['Name']} ({'+' if act_data.get('Attack Bonus', 0)>=0 else ''}{act_data.get('Attack Bonus', 0)} to hit) | {act_data['Damage']} {act_data['Damage Type']} {proficient}" #There is more to throwing a weapon than this...
                        else:
                            display_text = f"(Improvised Throw) {act_data['Name']} (0 to hit) | 1d4 Bludgeoning"
                    else:                
                        display_text = f"{act_data['Name']} ({'+' if act_data.get('Attack Bonus', 0)>=0 else ''}{act_data.get('Attack Bonus', 0)} to hit) | {act_data['Damage']} {act_data['Damage Type']} {proficient}"
            print(f"{idx} - {display_text}")

        choice = (input("Select an option: ")).strip()
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
            print("Invalid choice. Try again.")
            continue
        selected = options[int(choice) - 1]
        label,act = selected
        #print(f"The label you selected: {label}, the act: {act}") #debug
        if act == "Pickup&Move":
            print(f"{creature.name} picks up {creature.disarmed_item['Name']} and moves.")
            creature.mainhand = creature.disarmed_item
            creature.disarmed_item = None
            creature.disarmed = False
            move_creature(creature, announcer, home_team, opponent_team, current_turn, double=False)
            available_movement = False      
     
            #elif pick up specific items          
        if label == "Action": 
            #print(f"Act is {act}") #debug
            throw_act = None
            if "Throw" in act:
                throw_act = act
                act = act[6:]   
            verse = ""
            if (act is not None) and ((act.endswith(" (1H)")) or (act.endswith(" (2H)"))):
                verse = act[-5:]        # Get ' (1H)' or ' (2H)'
                act = act[:-5]          # Remove the suffix to get the base weapon name 
            action_data = creature.actions.get(act, {})
            atk_type = action_data.get("Attack Type")
            atk_ogname = action_data.get("Original Name")
            #print(f"Action is {action_data}") #debug
            if act == "Dash":
                move_creature(creature, announcer, home_team, opponent_team, current_turn, double = True)
                available_movement = False
                available_actions.clear()
            if "Pick up" in act and creature.disarmed:
                if "shield" in creature.disarmed_item['Name'].lower():
                    old_ac = creature.armor_class #debug
                    new_ac = old_ac + 2 #debug
                    print(f"Your dropped item was a shield! AC changed, from {old_ac} to {new_ac}.")
                    creature.offhand = creature.disarmed_item
                    creature.armor_class += 2     
                    creature.disarmed_item = None
                    creature.disarmed = False 
                    available_actions.clear()
                else:       
                    weapon = creature.disarmed_item
                    creature.equipment.append(weapon)
                    creature.mainhand = weapon
                    creature.disarmed_item = None
                    creature.disarmed = False
                    print(f"{creature.name} picks up their {weapon['Name']} to attack.")
                    act = weapon["Name"]  # Replace act string with actual weapon name
                    action_data = creature.actions.get(act)
                    atk_type = action_data.get("Attack Type")
                    atk_ogname = action_data.get("Original Name")                
            if atk_type is not None:
                #print(f"{act} is an attack") #debug
                if throw_act:
                    #print(f"{throw_act} is now {act}") #debug
                    #print(f"Therefore, act data is {action_data}") #debug
                    if action_data.get('Properties', {}).get('Type', '') == "Thrown":
                        print(f"Need to pick a target to use {act} on.")
                        target = choose_target(creature, action_data, all_combatants)
                        creature.mainhand = creature.actions[act].copy()  
                        creature.mainhand["Thrown Range"] = creature.mainhand["Properties"]["Range"]
                        properties = list(action_data.get('Properties', {}).keys())
                        if "Finesse" in properties:
                            creature.mainhand['Damage Bonus'] = max(creature.StrMod, creature.DexMod)
                            creature.mainhand["Attack Bonus"] = creature.mainhand.get("Damage Bonus", 0) + (creature.profbonus if creature.mainhand["Proficient"] == True else 0)
                        else:
                            creature.mainhand['Damage Bonus'] = creature.StrMod
                            creature.mainhand["Attack Bonus"] = creature.mainhand.get("Damage Bonus", 0) + (creature.profbonus if creature.mainhand["Proficient"] == True else 0)
                        weapon_attack(creature, act, target, announcer, current_turn, home_team, opponent_team, init_tracker, attack_data = creature.mainhand)
                        print(f"You threw {creature.mainhand['Name']}")
                        creature.disarmed = True
                        creature.disarmed_item = creature.actions[act]
                        # Remove item from equipment by matching its name; before I used the whole dictionary, but now the name will suffice
                        for item in creature.equipment:
                            if item.get("Name") == creature.actions[act].get("Name"):
                                creature.equipment.remove(item)
                                break                    
                        creature.mainhand = None
                    else:
                        print(f"Need to pick a target to use {act} on.")
                        target = choose_target(creature, action_data, all_combatants)
                        creature.mainhand = creature.actions[act].copy()
                        creature.mainhand['Normal Damage'] = creature.mainhand['Damage']
                        creature.mainhand['Normal Damage Type'] = creature.mainhand['Damage Type']
                        creature.mainhand['Normal Modifier'] = creature.mainhand['Modifier']
                        creature.mainhand['Normal Damage Bonus'] = creature.mainhand['Damage Bonus']
                        creature.mainhand['Normal Attack Bonus'] = creature.mainhand['Attack Bonus']
                        creature.mainhand['Damage'] = "1d4"
                        creature.mainhand['Damage Type'] = "Bludgeoning"
                        creature.mainhand['Modifier'] = ""
                        creature.mainhand['Damage Bonus'] = 0
                        creature.mainhand['Attack Bonus'] = 0
                        creature.mainhand["Thrown Range"] = {
                            "Min": 20,
                            "Max": 60,
                        }
                        #print(f"Before throwing, weapon is {creature.mainhand}") #debug
                        weapon_attack(creature, act, target, announcer, current_turn, home_team, opponent_team, init_tracker, attack_data = creature.mainhand)
                        print(f"You threw {creature.mainhand['Name']}") 
                        creature.disarmed = True
                        creature.disarmed_item = creature.actions[act]
                        # Remove item from equipment by matching its name; before I used the whole dictionary, but now the name will suffice
                        for item in creature.equipment:
                            if item.get("Name") == creature.actions[act].get("Name"):
                                creature.equipment.remove(item)
                                break                        
                        creature.mainhand = None
                        print(f"It made it to the end of throwing something.")
                elif "Weapon" in action_data.get("Attack Type"):
                    print(f"{act} is a weapon attack")
                    print(f"Need to pick a target to use {act} on.")
                    target = choose_target(creature, action_data, all_combatants)
                    creature.mainhand = creature.actions[act]
                    if verse == " (1H)":
                        print(f"You are using {act} as a 1H weapon.")
                        weapon_attack(creature, act, target, announcer, current_turn, home_team, opponent_team, init_tracker)
                    elif verse == " (2H)":
                        print(f"You are using {act} as a 2H weapon.")
                        if creature.offhand:                            
                            if "shield" in creature.offhand['Name'].lower():
                                old_ac = creature.armor_class #debug
                                new_ac = old_ac - 2 #debug
                                print(f"You drop {creature.offhand['Name']}, lowering your AC by 2, from {old_ac} to {new_ac}.")
                                creature.disarmed = True
                                creature.disarmed_item = creature.offhand
                                creature.equipment.remove(creature.disarmed_item)
                                creature.offhand = None
                                creature.armor_class -= 2
                        old_dmg = action_data.get("Damage", '')
                        verse_dmg = action_data.get("Properties", {}).get("Versatile", "???")
                        action_data['Damage'] = verse_dmg
                        weapon_attack(creature, act, target, announcer, current_turn, home_team, opponent_team, init_tracker, attack_data = creature.mainhand)
                        action_data['Damage'] = old_dmg
                    else:
                        weapon_attack(creature, act, target, announcer, current_turn, home_team, opponent_team, init_tracker)
                    #need to find a way to reference the option chosen
                    #weapon_attack(creature, act, target, announcer, current_turn, home_team, opponent_team, init_tracker)
                elif "Spell" in action_data.get("Attack Type"):
                    print(f"{act} is a spell attack")
                    print(f"Need to pick a target to use {act} on.")
                    target = choose_target(creature, action_data, all_combatants)
                    cast_spell(creature, target, announcer, current_turn, home_team, opponent_team, init_tracker, act)       
                    if action_data['Name'] == "Breath Weapon":
                        action_data['Current Uses'] -= 1     
                elif "Saving Throw" in action_data.get('Attack Type'):
                    print(f"Name is: {action_data['Name']}")
                    if action_data['Name'] == 'Unarmed Strike: Grapple':
                        print(f"Need to pick a target to Grapple. Can only used on a creature one size larger than you and if you have a hand free to grab it.")
                        if creature.offhand == None:
                            target = choose_target(creature, action_data, all_combatants)
                            print(f"You chose the target to be: {target.name}")
                            if not any(c.get('Name') == "Grappled" for c in target.conditions):
                                save_type = ("STR" if target.ability_scores["STR"] > target.ability_scores["DEX"] else "DEX")
                                save_dc = 8 + creature.StrMod + creature.profbonus
                                dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
                                print(f"{target.name} rolls a {dice_roll} {save_type} save vs DC {save_dc}")            

                                if dice_roll >= save_dc:
                                    print(f"{target.name} saves!")
                                else:
                                    condition_to_apply = {
                                        "Name": "Grappled",
                                        "Source": creature,
                                        "Escape Modifier": save_type,
                                        "Escape DC": save_dc,
                                        "Expires": "Escape"
                                    }      
                                    target.conditions.append(condition_to_apply)
                                    creature.grappling.append(target)
                                    print(f"{target.name} is grappled!")     
                            else:
                                print(f"{target.name} is already grappled, cannot grapple again!")
                                continue                         
                    elif action_data['Name'] == 'Unarmed Strike: Shove':
                        print(f"Need to pick a target to Shove. Can only used on a creature one size larger than you.")
                        target = choose_target(creature, action_data, all_combatants)
                        print(f"You chose the target to be: {target.name}")
                        print("Now, decide if you are knocking them over or pushing them away.")
                        while True:
                            try:
                                us_shove_opt = ["Push 5ft away", "Knock Prone"]
                                for idx, usso in enumerate(us_shove_opt, 1):
                                    print(f"{idx} - {usso}")
                                choice = int(input(f"How would you like to shove {target.name} "))
                                if 1 <= choice <= len(us_shove_opt):
                                    decision = us_shove_opt[choice-1]
                                    break
                                else:
                                    print("Invalid option.")
                            except ValueError:
                                print("Enter a valid number.")
                        if decision == "Push 5ft away":
                            save_type = ("STR" if target.ability_scores["STR"] > target.ability_scores["DEX"] else "DEX")
                            save_dc = 8 + creature.StrMod + creature.profbonus
                            dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
                            print(f"{target.name} rolls a {dice_roll} {save_type} save vs DC {save_dc}")            

                            if dice_roll >= save_dc:
                                print(f"{target.name} saves!")
                            else:                            
                                print(f"You push {target.name} 5 ft away")
                        elif decision == "Knock Prone":
                            if not any(c.get('Name') == "Prone" for c in target.conditions):
                                save_type = ("STR" if target.ability_scores["STR"] > target.ability_scores["DEX"] else "DEX")
                                save_dc = 8 + creature.StrMod + creature.profbonus
                                dice_roll = dice(20) + math.floor((target.ability_scores[save_type]-10)/2) + max((target.profbonus if f"{save_type}ST" in target.skills else 0), target.saving_throws[f"{save_type} ST"])
                                print(f"{target.name} rolls a {dice_roll} {save_type} save vs DC {save_dc}")            

                                if dice_roll >= save_dc:
                                    print(f"{target.name} saves!")
                                else:
                                    condition_to_apply = {
                                        "Name": "Prone",
                                        "Source": creature,
                                        "Escape Modifier": save_type,
                                        "Escape DC": save_dc,
                                        "Expires": "Escape"
                                    }      
                                    target.conditions.append(condition_to_apply)
                                    print(f"{target.name} is Prone!")     
                            else:
                                print(f"{target.name} is already prone, cannot knock prone again!")
                                continue                         
            available_actions.clear()
        elif label == "Move":
            print(f"You picked {label}")
            move_creature(creature, announcer, home_team, opponent_team, current_turn, double=False)
            available_movement = False
        elif label == "End Turn":
            print("Ending turn.")
            break

        #Left Off Here

            '''if 1 <= choice <= len(available_actions):
                action = available_actions[choice-1]
                action_data = creature.actions[action]
                print(f"Action is {action_data}")
                #Probably use the "type" tag to determine what to do, I think "if "spell" not in tag.lower() perform attack
                if "Spell" not in action_data["Attack Type"]:
                    perform_attack(creature, target, current_turn, home_team, opponent_team, init_tracker, WeaponorSpell="Weapon")
                    available_actions.clear()
                    if check_combat_end(player_list, opponent_team):
                        return
                elif action == "Cast Cantrip or Spell":
                    cast_spell(creature, target, current_turn, home_team, opponent_team, init_tracker)
                    available_actions.clear()
                    if check_combat_end(player_list, opponent_team):
                        return                    
                elif action == "Dash":
                    print(f"{creature.name} uses Dash.")
                    move_creature(creature, all_combatants, current_turn, double=True)
                    available_movement = False  # Dash uses up movement
                    available_actions.clear()
            elif choice == len(available_actions) + 1 and available_movement:
                move_creature(creature, all_combatants, current_turn, double=False)
                if "Dash" not in available_actions and available_actions:
                    available_actions.append("Dash")  # Optional — only if you want to allow Dash after movement
                available_movement = False
            elif choice == len(available_actions) + 2:
                return 
            else:
                print("Invalid option.")
        except ValueError:
            print("Enter a valid number.")
            '''


def check_combat_end(player_list, announcer, contestant_team):
    if all(creature.currenthitpoints <= 0 for creature in contestant_team):
        for pl in player_list:
            pl.conscious = True
            pl.currenthitpoints = pl.hitpoints
        return True
    return False

def remove_expired_conditions(turn_haver, all_creatures, announcer, current_turn, turn_status):
    #checking all creatures
    for creature in all_creatures:
        if isinstance(creature, Player):
            for attack in creature.attacksspellcasting: #I need to fix this for monsters... or do an if check for the Class
                attack_data = creature.attacksspellcasting[attack]
                attack_data_ae = attack_data.get('Active Effects')
                if attack_data_ae:
                    #print(f"Effects before: {attack_data_ae}") #debug, this should give a list of all the active effects on the weapon
                    new_wep_conditions = []
                    for active_effect in attack_data_ae:
                        print(f"Active Effect is {active_effect}") #debug
                        wep_expires = active_effect.get('Effect', {}).get('Conditions').get('Expires')
                        #print(f"This effect, {active_effect['Name']}, expires: {wep_expires}") #debug
                        wep_source = active_effect.get("Source")
                        #print(f"The source of this effect is {wep_source}") #debug
                        applied_turn = active_effect.get("Applied")
                        #print(f"This effect was applied on {applied_turn}") #debug
                        if (
                            wep_expires == "StartOfSourceTurn"
                            and turn_status == "Start"
                            and turn_haver == wep_source
                            and current_turn == applied_turn
                        ):
                            print(f"Effect being dropped from {creature.name}'s {attack}: {active_effect['Name']}, because it expires at {wep_expires}")
                            continue  # Effect expires, don't add it
                        elif (
                            wep_expires == "EndOfSourceTurn"
                            and turn_status == "End"
                            and creature == wep_source
                            and current_turn == applied_turn
                        ):
                            print(f"Effect being dropped from {creature.name}'s {attack}: {active_effect['Name']}, because it expires at {wep_expires}")
                            continue  # Effect expires, don't add it
                        else:
                            new_wep_conditions.append(active_effect)
                    attack_data['Active Effects'] = new_wep_conditions
                    #print(f"Effects after: {attack_data['Active Effects']}") #debug
        new_conditions = []       
        for condition in creature.conditions:
            expires = condition.get("Expires")
            source = condition.get("Source")
            applied_turn = condition.get("Applied", -1) 
            target = condition.get("Target")
            #print(f"Turn Haver: {turn_haver.name}") #debug
            #print(f"Turn Status: {turn_status}") #debug
            #print(f"Condition is {condition['Name']}") #debug
            #print(f"Source: {source.name}") #debug         
            #print(f"Current Turn: {current_turn}") #debug
            #print(f"Applied: {applied_turn}") #debug

            if (
                expires == "StartOfSourceTurn"
                and turn_status == "Start"
                and turn_haver == source
                and current_turn == applied_turn
            ):
                print(f"Effect being dropped from {creature.name}: {condition['Name']}, because it expired at {expires}")
                continue  # Effect expires, don't add it
            elif (
                expires == "EndOfSourceTurn"
                and turn_status == "End"
                and turn_haver == source
                and current_turn == applied_turn
            ):
                print(f"Effect being dropped from {creature.name}: {condition['Name']}, because it expired at {expires}")
                continue  # Effect expires, don't add it
            elif (
                expires == "StartOfSourceNextTurn"
                and turn_status == "Start"
                and turn_haver == source
                and current_turn > applied_turn
            ):
                print(f"Effect being dropped from {creature.name}: {condition['Name']}, because it expired at {expires}")
                continue  # Effect expires, don't add it
            elif (
                expires == "EndOfSourceNextTurn"
                and turn_status == "End"
                and turn_haver == source
                and current_turn > applied_turn
            ):
                print(f"Effect being dropped from {creature.name}: {condition['Name']}, because it expired at {expires}")
                continue  # Effect expires, don't add it            
            elif (
                expires == "StartOfTargetTurn"
                and turn_status == "Start"
                and turn_haver == target
                and current_turn > applied_turn
            ):
                print(f"Effect being dropped from {creature.name}: {condition['Name']}, because it expired at {expires}")
                continue  # Effect expires, don't add it            
            elif (
                expires == "EndOfTargetTurn"
                and turn_status == "End"
                and turn_haver == target
            ):
                print(f"{condition['Name']} has fallen off {creature.name}")
                continue 
            elif (
                expires == "Escape"
                and turn_status == "Start"
                and turn_haver is not source
            ):
                escape_mod = condition.get("Escape Modifier")
                escape_dc = condition.get("Escape DC")
                dice_roll = dice(20) + math.floor((turn_haver.ability_scores[escape_mod]-10)//2) + max((turn_haver.profbonus if f"{escape_mod}ST" in turn_haver.skills else 0), turn_haver.saving_throws[f"{escape_mod} ST"])
                print(f"{turn_haver.name} rolls a {dice_roll} {escape_mod} save vs DC {escape_dc} against condition: {condition.get('Name')}")
                if dice_roll >= escape_dc:
                    print(f"Save has been met! {condition.get('Name')} has been dropped!")
                    if "Grappled" in condition.get('Name'):
                        source = condition.get("Source")
                        source.grappling.remove(turn_haver)
                    continue
                else:
                    print(f"{turn_haver.name} did not meet the save, {condition.get('Name')} stays on.")
                    new_conditions.append(condition)
            elif condition["Name"] == "Swallowed" and condition["Source"] == turn_haver and turn_status == "End":
                if "Giant Frog" in turn_haver.name:
                    if current_turn > condition["TurnSwallowed"]:
                        target = condition["Target"]
                        damage = roll("2d4")
                        print(f"{target.name} takes {damage} acid damage inside {turn_haver.name}!")
                        target.take_damage(damage, "Acid", announcer)
                        if target.currenthitpoints <= 0:
                            print(f"{target.name} perishes inside the frog!")
                        else:
                            print(f"{turn_haver.name} disgorges {target.name}, who exits prone.")
                            prone_condition = {
                                "Name": "Prone",
                                "Target": target,
                                "Source": turn_haver,
                                "Expires": "Stand"

                            }
                            new_conditions.append(prone_condition)
                            turn_haver.has_swallowed = False    
                    else:
                        new_conditions.append(condition) #since swallow hasnt processed    
                elif "Giant Toad" in turn_haver.name:
                    target = condition["Target"]
                    damage = roll("3d6")
                    print(f"{target.name} takes {damage} acid damage inside {turn_haver.name}!")
                    target.take_damage(damage, "Acid", announcer)
                    if target.currenthitpoints <= 0:
                        print(f"{target.name} perishes inside the frog!")
                    new_conditions.append(condition) #since swallow doesnt fade unless the player breaks free or toad dies
            else:
                new_conditions.append(condition)
        creature.conditions = new_conditions

def select_combatants(available_players, monster_data, npc_data):
    contestants = []

    while True:
        choice_type = input("\nAdd a (P) - Player, (M) - Monster, (N) - NPC, or (D) - Done selecting? ").lower()
        
        if choice_type == 'd':
            if not contestants:
                print("You must select at least one combatant.")
                continue
            break

        elif choice_type == 'p':
            for idx, pl in enumerate(available_players, 1):
                print(f"{idx} - {pl.name}")
            try:
                choice = int(input("Select a player by number: "))
                if 0 <= choice <= len(available_players):
                    contestants.append(available_players[choice - 1])
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice_type in ('m', 'n'):
            data = monster_data if choice_type == 'm' else npc_data
            label = "Monster" if choice_type == 'm' else "NPC"

            #Build CR_list
            cr_list = []
            for entry in data.values():
                if entry["Challenge"] not in cr_list:
                    cr_list.append(entry["Challenge"])
            cr_list.sort()
            print(f"\nAvailable {label} Challenge Ratings:")
            print(f"0 - All {label}s")
            for idx, cr in enumerate(cr_list, 1):
                print(f"{idx} - CR {cr}")

            try:
                cr_choice = int(input(f"Choose a CR for {label}s (or 0 for All {label}s): "))
                if cr_choice == 0:
                    filtered_keys = list(data.keys())
                elif 1 <= cr_choice <= len(cr_list):
                    selected_cr = cr_list[cr_choice - 1]
                    filtered_keys = [key for key in data if data[key]["Challenge"] == selected_cr]
                else:
                    print("Invalid CR selection.")
                    continue
            except ValueError:
                print("Enter a valid number.")
                continue   

            if not filtered_keys:
                print(f"No {label}s found for selected CR.")
                continue

            print(f"\nAvailable {label}s:")
            print("0 - Random")
            for idx, key in enumerate(filtered_keys, 1):
                print(f"{idx} - {data[key]['Name']}")

            try:
                entity_choice = int(input(f"Choose a {label}: "))
                if entity_choice == 0:
                    selected_key = random.choice(filtered_keys)
                elif 1 <= entity_choice <= len(filtered_keys):
                    selected_key = filtered_keys[entity_choice - 1]
                else:
                    print("Invalid selection.")
                    continue
            except ValueError:
                print("Enter a valid number.")
                continue

            base_entity = Monster(data[selected_key])
            try:
                count = int(input(f"How many {base_entity.name}s to add? "))
                for i in range(1, count + 1):
                    entity_copy = copy.deepcopy(base_entity)
                    entity_copy.name = f"{base_entity.name} #{i}"
                    contestants.append(entity_copy)
            except ValueError:
                print("Invalid number.")

        else:
            print("Invalid input, choose P, M, N, or D.")
    return contestants

def choose_target(self, action_data, targets):
    target_name_list = []
    filtered_targets = []
    for t in targets:
        if ((action_data['Name'] == "Unarmed Strike: Grapple") or (action_data['Name'] == "Unarmed Strike: Shove")):
            if ((SIZE_ORDER.index(t.size) <= SIZE_ORDER.index(self.size) + 1) and (t != self)):
                target_name_list.append(t.name)
                filtered_targets.append(t)

        else:
            if t == self:
                target_name_list.append(f"{self.name} (Self)")
                filtered_targets.append(self)
            else:
                target_name_list.append(t.name)
                filtered_targets.append(t)
    while True:
        try:
            print("0 - Random Target")
            for i, tar in enumerate(target_name_list, 1):
                print(f"{i} - {tar}")
            choice = int(input("Choose a target. "))
            if choice == 0:
                target = random.choice(filtered_targets)
                break
            elif 1 <= choice <= len(target_name_list):
                target = filtered_targets[choice - 1]
                break   
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input, try again.")                        
    return target
     
def get_scaled_damage(scaling_dict, caster_level): #since we use "Scaling" so much
    keys = sorted(int(k) for k in scaling_dict.keys())
    applicable_level = max([lvl for lvl in keys if lvl <= caster_level], default=1)
    return scaling_dict[str(applicable_level)]

def evaluate_trait(creature, target, announcer, home_team):
    target_position = target.position
    traits = creature.traits
    trait_keys = list(traits.keys())
    print(f"{creature.name} has traits: {trait_keys}")
    for trait in trait_keys:
        if trait == "Bloodied Fury":
            if any(c.get("Name") == "Bloodied" for c in creature.conditions):
                creature.advantage = True
                print(f"{creature.name} has advantage because it is bloodied")
        if trait == "Pack Tactics":
            for ally in home_team:
                if ally is not creature:
                    print(f"The monster is: {creature.name}")
                    print(f"The ally is: {ally.name}")
                    ally_position = ally.position
                    x1, y1 = target_position
                    x2, y2 = ally_position
                    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                    if d <= 5 and not any(c.get("Name") == "Unconscious" for c in ally.conditions):
                        creature.advantage = True
                        print(f"{creature.name} gets advantage from Pack Tactics")
                        break #No need to keep checking allies if 1 meets the condition
        if trait == "Agile":
            creature.opportunity_attack_immune = True

def spawn_combatants(home_team, opponents):
    rows = 2
    cols = (len(home_team) + 1) // rows
    for i, c in enumerate(home_team):
        col = i % cols
        row = i // cols
        grid_x = -2 - col  
        grid_y = row - 1
        c.position = to_map_coords(grid_x, grid_y)
    cols = (len(opponents) + 1) // rows
    for i, c in enumerate(opponents):
        col = i % cols
        row = i // cols
        grid_x = 2 + col  
        grid_y = row - 1
        c.position = to_map_coords(grid_x, grid_y)

def setup_battlefield(home_team, opponents):
    print("Initializing battlefield.")
    spawn_combatants(home_team, opponents)
    print("Positions:")
    for c in home_team+opponents:
        print(f"{c.name} spawned at {c.position}")

def to_map_coords(grid_x,grid_y):
    return (grid_x * SQUARE_SIZE, grid_y * SQUARE_SIZE)

def to_grid_coords(pos_x, pos_y):
    return (round(pos_x / SQUARE_SIZE), round(pos_y / SQUARE_SIZE))

def get_occupied_squares(center_x, center_y, size):
    # Convert to grid square from feet
    grid_cx, grid_cy = to_grid_coords(center_x, center_y)

    # Map from size to how many grid squares the creature spans
    size_to_span = {
        "Tiny": 1,       # treated same as Small for now
        "Small": 1,
        "Medium": 1,
        "Large": 2,
        "Huge": 3,
        "Gargantuan": 4,
    }

    span = size_to_span.get(size, 1)
    half = span // 2

    squares = []
    for dx in range(-half, -half + span):
        for dy in range(-half, -half + span):
            squares.append((grid_cx + dx, grid_cy + dy))

    return squares

def opportunity_attack(creature, e, announcer, current_turn):                        
    available_actions = list(e.actions.keys())
    available_attacks = []
    for act in available_actions:
        if act == "Multiattack":
            attacks = e.actions[act]["Attacks"]
            for atk_key in attacks:
                attack = attacks[atk_key]
                print(f"Attack is {attack}")
                if "Melee" in attack.get("Attack Type"):
                    available_attacks.append(atk_key)
        else:
            attack = e.actions[act]
            if "Melee" in attack.get("Attack Type"):
                available_attacks.append(act)
    while True:
        try:
            print("0 - Random")
            for i, idx in enumerate(available_attacks, 1):
                print(f"{i} - {idx}")
            print(f"{i+1} - Skip Opportunity Attack")
            choice = int(input("What would you like to use for your opportunity attack, or would you? "))
            if choice == 0:
                attack_key = random.choice(available_attacks)
                break
            elif 1 <= choice <= len(available_attacks):
                attack_key = available_attacks[choice-1]
                break
            elif choice == len(available_attacks) + 1:
                print("Opportunity Attack Skipped") 
                attack_key = None
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input, try again.")
    if attack_key is not None:
        perform_melee_attack(creature, e, announcer, attack_key, current_turn)

def perform_melee_attack(target, attacker, announcer, attack_key, current_turn):
    if ((attack_key == "Bite" and "Hunter Shark" in attacker.name) or
        (attack_key == "Bite" and "Piranha" in attacker.name) or
        (attack_key == "Bites" and "Swarm of Piranhas" in attacker.name) or
        (attack_key == "Bite" and "Giant Shark" in attacker.name)):
        if target.currenthitpoints != target.hitpoints:
            attacker.advantage = True       
    print(f"{attacker.name} is attacking {target.name} with {attack_key}")
    random_atk_key = attacker.actions.get('Multiattack',{}).get('Attacks',{})
    if random_atk_key == {}:
        random_attack = attacker.actions[attack_key]
    else:
        random_attack = attacker.actions['Multiattack']['Attacks'][attack_key]
    attack1 = dice(20)
    attack2 = dice(20)
    
    if ((attacker.advantage == True) and (attacker.disadvantage == False)) or (attacker.advantage_against.get(f'{target.name}') == True):
        attack_roll = max(attack1, attack2)
        print(f"{attacker.name} has advantage, atk was {attack1} before, now it is {attack_roll}!")
    elif ((attacker.disadvantage == True) and (attacker.advantage == False)) or (attacker.disadvantage_against.get(f'{target.name}') == True):
        attack_roll = min(attack1, attack2)
        print(f"{attacker.name} has disadvantage, atk was {attack1} before, now it is {attack_roll}.")
    else:
        print(f"{attacker.name} rolls normally.") 
        attack_roll = attack1
    hit_mod = random_attack.get('Attack Bonus', 0)
    to_hit_roll = attack_roll + hit_mod
    damage_components = random_attack.get("Damage Components")
    print(f"To hit, you got a {attack_roll} + {hit_mod}, for a total of {to_hit_roll}, against {target.name}'s AC of {target.armor_class}")
    
    if attack_roll == 1:
        print("Natural 1! You fumble!")
    elif attack_roll == 20:
        print("Crit! Auto-hit, rolling crit damage...")
        if damage_components:
            for i, comp in enumerate(damage_components):
                dice_str = comp.get("Dice", "0")
                if dice_str.strip().isdigit():
                    dice_str = f"{dice_str.strip()}d1"
                dice_mod = comp.get("Modifier", "0")
                dice_str = dice_str+"+"+dice_mod
                if "Swarm of Venomous Snakes" in attacker.name:
                    if any(c.get("Name") == "Bloodied" for c in attacker.conditions):
                        if i == 0:
                            dice_str = random_attack['Bloodied Damage']
                        print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dice_str}")
                damage_type = comp.get("Type", "Unknown")
                dmg = crit(dice_str, announcer)
                print(f"{attacker.name} crits {target.name} for {dmg} {damage_type} damage!")
                target.take_damage(dmg, damage_type, announcer)  
        else:
            dmg_dice = random_attack['Damage']
            if "Conditional Extra" in random_attack:
                conditional = random_attack.get("Conditional Extra", {})
                req_cond = conditional.get("Condition")
                if any(c.get("Name") == req_cond for c in target.conditions):
                    print(f"{target.name} is taking extra damage because they are {req_cond}")
                    dmg_dice = conditional["Damage"]
                elif any(c.get("Name") == req_cond for c in attacker.conditions):
                    if "Swarm of" in attacker.name:
                        dmg_dice = conditional["Damage"]
                        print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dmg_dice}")
            dmg = crit(dmg_dice, announcer)
            damage_type = random_attack['Damage Type']
            print(f"{attacker.name} crits {target.name} with {random_attack['Name']}, dealing {dmg} {damage_type} damage!")
            target.take_damage(dmg, damage_type, announcer)
        process_effects(random_attack, attacker, target, current_turn)               
    elif to_hit_roll >= target.armor_class:
        if damage_components:
            for comp in damage_components:
                dice_str = comp.get("Dice", "0")
                if dice_str.strip().isdigit():
                    dice_str = f"{dice_str.strip()}d1"                            
                dice_mod = comp.get("Modifier", "0")
                dice_str = dice_str+"+"+dice_mod     
                if "Swarm of Venomous Snakes" in attacker.name:
                    if any(c.get("Name") == "Bloodied" for c in attacker.conditions):
                        dice_str = attack_key['Bloodied Damage']
                        print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dice_str}")                                                   
                damage_type = comp.get("Type", "Unknown")
                dmg = roll(dice_str)
                print(f"{attacker.name} hits {target.name} for {dmg} {damage_type} damage!")
                target.take_damage(dmg, damage_type, announcer)                              
        else:                    
            dmg_dice = random_attack['Damage']
            if "Conditional Extra" in random_attack:
                conditional = random_attack.get("Conditional Extra", {})
                req_cond = conditional.get("Condition")
                if any(c.get("Name") == req_cond for c in target.conditions):
                    print(f"{target.name} is taking extra damage because they are {req_cond}")
                    dmg_dice = conditional["Damage"]
                elif any(c.get("Name") == req_cond for c in attacker.conditions):
                    if "Swarm of" in attacker.name:
                        dmg_dice = conditional["Damage"]
                        print(f"Since {attacker.name} is bloodied, their damage has been reduced to {dmg_dice}")                                
            dmg = roll(dmg_dice)
            damage_type = random_attack['Damage Type']
            print(f"{attacker.name} hits {target.name} with {random_attack['Name']}, dealing {dmg} {damage_type} damage!")
            target.take_damage(dmg, damage_type, announcer)
        process_effects(random_attack, attacker, target, current_turn)        
    else:
        print(f"{attacker.name} missed {target.name}")

def distance(creature_a, creature_b): #This is a different version of it, written since size is now a thing to consider
    squares_a = occupied_squares(creature_a)
    squares_b = occupied_squares(creature_b)
    
    return min(
        math.hypot((ax - bx) * SQUARE_SIZE, (ay - by) * SQUARE_SIZE)
        for ax, ay in squares_a
        for bx, by in squares_b
    )        
def occupied_squares(creature): #This will take a creatures size and get how many squares they take up and add that to the position, for purposes of opportunity attacks.
    x0, y0 = to_grid_coords(*creature.position)
    SIZE_MAPPING = {
        "Tiny": 1,
        "Small": 1,
        "Medium": 1,
        "Large": 2,
        "Huge": 3,
        "Gargantuan": 4
    }
    size = SIZE_MAPPING[creature.size]
    return [(x0 + dx, y0 + dy) for dx in range(size) for dy in range(size)]

def controller_of(creature):
    return creature.team.controller

def run_ai_turn(creature):
    pass

def get_movement_options(creature, announcer, home_team, opponent_team, double):
    base_speed = max(creature.speed.values())
    effective_speed = base_speed * 2 if double else base_speed    
    all_combatants = home_team + opponent_team
    grid_x, grid_y = to_grid_coords(*creature.position)
    options = []

    # Add random valid grid spot
    dx, dy = random_grid_offset_within_speed(effective_speed)
    rand_gx, rand_gy = grid_x + dx, grid_y + dy
    if not is_square_occupied(rand_gx, rand_gy, all_combatants, creature):
        options.append(((rand_gx, rand_gy), "Random")) 
    else:
        print("The square is occupied, random was not added.")   
 
    if creature in home_team:
        opposing_team = opponent_team
    elif creature in opponent_team:
        opposing_team = home_team
    

    for target in opposing_team:
        tx, ty = to_grid_coords(*target.position)
        adj = [(tx + dx, ty + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)] #These are the 8 adjacent spots to the target
        for gx, gy in adj:
            if not is_square_occupied(gx, gy, all_combatants, creature):
                mx, my = to_map_coords(gx, gy)
                if distance(creature, target) <= effective_speed:
                    options.append(((gx, gy), f"Adjacent to {target.name}"))

    return options               

def check_opportunity_attack(creature, movement_type, trait_list):
    immune = False
    if creature.opportunity_attack_immune == True:
        immune = True
    if "Agile" in trait_list:
        immune = True
    if (("Flyby" in trait_list) and (movement_type == "Fly")):
        immune = True   

    return immune