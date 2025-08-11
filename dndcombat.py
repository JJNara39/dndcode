import random
import copy
from dnd_python_classes import Player, Monster, Team, Announcer
from dnd_monsters import monsters
from dnd_npc import npcs
from dnd_languagesskills import *
from dnd_combat_fn import *

def combat(player):
    announcer = Announcer()
    for pl in player:
        print(f"Player name and ac is: {pl.name} and {pl.armor_class}")
        pl.deathsave_success = 0
        pl.deathsave_fail = 0        
    monsters_data = monsters
    npc_data = npcs
    
    #This below list/while loop is meant to allow 2 people to clash with any combination of players/monsters
    #My plan with this was Marik v Dark Marik, or 100 Humans v 1 Silverback Gorilla
    print("Who is controlling Team 1? Enter name or 'AI':")
    team1_controller = input("> ").strip()
    print(f"Choose team for {team1_controller}:") #player1[:] makes a shallow copy, so we need to go deeper, with deepcopy
    contestant1_team = []

    for cr in select_combatants(player[:], monsters_data, npc_data):
        cr_copy = copy.deepcopy(cr)
        cr_copy.original_name = cr_copy.name
        cr_copy.name += f" from {team1_controller}'s Team"
        contestant1_team.append(cr_copy)

    team1 = Team(team1_controller, contestant1_team)
    for member in team1.members:
        member.team = team1
    
    print("Who is controlling Team 2? Enter name or 'AI':")
    team2_controller = input("> ").strip()
    print(f"Choose team for {team2_controller}:")
    contestant2_team = []
    for cr in select_combatants(player[:], monsters_data, npc_data):
        cr_copy = copy.deepcopy(cr)
        cr_copy.original_name = cr_copy.name
        cr_copy.name += f" from {team2_controller}'s Team"
        contestant2_team.append(cr_copy)

    team2 = Team(team2_controller, contestant2_team)
    for member in team2.members:
        member.team = team2

    combat_state = {
        "Participants": [],       # list of Creature objects, sorted by initiative
        "Turn_index": 0,          # whose turn it is in the list
        "Global_turn_counter": 0  # ticks once per full round
    }
    print("Lets roll for initiative!")
    initiative_tracker = []

    all_contestants = contestant1_team + contestant2_team

    for creature in all_contestants:
        initiative = dice(20) + creature.initiative
        initiative_tracker.append((creature, initiative))
        combat_state['Participants'].append(creature)
        if isinstance(creature, Player):
            print(f"{creature.name}({creature.playername}) gets {initiative} for initiative.")
        if isinstance(creature, Monster):
            print(f"{creature.name} gets {initiative} for initiative.")

    # Sort initiative from highest to lowest
    initiative_tracker.sort(key=lambda x: x[1], reverse=True)
    print("\n=== Initiative Order ===")
    for fighter, init in initiative_tracker:
        if isinstance(fighter, Player):
            print(f"Player - {fighter.name}: {init}")   
        if isinstance(fighter, Monster):
            print(f"Monster - {fighter.name}: {init}")

    #Map stuff will go here after all creatures are made but before combat starts so we can place them
    setup_battlefield(contestant1_team, contestant2_team)
    for c1 in contestant1_team:
        for c2 in contestant2_team:
            print(f"Distance between {c1.name} and {c2.name} is {distance(c1,c2)}ft.")

    turn_number = 1
    has_acted_this_round = {fighter.name: False for fighter, _ in initiative_tracker}
    print("Time for Combat!")
    while True:
        announcer.announce("start_round", round_num=turn_number) 
        attacker, init = initiative_tracker[0]
        if controller_of(attacker) == "AI":
            run_ai_turn(attacker)
        else:
            has_acted_this_round[attacker.name] = True
            print(f"{attacker.name}'s turn!")
            if attacker.conditions:
                print("Conditions it has:")
                for condition in attacker.conditions:
                    print(f"- {condition['Name']}")
            else:
                print("No conditions.")             
                
            print(f"Turn number is: {turn_number}")
            turn_status = "Start"
            remove_expired_conditions(attacker, all_contestants, announcer, turn_number, turn_status)   
            if attacker in contestant1_team:
                home_team = contestant1_team
                opponents = contestant2_team
            elif attacker in contestant2_team:
                home_team = contestant2_team
                opponents = contestant1_team     

            targets = []
            for target in opponents:
                if (not any(c.get("Name") == "Swallowed" for c in target.conditions)
                or (target.conscious == True) or target.currenthitpoints > 0):
                    targets.append(target)
                    print(f"Available Targets: {target.name}")       
            available_attacks = list(attacker.actions.keys())
            evaluate_trait(creature, target, announcer, home_team) 
            #Check Giant Frog, special case
            target = None
            if ("Giant Frog" in attacker.name) or ("Giant Toad" in attacker.name):
                # Check if the frog is currently grappling a Small (or smaller) creature
                grappling_target = None
                for grappled in attacker.grappling: 
                    target = grappled
                    if "Giant Frog" in attacker.name:
                        target_size = "Small"
                    if "Giant Toad" in attacker.name:
                        target_size = "Medium"
                    if SIZE_ORDER.index(target.size) <= SIZE_ORDER.index(target_size):
                        grappling_target = target
                        break
                if grappling_target:
                    atk_key = "Swallow"
                    target = grappling_target  # set target to the one it's grappling
                    if target:
                        perform_swallow(attacker, target, announcer, turn_number)
                    else:
                        print(f"No target, {attacker.name} skips its attack action.")
                else:
                    if "Giant Frog" in attacker.name:
                        atk_key = "Bite"  # default   
                        if targets:
                            target = random.choice(targets)                        
                            perform_attack(attacker, target, announcer, turn_number, home_team, opponents, initiative_tracker, WeaponorSpell="Weapon", attack_key=atk_key)           
                        else:
                            print(f"No target, {attacker.name} skips its attack action.")
                    elif "Giant Toad" in attacker.name:
                        if attacker.has_swallowed == True:
                            print(f"{attacker.name} cannot attack while a person is swallowed.")
                        else:
                            atk_key = "Bite"
                            if targets:
                                target = random.choice(targets) 
                                perform_attack(attacker, target, announcer, turn_number, home_team, opponents, initiative_tracker, WeaponorSpell="Weapon", attack_key=atk_key)           
            else: 
                if attacker.currenthitpoints > 0:  
                    take_turn(attacker, announcer, turn_number, player, contestant1_team, contestant2_team, initiative_tracker)
                elif attacker.currenthitpoints <= 0 and not isinstance(attacker, Monster):
                    if attacker.dead == False:
                        print(f"Time for {attacker.name} to make a death save!")
                        deathsave = dice(20)
                        if deathsave == 20:
                            announcer.announce("death_save_crit_success", attacker.name)
                            attacker.deathsave_success = 0
                            attacker.deathsave_fail = 0
                            for c in attacker.conditions:
                                if c.get("Name") == "Unconscious":
                                    attacker.conditions.remove(c)  
                            attacker.currenthitpoints = 1
                            take_turn(attacker, announcer, turn_number, player, contestant1_team, contestant2_team, initiative_tracker)                                                    
                        elif 10 <= deathsave < 20:
                            announcer.announce("death_save_success", attacker.name)
                            attacker.deathsave_success += 1
                        elif 1 < deathsave <= 9:
                            announcer.announce("death_save_fail", attacker.name)
                            attacker.deathsave_fail += 1
                        elif deathsave == 1:
                            announcer.announce("death_save_crit_fail", attacker.name)
                            attacker.deathsave_fail += 2
                        if attacker.deathsave_success >= 3:
                            announcer.announce("stable", attacker.name)
                            attacker.deathsave_success = 0
                            attacker.deathsave_fail = 0
                            attacker.currenthitpoints = 0
                            for c in attacker.conditions:
                                if c.get("Name") == "Unconscious":
                                    attacker.conditions.remove(c) 
                            condition_to_apply = {
                                "Name": "Stable",
                                "Target": target
                            }      
                            attacker.conditions.append(condition_to_apply)
                        elif attacker.deathsave_fail >= 3:          
                            announcer.announce("death", attacker.name)
                            attacker.dead = True
            #Code in death saves!
            turn_status = "End"
            remove_expired_conditions(attacker, all_contestants, announcer, turn_number, turn_status) 
            #End of turn, rotate tracker
            initiative_tracker.append(initiative_tracker.pop(0))

            if check_combat_end(player, announcer, contestant2_team):
                print(f"Contestant 1 with {', '.join(con.original_name for con in contestant1_team)} wins!")
                break  
            if check_combat_end(player, announcer, contestant1_team):
                print(f"Contestant 2 with {', '.join(con.original_name for con in contestant2_team)} wins!")
                break          
        # End of round check
        if all(has_acted_this_round.values()):
            turn_number += 1
            has_acted_this_round = {fighter.name: False for fighter, _ in initiative_tracker}
            print(f"\n--- Round {turn_number} begins ---\n")          