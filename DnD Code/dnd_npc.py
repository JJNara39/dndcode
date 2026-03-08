from fractions import Fraction

npcs = {
    "Aberrant Cultist": {
        "Name": "Aberrant Cultist",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral Evil",
        "AC": 14,
        "Initiative": 7,
        "HP": 137,
        "Hit Dice": "25d8 + 25",
        "Speed": {
            "Walk": 30
        },
        "STR": 10,
        "DEX": 19,
        "CON": 12,
        "INT": 16,
        "WIS": 18,
        "CHA": 15,
        "STR Save": 0,
        "DEX Save": 4,
        "CON Save": 1,
        "INT Save": 6,
        "WIS Save": 7,
        "CHA Save": 2,
        "Skills": {
            "Arcana": 6,
            "Perception": 7,
            "Religion": 6
        },
        "Senses": {
            "Darkvision": "90 ft.",
            "Passive Perception": 17
        },
        "Languages": ["Common", "Deep Speech", "Telepathy 30 ft."],
        "Challenge": 8,
        "XP": 3900,
        "Proficiency Bonus": 3,
        "Traits": {
            "Spellcasting": {
                "Description": "The cultist uses Wisdom for spellcasting (save DC 15).",
                "At Will": ["Detect Thoughts", "Minor Illusion"]
            }
        },
        "Gear": [],
        "Actions": {
            "Multiattack": {
                "Description": "The cultist makes two Tentacle Lash attacks. It can replace any attack with a use of Mind Rot."
            },
            "Tentacle Lash": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "10 ft.",
                "Hit Average": 21,
                "Damage": "1d6 + 4 slashing + 4d6 psychic",
                "Damage Type": "Slashing and Psychic",
                "Additional Effects": "Target is grappled (escape DC 14) and restrained until grapple ends if Large or smaller."
            },
            "Mind Rot": {
                "Attack Type": "Wisdom Saving Throw",
                "Save DC": 15,
                "Range": "90 ft.",
                "Hit Average": 27,
                "Damage": "6d8",
                "Damage Type": "Psychic",
                "Additional Effects": "Target is poisoned until the start of the cultist’s next turn on a failed save."
            }
        },
        "Reactions": {
            "Counterspell (2/Day)": {
                "Description": "The cultist casts Counterspell using its Wisdom spellcasting ability."
            }
        }
    },
    "Archmage": {
        "Name": "Archmage",
        "Size": "Medium or Small",
        "Type": "Humanoid (Wizard)",
        "Alignment": "Neutral",
        "AC": 17,
        "Initiative": 7,
        "HP": 170,
        "Hit Dice": "31d8 + 31",
        "Speed": {
            "Walk": 30
        },
        "STR": 10,
        "DEX": 14,
        "CON": 12,
        "INT": 20,
        "WIS": 15,
        "CHA": 16,
        "STR Save": 0,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": 9,
        "WIS Save": 6,
        "CHA Save": 3,
        "Skills": {
            "Arcana": 13,
            "History": 9,
            "Perception": 6
        },
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Common", "Five other languages"],
        "Challenge": Fraction(12, 1),
        "XP": 8000,
        "Proficiency Bonus": 4,
        "Gear": ["Wand"],
        "Immunities": ["Psychic", "Charmed (with Mind Blank)"],
        "Traits": {
            "Magic Resistance": {
                "Description": "The archmage has Advantage on saving throws against spells and other magical effects."
            }
        },
        "Actions": {
            "Multiattack": {
                "Description": "The archmage makes four Arcane Burst attacks."
            },
            "Arcane Burst": {
                "Attack Type": "Melee or Ranged Attack",
                "Attack Bonus": 9,
                "Reach": "5 ft.",
                "Range": "150 ft.",
                "Hit Average": 27,
                "Damage": "4d10 + 5",
                "Damage Type": "Force"
            },
            "Spellcasting": {
                "Description": "The archmage casts one of the following spells, using Intelligence (spell save DC 17):\n**At Will:** Detect Magic, Detect Thoughts, Disguise Self, Invisibility, Light, Mage Armor (included in AC), Mage Hand, Prestidigitation\n**2/day each:** Fly, Lightning Bolt (7th level)\n**1/day each:** Cone of Cold (9th level), Mind Blank (cast before combat), Scrying, Teleport"
            }
        },
        "Bonus Actions": {
            "Misty Step (3/day)": {
                "Description": "The archmage casts Misty Step using Intelligence as the spellcasting ability."
            }
        },
        "Reactions": {
            "Protective Magic (3/day)": {
                "Description": "The archmage casts Counterspell or Shield in response to a trigger, using Intelligence as the spellcasting ability."
            }
        }
    },
    "Assassin": {
        "Name": "Assassin",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 10,
        "HP": 97,
        "Hit Dice": "15d8 + 30",
        "Speed": {
            "Walk": 30
        },
        "STR": 11,
        "DEX": 18,
        "CON": 14,
        "INT": 16,
        "WIS": 11,
        "CHA": 10,
        "STR Save": 0,
        "DEX Save": 7,
        "CON Save": 2,
        "INT Save": 6,
        "WIS Save": 0,
        "CHA Save": 0,
        "Skills": {
            "Acrobatics": 7,
            "Perception": 6,
            "Stealth": 10
        },
        "Resistances": ["Poison"],
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Common", "Thieves’ Cant"],
        "Challenge": 8,
        "XP": 3900,
        "Proficiency Bonus": 3,
        "Traits": {
            "Evasion": {
                "Description": "If the assassin is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the assassin instead takes no damage if it succeeds on the save and only half damage if it fails. It can’t use this trait if it has the Incapacitated condition."
            }
        },
        "Gear": ["Light Crossbow", "Shortsword", "Studded Leather Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The assassin makes three attacks, using Shortsword or Light Crossbow in any combination."
            },
            "Shortsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "5 ft.",
                "Hit Average": 7,
                "Damage": "1d6 + 4",
                "Damage Type": "Piercing",
                "Additional Effect": "plus 17 (5d6) Poison damage, and the target has the Poisoned condition until the start of the assassin’s next turn."
            },
            "Light Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 7,
                "Range": "80/320 ft.",
                "Hit Average": 8,
                "Damage": "1d8 + 4",
                "Damage Type": "Piercing",
                "Additional Effect": "plus 21 (6d6) Poison damage."
            }
        },
        "Bonus Actions": {
            "Cunning Action": {
                "Description": "The assassin takes the Dash, Disengage, or Hide action."
            }
        }
    },
    "Bandit": {
        "Name": "Bandit",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 12,
        "Initiative": 1,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {
            "Walk": 30
        },
        "STR": 11,
        "DEX": 12,
        "CON": 12,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
        "STR Save": 0,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": 0,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common", "Thieves’ Cant"],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Gear": ["Leather Armor", "Light Crossbow", "Scimitar"],
        "Actions": {
            "Scimitar": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d6 + 1",
                "Damage Type": "Slashing"
            },
            "Light Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 3,
                "Range": "80/320 ft.",
                "Hit Average": 5,
                "Damage": "1d8 + 1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Bandit Captain": {
        "Name": "Bandit Captain",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 15,
        "Initiative": 3,
        "HP": 52,
        "Hit Dice": "8d8 + 16",
        "Speed": {
            "Walk": 30
        },
        "STR": 15,
        "DEX": 16,
        "CON": 14,
        "INT": 14,
        "WIS": 11,
        "CHA": 14,
        "STR Save": 4,
        "DEX Save": 5,
        "CON Save": 2,
        "INT Save": 2,
        "WIS Save": 2,
        "CHA Save": 2,
        "Skills": {
            "Athletics": 4,
            "Deception": 4
        },
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common", "Thieves’ Cant"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Gear": ["Pistol", "Scimitar", "Studded Leather Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The bandit makes two attacks, using Scimitar and Pistol in any combination."
            },
            "Scimitar": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Slashing"
            },
            "Pistol": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 5,
                "Range": "30/90 ft.",
                "Hit Average": 8,
                "Damage": "1d10 + 3",
                "Damage Type": "Piercing"
            }
        },
        "Reactions": {
            "Parry": {
                "Description": "When the bandit is hit by a melee attack while holding a weapon, it adds 2 to its AC against that attack."
            }
        }
    },
    "Bandit Deceiver": {
        "Name": "Bandit Deceiver",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 6,
        "HP": 130,
        "Hit Dice": "20d8 + 40",
        "Speed": {
            "Walk": 30
        },
        "STR": 8,
        "DEX": 16,
        "CON": 14,
        "INT": 17,
        "WIS": 12,
        "CHA": 16,
        "STR Save": -1,
        "DEX Save": 6,
        "CON Save": 2,
        "INT Save": 6,
        "WIS Save": 1,
        "CHA Save": 3,
        "Skills": {
            "Acrobatics": 6,
            "Perception": 4,
            "Stealth": 9
        },
        "Senses": {
            "Passive Perception": 14
        },
        "Languages": ["Common", "Thieves’ Cant"],
        "Challenge": 7,
        "XP": 2900,
        "Proficiency Bonus": 3,
        "Gear": ["Daggers (6)", "Wand"],
        "Traits": {
            "Spellcasting": {
                "Description": "The bandit casts the following spells using Intelligence (spell save DC 14):\nAt will: Disguise Self, Mage Hand, Minor Illusion\n1/day each: Hold Person (4th level), Mage Armor (included in AC), Major Image"
            }
        },
        "Actions": {
            "Multiattack": {
                "Description": "The bandit makes three Dagger attacks."
            },
            "Dagger": {
                "Attack Type": "Melee or Ranged Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Range": "20/60 ft.",
                "Hit Average": 18,
                "Damage": "2d4 + 3 piercing plus 3d6 poison",
                "Damage Type": "Piercing + Poison"
            },
            "Blinding Flash": {
                "Recharge": "4–6",
                "Description": "Each creature in a 10-foot-radius sphere (within 120 ft) makes a DC 14 Constitution save. On failure: 13 (3d6 + 3) radiant damage and Blinded until the start of the bandit's next turn. On success: half damage only."
            }
        }
    },
    "Bandit Crime Lord": {
        "Name": "Bandit Crime Lord",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 17,
        "Initiative": 9,
        "HP": 169,
        "Hit Dice": "26d8 + 52",
        "Speed": {
            "Walk": 30
        },
        "STR": 10,
        "DEX": 20,
        "CON": 14,
        "INT": 18,
        "WIS": 14,
        "CHA": 15,
        "STR Save": 0,
        "DEX Save": 9,
        "CON Save": 6,
        "INT Save": 4,
        "WIS Save": 2,
        "CHA Save": 2,
        "Skills": {
            "Acrobatics": 9,
            "Perception": 10,
            "Stealth": 13
        },
        "Senses": {
            "Passive Perception": 20
        },
        "Languages": ["Common", "Thieves’ Cant"],
        "Challenge": 11,
        "XP": 7200,
        "Proficiency Bonus": 4,
        "Gear": ["Pistols (2)", "Scimitar", "Studded Leather Armor"],
        "Traits": {
            "Evasion": {
                "Description": "If the bandit succeeds on a Dex save for half damage, it instead takes no damage. If it fails, it takes half. Doesn't work while Incapacitated."
            }
        },
        "Actions": {
            "Multiattack": {
                "Description": "The bandit makes three attacks, using Scimitar or Pistol in any combination."
            },
            "Scimitar": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 9,
                "Reach": "5 ft.",
                "Hit Average": 26,
                "Damage": "2d6 + 5 slashing plus 4d6 poison",
                "Damage Type": "Slashing + Poison"
            },
            "Pistol": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 9,
                "Range": "30/90 ft.",
                "Hit Average": 24,
                "Damage": "1d10 + 5 piercing plus 4d6 poison",
                "Damage Type": "Piercing + Poison"
            }
        },
        "Bonus Actions": {
            "Deadly Aim": {
                "Description": "Gain Advantage on next attack this turn. If it hits, deal extra 28 (8d6) poison damage."
            }
        }
    },
    "Berserker Commander": {
        "Name": "Berserker Commander",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 5,
        "HP": 136,
        "Hit Dice": "16d8 + 64",
        "Speed": {
            "Walk": 40
        },
        "STR": 19,
        "DEX": 14,
        "CON": 19,
        "INT": 10,
        "WIS": 14,
        "CHA": 9,
        "STR Save": 7,
        "DEX Save": 2,
        "CON Save": 7,
        "INT Save": 0,
        "WIS Save": 2,
        "CHA Save": -1,
        "Skills": {
            "Athletics": 7,
            "Perception": 5
        },
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": ["Common"],
        "Immunities": ["Charmed", "Frightened"],
        "Challenge": 8,
        "XP": 3900,
        "Proficiency Bonus": 3,
        "Traits": {
            "Bloodied Frenzy": {
                "Description": "While Bloodied, the berserker has Advantage on attack rolls and saving throws."
            }
        },
        "Gear": ["Greataxe", "Javelins (6)"],
        "Actions": {
            "Multiattack": {
                "Description": "The berserker makes three attacks, using Greataxe or Javelin in any combination."
            },
            "Greataxe": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "5 ft.",
                "Hit Average": 10,
                "Damage": "1d12 + 4",
                "Extra Damage": "3d6 Thunder to the target or another creature within 5 feet",
                "Damage Type": "Slashing + Thunder"
            },
            "Javelin": {
                "Attack Type": "Melee or Ranged Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "5 ft.",
                "Range": "30/120 ft.",
                "Hit Average": 18,
                "Damage": "4d6 + 4",
                "Damage Type": "Piercing",
                "Effect": "Target’s Speed decreases by 5 feet until the start of the berserker’s next turn"
            }
        },
        "Bonus Actions": {
            "Frenzied Rush": {
                "Description": "Each ally within 30 feet of the berserker can take a Reaction to move up to half the ally’s Speed without provoking Opportunity Attacks. The berserker can also move up to half its Speed without provoking Opportunity Attacks."
            }
        }
    },
    "Berserker": {
        "Name": "Berserker",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 1,
        "HP": 67,
        "Hit Dice": "9d8 + 27",
        "Speed": {
            "Walk": 30
        },
        "STR": 16,
        "DEX": 12,
        "CON": 17,
        "INT": 9,
        "WIS": 11,
        "CHA": 9,
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 3,
        "INT Save": -1,
        "WIS Save": 0,
        "CHA Save": -1,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {
            "Bloodied Frenzy": {
                "Description": "While Bloodied, the berserker has Advantage on attack rolls and saving throws."
            }
        },
        "Gear": ["Greataxe", "Hide Armor"],
        "Actions": {
            "Greataxe": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 9,
                "Damage": "1d12 + 3",
                "Damage Type": "Slashing"
            }
        }
    },
    "Commoner": {
        "Name": "Commoner",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 10,
        "Initiative": 0,
        "HP": 4,
        "Hit Dice": "1d8",
        "Speed": {
            "Walk": 30
        },
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
        "STR Save": 0,
        "DEX Save": 0,
        "CON Save": 0,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": 0,
        "Skills": {},  # DM chooses one, optionally fill like {"Animal Handling": 2}
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common"],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Training": {
                "Description": "The commoner has proficiency in one skill of the DM’s choice and has Advantage whenever it makes an ability check using that skill."
            }
        },
        "Gear": ["Club"],
        "Actions": {
            "Club": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 2,
                "Damage": "1d4",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Cultist": {
        "Name": "Cultist",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 12,
        "Initiative": 1,
        "HP": 9,
        "Hit Dice": "2d8",
        "Speed": {
            "Walk": 30
        },
        "STR": 11,
        "DEX": 12,
        "CON": 10,
        "INT": 10,
        "WIS": 11,
        "CHA": 10,
        "STR Save": 0,
        "DEX Save": 1,
        "CON Save": 0,
        "INT Save": 0,
        "WIS Save": 2,
        "CHA Save": 0,
        "Skills": {
            "Deception": 2,
            "Religion": 2
        },
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common"],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Gear": ["Leather Armor", "Sickle"],
        "Actions": {
            "Ritual Sickle": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 3,
                "Damage": "1d4 + 1",
                "Damage Type": "Slashing",
                "Additional Damage": {
                    "Average": 1,
                    "Damage": "1",
                    "Damage Type": "Necrotic"
                }
            }
        }
    },
    "Cultist Fanatic": {
        "Name": "Cultist Fanatic",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 2,
        "HP": 44,
        "Hit Dice": "8d8 + 8",
        "Speed": {
            "Walk": 30
        },
        "STR": 11,
        "DEX": 14,
        "CON": 12,
        "INT": 10,
        "WIS": 14,
        "CHA": 13,
        "STR Save": 0,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 4,
        "CHA Save": 1,
        "Skills": {
            "Deception": 3,
            "Persuasion": 3,
            "Religion": 2
        },
        "Senses": {
            "Passive Perception": 12
        },
        "Languages": ["Common"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Gear": ["Holy Symbol", "Leather Armor"],
        "Actions": {
            "Pact Blade": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Slashing",
                "Additional Damage": {
                    "Average": 7,
                    "Damage": "2d6",
                    "Damage Type": "Necrotic"
                }
            },
            "Spellcasting": {
                "Description": "The cultist casts one of the following spells, using Wisdom (spell save DC 12, +4 to hit with spell attacks): At Will: *Light*, *Thaumaturgy*; 2/Day: *Command*; 1/Day: *Hold Person*"
            }
        },
        "Bonus Actions": {
            "Spiritual Weapon (2/Day)": {
                "Description": "The cultist casts the *Spiritual Weapon* spell, using the same spellcasting ability as Spellcasting."
            }
        }
    },
    "Cultist Hierophant": {
        "Name": "Cultist Hierophant",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 8,
        "HP": 144,
        "Hit Dice": "17d8 + 68",
        "Speed": {
            "Walk": 30
        },
        "STR": 14,
        "DEX": 18,
        "CON": 18,
        "INT": 13,
        "WIS": 16,
        "CHA": 20,
        "STR Save": 2,
        "DEX Save": 4,
        "CON Save": 4,
        "INT Save": 1,
        "WIS Save": 7,
        "CHA Save": 9,
        "Skills": {
            "Perception": 7,
            "Persuasion": 9,
            "Religion": 5
        },
        "Senses": {
            "Passive Perception": 17
        },
        "Languages": ["Celestial", "Common"],
        "Challenge": Fraction(10, 1),
        "XP": 5900,
        "Proficiency Bonus": 4,
        "Gear": ["Breastplate", "Holy Symbol"],
        "Actions": {
            "Multiattack": {
                "Description": "The cultist makes three attacks, using Pact Blade or Radiant Ray in any combination."
            },
            "Pact Blade": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 9,
                "Reach": "5 ft.",
                "Hit Average": 12,
                "Damage": "2d6 + 5",
                "Damage Type": "Slashing",
                "Additional Damage": {
                    "Average": 18,
                    "Damage": "4d8",
                    "Damage Type": "Radiant"
                }
            },
            "Radiant Ray": {
                "Attack Type": "Ranged Spell Attack",
                "Attack Bonus": 9,
                "Range": "120 ft.",
                "Hit Average": 31,
                "Damage": "4d12 + 5",
                "Damage Type": "Radiant"
            },
            "Spellcasting": {
                "Description": "The cultist casts one of the following spells, using Charisma (spell save DC 17): At Will: *Mage Armor* (included in AC), *Thaumaturgy*; 1/Day Each: *Jallarzi’s Storm of Radiance* (7th-level), *Mass Suggestion*"
            }
        }
    },
    "Death Cultist": {
        "Name": "Death Cultist",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral Evil",
        "AC": 17,
        "Initiative": 4,
        "HP": 127,
        "Hit Dice": "15d8 + 60",
        "Speed": {
            "Walk": 30
        },
        "STR": 19,
        "DEX": 12,
        "CON": 18,
        "INT": 12,
        "WIS": 16,
        "CHA": 14,
        "STR Save": 4,
        "DEX Save": 1,
        "CON Save": 7,
        "INT Save": 1,
        "WIS Save": 6,
        "CHA Save": 2,
        "Skills": {
            "Insight": 6,
            "Perception": 6,
            "Religion": 4
        },
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Common"],
        "Challenge": 8,
        "XP": 3900,
        "Proficiency Bonus": 3,
        "Traits": {
            "Spellcasting": {
                "Description": "The cultist uses Wisdom for spellcasting (save DC 14).",
                "At Will": ["Speak with Dead", "Thaumaturgy"]
            }
        },
        "Gear": ["Splint Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The cultist makes three attacks using Dread Scythe or Deathly Ray in any combination."
            },
            "Dread Scythe": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "10 ft.",
                "Hit Average": 20,
                "Damage": "1d10 + 4 slashing + 2d10 necrotic",
                "Damage Type": "Slashing and Necrotic",
                "Additional Effects": "Target can’t regain hit points until the end of its next turn."
            },
            "Deathly Ray": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 6,
                "Range": "120 ft.",
                "Hit Average": 22,
                "Damage": "4d10",
                "Damage Type": "Necrotic"
            }
        }
    },
    "Druid": {
        "Name": "Druid",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 1,
        "HP": 44,
        "Hit Dice": "8d8+8",
        "Speed": {
            "Walk": 30
        },
        "STR": 10,
        "DEX": 12,
        "CON": 13,
        "INT": 12,
        "WIS": 16,
        "CHA": 11,
        "STR Save": 0,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": 1,
        "WIS Save": 3,
        "CHA Save": 0,
        "Skills": {
            "Medicine": 5,
            "Nature": 3,
            "Perception": 5
        },
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": ["Common", "Druidic", "Sylvan"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {},
        "Gear": ["Studded Leather Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The druid makes two attacks, using Vine Staff or Verdant Wisp in any combination."
            },
            "Vine Staff": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 7,
                "Damage": "1d8 + 3",
                "Damage Type": "Bludgeoning + 1d4 Poison"
            },
            "Verdant Wisp": {
                "Attack Type": "Ranged Spell Attack",
                "Attack Bonus": 5,
                "Range": "90 ft.",
                "Hit Average": 10,
                "Damage": "3d6",
                "Damage Type": "Radiant"
            },
            "Spellcasting": {
                "Description": "The druid casts one of the following spells (Wisdom is the spellcasting ability, DC 13):\nAt will: *Druidcraft*, *Speak with Animals*\n2/day each: *Entangle*, *Thunderwave*\n1/day each: *Animal Messenger*, *Longstrider*, *Moonbeam*"
            }
        }
    },
    "Elemental Cultist": {
    "Name": "Elemental Cultist",
    "Size": "Medium or Small",
    "Type": "Humanoid",
    "Alignment": "Chaotic Evil",
    "AC": 16,
    "Initiative": 4,
    "HP": 135,
    "Hit Dice": "18d8 + 54",
    "Speed": {
        "Walk": 30
    },
    "STR": 18,
    "DEX": 12,
    "CON": 16,
    "INT": 14,
    "WIS": 18,
    "CHA": 12,
    "STR Save": 4,
    "DEX Save": 1,
    "CON Save": 6,
    "INT Save": 2,
    "WIS Save": 7,
    "CHA Save": 1,
    "Skills": {
        "Arcana": 5,
        "Perception": 7,
        "Religion": 5
    },
    "Senses": {
        "Passive Perception": 17
    },
    "Languages": ["Common", "Primordial"],
    "Challenge": 8,
    "XP": 3900,
    "Proficiency Bonus": 3,
    "Traits": {
        "Spellcasting": {
            "Description": "The cultist uses Wisdom for spellcasting (save DC 15).",
            "At Will": ["Elementalism", "Mage Hand"]
        }
    },
    "Gear": ["Chain Mail"],
    "Actions": {
        "Multiattack": {
            "Description": "The cultist makes three attacks using Elemental Flail or Elemental Claw in any combination."
        },
        "Elemental Flail": {
            "Attack Type": "Melee Weapon Attack",
            "Attack Bonus": 7,
            "Reach": "5 ft.",
            "Hit Average": 25,
            "Damage": "6d6 + 4",
            "Damage Type": "Elemental (Acid, Cold, Fire, Lightning, or Thunder, chosen per attack)"
        },
        "Elemental Claw": {
            "Attack Type": "Ranged Weapon Attack",
            "Attack Bonus": 7,
            "Range": "120 ft.",
            "Hit Average": 22,
            "Damage": "4d10",
            "Damage Type": "Elemental (Acid, Cold, Fire, Lightning, or Thunder)",
            "Additional Effects": "If Medium or smaller, target is moved up to 10 feet toward or away from the cultist."
        }
    },
    "Reactions": {
        "Elemental Absorption (1/Day)": {
            "Description": "When taking elemental damage, the cultist gains Resistance to that damage and 10 temporary HP."
        }
    }
},
    "Fiend Cultist": {
    "Name": "Fiend Cultist",
    "Size": "Medium or Small",
    "Type": "Humanoid",
    "Alignment": "Neutral Evil",
    "AC": 16,
    "Initiative": 5,
    "HP": 127,
    "Hit Dice": "17d8 + 51",
    "Speed": {
        "Walk": 30
    },
    "STR": 19,
    "DEX": 15,
    "CON": 16,
    "INT": 12,
    "WIS": 18,
    "CHA": 10,
    "STR Save": 4,
    "DEX Save": 2,
    "CON Save": 6,
    "INT Save": 1,
    "WIS Save": 7,
    "CHA Save": 0,
    "Skills": {
        "Perception": 7,
        "Religion": 4
    },
    "Senses": {
        "Darkvision": "90 ft. (unimpeded by magical Darkness)",
        "Passive Perception": 17
    },
    "Languages": ["Abyssal", "Common", "Infernal"],
    "Challenge": 8,
    "XP": 3900,
    "Proficiency Bonus": 3,
    "Traits": {
        "Spellcasting": {
            "Description": "The cultist uses Wisdom for spellcasting (save DC 15, +7 to hit with spell attacks).",
            "At Will": ["Scorching Ray (5th level)", "Thaumaturgy"],
            "2/Day": ["Fireball (6th level)"]
        }
    },
    "Gear": ["Breastplate"],
    "Actions": {
        "Multiattack": {
            "Description": "The cultist makes three Pact Axe attacks."
        },
        "Pact Axe": {
            "Attack Type": "Melee Weapon Attack",
            "Attack Bonus": 7,
            "Reach": "5 ft.",
            "Hit Average": 23,
            "Damage": "1d12 + 4 slashing + 3d8 fire",
            "Damage Type": "Slashing and Fire"
        }
    },
    "Reactions": {
        "Hellish Rebuke": {
            "Description": "The cultist casts Hellish Rebuke using its Wisdom-based spellcasting."
        }
    }
},
    "Gladiator": {
        "Name": "Gladiator",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 5,
        "HP": 112,
        "Hit Dice": "15d8+45",
        "Speed": {
            "Walk": 30
        },
        "STR": 18,
        "DEX": 15,
        "CON": 16,
        "INT": 10,
        "WIS": 12,
        "CHA": 15,
        "STR Save": 7,
        "DEX Save": 5,
        "CON Save": 6,
        "INT Save": 0,
        "WIS Save": 4,
        "CHA Save": 2,
        "Skills": {
            "Athletics": 10,
            "Performance": 5
        },
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": ["Common"],
        "Challenge": 5,
        "XP": 1800,
        "Proficiency Bonus": 3,
        "Traits": {},
        "Gear": ["Shield", "Spears (3)", "Studded Leather Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The gladiator makes three Spear attacks. It can replace one attack with a Shield Bash."
            },
            "Spear": {
                "Attack Type": "Melee or Ranged Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "5 ft.",
                "Range": "20/60 ft.",
                "Hit Average": 11,
                "Damage": "2d6 + 4",
                "Damage Type": "Piercing"
            },
            "Shield Bash": {
                "Attack Type": "Special Melee Attack",
                "Save DC": 15,
                "Effect": "One creature within 5 feet makes a Strength save. On failure, takes 9 (2d4 + 4) bludgeoning damage and is knocked prone if Medium or smaller."
            }
        },
        "Reactions": {
            "Parry": {
                "Description": "When hit by a melee attack while holding a weapon, the gladiator adds 3 to its AC against that attack, possibly causing it to miss."
            }
        }
    },
    "Guard": {
        "Name": "Guard",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 1,
        "HP": 11,
        "Hit Dice": "2d8+2",
        "Speed": {
            "Walk": 30
        },
        "STR": 13,
        "DEX": 12,
        "CON": 12,
        "INT": 10,
        "WIS": 11,
        "CHA": 10,
        "STR Save": 1,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": 0,
        "Skills": {
            "Perception": 2
        },
        "Senses": {
            "Passive Perception": 12
        },
        "Languages": ["Common"],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {},
        "Gear": ["Chain Shirt", "Shield", "Spear"],
        "Actions": {
            "Spear": {
                "Attack Type": "Melee or Ranged Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Range": "20/60 ft.",
                "Hit Average": 4,
                "Damage": "1d6 + 1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Guard Captain": {
        "Name": "Guard Captain",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 18,
        "Initiative": 4,
        "HP": 75,
        "Hit Dice": "10d8+30",
        "Speed": {
            "Walk": 30
        },
        "STR": 18,
        "DEX": 14,
        "CON": 16,
        "INT": 12,
        "WIS": 14,
        "CHA": 13,
        "STR Save": 4,
        "DEX Save": 2,
        "CON Save": 3,
        "INT Save": 1,
        "WIS Save": 2,
        "CHA Save": 1,
        "Skills": {
            "Athletics": 6,
            "Perception": 4
        },
        "Senses": {
            "Passive Perception": 14
        },
        "Languages": ["Common"],
        "Challenge": 4,
        "XP": 1100,
        "Proficiency Bonus": 2,
        "Traits": {},
        "Gear": ["Breastplate", "Shield", "Javelins (6)", "Longsword"],
        "Actions": {
            "Multiattack": {
                "Description": "The captain makes two attacks, using Javelin or Longsword in any combination."
            },
            "Javelin": {
                "Attack Type": "Melee or Ranged Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Range": "30/120 ft.",
                "Hit Average": 14,
                "Damage": "3d6 + 4",
                "Damage Type": "Piercing"
            },
            "Longsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 15,
                "Damage": "2d10 + 4",
                "Damage Type": "Slashing"
            }
        }
    },
    "Knight": {
        "Name": "Knight",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 18,
        "Initiative": 0,
        "HP": 52,
        "Hit Dice": "8d8 + 16",
        "Speed": {
            "Walk": 30
        },
        "STR": 16,
        "DEX": 11,
        "CON": 14,
        "INT": 11,
        "WIS": 11,
        "CHA": 15,
        "STR Save": 3,
        "DEX Save": 0,
        "CON Save": 4,
        "INT Save": 0,
        "WIS Save": 2,
        "CHA Save": 2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common", "One other language"],
        "Condition Immunities": ["Frightened"],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 2,
        "Gear": ["Greatsword", "Heavy Crossbow", "Plate Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The knight makes two attacks, using Greatsword or Heavy Crossbow in any combination."
            },
            "Greatsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 14,
                "Damage": "2d6 + 3 plus 1d8",
                "Damage Type": "Slashing plus Radiant"
            },
            "Heavy Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 2,
                "Range": "100/400 ft.",
                "Hit Average": 15,
                "Damage": "2d10 plus 1d8",
                "Damage Type": "Piercing plus Radiant"
            }
        },
        "Reactions": {
            "Parry": {
                "Description": "When hit by a melee attack while holding a weapon, the knight adds 2 to its AC against that attack, possibly causing it to miss."
            }
        }
    },
    "Mage": {
        "Name": "Mage",
        "Size": "Medium or Small",
        "Type": "Humanoid (Wizard)",
        "Alignment": "Neutral",
        "AC": 15,
        "Initiative": 2,
        "HP": 81,
        "Hit Dice": "18d8",
        "Speed": {
            "Walk": 30
        },
        "STR": 9,
        "DEX": 14,
        "CON": 11,
        "INT": 17,
        "WIS": 12,
        "CHA": 11,
        "STR Save": -1,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": 6,
        "WIS Save": 4,
        "CHA Save": 0,
        "Skills": {
            "Arcana": 6,
            "History": 6,
            "Perception": 4
        },
        "Senses": {
            "Passive Perception": 14
        },
        "Languages": ["Common", "Three other languages"],
        "Challenge": 6,
        "XP": 2300,
        "Proficiency Bonus": 3,
        "Gear": ["Wand"],
        "Actions": {
            "Multiattack": {
                "Description": "The mage makes three Arcane Burst attacks."
            },
            "Arcane Burst": {
                "Attack Type": "Melee or Ranged Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Range": "120 ft.",
                "Hit Average": 16,
                "Damage": "3d8 + 3",
                "Damage Type": "Force"
            },
            "Spellcasting": {
                "Description": "The mage casts one of the following spells, using Intelligence (spell save DC 14):\n**At Will:** Detect Magic, Light, Mage Armor (included in AC), Mage Hand, Prestidigitation\n**2/day each:** Fireball (4th level), Invisibility\n**1/day each:** Cone of Cold, Fly"
            }
        },
        "Bonus Actions": {
            "Misty Step (3/day)": {
                "Description": "The mage casts Misty Step using Intelligence as the spellcasting ability."
            }
        },
        "Reactions": {
            "Protective Magic (3/day)": {
                "Description": "The mage casts Counterspell or Shield in response to a trigger, using Intelligence as the spellcasting ability."
            }
        }
    },
    "Mage Apprentice": {
        "Name": "Mage Apprentice",
        "Size": "Medium or Small",
        "Type": "Humanoid (Wizard)",
        "Alignment": "Neutral",
        "AC": 15,
        "Initiative": 2,
        "HP": 49,
        "Hit Dice": "9d8 + 9",
        "Speed": {
            "Walk": 30
        },
        "STR": 8,
        "DEX": 14,
        "CON": 12,
        "INT": 16,
        "WIS": 13,
        "CHA": 10,
        "STR Save": -1,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": 5,
        "WIS Save": 3,
        "CHA Save": 0,
        "Skills": {
            "Arcana": 5,
            "Perception": 3
        },
        "Senses": {
            "Passive Perception": 13
        },
        "Languages": ["Common", "One other language"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Gear": ["Component Pouch"],
        "Actions": {
            "Arcane Burst": {
                "Attack Type": "Melee or Ranged Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Range": "120 ft.",
                "Hit Average": 14,
                "Damage": "2d10 + 3",
                "Damage Type": "Force"
            },
            "Spellcasting": {
                "Description": "The mage casts one of the following spells, using Intelligence (spell save DC 13, +5 to hit with spell attacks):\n**At Will:** Mage Hand, Prestidigitation\n**1/day each:** Disguise Self, Ice Knife, Mage Armor (included in AC), Thunderwave"
            }
        }
    },
    "Noble": {
        "Name": "Noble",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 15,
        "Initiative": 1,
        "HP": 9,
        "Hit Dice": "2d8",
        "Speed": {
            "Walk": 30
        },
        "STR": 11,
        "DEX": 12,
        "CON": 11,
        "INT": 12,
        "WIS": 14,
        "CHA": 16,
        "STR Save": 0,
        "DEX Save": 1,
        "CON Save": 0,
        "INT Save": 1,
        "WIS Save": 2,
        "CHA Save": 3,
        "Skills": {
            "Deception": 5,
            "Insight": 4,
            "Persuasion": 5
        },
        "Senses": {
            "Passive Perception": 12
        },
        "Languages": ["Common", "Two other languages"],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Gear": ["Rapier", "Breastplate"],
        "Actions": {
            "Rapier": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d8 + 1",
                "Damage Type": "Piercing"
            }
        },
        "Reactions": {
            "Parry": {
                "Description": "When hit by a melee attack while holding a weapon, the noble adds 2 to its AC against that attack, possibly causing it to miss."
            }
        }
    },
    "Noble Prodigy": {
        "Name": "Noble Prodigy",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 7,
        "HP": 148,
        "Hit Dice": "27d8 + 27",
        "Speed": {
            "Walk": 30
        },
        "STR": 8,
        "DEX": 16,
        "CON": 12,
        "INT": 15,
        "WIS": 14,
        "CHA": 19,
        "STR Save": -1,
        "DEX Save": 7,
        "CON Save": 5,
        "INT Save": 2,
        "WIS Save": 6,
        "CHA Save": 8,
        "Skills": {
            "Perception": 6,
            "Persuasion": 8
        },
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Common", "Two other languages"],
        "Challenge": Fraction(10, 1),
        "XP": 5900,
        "Proficiency Bonus": 4,
        "Actions": {
            "Multiattack": {
                "Description": "The noble makes three Beguiling Strike attacks."
            },
            "Beguiling Strike": {
                "Attack Type": "Melee or Ranged Spell Attack",
                "Attack Bonus": 8,
                "Reach": "5 ft.",
                "Range": "60 ft.",
                "Hit Average": 18,
                "Damage": "4d6 + 4",
                "Damage Type": "Psychic; target is Charmed until start of noble's next turn"
            },
            "Spellcasting": {
                "Description": "The noble casts the following spells without material components (Charisma-based, DC 16): At Will – Mage Armor (included), Mage Hand, Minor Illusion; 1/day each – Befuddlement, Detect Thoughts, Fly, Scrying, Shatter (7th level)"
            }
        },
        "Reactions": {
            "Shield (2/Day)": {
                "Description": "The noble casts Shield in response to its trigger, using Charisma as the spellcasting ability."
            }
        }
    },
    "Priest": {
        "Name": "Priest",
        "Size": "Medium or Small",
        "Type": "Humanoid (Cleric)",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 0,
        "HP": 38,
        "Hit Dice": "7d8 + 7",
        "Speed": {
            "Walk": 30
        },
        "STR": 16,
        "DEX": 10,
        "CON": 12,
        "INT": 13,
        "WIS": 16,
        "CHA": 13,
        "STR Save": 3,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": 1,
        "WIS Save": 3,
        "CHA Save": 1,
        "Skills": {
            "Medicine": 7,
            "Perception": 5,
            "Religion": 5
        },
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": ["Common", "One other language"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Gear": ["Chain Shirt", "Holy Symbol", "Mace"],
        "Actions": {
            "Multiattack": {
                "Description": "The priest makes two attacks, using Mace or Radiant Flame in any combination."
            },
            "Mace": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Bludgeoning",
                "Bonus Damage": {
                    "Amount": "2d4",
                    "Type": "Radiant"
                }
            },
            "Radiant Flame": {
                "Attack Type": "Ranged Spell Attack",
                "Attack Bonus": 4,
                "Range": "60 ft.",
                "Hit Average": 11,
                "Damage": "2d10",
                "Damage Type": "Radiant"
            },
            "Spellcasting": {
                "Description": "The priest casts one of the following spells, using Wisdom as the spellcasting ability:",
                "At Will": ["Light", "Thaumaturgy"],
                "1/Day": ["Spirit Guardians"]
            }
        },
        "Bonus Actions": {
            "Divine Aid (3/Day)": {
                "Description": "The priest casts Bless, Dispel Magic, Healing Word, or Lesser Restoration, using Wisdom as the spellcasting ability."
            }
        }
    },
    "Priest Acolyte": {
        "Name": "Priest Acolyte",
        "Size": "Medium or Small",
        "Type": "Humanoid (Cleric)",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 0,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {
            "Walk": 30
        },
        "STR": 14,
        "DEX": 10,
        "CON": 12,
        "INT": 10,
        "WIS": 14,
        "CHA": 11,
        "STR Save": 2,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 2,
        "CHA Save": 0,
        "Skills": {
            "Medicine": 4,
            "Religion": 2
        },
        "Senses": {
            "Passive Perception": 12
        },
        "Languages": ["Common"],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Gear": ["Chain Shirt", "Holy Symbol", "Mace"],
        "Actions": {
            "Mace": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Bludgeoning",
                "Bonus Damage": {
                    "Amount": "1d4",
                    "Type": "Radiant"
                }
            },
            "Radiant Flame": {
                "Attack Type": "Ranged Spell Attack",
                "Attack Bonus": 4,
                "Range": "60 ft.",
                "Hit Average": 7,
                "Damage": "2d6",
                "Damage Type": "Radiant"
            },
            "Spellcasting": {
                "Description": "The priest casts one of the following spells, using Wisdom as the spellcasting ability:",
                "At Will": ["Light", "Thaumaturgy"]
            }
        },
        "Bonus Actions": {
            "Divine Aid (1/Day)": {
                "Description": "The priest casts Bless, Healing Word, or Sanctuary, using Wisdom as the spellcasting ability."
            }
        }
    },
    "Questing Knight": {
        "Name": "Questing Knight",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 18,
        "Initiative": 7,
        "HP": 202,
        "Hit Dice": "27d8 + 81",
        "Speed": {
            "Walk": 30
        },
        "STR": 20,
        "DEX": 16,
        "CON": 16,
        "INT": 11,
        "WIS": 12,
        "CHA": 18,
        "STR Save": 9,
        "DEX Save": 3,
        "CON Save": 7,
        "INT Save": 0,
        "WIS Save": 5,
        "CHA Save": 8,
        "Skills": {
            "Athletics": 9,
            "Perception": 5,
            "Persuasion": 8
        },
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": ["Common", "One other language"],
        "Condition Immunities": ["Charmed", "Frightened"],
        "Challenge": Fraction(12, 1),
        "XP": 8400,
        "Proficiency Bonus": 4,
        "Traits": {
            "Aura of Bravery": {
                "Description": "Creatures of the knight’s choice within 30 ft. of it are immune to the Charmed and Frightened conditions."
            }
        },
        "Gear": ["Greatsword", "Longbow", "Plate Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The knight makes three attacks, using Greatsword or Longbow in any combination."
            },
            "Greatsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 9,
                "Reach": "5 ft.",
                "Hit Average": 34,
                "Damage": "2d6 + 5 plus 5d8",
                "Damage Type": "Slashing plus Radiant"
            },
            "Longbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 7,
                "Range": "150/600 ft.",
                "Hit Average": 34,
                "Damage": "2d8 + 3 plus 5d8",
                "Damage Type": "Piercing plus Radiant"
            },
            "Spellcasting": {
                "Description": "The knight casts one of the following spells (DC 16, Charisma): 1/day each - Daylight, Dispel Evil and Good, Greater Restoration, Phantom Steed"
            }
        }
    },
    "Scout": {
        "Name": "Scout",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 2,
        "HP": 16,
        "Hit Dice": "3d8 + 3",
        "Speed": {
            "Walk": 30
        },
        "STR": 11,
        "DEX": 14,
        "CON": 12,
        "INT": 11,
        "WIS": 13,
        "CHA": 11,
        "STR Save": 0,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 1,
        "CHA Save": 0,
        "Skills": {
            "Nature": 4,
            "Perception": 5,
            "Stealth": 6,
            "Survival": 5
        },
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": ["Common", "One other language"],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Gear": ["Leather Armor", "Longbow", "Shortsword"],
        "Actions": {
            "Multiattack": {
                "Description": "The scout makes two attacks, using Shortsword and Longbow in any combination."
            },
            "Shortsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Piercing"
            },
            "Longbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 4,
                "Range": "150/600 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Piercing"
            }
        }
    },
    "Scout Captain": {
        "Name": "Scout Captain",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 15,
        "Initiative": 5,
        "HP": 66,
        "Hit Dice": "12d8 + 12",
        "Speed": {
            "Walk": 30,
            "Climb": 30
        },
        "STR": 11,
        "DEX": 16,
        "CON": 12,
        "INT": 14,
        "WIS": 15,
        "CHA": 11,
        "STR Save": 0,
        "DEX Save": 5,
        "CON Save": 1,
        "INT Save": 4,
        "WIS Save": 2,
        "CHA Save": 0,
        "Skills": {
            "Perception": 6,
            "Stealth": 7,
            "Survival": 6
        },
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Common", "One other language"],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 2,
        "Gear": ["Studded Leather Armor", "Longbow", "Shortsword"],
        "Traits": {},
        "Actions": {
            "Multiattack": {
                "Description": "The scout makes two attacks, using Shortsword or Longbow in any combination."
            },
            "Shortsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Piercing",
                "Extra Damage": "10 (3d6) Piercing damage if the attack was made with Advantage."
            },
            "Longbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 5,
                "Range": "150/600 ft.",
                "Hit Average": 7,
                "Damage": "1d8 + 3",
                "Damage Type": "Piercing",
                "Extra Damage": "10 (3d6) Piercing damage if the attack was made with Advantage."
            }
        },
        "Bonus Actions": {
            "Aim": {
                "Description": "The scout has Advantage on the next attack roll it makes during the current turn."
            }
        },
        "Reactions": {
            "Uncanny Dodge": {
                "Trigger": "The scout is hit by an attack roll.",
                "Response": "The scout halves the damage (round down) it takes from that attack."
            }
        }
    },
    "Spy": {
        "Name": "Spy",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 12,
        "Initiative": 4,
        "HP": 27,
        "Hit Dice": "6d8",
        "Speed": {
            "Walk": 30,
            "Climb": 30
        },
        "STR": 10,
        "DEX": 15,
        "CON": 10,
        "INT": 12,
        "WIS": 14,
        "CHA": 16,
        "STR Save": 0,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": 1,
        "WIS Save": 2,
        "CHA Save": 3,
        "Skills": {
            "Deception": 5,
            "Insight": 4,
            "Investigation": 5,
            "Perception": 6,
            "Sleight of Hand": 4,
            "Stealth": 6
        },
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Common", "One other language"],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Gear": ["Hand Crossbow", "Shortsword", "Thieves’ Tools"],
        "Actions": {
            "Shortsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Piercing",
                "Extra Damage": "7 (2d6) Poison damage"
            },
            "Hand Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 4,
                "Range": "30/120 ft.",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Piercing",
                "Extra Damage": "7 (2d6) Poison damage"
            }
        },
        "Bonus Actions": {
            "Cunning Action": {
                "Description": "The spy takes the Dash, Disengage, or Hide action."
            }
        }
    },
    "Spy Master": {
        "Name": "Spy Master",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 19,
        "Initiative": 9,
        "HP": 137,
        "Hit Dice": "25d8 + 25",
        "Speed": {
            "Walk": 30,
            "Climb": 30
        },
        "STR": 10,
        "DEX": 20,
        "CON": 12,
        "INT": 18,
        "WIS": 16,
        "CHA": 16,
        "STR Save": 0,
        "DEX Save": 9,
        "CON Save": 5,
        "INT Save": 8,
        "WIS Save": 7,
        "CHA Save": 3,
        "Skills": {
            "Deception": 7,
            "Insight": 7,
            "Investigation": 8,
            "Perception": 11,
            "Sleight of Hand": 9,
            "Stealth": 13
        },
        "Senses": {
            "Passive Perception": 21
        },
        "Languages": ["Common", "Two other languages"],
        "Challenge": Fraction(10, 1),
        "XP": 5900,
        "Proficiency Bonus": 4,
        "Gear": ["Hand Crossbow", "Rapier", "Thieves’ Tools"],
        "Actions": {
            "Multiattack": {
                "Description": "The spy makes three attacks, using Rapier or Hand Crossbow in any combination."
            },
            "Rapier": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 9,
                "Reach": "5 ft.",
                "Hit Average": 14,
                "Damage": "2d8 + 5",
                "Damage Type": "Piercing",
                "Extra Damage": "7 (2d6) Poison damage"
            },
            "Hand Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 9,
                "Range": "30/120 ft.",
                "Hit Average": 12,
                "Damage": "2d6 + 5",
                "Damage Type": "Piercing",
                "Extra Damage": "9 (2d8) Poison damage"
            },
            "Smoke Bomb": {
                "Usage": "1/Day",
                "Description": "Throws a bomb to a point it can see within 30 ft. Creatures in 20-ft-radius sphere must make DC 16 CON save. On fail: 28 (8d6) poison damage and Blinded until end of spy’s next turn. Success: Half damage."
            }
        },
        "Bonus Actions": {
            "Cunning Action": {
                "Description": "The spy takes the Dash, Disengage, or Hide action."
            }
        }
    },
    "Tough": {
        "Name": "Tough",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 12,
        "Initiative": 1,
        "HP": 32,
        "Hit Dice": "5d8+10",
        "Speed": {
            "Walk": 30
        },
        "STR": 15,
        "DEX": 12,
        "CON": 14,
        "INT": 10,
        "WIS": 10,
        "CHA": 11,
        "STR Save": 2,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": 0,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common"],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": {
                "Description": "The tough has Advantage on an attack roll against a creature if at least one of the tough’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
            }
        },
        "Gear": ["Heavy Crossbow", "Leather Armor", "Mace"],
        "Actions": {
            "Mace": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d6+2",
                "Damage Type": "Bludgeoning"
            },
            "Heavy Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 3,
                "Range": "100/400 ft.",
                "Hit Average": 6,
                "Damage": "1d10+1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Tough Boss": {
        "Name": "Tough Boss",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 16,
        "Initiative": 2,
        "HP": 82,
        "Hit Dice": "11d8+33",
        "Speed": {
            "Walk": 30
        },
        "STR": 17,
        "DEX": 14,
        "CON": 16,
        "INT": 11,
        "WIS": 10,
        "CHA": 11,
        "STR Save": 5,
        "DEX Save": 2,
        "CON Save": 5,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": 2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common", "One other language"],
        "Challenge": 4,
        "XP": 1100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": {
                "Description": "The tough has Advantage on an attack roll against a creature if at least one of the tough’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
            }
        },
        "Gear": ["Chain Mail", "Heavy Crossbow", "Warhammer"],
        "Actions": {
            "Multiattack": {
                "Description": "The tough makes two attacks, using Warhammer or Heavy Crossbow in any combination."
            },
            "Warhammer": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 12,
                "Damage": "2d8+3",
                "Damage Type": "Bludgeoning",
                "Additional Effect": "If the target is a Large or smaller creature, the tough pushes the target up to 10 feet straight away from itself."
            },
            "Heavy Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 4,
                "Range": "100/400 ft.",
                "Hit Average": 13,
                "Damage": "2d10+2",
                "Damage Type": "Piercing"
            }
        }
    },
    "Warrior Infantry": {
        "Name": "Warrior Infantry",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 13,
        "Initiative": 0,
        "HP": 9,
        "Hit Dice": "2d8",
        "Speed": {
            "Walk": 30
        },
        "STR": 13,
        "DEX": 11,
        "CON": 11,
        "INT": 8,
        "WIS": 11,
        "CHA": 8,
        "STR Save": 1,
        "DEX Save": 0,
        "CON Save": 0,
        "INT Save": -1,
        "WIS Save": 0,
        "CHA Save": -1,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common"],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": {
                "Description": "The warrior has Advantage on an attack roll against a creature if at least one of the warrior’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
            }
        },
        "Gear": ["Chain Shirt", "Spear"],
        "Actions": {
            "Spear": {
                "Attack Type": "Melee or Ranged Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Range": "20/60 ft.",
                "Hit Average": 4,
                "Damage": "1d6+1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Warrior Veteran": {
        "Name": "Warrior Veteran",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 17,
        "Initiative": 3,
        "HP": 65,
        "Hit Dice": "10d8+20",
        "Speed": {
            "Walk": 30
        },
        "STR": 16,
        "DEX": 13,
        "CON": 14,
        "INT": 10,
        "WIS": 11,
        "CHA": 10,
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": 0,
        "Skills": {
            "Athletics": 5,
            "Perception": 2
        },
        "Senses": {
            "Passive Perception": 12
        },
        "Languages": ["Common", "One other language"],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 2,
        "Gear": ["Greatsword", "Heavy Crossbow", "Splint Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The warrior makes two Greatsword or Heavy Crossbow attacks."
            },
            "Greatsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 10,
                "Damage": "2d6+3",
                "Damage Type": "Slashing"
            },
            "Heavy Crossbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 3,
                "Range": "100/400 ft.",
                "Hit Average": 12,
                "Damage": "2d10+1",
                "Damage Type": "Piercing"
            }
        },
        "Reactions": {
            "Parry": {
                "Trigger": "The warrior is hit by a melee attack roll while holding a weapon.",
                "Response": "The warrior adds 2 to its AC against that attack, possibly causing it to miss."
            }
        }
    },
    "Warrior Commander": {
        "Name": "Warrior Commander",
        "Size": "Medium or Small",
        "Type": "Humanoid",
        "Alignment": "Neutral",
        "AC": 18,
        "Initiative": 9,
        "HP": 161,
        "Hit Dice": "19d8 + 76",
        "Speed": {
            "Walk": 30
        },
        "STR": 21,
        "DEX": 20,
        "CON": 18,
        "INT": 14,
        "WIS": 16,
        "CHA": 14,
        "STR Save": 9,
        "DEX Save": 9,
        "CON Save": 8,
        "INT Save": 2,
        "WIS Save": 7,
        "CHA Save": 2,
        "Skills": {
            "Athletics": 9,
            "Insight": 7,
            "Perception": 7
        },
        "Senses": {
            "Passive Perception": 17
        },
        "Languages": ["Common", "One other language"],
        "Challenge": Fraction(10, 1),
        "XP": 5900,
        "Proficiency Bonus": 4,
        "Traits": {},
        "Gear": ["Greatsword", "Longbow", "Plate Armor"],
        "Actions": {
            "Multiattack": {
                "Description": "The warrior makes three attacks, using Greatsword or Longbow in any combination."
            },
            "Greatsword": {
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 9,
                "Reach": "5 ft.",
                "Hit Average": 19,
                "Damage": "4d6 + 5",
                "Damage Type": "Slashing",
                "Additional Effects": [
                    "Sap: The target has Disadvantage on its next attack roll before the start of the warrior’s next turn.",
                    "Maneuver: One ally who can see or hear the warrior can take a Reaction to move up to half the ally’s Speed without provoking Opportunity Attacks."
                ]
            },
            "Longbow": {
                "Attack Type": "Ranged Weapon Attack",
                "Attack Bonus": 9,
                "Range": "150/600 ft.",
                "Hit Average": 18,
                "Damage": "3d8 + 5",
                "Damage Type": "Piercing",
                "Additional Effects": [
                    "The target’s Speed decreases by 10 feet until the end of the target’s next turn."
                ]
            }
        },
        "Bonus Actions": {
            "Tactical Charge": {
                "Description": "The warrior moves up to half its Speed straight toward an enemy it can see without provoking Opportunity Attacks."
            }
        },
        "Reactions": {
            "Counterattack": {
                "Trigger": "The warrior is hit by an attack roll.",
                "Response": "The warrior adds 4 to its AC against that attack, possibly causing it to miss. On a miss, the warrior can make one Greatsword or Longbow attack against the attacker."
            }
        }
    },
}