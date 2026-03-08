spells = {
    "Acid Splash": {
        "Name": "Acid Splash",
        "Level": 0,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Save": "DEX",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Acid",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        },        
        "Description": (
            "You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range "
            "that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take "
            "acid damage. The damage increases at certain levels."
        )
    },    
    "Aid": {
        "Name": "Aid",
        "Level": 2,
        "School": "Abjuration",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "8 hours",
        "Spell List": ['Artificer', 'Bard', 'Cleric', 'Paladin', 'Ranger'],
        "Components": ["V", "S", "M (a tiny strip of white cloth)"],
        "Description": (
            "Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range. "
            "Each target's hit point maximum and current hit points increase by 5 for the duration.\n\n"
            "When you cast this spell using a spell slot of 3rd level or higher, a target's hit points increase by an "
            "additional 5 for each slot level above 2nd."
        ),
        "Effect": {
            "Type": "HP Increase",
            "Scaling": {
                2: 5,
                3: 10,
                4: 15,
                5: 20,
                6: 25,
                7: 30,
                8: 35,
                9: 40
            }
        }
    },   
    "Alarm": {
        "Name": "Alarm",
        "Level": 1,
        "School": "Abjuration",
        "Ritual": True,
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "8 hours",
        "Spell List": ["Artificer", "Ranger", "Wizard"],
        "Components": ["V", "S", "M (a tiny bell and a piece of fine silver wire)"],
        "Description": (
            "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger "
            "than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or "
            "enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm.\n\n"
            "You also choose whether the alarm is mental or audible. A mental alarm alerts you with a ping in your mind if you "
            "are within 1 mile of the warded area. An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet."
        )
    },    
    "Alter Self": {
        "Name": "Alter Self",
        "Level": 2,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "1 hour (concentration)",
        "Spell List": ["Artificer", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You assume a different form. When you cast this spell, choose one of the following options, the effects of which "
            "last for the duration. While the spell lasts, you can end one option as an action to gain the benefits of a different one."
        ),
        "Options": {
            "Aquatic Adaptation": (
                "You adapt to an aquatic environment: you grow gills and webbing between your fingers. "
                "You can breathe underwater and gain a swimming speed equal to your walking speed."
            ),
            "Change Appearance": (
                "You transform your appearance. You decide what you look like, including your height, weight, facial features, "
                "sound of your voice, hair length, coloration, and distinguishing characteristics, if any. You can make yourself appear "
                "as a member of another race, though none of your statistics change. You also can't appear as a creature of a different "
                "size or a different limb configuration."
            ),
            "Natural Weapons": (
                "You grow natural weapons like claws, fangs, spines, horns, or a different natural weapon of your choice. "
                "Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing damage, as appropriate. You are proficient with these natural weapons."
            )
        }
    },     
    "Animal Friendship": {
        "Name": "Animal Friendship",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "24 hours",
        "Spell List": ["Bard", "Druid", "Ranger"],
        "Components": ["V", "S", "M (a morsel of food)"],
        "Description": (
            "This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. "
            "It must see and hear you. If the beast’s Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed "
            "on a Wisdom saving throw or be charmed by you for the spell’s duration. If you or one of your companions harms the target, the spell ends."
        ),
        "Effect": {
            "Type": "Beasts Affected",
            "Scaling": {
                1: 1,
                2: 2,
                3: 3,
                4: 4,
                5: 5,
                6: 6,
                7: 7,
                8: 8,
                9: 9
            }            
        }
    },    
    "Animal Messenger": {
        "Name": "Animal Messenger",
        "Level": 2,
        "School": "Enchantment",
        "Ritual": True,
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "24 hours",
        "Spell List": ['Bard', 'Druid', 'Ranger'],
        "Components": ["V", "S", "M (a morsel of food)"],
        "Description": (
            "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, "
            "a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as "
            "'a man or woman dressed in the uniform of the town guard' or 'a red-haired dwarf wearing a pointed hat.'\n\n"
            "You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the location, "
            "covering about 50 miles per 24 hours. When it arrives, it delivers your message to the creature that you described, replicating the sound "
            "of your voice. The messenger speaks only to a creature matching the description you gave."
        ),
        "Effect": {
            "Type": "Duration",
            "Scaling": {
                2: "24 hours",
                3: "48 hours",
                4: "96 hours",
                5: "144 hours",
                6: "192 hours",
                7: "240 hours",
                8: "288 hours",
                9: "336 hours"
            }  
        }
    },    
    "Animal Shapes": {
        "Name": "Animal Shapes",
        "Level": 8,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Up to 24 hours (concentration)",
        "Spell List": ["Druid"],
        "Components": ["V", "S"],        
        "Description": (
            "Your magic turns others into beasts. Choose any number of willing creatures within range. You transform each target into the beast form "
            "of your choice. The transformation lasts for the duration, or until a target drops to 0 hit points or dies.\n\n"
            "You can choose the same form or different ones for each target. The new form can be any beast with a challenge rating of 1 or lower. "
            "A target’s game statistics are replaced by the statistics of the chosen beast, though they retain their Intelligence, Wisdom, and Charisma scores. "
            "They also retain their alignment and personality.\n\n"
            "Each target assumes the hit points of its new form. When the spell ends, the creature returns to its normal hit points. "
            "If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form."
        )
    },    
    "Animate Dead": {
        "Name": "Animate Dead",
        "Level": 3,
        "School": "Necromancy",
        "Casting Time": "1 minute",
        "Range": "10 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Cleric", "Wizard"],
        "Components": ["V", "S", "M (a drop of blood, a piece of flesh, and a pinch of bone dust)"],
        "Description": (
            "You raise the dead to serve you. Choose a pile of bones or a corpse of a Medium or Small humanoid within range. "
            "The target must have been dead no longer than 24 hours. The creature becomes a skeleton or zombie (your choice), "
            "which is under your control.\n\n"
            "The creature can be commanded to perform any task or serve as a guardian. The creature has the same statistics it had in life, "
            "except that its Intelligence and Charisma scores become 2, it cannot cast spells, and it obeys only your commands.\n\n"
            "At the end of each of the creature's turns, it must make a Wisdom saving throw. On a failed save, the creature falls under your control until "
            "it takes damage. On a successful save, the creature acts independently and may take actions on its own.\n\n"
            "You can control up to 4 creatures with this spell. You may raise additional creatures by using additional spell slots of level 3 or higher."
        ),    
        "Effect": {
            "Type": "Animate Undead Creatures",
            "Scaling" : {
                3: 4,
                4: 6,
                5: 8, 
                6: 10,
                7: 12,
                8: 14,
                9: 16
            }
        }
    },
    #Animate Objects
    "Antilife Shell": {
        "Name": "Antilife Shell",
        "Level": 5,
        "School": "Abjuration",
        "Casting Time": "1 action",
        "Range": "Self (10 feet radius)",
        "Duration": "Concentration, up to 1 hour",
        "Spell List": ["Druid"],
        "Components": ["V", "S"],
        "Description": (
            "A shimmering barrier surrounds you. You create a spherical force field with a 10-foot radius around you. "
            "The barrier prevents creatures that are not undead or constructs from passing through it. Any creature attempting to pass through the barrier "
            "must succeed on a Strength saving throw or be pushed back 10 feet.\n\n"
            "The barrier doesn’t prevent spells from affecting you, but it does block any creature from attacking you with melee or ranged attacks, "
            "and creatures cannot enter or exit the barrier unless they are undead.\n\n"
            "The barrier lasts for the duration, or until you lose concentration."
        )
    }, 
    "Arms of Hadar": {
        "Name": "Arms of Hadar",
        "Level": 1,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "Self (10 foot radius)",
        "Duration": "Instantaneous",
        "Spell List": ["Warlock"],
        "Components": ["V", "S"],
        "Description": (
            "Tendrils of dark energy erupt from you and batter all creatures within 10 feet. Each creature must make a Strength saving throw. "
            "On a failed save, a target takes 2d6 necrotic damage and can’t take reactions until its next turn. On a successful save, the creature takes half damage but suffers no other effect."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Necrotic",
            "Scaling": {
                1: "2d6",
                2: "3d6",
                3: "4d6",
                4: "5d6",
                5: "6d6",
                6: "7d6",
                7: "8d6",
                8: "9d6",
                9: "10d6"

            }
        }
    },
    "Bane": {
        "Name": "Bane",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Bard", "Cleric"],
        "Components": ["V", "S", "M (a drop of blood)"],
        "Description": (
            "Up to three creatures of your choice within range must make Charisma saving throws. "
            "Whenever a target that fails this saving throw makes an attack roll or a saving throw before the spell ends, "
            "the target must roll a d4 and subtract the number rolled from the attack roll or saving throw."
        ),
        "Effect": {
            "Type": "Debuff (-1d4 on attacks and saves)",
            "Scaling": {
                1: "Affects 3 creatures",
                2: "Affects 4 creatures",
                3: "Affects 5 creatures",
                4: "Affects 6 creatures",
                5: "Affects 7 creatures",
                6: "Affects 8 creatures",
                7: "Affects 9 creatures",
                8: "Affects 10 creatures",
                9: "Affects 11 creatures"
            }
        }
    },    
    "Bless": {
        "Name": "Bless",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Cleric", "Paladin"],
        "Components": ["V", "S", "M"],
        "Materials": "A sprinkling of holy water",
        "Description": (
            "You bless up to three creatures of your choice within range. Whenever a target makes an attack roll or a "
            "saving throw before the spell ends, the target can roll a d4 and add the number rolled to the attack roll "
            "or saving throw."
        ),
        "Effect": {
            "Type": "Buff",
            "Scaling": {
                2: "Bless 1 additional creature (4 total)",
                3: "Bless 2 additional creatures (5 total)",
                4: "Bless 3 additional creatures (6 total)",
                5: "Bless 4 additional creatures (7 total)",
                6: "Bless 5 additional creatures (8 total)",
                7: "Bless 6 additional creatures (9 total)",
                8: "Bless 7 additional creatures (10 total)",
                9: "Bless 8 additional creatures (11 total)"
            }
        }
    },    
    "Blade Ward": {
        "Name": "Blade Ward",
        "Level": 0,
        "School": "Abjuration",
        "Casting Time": "1 action",
        "Range": "Self",
        "Spell List": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Effect": {
            "Type" : "Player Buff",
            "Resistance" : ["Bludgeoning", "Piercing", "Slashing"],
            "Duration": 1 #in rounds
        },
        "Description": (
            "You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance "
            "against bludgeoning, piercing, and slashing damage dealt by weapon attacks."
        )
    },
    "Booming Blade": {
        "Name": "Booming Blade",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Self (5 foot radius)",
        "Duration": 1,
        "Spell List": ["Sorcerer", "Warlock", "Wizard", "Artificer"],
        "Components": ["S", "M"],
        "Materials": "A melee weapon worth at least 1 sp",
        "Description": (
            "You brandish the weapon used in the spell’s casting and make a melee attack with it against one creature within 5 feet of you. "
            "On a hit, the target suffers the weapon attack’s normal effects, and it becomes sheathed in booming energy until the start of your next turn. "
            "If the target willingly moves before then, it immediately takes 1d8 thunder damage. "
            "This spell’s damage increases when you reach higher levels."
        ),
        "Effect": {
            "Type": "Weapon Buff",
            "Conditions": {
                'Name': "Booming Blade",
                'MovementScaling': {
                    1: {'NumDice': 1, 'Dice': 8, 'Type': 'Thunder'},
                    5: {'NumDice': 2, 'Dice': 8, 'Type': 'Thunder'},
                    11: {'NumDice': 3, 'Dice': 8, 'Type': 'Thunder'},
                    17: {'NumDice': 4, 'Dice': 8, 'Type': 'Thunder'},
                },
                "Trigger": "Move",
                "Duration": 1,
                "Expires": "EndOfSourceTurn",
            },
            "Damage Type": "Thunder",
            "Scaling": {
                5: "1d8",
                11: "2d8",
                17: "3d8"
            }
        },    
    }, 
    "Burning Hands": {
        "Name": "Burning Hands",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Self (15-foot cone)",
        "Duration": "Instantaneous",
        "Spell List": ["Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. "
            "Each creature in a 15-foot cone must make a Dexterity saving throw. "
            "A creature takes fire damage on a failed save, or half as much damage on a successful one."
        ),
        "Effect": {
            "Type": "Damage (Fire)",
            "Scaling": {
                1: "3d6",
                2: "4d6",
                3: "5d6",
                4: "6d6",
                5: "7d6",
                6: "8d6",
                7: "9d6",
                8: "10d6",
                9: "11d6"
            }
        }
    },    
    "Charm Person": {
        "Name": "Charm Person",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "1 hour",
        "Spell List": ["Bard", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions "
            "are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. "
            "The charmed creature regards you as a friendly acquaintance. When the spell ends, the creature knows it was charmed by you."
        ),
        "Effect": {
            "Type": "Charm"
        }
    },    
    "Control Flames": {
        "Name": "Control Flames",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "60 feet (5-foot Cube)",
        "Duration": "Instantaneous or 1 hour",
        "Spell List": ["Druid", "Sorcerer", "Wizard"],
        "Components": ["S"],
        "Description": "You choose nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of several ways: expand it, extinguish it, double or halve its brightness, or cause simple shapes like letters to appear in the flames for 1 hour. You can affect up to three flames at once.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },       
    "Create Bonfire": {
        "Name": "Create Bonfire",
        "Level": 0,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Artificer", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Description": "You create a bonfire on the ground in a space you can see within range. Any creature in the bonfire's space when you cast the spell must succeed on a Dexterity saving throw or take fire damage. A creature must also make the saving throw when it enters the bonfire's space for the first time on a turn or ends its turn there.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Fire",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },    
    "Create or Destroy Water": {
        "Name": "Create or Destroy Water",
        "Level": 1,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Cleric", "Druid"],
        "Components": ["V", "S", "M (a drop of water if creating water or a few grains of sand if destroying it)"],
        "Description": (
            "You either create or destroy water.\n\n"
            "**Create Water.** You create up to 10 gallons of clean water within range in an open container.\n"
            "**Destroy Water.** You destroy up to 10 gallons of water in an open container or fog in a 30-foot cube."
        ),
        "Effect": {
            "Type": "Utility",
            "Scaling": {
                1: "10 gallons",
                2: "20 gallons",
                3: "30 gallons",
                4: "40 gallons",
                5: "50 gallons",
                6: "60 gallons",
                7: "70 gallons",
                8: "80 gallons",
                9: "90 gallons"
            }
        }
    },    
    "Chill Touch": {
        "Name": "Chill Touch",
        "Level": 0,
        "School": "Necromancy",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "1 round",
        "Spell List": ["Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. "
            "On a hit, the target takes 1d8 necrotic damage, and it can’t regain hit points until the start of your next turn. "
            "Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn. "
            "The damage increases at higher levels."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Necrotic",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },
    "Clairvoyance": {
        "Name": "Clairvoyance",
        "Level": 3,
        "School": "Divination",
        "Casting Time": "10 minutes",
        "Range": "1 mile",
        "Duration": "Concentration, up to 10 minutes",
        "Spell List": ["Bard", "Cleric", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M"],
        "Materials": "A focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing",
        "Description": (
            "You create an invisible sensor within range in a location familiar to you (a place you have visited or seen before) "
            "or in an obvious location that is unfamiliar to you (such as behind a door, around a corner, or in a grove of trees). "
            "The sensor remains in place for the duration, and it can’t be attacked or otherwise interacted with. "
            "When you cast the spell, you choose seeing or hearing. You can use the chosen sense through the sensor as if you were in its space. "
            "As your action, you can switch between seeing and hearing. "
            "A creature that can see the sensor (such as a creature benefitting from see invisibility or truesight) sees a luminous, intangible orb about the size of your fist."
        )
    },    
    "Color Spray": {
        "Name": "Color Spray",
        "Level": 1,
        "School": "Illusion",
        "Casting Time": "1 action",
        "Range": "15 feet",
        "Duration": "1 round",
        "Spell List": ["Bard", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M"],
        "Materials": "A pinch of powder or sand that is colored red, yellow, and blue",
        "Description": (
            "A dazzling array of flashing, colored light springs from your hand. Roll 6d10; the total is how many hit points of creatures this spell can affect. "
            "Starting with the creature that has the lowest current HP, each creature in a 15-foot cone originating from you is blinded until the end of your next turn, subtracting HP from the total as you go. "
            "The spell ignores unconscious creatures and creatures that can't see. "
            "Starting with the creature that has the lowest current hit points, each creature affected by this spell is blinded until the spell ends. Subtract each creature’s hit points from the total before moving on to the creature with the next lowest hit points. A creature’s hit points must be equal to or less than the remaining total for the creature to be affected."
            "At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d10 for each slot level above 1st."        
        ),
        "Effect": {
            "Type": "Control",
            "Tags": ["Blind", "Area"]
        }
    },    
    "Command": {
        "Name": "Command",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "1 round",
        "Spell List": ["Bard", "Cleric", "Paladin"],
        "Components": ["V"],
        "Description": (
            "You speak a one-word command to a creature you can see within range. "
            "The target must succeed on a Wisdom saving throw or follow the command on its next turn. "
            "The spell has no effect if the target is undead, doesn't understand your language, or if your command is directly harmful to it."
        ),
        "Effect": {
            "Type": "Control (Command)",
            "Scaling": {
                1: "1 target",
                2: "2 targets",
                3: "3 targets",
                4: "4 targets",
                5: "5 targets",
                6: "6 targets",
                7: "7 targets",
                8: "8 targets",
                9: "9 targets"
            }
        }
    },    
    "Cure Wounds": {
        "Name": "Cure Wounds",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Bard", "Cleric", "Druid", "Paladin", "Ranger"],
        "Components": ["V", "S"],
        "Description": (
            "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. "
            "This spell has no effect on undead or constructs."
        ),
        "Effect": {
            "Type": "Healing",
            "Scaling": {
                1: "1d8 + spellcasting ability modifier",
                2: "2d8 + spellcasting ability modifier",
                3: "3d8 + spellcasting ability modifier",
                4: "4d8 + spellcasting ability modifier",
                5: "5d8 + spellcasting ability modifier",
                6: "6d8 + spellcasting ability modifier",
                7: "7d8 + spellcasting ability modifier",
                8: "8d8 + spellcasting ability modifier",
                9: "9d8 + spellcasting ability modifier"
            }
        }
    },    
    "Dancing Lights": {
        "Name": "Dancing Lights",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Artificer", "Bard", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M (a bit of phosphorus or wychwood, or a glowworm)"],
        "Description": "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air. You can also combine them into one vaguely humanoid form. Each light sheds dim light in a 10-foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },    
    "Detect Magic": {
        "Name": "Detect Magic",
        "Level": 1,
        "School": "Divination",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "Concentration, up to 10 minutes",
        "Spell List": ["Artificer", "Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Ritual": True,
        "Description": (
            "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, "
            "you can use your action to see a faint aura around any visible creature or object in the area that bears "
            "magic, and you learn its school of magic, if any. The spell can penetrate most barriers, but it is blocked "
            "by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."
        )
    },    
    "Detect Evil and Good": {
        "Name": "Detect Evil and Good",
        "Level": 1,
        "School": "Divination",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "Concentration, up to 10 minutes",
        "Spell List": ["Cleric", "Paladin"],
        "Components": ["V", "S"],
        "Ritual": False,
        "Description": (
            "For the duration, you know if there is an aberration, celestial, elemental, fey, fiend, or undead "
            "within 30 feet of you, as well as where the creature is located. Similarly, you know if there is a place "
            "or object within 30 feet of you that has been magically consecrated or desecrated. "
            "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, "
            "a thin sheet of lead, or 3 feet of wood or dirt."
        )
    },    
    "Disguise Self": {
        "Name": "Disguise Self",
        "Level": 1,
        "School": "Illusion",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "1 hour",
        "Spell List": ["Artificer", "Bard", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You make yourself—including your clothing, armor, weapons, and other belongings on your person—look different until the spell ends or until you "
            "use your action to dismiss it. You can seem 1 foot shorter or taller and can appear thin, fat, or in between. You can't change your body type, so you must adopt "
            "a form that has the same basic arrangement of limbs. Otherwise, the extent of the illusion is up to you."
        ),
        "Effect": {
            "Type": "Utility",
            "Tags": ["Illusion", "Social"]
        }
    },    
    "Dissonant Whispers": {
        "Name": "Dissonant Whispers",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Bard"],
        "Components": ["V"],
        "Description": (
            "You whisper a discordant melody that only one creature of your choice within range can hear, wracking it with terrible pain. "
            "It must make a Wisdom saving throw. On a failed save, it takes psychic damage and must immediately use its reaction to move "
            "as far as its speed allows away from you. The creature doesn't move into obviously dangerous ground. On a successful save, "
            "it takes half damage and doesn't have to move."
        ),
        "Effect": {
            "Type": "Damage (Psychic) + Forced Movement",
            "Scaling": {
                1: "3d6 psychic + flee on fail",
                2: "4d6 psychic + flee on fail",
                3: "5d6 psychic + flee on fail",
                4: "6d6 psychic + flee on fail",
                5: "7d6 psychic + flee on fail",
                6: "8d6 psychic + flee on fail",
                7: "9d6 psychic + flee on fail",
                8: "10d6 psychic + flee on fail",
                9: "11d6 psychic + flee on fail"
                
            }
        }
    },    
    "Divine Favor": {
        "Name": "Divine Favor",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 bonus action",
        "Range": "Self",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Paladin"],
        "Components": ["V", "S"],
        "Description": (
            "Your prayer empowers your weapon strikes with divine radiance. Until the spell ends, your weapon attacks deal an extra 1d4 radiant damage on a hit."
        ),
        "Effect": {
            "Type": "Buff",
            "Buff": "Weapon damage bonus",
            "Damage Type": "Radiant",
            "Scaling": {
                1: "1d4"
            }
        }
    },    
    "Druidcraft": {
        "Name": "Druidcraft",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Druid"],
        "Components": ["V", "S"],
        "Description": "Whispering to the spirits of nature, you create one of the following effects within range:\n- Predict the weather for the next 24 hours.\n- Instantly make a flower bloom, a seed pod open, or a leaf bud bloom.\n- Instantly light or snuff out a candle, torch, or small campfire.\n- Create an instantaneous harmless sensory effect, such as falling leaves, a puff of wind, the sound of a small animal, or the faint odor of skunk.\n- Create a tiny, harmless sensory effect that lasts for 1 round.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },    
    "Earth Tremor": {
        "Name": "Earth Tremor",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "10 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Bard", "Druid", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You cause a tremor in the ground in a 10-foot radius. Each creature other than you in that area must make a Dexterity saving throw. "
            "On a failed save, a creature takes bludgeoning damage and is knocked prone. If the ground in that area is loose earth or stone, it becomes difficult terrain."
        ),
        "Effect": {
            "Type": "Damage + Prone + Terrain",
            "Damage Type": "Bludgeoning",
            "Scaling": {
                1: "1d6, 10-ft radius",
                2: "2d6, 10-ft radius",
                3: "3d6, 10-ft radius",
                4: "4d6, 10-ft radius",
                5: "5d6, 10-ft radius",
                6: "6d6, 10-ft radius",
                7: "7d6, 10-ft radius",
                8: "8d6, 10-ft radius",
                9: "9d6, 10-ft radius"
            }
        }
    },    
    "Eldritch Blast": {
        "Name": "Eldritch Blast",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Warlock"],
        "Components": ["V", "S"],
        "Description": "A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage.\nAt Higher Levels. The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Force",
            "Damage": "1d10",
            "Rolls": {
                1: 1,
                5: 2,
                11: 3,
                17: 4
            }
        }
    },    
    "Encode Thoughts": {
        "Name": "Encode Thoughts",
        "Level": 0,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "8 hours",
        "Spell List": ["Wizard"],
        "Components": ["S"],
        "Description": "You pull a memory, idea, or message from a creature’s mind and transform it into a tangible string of glowing energy called a thought strand. The strand appears in an unoccupied space within 5 feet of you and is visible for the spell’s duration. Any creature that touches the strand can see the memory or hear the message as if experiencing it firsthand. A creature can only create one strand at a time, and the spell ends early if the strand is used or destroyed."
    },    
    "Faerie Fire": {
        "Name": "Faerie Fire",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Artificer", "Bard", "Druid"],
        "Components": ["V"],
        "Description": (
            "Each object in a 20-foot cube within range is outlined in blue, green, or violet light (your choice). "
            "Any creature in the area when the spell is cast is also outlined in light if it fails a Dexterity saving throw. "
            "For the duration, objects and affected creatures shed dim light in a 10-foot radius. "
            "Any attack roll against an affected creature or object has advantage if the attacker can see it, and the affected creature or object can't benefit from being invisible."
        )
    },    
    "False Life": {
        "Name": "False Life",
        "Level": 1,
        "School": "Necromancy",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "1 hour",
        "Spell List": ["Sorcerer", "Wizard", "Artificer"],
        "Components": ["V", "S", "M (a small amount of alcohol or distilled spirits)"],
        "Description": (
            "Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 temporary hit points for the duration."
        ),
        "Effect": {
            "Type": "Temp HP",
            "Scaling": {
                1: "1d4 + 4 temp HP",
                2: "1d4 + 9 temp HP",
                3: "1d4 + 14 temp HP",
                4: "1d4 + 19 temp HP",
                5: "1d4 + 24 temp HP",
                6: "1d4 + 29 temp HP",
                7: "1d4 + 34 temp HP",
                8: "1d4 + 39 temp HP",
                9: "1d4 + 44 temp HP"
            }
        }
    },    
    "Fire Bolt": {
        "Name": "Fire Bolt",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack. On a hit, the target takes fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Fire",
            "Scaling": {
                1: "1d10",
                5: "2d10",
                11: "3d10",
                17: "4d10"
            }
        }
    },  
    "Fog Cloud": {
        "Name": "Fog Cloud",
        "Level": 1,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "Concentration, up to 1 hour",
        "Spell List": ["Druid", "Ranger", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, "
            "and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed disperses it."
        ),
        "Effect": {
            "Type": "Obscurement",
            "Scaling": {
                1: "20-ft radius sphere",
                2: "40-ft radius",
                3: "60-ft radius",
                4: "80-ft radius",
                5: "100-ft radius",
                6: "120-ft radius",
                7: "140-ft radius",
                8: "160-ft radius",
                9: "180-ft radius"
            }
        }
    },    
    "Friends": {
        "Name": "Friends",
        "Level": 0,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["S", "M (a small amount of makeup applied to the face as this spell is cast)"],
        "Description": "For the duration, you have advantage on all Charisma checks directed at one creature of your choice that isn't hostile toward you. When the spell ends, the creature realizes that you used magic to influence its mood and becomes hostile toward you."
    },  
    "Frostbite": {
        "Name": "Frostbite",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer","Druid", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Save": "CON",
        "Description": "You cause numbing frost to form on one creature that you can see within range. The target must succeed on a Constitution saving throw or take cold damage and have disadvantage on the next weapon attack roll it makes before the end of its next turn.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Cold",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },     
    "Green-Flame Blade": {
        "Name": "Green-Flame Blade",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Self (5 foot radius)",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "M (a melee weapon worth at least 1 sp)"],
        "Description": "You brandish the weapon used in the spell's casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack's normal effects, and you can cause green fire to leap from the target to a different creature of your choice that you can see within 5 feet of it. The second creature takes fire damage equal to your spellcasting ability modifier.",
        "Effect": {
            "Type": "Weapon Buff",
            "Conditions": {
                'Name': "Green-Flame Blade",
                "Scaling": {
                    1: {"Mod": "Spellcasting", "Type": "Fire"},
                    5: {"NumDice": 1, "Dice": 8, "Mod": "Spellcasting", "Type": "Fire"},
                    11: {"NumDice": 2, "Dice": 8, "Mod": "Spellcasting", "Type": "Fire"},
                    17: {"NumDice": 3, "Dice": 8, "Mod": "Spellcasting", "Type": "Fire"}
                },            
                "FireScaling": {
                    5: {"NumDice": 1, "Dice": 8, "Type": "Fire"},
                    11: {"NumDice": 2, "Dice": 8, "Type": "Fire"},
                    17: {"NumDice": 3, "Dice": 8, "Type": "Fire"}
                },
                "Expires": "EndOfSourceTurn",
            }
        }
    },   
    "Goodberry": {
        "Name": "Goodberry",
        "Level": 1,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Instantaneous",
        "Spell List": ["Druid", "Ranger"],
        "Components": ["V", "S", "M"],
        "Materials": "A sprig of mistletoe",
        "Description": (
            "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its "
            "action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to "
            "sustain a creature for one day. The berries lose their potency if they have not been consumed within 24 hours "
            "of the casting of this spell."
        ),
        "Effect": {
            "Type": "Healing",
            "Healing": "10 berries, 1 HP each"
        }
    },    
    "Guidance": {
        "Name": "Guidance",
        "Level": 0,
        "School": "Divination",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Artificer", "Cleric", "Druid"],
        "Components": ["V", "S"],
        "Description": "You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one ability check of its choice. It can roll the die before or after making the check. The spell then ends.",
        "Effect": {
            "Name": "Guidance",
            "Type": "Player Buff"
        }
    },     
    "Guiding Bolt": {
        "Name": "Guiding Bolt",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "1 round",
        "Spell List": ["Cleric"],
        "Components": ["V", "S"],
        "Description": (
            "A flash of light streaks toward a creature of your choice within range. Make a ranged spell attack against the target. "
            "On a hit, the target takes radiant damage, and the next attack roll made against this target before the end of your next turn has advantage."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Radiant",
            "Scaling": {
                1: "4d6",
                2: "5d6",
                3: "6d6",
                4: "7d6",
                5: "8d6",
                6: "9d6",
                7: "10d6",
                8: "11d6",
                9: "12d6"
            }
        }
    },    
    "Gust": {
        "Name": "Gust",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Druid", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": "You seize the air and compel it to create one of the following effects at a point you can see within range:\n- One Medium or smaller creature is pushed 5 feet away from you.\n- You create a small blast of air capable of moving one object that is neither held nor carried and weighs no more than 5 pounds.\n- You create a harmless sensory effect using air, such as causing leaves to rustle or your cloak to billow dramatically in the wind."
    },      
    "Heroism": {
        "Name": "Heroism",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Bard", "Paladin"],
        "Components": ["V", "S"],
        "Description": (
            "A willing creature you touch is imbued with bravery. Until the spell ends, the creature is immune to being frightened and gains temporary "
            "hit points equal to your spellcasting ability modifier at the start of each of its turns."
        ),
        "Effect": {
            "Type": "Buff",
            "Buff": "Temporary Hit Points, Frightened Immunity"
        }
    },    
    "Identify": {
        "Name": "Identify",
        "Level": 1,
        "School": "Divination",
        "Casting Time": "1 minute",
        "Range": "Touch",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Bard", "Wizard"],
        "Components": ["V", "S", "M"],
        "Materials": "A pearl worth at least 100 gp and an owl feather",
        "Ritual": True,
        "Description": (
            "You choose one object that you must touch throughout the casting of the spell. If it is a magic item or some "
            "other magic-imbued object, you learn its properties and how to use them, whether it requires attunement to "
            "use, and how many charges it has, if any. You learn whether any spells are affecting the item and what they "
            "are. If the item was created by a spell, you learn which spell created it. If you instead touch a creature "
            "throughout the casting, you learn what spells, if any, are currently affecting it."
        )
    },    
    "Infestation": {
        "Name": "Infestation",
        "Level": 0,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Druid", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S", "M (a living flea)"],
        "Save": "CON",
        "Description": "You cause a cloud of mites, fleas, and other parasites to appear momentarily on one creature you can see within range. The target must succeed on a Constitution saving throw or take poison damage and move 5 feet in a random direction if it can move and its speed is at least 5 feet.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Poison",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },     
    "Light": {
        "Name" : "Light",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "1 hour",
        "Spell List" : ['Artificer', 'Bard', 'Cleric', 'Sorcerer', 'Wizard'],
        "Components": ["V", "M (a firefly or phosphorescent moss)"],
        "Description": "You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. Completely covering the object with something opaque blocks the light. The spell ends if you cast it again or dismiss it as an action.\nIf you target an object held or worn by a hostile creature, that creature must succeed on a Dexterity saving throw to avoid the spell.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose    
    },
    "Lightning Lure": {
        "Name": "Lightning Lure",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Self (15-foot radius)",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V"],
        "Save": "STR",
        "Description": "You create a lash of lightning energy that strikes at one creature of your choice within 15 feet of you. The target must succeed on a Strength saving throw or be pulled up to 10 feet in a straight line toward you and then take lightning damage if it is within 5 feet of you.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Lightning",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },    
    "Longstrider": {
        "Name": "Longstrider",
        "Level": 1,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "1 hour",
        "Spell List": ["Bard", "Druid", "Ranger", "Wizard", "Artificer"],
        "Components": ["V", "S", "M"],
        "Materials": "A pinch of dirt",
        "Description": (
            "You touch a creature. The target’s speed increases by 10 feet until the spell ends. The spell can target additional creatures when cast at higher levels."
        ),
        "Effect": {
            "Type": "Buff",
            "Buff": "+10 ft movement speed",
            "Scaling": {
                1: "1 creature",
                2: "2 creatures",
                3: "3 creatures",
                4: "4 creatures",
                5: "5 creatures"
            }
        }
    },    
    "Mage Armor": {
        "Name": "Mage Armor",
        "Level": 1,
        "School": "Abjuration",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "8 hours",
        "Spell List": ["Sorcerer", "Wizard"],
        "Components": ["V", "S", "M (a piece of cured leather)"],
        "Description": (
            "You touch a willing creature who isn't wearing armor, and a magical force protects it until the spell ends. "
            "The target's base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or if you dismiss the spell as an action."
        ),
        "Effect": {
            "Type": "AC Buff",
            "Scaling": {
                1: "AC = 13 + Dex, lasts 8 hours",
            }
        }
    },    
    "Mage Hand": {
        "Name": "Mage Hand",
        "Level": 0,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "1 minute",
        "Spell List": ["Artificer", "Bard", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Description": "A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration or until you dismiss it as an action. The hand vanishes if it is ever more than 30 feet away from you or if you cast this spell again.\n\n"
                       "You can use your action to control the hand. You can use the hand to manipulate an object, open an unlocked door or container, stow or retrieve an item from an open container, or pour the contents out of a vial. You can move the hand up to 30 feet each time you use it.\n\n"
                       "The hand can’t attack, activate magical items, or carry more than 10 pounds.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },   
    "Magic Stone": {
        "Name": "Magic Stone",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 bonus action",
        "Range": "Touch",
        "Duration": "1 minute",
        "Spell List": ["Artificer", "Druid", "Warlock"],
        "Components": ["V", "S"],
        "Description": "You touch one to three pebbles and imbue them with magic. A creature can make a ranged spell attack with one of the pebbles by throwing it or hurling it with a sling. On a hit, the target takes bludgeoning damage as if struck by a magic projectile.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Bludgeoning",
            "Scaling": {
                1: "1d6 + Mod"
            }
        }
    },    
    "Magic Missile": {
        "Name": "Magic Missile",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see "
            "within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you "
            "can direct them to hit one creature or several."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Force",
            "Scaling": {
                1: "3 darts (1d4 + 1 each)",
                2: "4 darts",
                3: "5 darts",
                4: "6 darts",
                5: "7 darts",
                6: "8 darts",
                7: "9 darts",
                8: "10 darts",
                9: "11 darts"
            }
        }
    },    
    "Mending": {
        "Name": "Mending",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 minute",
        "Range": "Touch",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Bard", "Cleric", "Druid", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M (two lodestones)"],
        "Description": "This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, a torn cloak, or a leaking wineskin. As long as the break or tear is no larger than 1 foot in any dimension, you mend it, leaving no trace of the former damage. The spell can physically repair a magic item or construct, but the spell can't restore magic to such an object.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },    
    "Message": {
        "Name": "Message",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "120 feet",
        "Duration": "1 round",
        "Spell List": ["Artificer", "Bard", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M (a short piece of copper wire)"],
        "Description": "You point your finger toward a creature within range and whisper a message. The target (and only the target) hears the message and can reply in a whisper that only you can hear. You can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier. Magical silence, 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the spell. The spell doesn't have to follow a straight line and can travel freely around corners.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },    
    "Mind Sliver": {
        "Name": "Mind Sliver",
        "Level": 0,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "1 round",
        "Spell List": ["Sorcerer", "Warlock", "Wizard"],
        "Components": ["V"],
        "Save": "INT",
        "Description": "You drive a disorienting spike of psychic energy into the mind of one creature you can see within range. The target must succeed on an Intelligence saving throw or take psychic damage and subtract 1d4 from the next saving throw it makes before the end of your next turn.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Psychic",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },    
    "Minor Illusion": {
        "Name": "Minor Illusion",
        "Level": 0,
        "School": "Illusion",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "1 minute",
        "Spell List": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["S", "M (a bit of fleece)"],
        "Description": "You create a sound or an image of an object within range that lasts for the duration. The illusion ends if you dismiss it as an action or cast this spell again. If a creature uses its action to examine the illusion, it can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose    
    },
    "Mold Earth": {
        "Name": "Mold Earth",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet (5 -foot cube)",
        "Duration": "Instantaneous or 1 hour",
        "Spell List": ["Druid", "Sorcerer", "Wizard"],
        "Components": ["S"],
        "Description": "You choose a portion of dirt or stone that you can see within range and that fits within a 5-foot cube. You manipulate it in one of the following ways:\n\n- If you target an area of loose earth, you can instantaneously excavate it, move it along the ground, and deposit it up to 5 feet away.\n- You can cause shapes, colors, or both to appear on the dirt or stone, spelling out words or creating images or patterns.\n- If the dirt or stone you target is on the ground, you cause it to become difficult terrain or normal terrain.\n\nEach effect lasts for 1 hour unless you use this spell again or dismiss it as an action. If you cast this spell multiple times, you can have no more than two of its non-instantaneous effects active at a time."
    },
    "Poison Spray": {
        "Name": "Poison Spray",
        "Level": 0,
        "School": "Conjuration", 
        "Casting Time": "1 action",
        "Range": "10 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Description": "You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm. The creature must succeed on a Constitution saving throw or take poison damage.",
        "Save": "CON",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Poison",
            "Scaling": {
                1: "1d12",
                5: "2d12",
                11: "3d12",
                17: "4d12"
            }
        }
    },
    "Prestidigitation": {
        "Name": "Prestidigitation",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "10 feet",
        "Duration": "Up to 1 hour",
        "Spell List": ['Artificer', 'Bard', 'Sorcerer', 'Warlock', 'Wizard'],
        "Components": ["V", "S"],
        "Description": "This spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects within range:\n"
                    "- Create an instantaneous, harmless sensory effect such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.\n"
                    "- Light or snuff out a candle, a torch, or a small campfire.\n"
                    "- Clean or soil an object no larger than 1 cubic foot.\n"
                    "- Chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.\n"
                    "- Make a color, a small mark, or a symbol appear on an object or a surface for 1 hour.\n"
                    "- Create a non-magical trinket or an illusory image that can fit in your hand and lasts until the end of your next turn.\n"
                    "You can have up to three of these effects active at a time, and you can dismiss an effect as an action.",
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },    
    "Primal Savagery": {
        "Name": "Primal Savagery",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "Instantaneous",
        "Spell List": ["Druid"],
        "Components": ["S"],
        "Description": "You channel primal magic to cause your teeth or fingernails to sharpen, ready to deliver a corrosive attack. Make a melee spell attack against one creature within 5 feet of you. On a hit, the target takes acid damage, and your teeth or fingernails return to normal after the attack.",
        "Effect": {
            "Type": "Self Buff",
            "Damage Type": "Acid",
            "Scaling": {
                1: "1d10",
                5: "2d10",
                11: "3d10",
                17: "4d10"
            }
        }
    },
    "Produce Flame": {
        "Name": "Produce Flame",
        "Level": 0,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "10 minutes",
        "Spell List": ["Druid"],
        "Components": ["V", "S"],
        "Description": "A flickering flame appears in your hand. The flame remains there for the duration and harms neither you nor your equipment. The flame sheds bright light in a 10-foot radius and dim light for an additional 10 feet. The spell ends if you dismiss it as an action or if you cast it again.\n\nYou can also attack with the flame, although doing so ends the spell. When you cast this spell, or as an action on a later turn, you can hurl the flame at a creature within 30 feet of you. Make a ranged spell attack. On a hit, the target takes fire damage.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Fire",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },
    "Protection from Evil and Good": {
        "Name": "Protection from Evil and Good",
        "Level": 1,
        "School": "Abjuration",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Concentration, up to 10 minutes",
        "Spell List": ["Cleric", "Druid", "Paladin", "Warlock", "Wizard"],
        "Components": ["V", "S", "M"],
        "Materials": "Holy water or powdered silver and iron, which the spell consumes",
        "Description": (
            "Until the spell ends, one willing creature you touch is protected against certain types of creatures: "
            "aberrations, celestials, elementals, fey, fiends, and undead. The protection grants several benefits. "
            "Creatures of those types have disadvantage on attack rolls against the target. The target also can't be "
            "charmed, frightened, or possessed by them. If the target is already charmed, frightened, or possessed, "
            "the target has advantage on any new saving throw against the relevant effect."
        )
    },    
    "Ray of Frost": {
        "Name": "Ray of Frost",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Sorcerer", "Wizard", "Artificer"],
        "Components": ["V", "S"],
        "Description": "A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes cold damage, and its speed is reduced by 10 feet until the start of your next turn.",
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Cold",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },
    "Ray of Sickness": {
        "Name": "Ray of Sickness",
        "Level": 1,
        "School": "Necromancy",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "A ray of sickening green energy lashes out toward a creature within range. Make a ranged spell attack against the target. "
            "On a hit, the target takes 2d8 poison damage and must make a Constitution saving throw. On a failed save, it is poisoned until the end of your next turn."
        ),
        "Effect": {
            "Type": "Damage (Poison) + Condition (Poisoned)",
            "Scaling": {
                1: "2d8 poison + CON save or poisoned",
                2: "3d8 poison + CON save or poisoned",
                3: "4d8 poison + CON save or poisoned",
                4: "5d8 poison + CON save or poisoned",
                5: "6d8 poison + CON save or poisoned",
                6: "7d8 poison + CON save or poisoned",
                7: "8d8 poison + CON save or poisoned",
                8: "9d8 poison + CON save or poisoned",
                9: "10d8 poison + CON save or poisoned",                
            }
        }
    },    
    "Resistance": {
        "Name": "Resistance",
        "Level": 0,
        "School": "Abjuration",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Artificer", "Cleric", "Druid"],
        "Components": ["V", "S", "M (a miniature cloak)"],
        "Description": (
            "You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one saving throw "
            "of its choice. It can roll the die before or after making the saving throw. The spell then ends."
        ),
        "Effect": {
            "Name": "Resistance",
            "Type": "Player Buff"
        }
    },
    "Sacred Flame": {
        "Name": "Sacred Flame",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Cleric"],
        "Components": ["V", "S"],
        "Save": "DEX",
        "Description": (
            "Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take "
            "1d8 radiant damage. The target gains no benefit from cover for this saving throw."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Radiant",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },
    "Sanctuary": {
        "Name": "Sanctuary",
        "Level": 1,
        "School": "Abjuration",
        "Casting Time": "1 bonus action",
        "Range": "30 feet",
        "Duration": "1 minute",
        "Spell List": ["Cleric", "Artificer"],
        "Components": ["V", "S", "M (a small silver mirror)"],
        "Description": (
            "You ward a creature within range against attack. Until the spell ends, any creature who targets the warded creature with an attack or a harmful spell "
            "must first make a Wisdom saving throw. On a failed save, the creature must choose a new target or lose the attack or spell. "
            "The spell doesn't protect the warded creature from area effects. If the warded creature makes an attack or casts a spell that affects an enemy, the spell ends."
        )
    },    
    "Sapping Sting": {
        "Name": "Sapping Sting",
        "Level": 0,
        "School": "Necromancy",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Dunamancy"],
        "Save": "CON",
        "Components": ["V", "S"],
        "Description": (
            "You sap the vitality of one creature you can see within range. The target must succeed on a Constitution saving throw or take 1d4 necrotic "
            "damage and fall prone."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Necrotic",
            "Scaling": {
                1: "1d4",
                5: "2d4",
                11: "3d4",
                17: "4d4"
            },
        }
    },
    "Searing Smite": {
        "Name": "Searing Smite",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 bonus action",
        "Range": "Self",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Paladin", "Ranger"],
        "Components": ["V"],
        "Description": (
            "The next time you hit a creature with a melee weapon attack during this spell’s duration, your weapon flares "
            "with white-hot intensity, and the attack deals an extra 1d6 fire damage to the target and causes it to ignite in flames. "
            "At the start of each of its turns until the spell ends, the target must make a Constitution saving throw. "
            "On a failed save, it takes 1d6 fire damage. On a successful save, the spell ends."
        ),
        "Effect": {
            "Type": "Damage Over Time",
            "Damage Type": "Fire",
            "Scaling": {
                1: "1d6",
                2: "2d6",
                3: "3d6",
                4: "4d6",
                5: "5d6",
                6: "6d6",
                7: "7d6",
                8: "8d6",
                9: "9d6",
            }
        }
    },    
    "Shape Water": {
        "Name": "Shape Water",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet (5-foot cube)",
        "Duration": "Instantaneous or 1 hour",
        "Spell List": ["Druid", "Sorcerer", "Wizard"],
        "Components": ["S"],
        "Description": (
            "You choose an area of water that you can see within range and that fits within a 5-foot cube. You manipulate it in one of the following ways:\n\n"
            "- You instantaneously move or otherwise change the flow of the water as you direct, up to 5 feet in any direction. This movement doesn't "
            "have enough force to cause damage.\n"
            "- You cause the water to form into simple shapes and animate at your direction. This change lasts for 1 hour.\n"
            "- You change the water's color or opacity. The water must be changed in the same way throughout. This change lasts for 1 hour.\n"
            "- You freeze the water, provided that there are no creatures in it. The water unfreezes in 1 hour.\n\n"
            "If you cast this spell multiple times, you can have up to two of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action."
        )
    },
    "Shield": {
        "Name": "Shield",
        "Level": 1,
        "School": "Abjuration",
        "Casting Time": "1 reaction, which you take when you are hit by an attack or targeted by Magic Missile",
        "Range": "Self",
        "Duration": "1 round",
        "Spell List": ["Sorcerer", "Wizard", "Artificer"],
        "Components": ["V", "S"],
        "Description": (
            "An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, "
            "including against the triggering attack, and you take no damage from Magic Missile."
        ),
        "Effect": {
            "Type": "AC Buff (Reaction)",
            "Scaling": {
                1: "+5 AC for 1 round",
            }
        }
    },
    "Shield of Faith": {
        "Name": "Shield of Faith",
        "Level": 1,
        "School": "Abjuration",
        "Casting Time": "1 bonus action",
        "Range": "60 feet",
        "Duration": "Concentration, up to 10 minutes",
        "Spell List": ["Cleric", "Paladin"],
        "Components": ["V", "S", "M"],
        "Materials": "A small parchment with a bit of holy text written on it",
        "Description": (
            "A shimmering field appears and surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration."
        ),
        "Effect": {
            "Type": "Buff",
            "Buff": "+2 AC"
        }
    },
    "Shillelagh": {
        "Name": "Shillelagh",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 bonus action",
        "Range": "Touch",
        "Duration": "1 minute",
        "Spell List": ["Druid"],
        "Components": ["V", "S", "M (mistletoe, a shamrock leaf, and a club or quarterstaff)"],
        "Description": (
            "The wood of a club or quarterstaff you are holding is imbued with nature's power. For the duration, you can use your spellcasting ability "
            "instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon's damage die becomes a d8. "
            "The weapon also becomes magical, if it isn't already. The spell ends if you cast it again or let go of the weapon."
        ),
        "Effect": {
            "Type": "Weapon Buff",
            "Conditions": {
                "Name": "Shillelagh",
                "Expires": "OneMinute"
            }
        }        
    },
    "Shocking Grasp": {
        "Name": "Shocking Grasp",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "Lightning springs from your hand to deliver a shock to a creature you try to touch. Make a melee spell attack against the target. "
            "You have advantage on the attack roll if the target is wearing armor made of metal. On a hit, the target takes 1d8 lightning damage, "
            "and it can't take reactions until the start of its next turn."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Lightning",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            }
        }
    },
    "Silent Image": {
        "Name": "Silent Image",
        "Level": 1,
        "School": "Illusion",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Concentration, up to 10 minutes",
        "Spell List": ["Bard", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M"],
        "Materials": "A bit of fleece",
        "Description": (
            "You create the image of an object, a creature, or some other visible phenomenon that is no larger than a 15-foot cube. "
            "The image appears at a spot within range and lasts for the duration. The image is purely visual; it isn’t accompanied by "
            "sound, smell, or other sensory effects. You can move the image within the range. Physical interaction reveals it to be an illusion."
        ),
        "Effect": {
            "Type": "Illusion"
        }
    },    
    "Sleep": {
        "Name": "Sleep",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "90 feet",
        "Duration": "1 minute",
        "Spell List": ["Bard", "Sorcerer", "Wizard"],
        "Components": ["V", "S", "M (a pinch of fine sand, rose petals, or a cricket)"],
        "Description": (
            "This spell sends creatures into a magical slumber. Roll 5d8; the total is how many hit points of creatures this spell can affect. "
            "Creatures within 20 feet of a point you choose are affected in ascending order of their current hit points, ignoring unconscious creatures. "
            "A creature falls unconscious until the spell ends, the sleeper takes damage, or someone uses an action to shake or slap the sleeper awake. "
            "Undead and creatures immune to being charmed aren't affected."
        ),
        "Effect": {
            "Type": "Hit Points",
            "Scaling": {
                1: "5d8",
                2: "7d8",
                3: "9d8",
                4: "11d8",
                5: "13d8",
                6: "15d8",
                7: "17d8",
                8: "19d8",
                9: "21d8"
            }
        }
    },   
    "Spare the Dying": {
        "Name": "Spare the Dying",
        "Level": 0,
        "School": "Necromancy",
        "Casting Time": "1 action",
        "Range": "Touch",
        "Duration": "Instantaneous",
        "Spell List": ["Cleric", "Artificer"],
        "Components": ["V", "S"],
        "Description": (
            "You touch a living creature that has 0 hit points. The creature becomes stable. "
            "This spell has no effect on undead or constructs."
        ),
        "Effect": {
            "Name": "Spare the Dying",
            "Type": "Player Buff"
        }        
    },
    "Speak with Animals": {
        "Name": "Speak with Animals",
        "Level": 1,
        "School": "Divination",
        "Casting Time": "1 action",
        "Range": "Self",
        "Duration": "10 minutes",
            "Spell List": ["Bard", "Druid", "Ranger"],
            "Components": ["V", "S"],
            "Ritual": True,
            "Description": (
                "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts "
                "is limited by their intelligence, but at minimum, beasts can give you information about nearby locations and monsters, including whatever "
                "they can perceive or have perceived within the past day. You might be able to persuade a beast to perform a small favor for you, at the DM’s discretion."
            ),
            "Effect": {
                "Type": "Communication"
            }
    },      
    "Sword Burst": {
        "Name": "Sword Burst",
        "Level": 0,
        "School": "Conjuration",
        "Casting Time": "1 action",
        "Range": "5 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["V"],
        "Save": "DEX",
        "Description": (
            "You create a momentary circle of spectral blades that sweep around you. "
            "All other creatures within 5 feet of you must succeed on a Dexterity saving throw or take force damage."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Force",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },
    "Tasha's Hideous Laughter": {
        "Name": "Tasha's Hideous Laughter",
        "Level": 1,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Bard", "Wizard"],
        "Components": ["V", "S", "M (tiny tarts and a feather that is waved in the air)"],
        "Description": (
            "A creature of your choice that you can see within range perceives everything as hilariously funny and falls into fits of laughter "
            "if this spell affects it. The target must succeed on a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand "
            "up for the duration. The target can make another Wisdom saving throw at the end of each of its turns, and each time it takes damage, "
            "ending the effect on a success."
        ),
        "Effect": {
            "Type": "Debuff (Prone + Incapacitated)",
            "Scaling": {
                1: "1 target, WIS save or prone/incapacitated",
            }
        }
    },    
    "Thaumaturgy": {
        "Name": "Thaumaturgy",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Up to 1 minute",
        "Spell List": ["Cleric"],
        "Components": ["V"],
        "Description": (
            "You manifest a minor wonder, a sign of supernatural power, within range. You create one of the following magical effects:\n\n"
            "- Your voice booms up to three times as loud as normal for 1 minute.\n"
            "- You cause flames to flicker, brighten, dim, or change color for 1 minute.\n"
            "- You cause harmless tremors in the ground for 1 minute.\n"
            "- You create an instantaneous sound that originates from a point of your choice within range.\n"
            "- You instantaneously cause an unlocked door or window to fly open or slam shut.\n"
            "- You alter the appearance of your eyes for 1 minute.\n\n"
            "If you cast this spell multiple times, you can have up to three of its effects active at once, and you can dismiss such an effect as an action."
        ),
        "Flavor": True #This is the case for several spells until the map is implemented, then they will have an environmental purpose
    },
    "Thorn Whip": {
        "Name": "Thorn Whip",
        "Level": 0,
        "School": "Transmutation",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Druid"],
        "Components": ["V", "S", "M (the stem of a plant with thorns)"],
        "Description": (
            "You create a long, vine-like whip covered in thorns that lashes out at your command toward a creature in range. "
            "Make a melee spell attack against the target. If the attack hits, the creature takes piercing damage, "
            "and if the creature is Large or smaller, you pull the creature up to 10 feet closer to you."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Piercing",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },
    "Thunderclap": {
        "Name": "Thunderclap",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Self (5 foot radius)",
        "Duration": "Instantaneous",
        "Spell List": ["Artificer", "Bard", "Druid", "Sorcerer", "Warlock", "Wizard"],
        "Save": "CON",
        "Components": ["S"],
        "Description": (
            "You create a burst of thunderous sound that can be heard up to 100 feet away. "
            "Each creature other than you within 5 feet must succeed on a Constitution saving throw or take thunder damage."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Thunder",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },
    "Thunderwave": {
        "Name": "Thunderwave",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "Self (15-foot cube)",
        "Duration": "Instantaneous",
        "Spell List": ["Bard", "Druid", "Sorcerer", "Wizard"],
        "Components": ["V", "S"],
        "Description": (
            "A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. "
            "On a failed save, a creature takes thunder damage and is pushed 10 feet away from you. "
            "On a successful save, the creature takes half as much damage and isn't pushed."
        ),
        "Effect": {
            "Type": "Damage (Thunder) + Push",
            "Scaling": {
                1: "2d8",
                2: "3d8",
                3: "4d8",
                4: "5d8",
                5: "6d8",
                6: "7d8",
                7: "8d8",
                8: "9d8",
                9: "10d8"
            }
        }
    },
    "Toll the Dead": {
        "Name": "Toll the Dead",
        "Level": 0,
        "School": "Necromancy",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Cleric", "Warlock", "Wizard"],
        "Components": ["V", "S"],
        "Save": "WIS",
        "Description": (
            "You point at one creature you can see within range, and the sound of a dolorous bell fills the air around it for a moment. "
            "The target must succeed on a Wisdom saving throw or take necrotic damage. If the target is missing any of its hit points, "
            "it instead takes more damage."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Necrotic",
            "Scaling": {
                1: "1d8",
                5: "2d8",
                11: "3d8",
                17: "4d8"
            },
            "HurtScaling": {
                1: "1d12",
                5: "2d12",
                11: "3d12",
                17: "4d12"                
            }
        }
    },
    "True Strike": {
        "Name": "True Strike",
        "Level": 0,
        "School": "Divination",
        "Casting Time": "1 action",
        "Range": "30 feet",
        "Duration": "Concentration, up to 1 round",
        "Spell List": ["Bard", "Sorcerer", "Warlock", "Wizard"],
        "Components": ["S"],
        "Description": (
            "You extend your hand and point a finger at a target in range. Your magic grants you a brief insight into the target's defenses. "
            "On your next turn, you gain advantage on your first attack roll against the target, provided that this spell hasn’t ended."
        ),
        "Effect": {
            "Name": "True Strike",
            "Type": "Player Buff"
        }        
    },
    "Veil of Dusk":  {
        "Name": "Veil of Dusk",
        "Level": 1,
        "School": "Abjuration",
        "Casting Time": "1 bonus action",
        "Range": "60 feet",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Druid", "Warlock",],
        "Components": ["V", "S", "M"],
        "Materials" : "A pinch of soot",
        "Description": (
           "You incant towards a creature, cloaking them in a shadowy veil of darkness and silence. "
           "The target gains a +1 bonus their armor class and makes Stealth checks with advantage for the duration of the spell."
        )
    },        
    "Vicious Mockery": {
        "Name": "Vicious Mockery",
        "Level": 0,
        "School": "Enchantment",
        "Casting Time": "1 action",
        "Range": "60 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Bard"],
        "Components": ["V"],
        "Save": "WIS",
        "Description": (
            "You unleash a string of insults laced with subtle enchantments at a creature you can see within range. "
            "If the target can hear you (though it need not understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic damage "
            "and have disadvantage on the next attack roll it makes before the end of its next turn."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Psychic",
            "Scaling": {
                1: "1d4",
                5: "2d4",
                11: "3d4",
                17: "4d4"
            }
        }
    },
    "Word of Radiance": {
        "Name": "Word of Radiance",
        "Level": 0,
        "School": "Evocation",
        "Casting Time": "1 action",
        "Range": "5 feet",
        "Duration": "Instantaneous",
        "Spell List": ["Cleric"],
        "Components": ["V", "M (a holy symbol)"],
        "Save": "CON",
        "Description": (
            "You utter a divine word, and burning radiance erupts from you. Each creature of your choice that you can see within range must succeed "
            "on a Constitution saving throw or take 1d6 radiant damage."
        ),
        "Effect": {
            "Type": "Damage",
            "Damage Type": "Radiant",
            "Scaling": {
                1: "1d6",
                5: "2d6",
                11: "3d6",
                17: "4d6"
            }
        }
    },
    "Wrathful Smite": {
        "Name": "Wrathful Smite",
        "Level": 1,
        "School": "Evocation",
        "Casting Time": "1 bonus action",
        "Range": "Self",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Paladin"],
        "Components": ["V"],
        "Description": (
            "The next time you hit with a melee weapon attack during this spell’s duration, your attack deals an extra 1d6 psychic damage. "
            "Additionally, if the target is a creature, it must make a Wisdom saving throw or be frightened until the spell ends. "
            "As an action, the creature can make a Wisdom check against your spell save DC to end this effect."
        ),
        "Effect": {
            "Type": "Damage (Psychic) + Frightened",
            "Scaling": {
                1: "1d6 psychic + WIS save or frightened",
            }
        }
    },    
    "Zephyr Strike": {
        "Name": "Zephyr Strike",
        "Level": 1,
        "School": "Transmutation",
        "Casting Time": "1 bonus action",
        "Range": "Self",
        "Duration": "Concentration, up to 1 minute",
        "Spell List": ["Ranger"],
        "Components": ["V"],
        "Description": (
            "You move like the wind. Until the spell ends, your movement doesn’t provoke opportunity attacks. "
            "Once before the spell ends, you can give yourself advantage on one weapon attack roll on your turn. "
            "That attack deals an extra 1d8 force damage, and your speed increases by 30 feet until the end of that turn."
        ),
        "Effect": {
            "Type": "Mobility + Damage Buff",
            "Scaling": {
                1: "1d8 force, +30 ft speed, no opportunity attacks",
            }
        }
    },
}