from fractions import Fraction

monsters = {
    "Ankylosaurus": {
        "Name": "Ankylosaurus",
        "Size": "Huge",
        "Type": "Beast (Dinosaur)",
        "Alignment": "Unaligned",
        "AC": 15,
        "Initiative": 0,
        "HP": 68,
        "Hit Dice": "8d12 + 16",
        "Speed": {"Walk": 30},
        "Ability Scores": {
            "STR": 19,
            "DEX": 11,
            "CON": 15,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 6,
        "DEX Save": 0,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {},
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": 3,
        "Proficiency Bonus": 2,
        "XP": 700,
        "Actions": {
            "Multiattack": {
                "Description": "The ankylosaurus makes two Tail attacks.",
                "Sequence": ["Tail", "Tail"],
                "Attacks": {
                    "Tail": {
                        "Name": "Tail",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 6,
                        "Target Size": "Huge",
                        "Reach": "10 ft.",
                        "Hit Average": 9,
                        "Damage": "1d10 + 4",
                        "Damage Type": "Bludgeoning",
                        "Effect": "If the target is a Huge or smaller creature, it is knocked Prone."
                    }
                }
            }
        }
    },
    "Ape": {
        "Name": "Ape",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 19,
        "Hit Dice": "3d8+6",
        "Speed": {'Walk': 30, 'Climb': 30},
        "Ability Scores": {
            "STR": 16,
            "DEX": 14,
            "CON": 14,
            "INT": 6,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 3,
        "DEX Save": 2,
        "CON Save": 2,
        "INT Save": -2,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {'Athletics': 5, 'Perception': 3},
        "Senses": {
            "Passive Perception": 13,
        },
        "Challenge": Fraction(1,2),
        "Proficiency Bonus": 2,
        "XP": 100,        
        "Actions": {
            "Multiattack": {
                "Description": "The ape makes two fist attacks.",
                "Sequence": ["Fist", "Fist"],
                "Attacks": {
                    "Fist": {
                        "Name": "Fist",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Hit Average": 5,
                        "Damage": "1d4 + 3",
                        "Damage Type": "Bludgeoning"
                    },
                },
            },
            "Rock": {
                "Name": "Rock",
                "Attack Type": "Ranged Weapon Attack",
                "Recharge": 6,
                "Attack Bonus": 5,
                "Range": {
                    "Normal": 25,
                    "Long": 50,
                },
                "Hit Average": 10,
                "Damage": "2d6 + 3",
                "Damage Type": "Bludgeoning"
            },
        },
    }, 
    "Awakened Shrub": {
        "Name": "Awakened Shrub",
        "Size": "Small",
        "Type": "Plant",
        "Alignment": "Unaligned",
        "AC": 9,
        "Initiative": -1,
        "HP": 10,
        "Hit Dice": "3d6",
        "Speed": {'Walk': 20},
        "Ability Scores": {
            "STR": 3,
            "DEX": 8,
            "CON": 11,
            "INT": 10,
            "WIS": 10,
            "CHA": 6,
        },
        "STR Save": -4,
        "DEX Save": -1,
        "CON Save": 0,
        "INT Save": 0,
        "WIS Save": 0,
        "CHA Save": -2,
        "Vulnerabilities": ["Fire"],
        "Resistances": ["Piercing"],
        "Languages": ["Common", "One Other"],
        "Skills": {},
        "Senses": {
            "Passive Perception": 10,
        },
        "Challenge": 0,
        "Proficiency Bonus": 2,
        "XP": 10,
        "Traits": {
            "False Appearance": {
                "Description": "While the shrub remains motionless, it is indistinguishable from a normal shrub."
            }
        },
        "Actions": {
            "Rake": {
                "Name": "Rake",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 1,
                "Reach": "5 ft.",
                "Damage": "1",
                "Damage Type": "Slashing"
            }
        }
    },
    "Awakened Tree": {
        "Name": "Awakened Tree",
        "Size": "Huge",
        "Type": "Plant",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": -2,
        "HP": 59,
        "Hit Dice": "7d12 + 14",
        "Speed": {"Walk": 20},
        "Ability Scores": {
            "STR": 19,
            "DEX": 6,
            "CON": 15,
            "INT": 10,
            "WIS": 10,
            "CHA": 7,
        },
        "STR Save": 4,
        "Skills": {},
        "Vulnerabilities": ["Fire"],
        "Resistances": ["Bludgeoning", "Piercing"],
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": ["Common", "One Other"],
        "Challenge": 2,
        "Proficiency Bonus": 2,
        "XP": 450,
        "Actions": {
            "Slam": {
                "Name": "Slam",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "10 ft.",
                "Hit Average": 14,
                "Damage": "3d6 + 4",
                "Damage Type": "Bludgeoning",
            }
        }
    },
    "Axe Beak": {
        "Name": "Axe Beak",
        "Size": "Large",
        "Type": "Monstrosity",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 19,
        "Hit Dice": "3d10 + 3",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 14,
            "DEX": 12,
            "CON": 13,
            "INT": 2,
            "WIS": 10,
            "CHA": 5,
        },
        "STR Save": 2,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1,4),
        "Proficiency Bonus": 2,
        "XP": 50,
        "Actions": {
            "Beak": {
                "Name": "Beak",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Slashing"
            }
        }
    },
    "Baboon": {
        "Name": "Baboon",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 3,
        "Hit Dice": "1d6",
        "Speed": {
            "Walk": 30,
            "Climb": 30
        },
        "Ability Scores": {
            "STR": 8,
            "DEX": 14,
            "CON": 11,
            "INT": 4,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": -1,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -3,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": 0,
        "Proficiency Bonus": 2,
        "XP": 10,
        "Traits": {
            "Pack Tactics": "The baboon has Advantage on an attack roll against a creature if at least one of the baboon’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 1,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1d4 - 1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Badger": {
        "Name": "Badger",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 0,
        "HP": 5,
        "Hit Dice": "1d4 + 3",
        "Speed": {
            "Walk": 20,
            "Burrow": 5
        },
        "Ability Scores": {
            "STR": 10,
            "DEX": 11,
            "CON": 16,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 0,
        "DEX Save": 0,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {
            "Perception": 3
        },
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 13
        },
        "Resistances": ["Poison"],
        "Vulnerabilities": [],
        "Languages": [],
        "Challenge": 0,
        "Proficiency Bonus": 2,
        "XP": 10,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Bat": {
        "Name": "Bat",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {
            "Walk": 5,
            "Fly": 30
        },
        "Ability Scores": {
            "STR": 2,
            "DEX": 15,
            "CON": 8,
            "INT": 2,
            "WIS": 12,
            "CHA": 4,
        },
        "STR Save": -4,
        "DEX Save": 2,
        "CON Save": -1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {},
        "Senses": {
            "Blindsight": 60,
            "Passive Perception": 11
        },
        "Resistances": [],
        "Vulnerabilities": [],
        "Languages": [],
        "Challenge": 0,
        "Proficiency Bonus": 2,
        "XP": 10,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Black Bear": {
        "Name": "Black Bear",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 19,
        "Hit Dice": "3d8 + 6",
        "Speed": {"Walk": 30, "Climb": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 15,
            "DEX": 12,
            "CON": 14,
            "INT": 2,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 2,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 5},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The bear makes two Rend attacks.",
                "Sequence": ["Rend", "Rend"],
                "Attacks": {
                    "Rend": {
                        "Name": "Rend",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 4,
                        "Reach": "5 ft.",
                        "Hit Average": 5,
                        "Damage": "1d6 + 2",
                        "Damage Type": "Slashing"
                    }
                }
            }
        }
    },
    "Blink Dog": {
        "Name": "Blink Dog",
        "Size": "Medium",
        "Type": "Fey",
        "Alignment": "Lawful Good",
        "AC": 13,
        "Initiative": 3,
        "HP": 22,
        "Hit Dice": "4d8 + 4",
        "Speed": {
            "Walk": 40
        },
        "Ability Scores": {
            "STR": 12,
            "DEX": 17,
            "CON": 12,
            "INT": 10,
            "WIS": 13,
            "CHA": 11,
        },
        "STR Save": 1,
        "DEX Save": 3,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 1,
        "CHA Save": 0,
        "Skills": {
            "Perception": 5,
            "Stealth": 5
        },
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": ["Blink Dog (spoken)", "Understands Elvish", "Understands Sylvan"],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d4 + 3",
                "Damage Type": "Piercing"
            }
        },
        "Bonus Actions": {
            "Teleport": {
                "Description": "The dog teleports up to 40 feet to an unoccupied space it can see.",
                "Recharge": [4, 5, 6]
            }
        }
    },   
    "Blood Hawk": {
        "Name": "Blood Hawk",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 7,
        "Hit Dice": "2d6",
        "Speed": {"Walk": 10, "Fly": 60},
        "Ability Scores": {
            "STR": 6,
            "DEX": 14,
            "CON": 10,
            "INT": 3,
            "WIS": 14,
            "CHA": 5,
        },
        "STR Save": -2,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 2,
        "CHA Save": -3,
        "Skills": {"Perception": 6},
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The hawk has Advantage on an attack roll against a creature if at least one of the hawk’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
        },
        "Actions": {
            "Beak": {
                "Name": "Beak",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Piercing",
                "Conditional Extra": {
                    "Condition": "Bloodied",
                    "Damage": "1d8 + 2",
                    "Damage Average": 6
                }
            }
        }
    },
    "Boar": {
        "Name": "Boar",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 0,
        "HP": 13,
        "Hit Dice": "2d8 + 4",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 13,
            "DEX": 11,
            "CON": 14,
            "INT": 2,
            "WIS": 9,
            "CHA": 5,
        },
        "STR Save": 1,
        "DEX Save": 0,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": -1,
        "CHA Save": -3,
        "Senses": {
            "Passive Perception": 9
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Bloodied Fury": "While Bloodied, the boar has Advantage on attack rolls."
        },
        "Actions": {
            "Gore": {
                "Name": "Gore",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d6 + 1",
                "Damage Type": "Piercing",
                "Bonus Damage": {
                    "Condition": "Moved 20+ ft. straight toward target",
                    "Bonus": "1d6",
                    "Bonus Average": 3,
                    "Extra Effect": "Target (Medium or smaller) is knocked Prone"
                }
            }
        }
    },
    "Brown Bear": {
        "Name": "Brown Bear",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 22,
        "Hit Dice": "3d10 + 6",
        "Speed": {"Walk": 40, "Climb": 30},
        "Ability Scores": {
            "STR": 17,
            "DEX": 12,
            "CON": 15,
            "INT": 2,
            "WIS": 13,
            "CHA": 7,
        },
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The bear makes one Bite attack and one Claw attack.",
                "Sequence": ["Bite", "Claw"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Hit Average": 7,
                        "Damage": "1d8 + 3",
                        "Damage Type": "Piercing"
                    },
                    "Claw": {
                        "Name": "Claw",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Target Size": "Large",
                        "Hit Average": 5,
                        "Damage": "1d4 + 3",
                        "Damage Type": "Slashing",
                        "Effect": "If the target is a Large or smaller creature, it is knocked Prone."
                    }
                }
            }
        }
    },
    "Camel": {
        "Name": "Camel",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": -1,
        "HP": 17,
        "Hit Dice": "2d10 + 6",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 15,
            "DEX": 8,
            "CON": 17,
            "INT": 2,
            "WIS": 11,
            "CHA": 5,
        },
        "STR Save": 2,
        "DEX Save": -1,
        "CON Save": 5,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Cat": {
        "Name": "Cat",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 2,
        "Hit Dice": "1d4",
        "Speed": {"Walk": 40, "Climb": 40},
        "Ability Scores": {
            "STR": 3,
            "DEX": 15,
            "CON": 10,
            "INT": 3,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": -4,
        "DEX Save": 4,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3, "Stealth": 4},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Jumper": "The cat’s jump distance is determined using its Dexterity rather than its Strength."
        },
        "Actions": {
            "Scratch": {
                "Name": "Scratch",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Slashing"
            }
        }
    },
    "Constrictor Snake": {
        "Name": "Constrictor Snake",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 2,
        "HP": 13,
        "Hit Dice": "2d10 + 2",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 15,
            "DEX": 14,
            "CON": 12,
            "INT": 1,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": 2,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {"Perception": 2, "Stealth": 4},
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Piercing"
            },
            "Constrict": {
                "Name": "Constrict",
                "Attack Type": "Saving Throw",
                "Save Type": "STR",
                "Save DC": 12,
                "Reach": "5 ft.",
                "Target Size": "Medium",
                "Hit Average": 7,
                "Damage": "3d4",
                "Damage Type": "Bludgeoning",
                "Effect": {
                    "Name": "Grappled",
                    "Escape Modifier": "STR",
                    "Escape DC": 12,
                }
            }
        }
    },
    "Crab": {
        "Name": "Crab",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 0,
        "HP": 3,
        "Hit Dice": "1d4 + 1",
        "Speed": {"Walk": 20, "Swim": 20},
        "Ability Scores": {
            "STR": 6,
            "DEX": 11,
            "CON": 12,
            "INT": 1,
            "WIS": 8,
            "CHA": 2,
        },
        "STR Save": -2,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": -5,
        "WIS Save": -1,
        "CHA Save": -4,
        "Skills": {"Stealth": 2},
        "Senses": {
            "Blindsight": 30,
            "Passive Perception": 9
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Amphibious": "The crab can breathe air and water."
        },
        "Actions": {
            "Claw": {
                "Name": "Claw",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Crocodile": {
        "Name": "Crocodile",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 0,
        "HP": 13,
        "Hit Dice": "2d10 + 2",
        "Speed": {"Walk": 20, "Swim": 30},
        "Ability Scores": {
            "STR": 15,
            "DEX": 10,
            "CON": 13,
            "INT": 2,
            "WIS": 10,
            "CHA": 5,
        },
        "STR Save": 2,
        "DEX Save": 0,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Stealth": 2},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Hold Breath": "The crocodile can hold its breath for 1 hour."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Piercing",
                "Target Size": "Medium",
                "Effect": {
                    "Name": "Grappled (Restrained)",
                    "Escape Modifier": "STR",
                    "Escape DC": 12,
                }
            }
        }
    },
    "Death Dog": {
        "Name": "Death Dog",
        "Size": "Medium",
        "Type": "Monstrosity",
        "Alignment": "Neutral Evil",
        "AC": 12,
        "Initiative": 2,
        "HP": 39,
        "Hit Dice": "6d8 + 12",
        "Speed": {
            "Walk": 40
        },
        "Ability Scores": {
            "STR": 15,
            "DEX": 14,
            "CON": 14,
            "INT": 3,
            "WIS": 13,
            "CHA": 6,
        },
        "STR Save": 2,
        "DEX Save": 2,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {
            "Perception": 5,
            "Stealth": 4
        },
        "Immunities": ["Blinded", "Charmed", "Deafened", "Frightened", "Stunned", "Unconscious"],
        "Senses": {
            "Darkvision": 120,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The death dog makes two Bite attacks.",
                "Sequence": ["Bite", "Bite"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 4,
                        "Reach": "5 ft.",
                        "Hit Average": 4,
                        "Damage": "1d4 + 2",
                        "Damage Type": "Piercing",
                        "Effect": {
                            "Name": "Poisoned",
                            "Save Type": "CON",
                            "Save DC": 12,
                            "Condition Dice": "1d10"
                        }
                    }
                }
            }
        }
    },    
    "Deer": {
        "Name": "Deer",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 4,
        "Hit Dice": "1d8",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 11,
            "DEX": 16,
            "CON": 11,
            "INT": 2,
            "WIS": 14,
            "CHA": 5,
        },
        "STR Save": 0,
        "DEX Save": 3,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 2,
        "CHA Save": -3,
        "Skills": {"Perception": 4},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 14
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Agile": "The deer doesn’t provoke an Opportunity Attack when it moves out of an enemy’s reach."
        },
        "Actions": {
            "Ram": {
                "Name": "Ram",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 2,
                "Damage": "1d4",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Dire Wolf": {
        "Name": "Dire Wolf",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 2,
        "HP": 22,
        "Hit Dice": "3d10 + 6",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 17,
            "DEX": 15,  
            "CON": 15,
            "INT": 3,
            "WIS": 12,
            "CHA": 7,   
        },
        "STR Save": 3,
        "DEX Save": 2,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 5, "Stealth": 4},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The wolf has Advantage on an attack roll against a creature if at least one of the wolf’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Target Size": "Large",
                "Hit Average": 8,
                "Damage": "1d10 + 3",
                "Damage Type": "Piercing",
                "Effect": "If the target is a Large or smaller creature, it is knocked Prone."
            }
        }
    },
    "Diseased Giant Rat": {
        "Name": "Diseased Giant Rat",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 7,
        "Hit Dice": "2d6",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 7,
            "DEX": 16,
            "CON": 11,
            "INT": 2,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": -2,
        "DEX Save": 5,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The rat has advantage on an attack roll against a creature if at least one of the rat’s allies is within 5 feet of the creature and the ally isn’t incapacitated."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Piercing",
                "Effect": {
                    "Name": "Diseased",
                    "Save Type": "CON",
                    "Save DC": 10,
                },
                "Description": "If the target is a creature, it must succeed on a DC 10 Constitution saving throw or contract a disease. Until the disease is cured, the target can't regain hit points except by magical means, and the target's hit point maximum decreases by 3 (1d6) every 24 hours. If the target's hit point maximum drops to 0 as a result of this disease, the target dies."
            }
        }
    },    
    "Draft Horse": {
        "Name": "Draft Horse",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 15,
        "Hit Dice": "2d10 + 4",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 18,
            "DEX": 10,
            "CON": 15,
            "INT": 2,
            "WIS": 11,
            "CHA": 7,
        },
        "STR Save": 4,
        "DEX Save": 0,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Hooves": {
                "Name": "Hooves",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d4 + 4",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Elephant": {
        "Name": "Elephant",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": -1,
        "HP": 76,
        "Hit Dice": "8d12 + 24",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 22,
            "DEX": 9,
            "CON": 17,
            "INT": 3,
            "WIS": 11,
            "CHA": 6,
        },
        "STR Save": 6,
        "DEX Save": -1,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 4,
        "XP": 1100,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The elephant makes two Gore attacks.",
                "Sequence": ["Gore", "Gore"],
                "Attacks": {
                    "Gore": {
                        "Name": "Gore",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 8,
                        "Reach": "5 ft.",
                        "Hit Average": 15,
                        "Damage": "2d8 + 6",
                        "Damage Type": "Piercing",
                        "Extra Effect": "If the target is Huge or smaller and the elephant moved 20+ feet straight toward it, the target is knocked Prone."
                    }
                }                
            },
        },
        "Bonus Actions": {
            "Trample": {
                "Save Type": "Dexterity",
                "Save DC": 16,
                "Target": "One creature within 5 ft. that is Prone",
                "Failure": "17 (2d10 + 6) Bludgeoning damage",
                "Success": "Half damage"
            }
        }
    },
    "Eagle": {
        "Name": "Eagle",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 4,
        "Hit Dice": "1d6 + 1",
        "Speed": {"Walk": 10, "Fly": 60},
        "Ability Scores": {
            "STR": 6,
            "DEX": 15,
            "CON": 12,
            "INT": 2,
            "WIS": 14,
            "CHA": 7,
        },
        "STR Save": -2,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 2,
        "CHA Save": -2,
        "Skills": {"Perception": 6},
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Actions": {
            "Talons": {
                "Name": "Talons",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Slashing"
            }
        }
    },
    "Elk": {
        "Name": "Elk",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 11,
        "Hit Dice": "2d10",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 16,
            "DEX": 10,
            "CON": 11,
            "INT": 2,
            "WIS": 10,
            "CHA": 6,
        },
        "STR Save": 3,
        "DEX Save": 0,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Skills": {"Perception": 2},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Ram": {
                "Name": "Ram",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Bludgeoning",
                "Extra Effect": "If the elk moved 20+ feet straight toward the target, it takes an extra 3 (1d6) Bludgeoning damage and is knocked Prone."
            }
        }
    },
    "Flying Snake": {
        "Name": "Flying Snake",
        "Size": "Tiny",
        "Type": "Monstrosity",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 2,
        "HP": 5,
        "Hit Dice": "2d4",
        "Speed": {"Walk": 30, "Fly": 60, "Swim": 30},
        "Ability Scores": {
            "STR": 4,
            "DEX": 15,
            "CON": 11,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": -3,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {},
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Flyby": "The snake doesn’t provoke an Opportunity Attack when it flies out of an enemy’s reach."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage Components": [
                    {"Dice": "1", "Modifier": "1", "Type": "Piercing"},
                    {"Dice": "2d4", "Type": "Poison"}
                ]
            }
        }
    },
    "Frog": {
        "Name": "Frog",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 20, "Swim": 20},
        "Ability Scores": {
            "STR": 1,
            "DEX": 13,
            "CON": 8,
            "INT": 1,
            "WIS": 8,
            "CHA": 3,
        },
        "STR Save": -5,
        "DEX Save": 1,
        "CON Save": -1,
        "INT Save": -5,
        "WIS Save": -1,
        "CHA Save": -4,
        "Skills": {"Perception": 1, "Stealth": 3},
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Amphibious": "The frog can breathe air and water.",
            "Standing Leap": "The frog’s Long Jump is up to 10 feet and its High Jump is up to 5 feet with or without a running start."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Giant Ape": {
        "Name": "Giant Ape",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 168,
        "Hit Dice": "16d12 + 64",
        "Speed": {"Walk": 40, "Climb": 40},
        "Ability Scores": {
            "STR": 23,
            "DEX": 14,
            "CON": 18,
            "INT": 5,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 6,
        "DEX Save": 2,
        "CON Save": 4,
        "INT Save": -3,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Athletics": 9, "Perception": 4, "Survival": 4},
        "Senses": {
            "Passive Perception": 14
        },
        "Languages": [],
        "Challenge": 7,
        "XP": 2900,
        "Proficiency Bonus": 3,
        "Actions": {
            "Multiattack": {
                "Description": "The ape makes two Fist attacks.",
                "Sequence": ["Fist", "Fist"],
                "Attacks": {
                    "Fist": {
                        "Name": "Fist",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 9,
                        "Reach": "10 ft.",
                        "Hit Average": 22,
                        "Damage": "3d10 + 6",
                        "Damage Type": "Bludgeoning"
                    }
                }
            },
            "Boulder Toss": {
                "Name": "Boulder Toss",
                "Description": "The ape hurls a boulder at a point it can see within 90 ft.",
                "Recharge": 6,
                "Attack Type": "Area",
                "Range": "90 ft.",
                "Area": "5-ft-radius sphere",
                "Save DC": 17,
                "Save Type": "Dexterity",
                "Hit Average": 24,
                "Damage": "7d6",
                "Damage Type": "Bludgeoning",
                "Effect on Fail": "Takes full damage and becomes Prone (if Large or smaller)",
                "Effect on Success": "Half damage"
            }
        },
        "Bonus Actions": {
            "Leap": {
                "Description": "The ape jumps up to 30 feet by spending 10 feet of movement."
            }
        }
    },
    "Giant Badger": {
        "Name": "Giant Badger",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 0,
        "HP": 15,
        "Hit Dice": "2d8 + 6",
        "Speed": {"Walk": 30, "Burrow": 10},
        "Ability Scores": {
            "STR": 13,
            "DEX": 10,
            "CON": 17,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 1,
        "DEX Save": 0,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {"Perception": 3},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Resistances": ["Poison"],
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "2d4 + 1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Giant Bat": {
        "Name": "Giant Bat",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 22,
        "Hit Dice": "4d10",
        "Speed": {"Walk": 10, "Fly": 60},
        "Ability Scores": {
            "STR": 15,
            "DEX": 16,
            "CON": 11,
            "INT": 2,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": 2,
        "DEX Save": 3,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {},
        "Senses": {
            "Blindsight": 120,
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Piercing"
            }
        }
    },
    "Giant Boar": {
        "Name": "Giant Boar",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 0,
        "HP": 42,
        "Hit Dice": "5d10 + 15",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 17,
            "DEX": 10,
            "CON": 16,
            "INT": 2,
            "WIS": 7,
            "CHA": 5,
        },
        "STR Save": 5,
        "DEX Save": 0,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": -2,
        "CHA Save": -3,
        "Skills": {},
        "Senses": {
            "Passive Perception": 8
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {
            "Bloodied Fury": "The boar has Advantage on melee attack rolls while it is Bloodied."
        },
        "Actions": {
            "Gore": {
                "Name": "Gore",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 10,
                "Damage": "2d6 + 3",
                "Damage Type": "Piercing",
                "Additional Effect": "If the target is a Large or smaller creature and the boar moved 20+ feet straight toward it immediately before the hit, the target takes an extra 2d6 Piercing damage and is knocked Prone."
            }
        }
    },
    "Giant Centipede": {
        "Name": "Giant Centipede",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 2,
        "HP": 9,
        "Hit Dice": "2d6 + 2",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 5,
            "DEX": 14,
            "CON": 12,
            "INT": 1,
            "WIS": 7,
            "CHA": 3,
        },
        "STR Save": -3,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -5,
        "WIS Save": -2,
        "CHA Save": -4,
        "Senses": {
            "Blindsight": 30,
            "Passive Perception": 8
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Piercing",
                "Additional Effects": "The target is Poisoned until the start of the centipede’s next turn."
            }
        }
    },
    "Giant Constrictor Snake": {
        "Name": "Giant Constrictor Snake",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 60,
        "Hit Dice": "8d12 + 8",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 19,
            "DEX": 14,
            "CON": 12,
            "INT": 1,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": 4,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {"Perception": 2},
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The snake makes one Bite attack and uses Constrict.",
                "Sequence": ["Bite", "Constrict"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 6,
                        "Reach": "10 ft.",
                        "Hit Average": 11,
                        "Damage": "2d6 + 4",
                        "Damage Type": "Piercing"
                    },
                    "Constrict": {
                        "Name": "Constrict",
                        "Attack Type": "Saving Throw",
                        "Save Type": "STR",
                        "Save DC": 14,
                        "Reach": "5 ft.",
                        "Target Size": "Large",
                        "Hit Average": 13,
                        "Damage": "2d8 + 4",
                        "Damage Type": "Bludgeoning",
                        "Effect": {
                            "Name": "Grappled",
                            "Escape Modifier": "STR",
                            "Escape DC": 14,
                        }
                    }
                }
            }
        }
    },
    "Giant Crab": {
        "Name": "Giant Crab",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 15,
        "Initiative": 1,
        "HP": 13,
        "Hit Dice": "3d8",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 13,
            "DEX": 13,
            "CON": 11,
            "INT": 1,
            "WIS": 9,
            "CHA": 3,
        },
        "STR Save": 1,
        "DEX Save": 1,
        "CON Save": 0,
        "INT Save": -5,
        "WIS Save": -1,
        "CHA Save": -4,
        "Skills": {"Stealth": 3},
        "Senses": {
            "Blindsight": 30,
            "Passive Perception": 9
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Amphibious": "The crab can breathe air and water."
        },
        "Actions": {
            "Claw": {
                "Name": "Claw",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Target Size": "Medium",
                "Damage": "1d6 + 1",
                "Damage Type": "Bludgeoning",
                "Effect": {
                    "Name": "Grappled",
                    "Escape Modifier": "STR",
                    "Escape DC": 11,
                }
            }
        }
    },
    "Giant Crocodile": {
        "Name": "Giant Crocodile",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": -1,
        "HP": 85,
        "Hit Dice": "9d12 + 27",
        "Speed": {"Walk": 30, "Swim": 50},
        "Ability Scores": {
            "STR": 21,
            "DEX": 9,
            "CON": 17,
            "INT": 2,
            "WIS": 10,
            "CHA": 7,
        },
        "STR Save": 5,
        "DEX Save": -1,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Skills": {"Stealth": 5},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 5,
        "XP": 1800,
        "Proficiency Bonus": 3,
        "Traits": {
            "Hold Breath": "The crocodile can hold its breath for 1 hour."
        },
        "Actions": {
            "Multiattack": {
                "Description": "The crocodile makes one Bite attack and one Tail attack.",
                "Sequence": ["Bite", "Tail"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 8,
                        "Reach": "5 ft.",
                        "Target Size": "Large",
                        "Hit Average": 21,
                        "Damage": "3d10 + 5",
                        "Damage Type": "Piercing",
                        "Effect": {
                            "Name": "Grappled (Restrained)",
                            "Escape Modifier": "STR",
                            "Escape DC": 15,
                        }                        
                    },
                    "Tail": {
                        "Name": "Tail",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 8,
                        "Target Size": "Large",
                        "Reach": "10 ft.",
                        "Hit Average": 18,
                        "Damage": "3d8 + 5",
                        "Damage Type": "Bludgeoning",
                        "Effect": "If the target is Large or smaller, it is knocked Prone."
                    }
                }
            }
        }
    },
    "Giant Eagle": {
        "Name": "Giant Eagle",
        "Size": "Large",
        "Type": "Celestial",
        "Alignment": "Neutral Good",
        "AC": 13,
        "Initiative": 3,
        "HP": 26,
        "Hit Dice": "4d10 + 4",
        "Speed": {"Walk": 10, "Fly": 80},
        "Ability Scores": {
            "STR": 16,
            "DEX": 17,
            "CON": 13,
            "INT": 8,
            "WIS": 14,
            "CHA": 10,
        },
        "STR Save": 3,
        "DEX Save": 3,
        "CON Save": 1,
        "INT Save": -1,
        "WIS Save": 2,
        "CHA Save": 0,
        "Skills": {"Perception": 6},
        "Resistances": ["Necrotic", "Radiant"],
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": ["Celestial"],
        "Understands": ["Common", "Primordial (Auran)"],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The eagle makes two Rend attacks.",
                "Sequence": ["Rend", "Rend"],
                "Attacks": {
                    "Rend": {
                        "Name": "Rend",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Hit Average": 5,
                        "Damage Components": [
                            {"Dice": "1d4", "Modifier": "3", "Type": "Slashing"},
                            {"Dice": "1d6", "Type": "Radiant"}
                        ]
                    }
                }
            }
        }
    },
    "Giant Elk": {
        "Name": "Giant Elk",
        "Size": "Huge",
        "Type": "Celestial",
        "Alignment": "Neutral Good",
        "AC": 14,
        "Initiative": 6,
        "HP": 42,
        "Hit Dice": "5d12 + 10",
        "Speed": {"Walk": 60},
        "Ability Scores": {
            "STR": 19,
            "DEX": 18,
            "CON": 14,
            "INT": 7,
            "WIS": 14,
            "CHA": 10,
        },
        "STR Save": 6,
        "DEX Save": 6,
        "CON Save": 2,
        "INT Save": -2,
        "WIS Save": 2,
        "CHA Save": 0,
        "Skills": {"Perception": 4},
        "Resistances": ["Necrotic", "Radiant"],
        "Senses": {
            "Darkvision": 90,
            "Passive Perception": 14
        },
        "Languages": ["Celestial"],
        "Understands": ["Common", "Elvish", "Sylvan"],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Actions": {
            "Ram": {
                "Name": "Ram",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "10 ft.",
                "Hit Average": 11,
                "Damage Components": [
                    {"Dice": "2d6", "Modifier": "4", "Type": "Bludgeoning"},
                    {"Dice": "2d4", "Type": "Radiant"}
                ],              
                "Additional Effects": "If the elk moved 20 ft. straight toward the target before the hit, it deals an extra 2d4 Bludgeoning damage and the target is knocked Prone (if Huge or smaller)."
            }
        }
    },
    "Giant Fire Beetle": {
        "Name": "Giant Fire Beetle",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 0,
        "HP": 4,
        "Hit Dice": "1d6 + 1",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 8,
            "DEX": 10,
            "CON": 12,
            "INT": 1,
            "WIS": 7,
            "CHA": 3,
        },
        "STR Save": -1,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": -5,
        "WIS Save": -2,
        "CHA Save": -4,
        "Skills": {},
        "Senses": {
            "Blindsight": 30,
            "Passive Perception": 8
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Resistances": ["Fire"],
        "Traits": {
            "Illumination": "The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 1,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Fire"
            }
        }
    },
    "Giant Frog": {
        "Name": "Giant Frog",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 18,
        "Hit Dice": "4d8",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 12,
            "DEX": 13,
            "CON": 11,
            "INT": 2,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": 1,
        "DEX Save": 1,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {"Perception": 2, "Stealth": 4},
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Amphibious": "The frog can breathe air and water.",
            "Standing Leap": "The frog’s long jump is up to 20 feet and its high jump is up to 10 feet with or without a running start."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Target Size": "Medium",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Piercing",
                "Effect": {
                    "Name": "Grappled",
                    "Escape Modifier": "STR",
                    "Escape DC": 11,
                }  
            },
            "Swallow": {
                "Description": "The frog swallows a Small or smaller target it is grappling. The target is Blinded and Restrained, and has Total Cover against attacks outside the frog. The frog can't use Bite while it swallows a creature. If the frog dies, the swallowed target can escape from the corpse using 5 feet of movement, exiting Prone. At the end of the frog’s next turn, the target takes 5 (2d4) Acid damage. If that doesn’t kill it, the frog disgorges it, and it exits Prone."
            }
        }
    },
    "Giant Goat": {
        "Name": "Giant Goat",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 19,
        "Hit Dice": "3d10 + 3",
        "Speed": {"Walk": 40, "Climb": 30},
        "Ability Scores": {
            "STR": 17,
            "DEX": 13,
            "CON": 12,
            "INT": 3,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": 5,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Actions": {
            "Ram": {
                "Name": "Ram",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Bludgeoning",
                "Effect": "If the target is a Large or smaller creature and the goat moved 20+ feet straight toward it immediately before the hit, it takes an extra 5 (2d4) bludgeoning damage and is knocked Prone."
            }
        }
    },
    "Giant Hyena": {
        "Name": "Giant Hyena",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 45,
        "Hit Dice": "6d10 + 12",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 16,
            "DEX": 14,
            "CON": 14,
            "INT": 2,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 3,
        "DEX Save": 2,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 10,
                "Damage": "2d6 + 3",
                "Damage Type": "Piercing"
            }
        },
        "Bonus Actions": {
            "Rampage (1/Day)": {
                "Description": "After dealing damage to a Bloodied creature, the hyena moves up to half its speed and makes one Bite attack."
            }
        }
    },
    "Giant Lizard": {
        "Name": "Giant Lizard",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 1,
        "HP": 19,
        "Hit Dice": "3d10 + 3",
        "Speed": {"Walk": 40, "Climb": 40},
        "Ability Scores": {
            "STR": 15,
            "DEX": 12,
            "CON": 13,
            "INT": 2,
            "WIS": 10,
            "CHA": 5,
        },
        "STR Save": 2,
        "DEX Save": 3,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Spider Climb": "The lizard can climb difficult surfaces, including along ceilings, without needing to make an ability check."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Piercing"
            }
        }
    },
    "Giant Octopus": {
        "Name": "Giant Octopus",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 45,
        "Hit Dice": "7d10 + 7",
        "Speed": {"Walk": 10, "Swim": 60},
        "Ability Scores": {
            "STR": 17,
            "DEX": 13,
            "CON": 13,
            "INT": 5,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -3,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 4, "Stealth": 5},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 14
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Water Breathing": "The octopus can breathe only underwater. It can hold its breath for 1 hour outside water."
        },
        "Actions": {
            "Tentacles": {
                "Name": "Tentacles",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Target Size": "Medium",
                "Reach": "10 ft.",
                "Hit Average": 10,
                "Damage": "2d6 + 3",
                "Damage Type": "Bludgeoning",
                "Effect": {
                    "Name": "Grappled (Restrained)",
                    "Escape Modifier": "STR",
                    "Escape DC": 13,
                }  
            }
        },
        "Reactions": {
            "Ink Cloud (1/Day)": {
                "Description": "When the octopus takes damage underwater, it releases ink in a 10-foot cube centered on itself (heavily obscured for 1 minute unless dispersed), and moves up to its Swim Speed."
            }
        }
    },
    "Giant Owl": {
        "Name": "Giant Owl",
        "Size": "Large",
        "Type": "Celestial",
        "Alignment": "Neutral",
        "AC": 12,
        "Initiative": 2,
        "HP": 19,
        "Hit Dice": "3d10 + 3",
        "Speed": {"Walk": 5, "Fly": 60},
        "Ability Scores": {
            "STR": 13,
            "DEX": 15,
            "CON": 12,
            "INT": 10,
            "WIS": 14,
            "CHA": 10,
        },
        "STR Save": 1,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": 0,
        "WIS Save": 4,
        "CHA Save": 0,
        "Skills": {"Perception": 6, "Stealth": 6},
        "Senses": {
            "Darkvision": 120,
            "Passive Perception": 16
        },
        "Resistances": ["Necrotic", "Radiant"],
        "Languages": ["Celestial"],
        "Understands": ["Common", "Elvish", "Sylvan"],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Flyby": "The owl doesn’t provoke an Opportunity Attack when it flies out of an enemy’s reach."
        },
        "Actions": {
            "Talons": {
                "Name": "Talons",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 7,
                "Damage": "1d10 + 2",
                "Damage Type": "Slashing"
            },
            "Spellcasting": {
                "Name": "Spellcasting",
                "Description": "The owl casts one of the following spells, requiring no components. Wisdom is the spellcasting ability.",
                "Modifier": "WIS",
                "At Will": ["Detect Evil and Good", "Detect Magic"],
                "1/Day": ["Clairvoyance"]
            }
        }
    },
    "Giant Rat": {
        "Name": "Giant Rat",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 7,
        "Hit Dice": "2d6",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 7,
            "DEX": 16,
            "CON": 11,
            "INT": 2,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": -2,
        "DEX Save": 5,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The rat has advantage on an attack roll against a creature if at least one of the rat’s allies is within 5 feet of the creature and the ally isn’t incapacitated."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d4 + 3",
                "Damage Type": "Piercing"
            }
        }
    },
    "Giant Seahorse": {
        "Name": "Giant Seahorse",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 1,
        "HP": 16,
        "Hit Dice": "3d10",
        "Speed": {"Walk": 5, "Swim": 40},
        "Ability Scores": {
            "STR": 15,
            "DEX": 12,
            "CON": 11,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 2,
        "DEX Save": 1,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Water Breathing": "The seahorse can breathe only underwater."
        },
        "Actions": {
            "Ram": {
                "Name": "Ram",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 9,
                "Damage": "2d6 + 2",
                "Damage Type": "Bludgeoning",
                "Extra": "Deals 11 (2d8 + 2) damage if it moved 20+ feet straight toward the target immediately before the hit."
            }
        },
        "Bonus Actions": {
            "Bubble Dash": {
                "Description": "While underwater, the seahorse moves up to half its Swim Speed without provoking Opportunity Attacks."
            }
        }
    },
    "Giant Scorpion": {
        "Name": "Giant Scorpion",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 15,
        "Initiative": 1,
        "HP": 52,
        "Hit Dice": "7d10 + 14",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 16,
            "DEX": 13,
            "CON": 15,
            "INT": 1,
            "WIS": 9,
            "CHA": 3,
        },
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": -5,
        "WIS Save": -1,
        "CHA Save": -4,
        "Skills": {},
        "Senses": {
            "Blindsight": 60,
            "Passive Perception": 9
        },
        "Languages": [],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 2,
        "Actions": {
            "Multiattack": {
                "Description": "The scorpion makes two Claw attacks and one Sting attack.",
                "Sequence": ["Claw", "Claw", "Sting"],
                "Attacks": {
                    "Claw": {
                        "Name": "Claw",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Target Size": "Large",
                        "Reach": "5 ft.",
                        "Hit Average": 6,
                        "Damage": "1d6 + 3",
                        "Damage Type": "Bludgeoning",
                        "Effect": {
                            "Name": "Grappled",
                            "Escape Modifier": "STR",
                            "Escape DC": 13,
                        }
                    },
                    "Sting": {
                        "Name": "Sting",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Hit Average": 7,
                        "Damage Components": [
                            {"Dice": "1d8", "Modifier": "3", "Type": "Piercing"},
                            {"Dice": "2d10", "Type": "Poison"}
                        ]
                    }
                }
            }
        }
    },
    "Giant Shark": {
        "Name": "Giant Shark",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 0,
        "HP": 92,
        "Hit Dice": "8d12 + 40",
        "Speed": {"Walk": 5, "Swim": 60},
        "Ability Scores": {
            "STR": 23,
            "DEX": 11,
            "CON": 21,
            "INT": 1,
            "WIS": 10,
            "CHA": 5,
        },
        "STR Save": 6,
        "DEX Save": 0,
        "CON Save": 5,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 3},
        "Senses": {
            "Blindsight": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 5,
        "XP": 1800,
        "Proficiency Bonus": 3,
        "Traits": {
            "Water Breathing": "The shark can breathe only underwater."
        },
        "Actions": {
            "Multiattack": {
                "Description": "The shark makes two Bite attacks.",
                "Sequence": ["Bite", "Bite"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 9,
                        "Reach": "5 ft.",
                        "Hit Average": 22,
                        "Damage": "3d10 + 6",
                        "Damage Type": "Piercing",
                        "Special": "Attack has Advantage if the target is not at full HP."
                    }
                }
            }
        }
    },
    "Giant Spider": {
        "Name": "Giant Spider",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 3,
        "HP": 26,
        "Hit Dice": "4d10 + 4",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 14,
            "DEX": 16,
            "CON": 12,
            "INT": 2,
            "WIS": 11,
            "CHA": 4,
        },
        "STR Save": 2,
        "DEX Save": 3,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 4, "Stealth": 7},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 14
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Spider Climb": "The spider can climb difficult surfaces, including ceilings, without an ability check.",
            "Web Walker": "Ignores movement restrictions from webs and senses creatures in the same web."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 7,
                "Damage Components": [
                    {"Dice": "1d8", "Modifier": "3", "Type": "Piercing"},
                    {"Dice": "2d6", "Type": "Poison"}
                ]                
            },
            "Web": {
                "Name": "Web",
                "Recharge": "5-6",
                "Attack Type": "Dexterity Saving Throw",
                "Save DC": 13,
                "Range": "60 ft.",
                "Effect": "On a failed save, the target is Restrained until the web (AC 10, HP 5) is destroyed. It is vulnerable to Fire and immune to Poison and Psychic damage."
            }
        }
    },
    "Giant Squid": {
        "Name": "Giant Squid",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 120,
        "Hit Dice": "16d12 + 16",
        "Speed": {"Walk": 5, "Swim": 80},
        "Ability Scores": {
            "STR": 23,
            "DEX": 14,
            "CON": 12,
            "INT": 5,
            "WIS": 11,
            "CHA": 4,
        },
        "STR Save": 9,
        "DEX Save": 5,
        "CON Save": 1,
        "INT Save": -3,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 6},
        "Senses": {
            "Darkvision": 120,
            "Passive Perception": 16
        },
        "Languages": [],
        "Challenge": 6,
        "XP": 2300,
        "Proficiency Bonus": 3,
        "Traits": {
            "Water Breathing": "The squid can breathe only underwater."
        },
        "Actions": {
            "Multiattack": {
                "Description": "The squid makes one Bite attack and one Tentacle attack.",
                "Sequence": ["Bite", "Tentacle"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 9,
                        "Reach": "5 ft.",
                        "Hit Average": 28,
                        "Damage": "4d10 + 6",
                        "Damage Type": "Piercing"
                    },
                    "Tentacle": {
                        "Name": "Tentacle",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 9,
                        "Target Size": "Huge",
                        "Reach": "15 ft.",
                        "Hit Average": 19,
                        "Damage": "3d8 + 6",
                        "Damage Type": "Bludgeoning",
                        "Effect": {
                            "Name": "Grappled",
                            "Escape Modifier": "STR",
                            "Escape DC": 16,
                            "Extra": "The squid can pull the target up to 10 feet straight toward itself.",
                        }                          
                    }
                }
            }
        },
        "Reactions": {
            "Ink Cloud (1/Day)": {
                "Trigger": "The squid takes damage while underwater.",
                "Response": "The squid releases ink that fills a 15-foot cube centered on itself and moves up to its Swim speed. The cube is Heavily Obscured for 1 minute or until dispersed."
            }
        }
    },
    "Giant Toad": {
        "Name": "Giant Toad",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 39,
        "Hit Dice": "6d10 + 6",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 15,
            "DEX": 13,
            "CON": 13,
            "INT": 2,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": 2,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Amphibious": "The toad can breathe air and water.",
            "Standing Leap": "The toad’s Long Jump is up to 20 feet and High Jump is up to 10 feet with or without a running start."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Target Size": "Medium",
                "Reach": "5 ft.",
                "Hit Average": 10,
                "Damage Components": [
                    {"Dice": "1d6", "Modifier": "2", "Type": "Piercing"},
                    {"Dice": "2d4", "Type": "Poison"}
                ],
                "Effect": {
                    "Name": "Grappled",
                    "Escape Modifier": "STR",
                    "Escape DC": 12,
                }  
            },
            "Swallow": {
                "Description": "The toad swallows a Medium or smaller target it is grappling.",
                "Effect": "While swallowed, the target is Blinded, Restrained, and has Total Cover. It takes 10 (3d6) Acid damage at the end of each of the toad’s turns. The toad can only have one target swallowed at a time and can’t use Bite while it has a swallowed target. If the toad dies, the creature is no longer Restrained and can escape using 5 feet of movement, exiting Prone."
            }
        }
    },
    "Giant Venomous Snake": {
        "Name": "Giant Venomous Snake",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 4,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {"Walk": 40, "Swim": 40},
        "Ability Scores": {
            "STR": 10,
            "DEX": 18,
            "CON": 13,
            "INT": 2,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": 0,
        "DEX Save": 4,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {"Perception": 2},
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "10 ft.",
                "Hit Average": 10,
                "Damage Components": [
                    {"Dice": "1d4", "Modifier": "4", "Type": "Piercing"},
                    {"Dice": "1d8", "Type": "Poison"}
                ]
            }
        }
    },
    "Giant Vulture": {
        "Name": "Giant Vulture",
        "Size": "Large",
        "Type": "Monstrosity",
        "Alignment": "Neutral Evil",
        "AC": 10,
        "Initiative": 0,
        "HP": 25,
        "Hit Dice": "3d10 + 9",
        "Speed": {"Walk": 10, "Fly": 60},
        "Ability Scores": {
            "STR": 15,
            "DEX": 10,
            "CON": 16,
            "INT": 6,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 2,
        "DEX Save": 0,
        "CON Save": 3,
        "INT Save": -2,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": ["Understands Common but can’t speak"],
        "Resistances": ["Necrotic"],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The vulture has Advantage on an attack roll against a creature if at least one of the vulture’s allies is within 5 feet of the creature and the ally isn’t Incapacitated."
        },
        "Actions": {
            "Gouge": {
                "Name": "Gouge",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 9,
                "Damage": "2d6 + 2",
                "Damage Type": "Piercing",
                "Effect": "The target is Poisoned until the end of its next turn."
            }
        }
    },
    "Giant Wasp": {
        "Name": "Giant Wasp",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 2,
        "HP": 22,
        "Hit Dice": "5d8",
        "Speed": {"Walk": 10, "Fly": 50},
        "Ability Scores": {
            "STR": 10,
            "DEX": 14,
            "CON": 10,
            "INT": 1,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": 0,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Flyby": "The wasp doesn’t provoke Opportunity Attacks when it flies out of an enemy’s reach."
        },
        "Actions": {
            "Sting": {
                "Name": "Sting",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage Components": [
                    {"Dice": "1d6", "Modifier": "2", "Type": "Piercing"},
                    {"Dice": "2d4", "Type": "Poison"}
                ]                
            }
        }
    },
    "Giant Weasel": {
        "Name": "Giant Weasel",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 9,
        "Hit Dice": "2d8",
        "Speed": {"Walk": 40, "Climb": 30},
        "Ability Scores": {
            "STR": 11,
            "DEX": 17,
            "CON": 10,
            "INT": 4,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 0,
        "DEX Save": 3,
        "CON Save": 0,
        "INT Save": -3,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {
            "Acrobatics": 5,
            "Perception": 3,
            "Stealth": 5
        },
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d4 + 3",
                "Damage Type": "Piercing"
            }
        }
    },
    "Giant Wolf Spider": {
        "Name": "Giant Wolf Spider",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {"Walk": 40, "Climb": 40},
        "Ability Scores": {
            "STR": 12,
            "DEX": 16,
            "CON": 13,
            "INT": 3,
            "WIS": 12,
            "CHA": 4,
        },
        "STR Save": 1,
        "DEX Save": 3,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {
            "Perception": 3,
            "Stealth": 7
        },
        "Senses": {
            "Blindsight": 10,
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Spider Climb": "The spider can climb difficult surfaces, including ceilings, without needing to make an ability check."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage Components": [
                    {"Dice": "1d4", "Modifier": "3", "Type": "Piercing"},
                    {"Dice": "2d4", "Type": "Poison"}
                ]                
            }
        }
    },
    "Goat": {
        "Name": "Goat",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 4,
        "Hit Dice": "1d8",
        "Speed": {"Walk": 40, "Climb": 30},
        "Ability Scores": {
            "STR": 11,
            "DEX": 10,
            "CON": 11,
            "INT": 2,
            "WIS": 10,
            "CHA": 5,
        },
        "STR Save": 2,
        "DEX Save": 0,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Actions": {
            "Ram": {
                "Name": "Ram",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1d4",
                "Damage Type": "Bludgeoning",
                "Bonus Condition": "If the goat moved 20+ feet straight toward the target immediately before the hit, deal 2 (1d4) instead."
            }
        }
    },
    "Hawk": {
        "Name": "Hawk",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 10, "Fly": 60},
        "Ability Scores": {
            "STR": 5,
            "DEX": 16,
            "CON": 8,
            "INT": 2,
            "WIS": 14,
            "CHA": 6,
        },
        "STR Save": -3,
        "DEX Save": 3,
        "CON Save": -1,
        "INT Save": -4,
        "WIS Save": 2,
        "CHA Save": -2,
        "Skills": {"Perception": 6},
        "Senses": {
            "Passive Perception": 16
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Actions": {
            "Talons": {
                "Name" : "Talons",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Slashing"
            }
        }
    },
    "Hippopotamus": {
        "Name": "Hippopotamus",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": -2,
        "HP": 82,
        "Hit Dice": "11d10 + 22",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 21,
            "DEX": 7,
            "CON": 15,
            "INT": 2,
            "WIS": 12,
            "CHA": 4,
        },
        "STR Save": 7,
        "DEX Save": -2,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {"Perception": 3},
        "Senses": {
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 4,
        "XP": 1100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Hold Breath": "The hippopotamus can hold its breath for 10 minutes."
        },
        "Actions": {
            "Multiattack": {
                "Description": "The hippopotamus makes two Bite attacks.",
                "Sequence": ["Bite", "Bite"],
                "Attacks": {
                    "Bite": {
                        "Name": "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 7,
                        "Reach": "5 ft.",
                        "Hit Average": 16,
                        "Damage": "2d10 + 5",
                        "Damage Type": "Piercing"
                    }
                }
            }
        }
    },
    "Hunter Shark": {
        "Name": "Hunter Shark",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 45,
        "Hit Dice": "6d10 + 12",
        "Speed": {"Walk": 5, "Swim": 40},
        "Ability Scores": {
            "STR": 18,
            "DEX": 14,
            "CON": 15,
            "INT": 1,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": 4,
        "DEX Save": 2,
        "CON Save": 2,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2},
        "Senses": {
            "Blindsight": 60,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {
            "Water Breathing": "The shark can breathe only underwater."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 14,
                "Damage": "3d6 + 4",
                "Damage Type": "Piercing",
                "Bonus Condition": "Attack has Advantage if the target doesn't have all its Hit Points."
            }
        }
    },
    "Hyena": {
        "Name": "Hyena",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 5,
        "Hit Dice": "1d8 + 1",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 11,
            "DEX": 13,
            "CON": 12,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 0,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {"Perception": 3},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The hyena has advantage on an attack roll against a creature if at least one of the hyena’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
        },
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 3,
                "Damage": "1d6",
                "Damage Type": "Piercing"
            }
        }
    },
    "Jackal": {
        "Name": "Jackal",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 3,
        "Hit Dice": "1d6",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 8,
            "DEX": 15,
            "CON": 11,
            "INT": 3,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": -1,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 5, "Stealth": 4},
        "Senses": {
            "Darkvision": 90,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name": "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 1,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1d4 - 1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Killer Whale": {
        "Name": "Killer Whale",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 90,
        "Hit Dice": "12d12 + 12",
        "Speed": {"Walk": 5, "Swim": 60},
        "Ability Scores": {
            "STR": 19,
            "DEX": 14,
            "CON": 13,
            "INT": 3,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 4,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3, "Stealth": 4},
        "Senses": {
            "Blindsight": 120,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 2,
        "Traits": {
            "Hold Breath": "The whale can hold its breath for 30 minutes."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 21,
                "Damage": "5d6 + 4",
                "Damage Type": "Piercing"
            }
        }
    },
    "Lion": {
        "Name": "Lion",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 22,
        "Hit Dice": "4d10",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 17,
            "DEX": 15,
            "CON": 11,
            "INT": 3,
            "WIS": 12,
            "CHA": 8,
        },
        "STR Save": 3,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -1,
        "Skills": {"Perception": 3, "Stealth": 4},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The lion has advantage on an attack roll against a creature if at least one of the lion’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition.",
            "Running Leap": "With a 10-foot running start, the lion can Long Jump up to 25 feet."
        },
        "Actions": {
            "Multiattack": {
                "Description": "The lion makes two Rend attacks. It can replace one attack with a use of Roar.",
                "Sequence": [["Rend", "Rend"], ["Rend", "Roar"], ["Roar", "Rend"]],  # or ["Rend", "Roar"]
                "Attacks": {
                    "Rend": {
                        "Name" : "Rend",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Hit Average": 7,
                        "Damage": "1d8 + 3",
                        "Damage Type": "Slashing"
                    },
                    "Roar": {
                        "Name" : "Roar",
                        "Attack Type": "Saving Throw", 
                        "Range": "15 ft.",
                        "Effect": {
                            "Name": "Frightened",
                            "Save Type": "WIS",
                            "Save DC": 11,
                        }
                    }
                }
            }
        }
    },
    "Lizard": {
        "Name": "Lizard",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 2,
        "Hit Dice": "1d4",
        "Speed": {"Walk": 20, "Climb": 20},
        "Ability Scores": {
            "STR": 2,
            "DEX": 11,
            "CON": 10,
            "INT": 1,
            "WIS": 8,
            "CHA": 3,
        },
        "STR Save": -4,
        "DEX Save": 0,
        "CON Save": 0,
        "INT Save": -5,
        "WIS Save": -1,
        "CHA Save": -4,
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 9
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Spider Climb": "The lizard can climb difficult surfaces, including along ceilings, without needing to make an ability check."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Mammoth": {
        "Name": "Mammoth",
        "Size": "Huge",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": -1,
        "HP": 126,
        "Hit Dice": "11d12 + 55",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 24,
            "DEX": 9,
            "CON": 21,
            "INT": 3,
            "WIS": 11,
            "CHA": 6,
        },
        "STR Save": 10,
        "DEX Save": -1,
        "CON Save": 8,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 6,
        "XP": 2300,
        "Proficiency Bonus": 3,
        "Actions": {
            "Multiattack": {
                "Description": "The mammoth makes two Gore attacks.",
                "Sequence": ["Gore", "Gore"],
                "Attacks": {
                    "Gore": {
                        "Name" : "Gore",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 10,
                        "Reach": "10 ft.",
                        "Hit Average": 18,
                        "Damage": "2d10 + 7",
                        "Damage Type": "Piercing",
                        "Additional Effect": "If the target is Huge or smaller and the mammoth moved 20+ feet straight toward it before the hit, the target is knocked Prone."
                    }
                }
            }
        },
        "Bonus Actions": {
            "Trample": {
                "Description": "One creature within 5 feet that is Prone must succeed on a DC 18 Dexterity saving throw or take 29 (4d10 + 7) bludgeoning damage. On success, takes half damage."
            }
        }
    },
    "Mastiff": {
        "Name": "Mastiff",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 5,
        "Hit Dice": "1d8 + 1",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 13,
            "DEX": 14,
            "CON": 12,
            "INT": 3,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 1,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 3,
        "CHA Save": -2,
        "Skills": {"Perception": 5},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Target Size": "Medium",
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d6 + 1",
                "Damage Type": "Piercing",
                "Effect": "If the target is Medium or smaller, it is knocked Prone."
            }
        }
    },
    "Mule": {
        "Name": "Mule",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 14,
            "DEX": 10,
            "CON": 13,
            "INT": 2,
            "WIS": 10,
            "CHA": 5,
        },
        "STR Save": 4,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Traits": {
            "Beast of Burden": "The mule counts as one size larger for the purpose of determining its carrying capacity."
        },
        "Actions": {
            "Hooves": {
                "Name" : "Hooves",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Octopus": {
        "Name": "Octopus",
        "Size": "Small",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 3,
        "Hit Dice": "1d6",
        "Speed": {"Walk": 5, "Swim": 30},
        "Ability Scores": {
            "STR": 4,
            "DEX": 15,
            "CON": 11,
            "INT": 3,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": -3,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2, "Stealth": 6},
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Compression": "The octopus can move through a space as narrow as 1 inch without expending extra movement to do so.",
            "Water Breathing": "The octopus can breathe only underwater."
        },
        "Actions": {
            "Tentacles": {
                "Name" : "Tentacles",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Bludgeoning"
            }
        },
        "Reactions": {
            "Ink Cloud (1/Day)": "When a creature ends its turn within 5 feet of the octopus while underwater, the octopus releases ink in a 5-foot cube centered on itself and moves up to its Swim Speed. The cube is heavily obscured for 1 minute or until dispersed."
        }
    },
    "Owl": {
        "Name": "Owl",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 5, "Fly": 60},
        "Ability Scores": {
            "STR": 3,
            "DEX": 13,
            "CON": 8,
            "INT": 2,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": -4,
        "DEX Save": 1,
        "CON Save": -1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 5, "Stealth": 5},
        "Senses": {
            "Darkvision": 120,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Flyby": "The owl doesn’t provoke an opportunity attack when it flies out of an enemy’s reach."
        },
        "Actions": {
            "Talons": {
                "Name" : "Talons",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Slashing"
            }
        }
    },
    "Panther": {
        "Name": "Panther",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 13,
        "Hit Dice": "3d8",
        "Speed": {"Walk": 50, "Climb": 40},
        "Ability Scores": {
            "STR": 14,
            "DEX": 16,
            "CON": 10,
            "INT": 3,
            "WIS": 14,
            "CHA": 7,
        },
        "STR Save": 2,
        "DEX Save": 3,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 2,
        "CHA Save": -2,
        "Skills": {"Perception": 4, "Stealth": 7},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 14
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Rend": {
                "Name" : "Rend",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d6 + 3",
                "Damage Type": "Slashing"
            }
        },
        "Bonus Actions": {
            "Nimble Escape": "The panther takes the Disengage or Hide action."
        }
    },
    "Phase Spider": {
        "Name": "Phase Spider",
        "Size": "Large",
        "Type": "Monstrosity",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 3,
        "HP": 45,
        "Hit Dice": "7d10 + 7",
        "Speed": {
            "Walk": 30,
            "Climb": 30
        },
        "Ability Scores": {
            "STR": 15,
            "DEX": 16,
            "CON": 12,
            "INT": 6,
            "WIS": 10,
            "CHA": 6,
        },
        "STR Save": 2,
        "DEX Save": 3,
        "CON Save": 1,
        "INT Save": -2,
        "WIS Save": 0,
        "CHA Save": -2,
        "Skills": {
            "Stealth": 7
        },
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 2,
        "Traits": {
            "Ethereal Sight": {
                "Description": "The spider can see 60 feet into the Ethereal Plane while on the Material Plane and vice versa."
            },
            "Spider Climb": {
                "Description": "The spider can climb difficult surfaces, including along ceilings, without needing to make an ability check."
            },
            "Web Walker": {
                "Description": "The spider ignores movement restrictions caused by webs, and it knows the location of any other creature in contact with the same web."
            }
        },
        "Actions": {
            "Multiattack": {
                "Description": "The spider makes two Bite attacks.",
                "Sequence": ["Bite", "Bite"],
                "Attacks": {
                    "Bite": {
                        "Name" : "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Hit Average": 8,
                        "Damage Components": [
                            {"Dice": "1d10", "Modifier": "3", "Type": "Piercing"},
                            {"Dice": "2d8", "Type": "Poison"}
                        ],   
                        "Conditional Extra": {
                            "Condition": "Unconscious",
                        },

                        "On Hit": {
                            "Condition": {
                                "Effect": "If reduced to 0 HP, the target becomes Stable and gains the Poisoned and Paralyzed conditions for 1 hour."
                            }
                        }
                    }
                }
            }
        },
        "Bonus Actions": {
            "Ethereal Jaunt": {
                "Description": "The spider teleports from the Material Plane to the Ethereal Plane or vice versa."
            }
        }
    },    
    "Piranha": {
        "Name": "Piranha",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 5, "Swim": 40},
        "Ability Scores": {
            "STR": 2,
            "DEX": 16,
            "CON": 9,
            "INT": 1,
            "WIS": 7,
            "CHA": 2,
        },
        "STR Save": -4,
        "DEX Save": 3,
        "CON Save": -1,
        "INT Save": -5,
        "WIS Save": -2,
        "CHA Save": -4,
        "Skills": {},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 8
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Water Breathing": "The piranha can breathe only underwater."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing",
                "Special": "Has advantage on the attack roll if the target doesn’t have all its hit points."
            }
        }
    },
    "Plesiosaurus": {
        "Name": "Plesiosaurus",
        "Size": "Large",
        "Type": "Beast (Dinosaur)",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 2,
        "HP": 68,
        "Hit Dice": "8d10 + 24",
        "Speed": {"Walk": 20, "Swim": 40},
        "Ability Scores": {
            "STR": 18,
            "DEX": 15,
            "CON": 16,
            "INT": 2,
            "WIS": 12,
            "CHA": 5,
        },
        "STR Save": 4,
        "DEX Save": 2,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {"Perception": 3, "Stealth": 4},
        "Senses": {
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {
            "Hold Breath": "The plesiosaurus can hold its breath for 1 hour."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "10 ft.",
                "Hit Average": 11,
                "Damage": "2d6 + 4",
                "Damage Type": "Piercing"
            }
        }
    },
    "Polar Bear": {
        "Name": "Polar Bear",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 42,
        "Hit Dice": "5d10 + 15",
        "Speed": {"Walk": 40, "Swim": 40},
        "Ability Scores": {
            "STR": 20,
            "DEX": 14,
            "CON": 16,
            "INT": 2,
            "WIS": 13,
            "CHA": 7,
        },
        "STR Save": 5,
        "DEX Save": 2,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 5, "Stealth": 4},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Resistances": ["Cold"],
        "Actions": {
            "Multiattack": {
                "Description": "The bear makes two Rend attacks.",
                "Sequence": ["Rend", "Rend"],
                "Attacks": {
                    "Rend": {
                        "Name" : "Rend",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 7,
                        "Reach": "5 ft.",
                        "Hit Average": 9,
                        "Damage": "1d8 + 5",
                        "Damage Type": "Slashing"
                    }
                }
            }
        }
    },
    "Pony": {
        "Name": "Pony",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 15,
            "DEX": 10,
            "CON": 13,
            "INT": 2,
            "WIS": 11,
            "CHA": 7,
        },
        "STR Save": 4,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Actions": {
            "Hooves": {
                "Name" : "Hooves",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage": "1d4 + 2",
                "Damage Type": "Bludgeoning"
            }
        }
    }, 
    "Pteranodon": {
        "Name": "Pteranodon",
        "Size": "Medium",
        "Type": "Beast (Dinosaur)",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 2,
        "HP": 13,
        "Hit Dice": "3d8",
        "Speed": {"Walk": 10, "Fly": 60},
        "Ability Scores": {
            "STR": 12,
            "DEX": 15,
            "CON": 10,
            "INT": 2,
            "WIS": 9,
            "CHA": 5,
        },
        "STR Save": 1,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": -1,
        "CHA Save": -3,
        "Skills": {"Perception": 1},
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Flyby": "The pteranodon doesn’t provoke an Opportunity Attack when it flies out of an enemy’s reach."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "1d8 + 2",
                "Damage Type": "Piercing"
            }
        }
    },
    "Rat": {
        "Name": "Rat",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 20, "Climb": 20},
        "Ability Scores": {
            "STR": 2,
            "DEX": 11,
            "CON": 9,
            "INT": 2,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": -4,
        "DEX Save": 0,
        "CON Save": -1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2},
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Agile": "The rat doesn’t provoke an Opportunity Attack when it moves out of an enemy’s reach."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Raven": {
        "Name": "Raven",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 2,
        "Hit Dice": "1d4",
        "Speed": {"Walk": 10, "Fly": 50},
        "Ability Scores": {
            "STR": 2,
            "DEX": 14,
            "CON": 10,
            "INT": 5,
            "WIS": 13,
            "CHA": 6,
        },
        "STR Save": -4,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -3,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 3},
        "Senses": {
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Mimicry": "The raven can mimic simple sounds it has heard, such as a whisper or chitter. A hearer can discern the sounds are imitations with a successful DC 10 Wisdom (Insight) check."
        },
        "Actions": {
            "Beak": {
                "Name" : "Beak",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Reef Shark": {
        "Name": "Reef Shark",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 22,
        "Hit Dice": "4d8 + 4",
        "Speed": {"Walk": 5, "Swim": 30},
        "Ability Scores": {
            "STR": 14,
            "DEX": 15,
            "CON": 13,
            "INT": 1,
            "WIS": 10,
            "CHA": 4,
        },
        "STR Save": 2,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {"Perception": 2},
        "Senses": {
            "Blindsight": 30,
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The shark has Advantage on an attack roll against a creature if at least one of the shark’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition.",
            "Water Breathing": "The shark can breathe only underwater."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 7,
                "Damage": "2d4 + 2",
                "Damage Type": "Piercing"
            }
        }
    },
    "Rhinoceros": {
        "Name": "Rhinoceros",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": -1,
        "HP": 45,
        "Hit Dice": "6d10 + 12",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 21,
            "DEX": 8,
            "CON": 15,
            "INT": 2,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": 5,
        "DEX Save": -1,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Actions": {
            "Gore": {
                "Name" : "Gore",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 7,
                "Reach": "5 ft.",
                "Hit Average": 14,
                "Damage": "2d8 + 5",
                "Damage Type": "Piercing",
                "Extra Effect": "If the target is a Large or smaller creature and the rhinoceros moved 20+ feet straight toward it immediately before the hit, the target takes an extra 9 (2d8) Piercing damage and has the Prone condition."
            }
        }
    },
    "Riding Horse": {
        "Name": "Riding Horse",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 13,
        "Hit Dice": "2d10 + 2",
        "Speed": {"Walk": 60},
        "Ability Scores": {
            "STR": 16,
            "DEX": 13,
            "CON": 12,
            "INT": 2,
            "WIS": 11,
            "CHA": 7,
        },
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Actions": {
            "Hooves": {
                "Name" : "Hooves",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 7,
                "Damage": "1d8 + 3",
                "Damage Type": "Bludgeoning"
            }
        }
    },
    "Saber-Toothed Tiger": {
        "Name": "Saber-Toothed Tiger",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 52,
        "Hit Dice": "7d10 + 14",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 18,
            "DEX": 17,
            "CON": 15,
            "INT": 3,
            "WIS": 12,
            "CHA": 8,
        },
        "STR Save": 6,
        "DEX Save": 5,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -1,
        "Skills": {"Perception": 5, "Stealth": 7},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {
            "Running Leap": "With a 10-foot running start, the tiger can Long Jump up to 25 feet."
        },
        "Actions": {
            "Multiattack": {
                "Description": "The tiger makes two Rend attacks.",
                "Sequence": ["Rend", "Rend"],
                "Attacks": {
                    "Rend": {
                        "Name" : "Rend",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 6,
                        "Reach": "5 ft.",
                        "Hit Average": 11,
                        "Damage": "2d6 + 4",
                        "Damage Type": "Slashing"
                    }
                }
            }
        },
        "Bonus Actions": {
            "Nimble Escape": "The tiger takes the Disengage or Hide action."
        }
    },
    "Scorpion": {
        "Name": "Scorpion",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 0,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 10},
        "Ability Scores": {
            "STR": 2,
            "DEX": 11,
            "CON": 8,
            "INT": 1,
            "WIS": 8,
            "CHA": 2,
        },
        "STR Save": -4,
        "DEX Save": 0,
        "CON Save": -1,
        "INT Save": -5,
        "WIS Save": -1,
        "CHA Save": -4,
        "Skills": {},
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 9
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Actions": {
            "Sting": {
                "Name" : "Sting",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage Components": [
                    {"Dice": "1", "Type": "Piercing"},
                    {"Dice": "1d6", "Type": "Poison"}
                ],   
            }
        }
    },
    "Seahorse": {
        "Name": "Seahorse",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 1,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 5, "Swim": 20},
        "Ability Scores": {
            "STR": 1,
            "DEX": 12,
            "CON": 8,
            "INT": 1,
            "WIS": 10,
            "CHA": 2,
        },
        "STR Save": -5,
        "DEX Save": 1,
        "CON Save": -1,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {"Perception": 2, "Stealth": 5},
        "Senses": {
            "Passive Perception": 12
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 0,
        "Proficiency Bonus": 2,
        "Traits": {
            "Water Breathing": "The seahorse can breathe only underwater."
        },
        "Actions": {
            "Bubble Dash": {
                "Description": "While underwater, the seahorse moves up to its Swim Speed without provoking Opportunity Attacks."
            }
        }
    },
    "Silverback Gorilla(Polar Bear)": {
        "Name": "Silverback Gorilla",
        "Size": "Large",
        "Creature Type": "Beast",
        "Creature Alignment": "Unaligned",
        "AC": 12,
        "Hit Points Average": 42,
        "Hit Points Roll": "5d10 + 15",
        "Speed": {'Walk': 40, 'Swim': 30},
        "Ability Scores": {
            "STR": 20,
            "DEX": 10,
            "CON": 16,
            "INT": 2,
            "WIS": 13,
            "CHA": 7,
        },
        "Perception": "+3",
        "Senses" : "passive Perception 13",
        "Challenge": 2,
        "XP": 450,  
        "Traits": {
            "Keen Smell": "The bear has advantage on Wisdom (Perception) checks that rely on smell.",
        },      
        "Actions": {
            "Multiattack": {
                "Description": "The bear makes two attacks: one with its bite and one with its fist.",
                "Sequence": ["Bite", "Fist"],
                "Attacks": {
                    "Bite": {
                        "Name" : "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Targets": 1,
                        "Hit Average": 8,
                        "Damage": "1d8 + 4",
                        "Damage Type": "Piercing"
                    },
                    "Fist": {
                        "Name" : "Fist",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 5,
                        "Reach": "5 ft.",
                        "Targets": 1,
                        "Hit Average": 11,
                        "Damage": "2d6 + 4",
                        "Damage Type": "Slashing"
                    },
                },
            },
        },
    },
    "Spider": {
        "Name": "Spider",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 20, "Climb": 20},
        "Ability Scores": {
            "STR": 2,
            "DEX": 14,
            "CON": 8,
            "INT": 1,
            "WIS": 10,
            "CHA": 2,
        },
        "STR Save": -4,
        "DEX Save": 2,
        "CON Save": -1,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Skills": {"Stealth": 4},
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Spider Climb": "The spider can climb difficult surfaces, including along ceilings, without needing to make an ability check.",
            "Web Walker": "The spider ignores movement restrictions caused by webs, and knows the location of any other creature in contact with the same web."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 3,
                "Damage Components": [
                    {"Dice": "1", "Type": "Piercing"},
                    {"Dice": "1d4", "Type": "Poison"}
                ],                  
            }
        }
    },
    "Swarm of Bats": {
        "Name": "Swarm of Bats",
        "Size": "Large",
        "Type": "Swarm of Tiny Beasts",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 11,
        "Hit Dice": "2d10",
        "Speed": {"Walk": 5, "Fly": 30},
        "Ability Scores": {
            "STR": 5,
            "DEX": 15,
            "CON": 10,
            "INT": 2,
            "WIS": 12,
            "CHA": 4,
        },
        "STR Save": -3,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Resistances": ["Bludgeoning", "Piercing", "Slashing"],
        "Immunities": ["Charmed", "Frightened", "Grappled", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned"],
        "Senses": {
            "Blindsight": 60,
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Swarm": "The swarm can occupy another creature’s space and vice versa, and can move through any opening large enough for a Tiny bat. It can’t regain Hit Points or gain Temporary Hit Points."
        },
        "Actions": {
            "Bites": {
                "Name" : "Bites",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "2d4",
                "Damage Type": "Piercing",
                "Conditional Extra": {
                    "Condition": "Bloodied",
                    "Damage": "1d4",
                    "Damage Average": 2
                }                
            }
        }
    },
    "Swarm of Insects": {
        "Name": "Swarm of Insects",
        "Size": "Medium",
        "Type": "Swarm of Tiny Beasts",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 19,
        "Hit Dice": "3d8 + 6",
        "Speed": {"Walk": 20, "Climb": 20, "Fly": 20},
        "Ability Scores": {
            "STR": 3,
            "DEX": 13,
            "CON": 14,
            "INT": 1,
            "WIS": 7,
            "CHA": 1,
        },
        "STR Save": -4,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": -5,
        "WIS Save": -2,
        "CHA Save": -5,
        "Resistances": ["Bludgeoning", "Piercing", "Slashing"],
        "Immunities": ["Charmed", "Frightened", "Grappled", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned"],
        "Senses": {
            "Blindsight": 30,
            "Passive Perception": 8
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Traits": {
            "Spider Climb": "If the swarm has a Climb speed, it can climb difficult surfaces, including ceilings, without making an ability check.",
            "Swarm": "The swarm can occupy another creature’s space and move through openings large enough for a Tiny insect. It can’t regain Hit Points or gain Temporary Hit Points."
        },
        "Actions": {
            "Bites": {
                "Name" : "Bites",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 6,
                "Damage": "2d4 + 1",
                "Damage Type": "Poison",
                "Conditional Extra": {
                    "Condition": "Bloodied",
                    "Damage": "1d4+1",
                    "Damage Average": 3
                }                    
            }
        }
    },
    "Swarm of Piranhas": {
        "Name": "Swarm of Piranhas",
        "Size": "Medium",
        "Type": "Swarm of Tiny Beasts",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 28,
        "Hit Dice": "8d8 - 8",
        "Speed": {"Walk": 5, "Swim": 40},
        "Ability Scores": {
            "STR": 13,
            "DEX": 16,
            "CON": 9,
            "INT": 1,
            "WIS": 7,
            "CHA": 2,
        },
        "STR Save": 1,
        "DEX Save": 3,
        "CON Save": -1,
        "INT Save": -5,
        "WIS Save": -2,
        "CHA Save": -4,
        "Resistances": ["Bludgeoning", "Piercing", "Slashing"],
        "Immunities": ["Charmed", "Frightened", "Grappled", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned"],
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 8
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Traits": {
            "Swarm": "The swarm can occupy another creature’s space and move through openings large enough for a Tiny piranha. It can’t regain Hit Points or gain Temporary Hit Points.",
            "Water Breathing": "The swarm can breathe only underwater."
        },
        "Actions": {
            "Bites": {
                "Name" : "Bites",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 8,
                "Damage": "2d4 + 3",
                "Damage Type": "Piercing",
                "Conditional Extra": {
                    "Condition": "Bloodied",
                    "Damage": "1d4 + 3",
                    "Damage Average": 5
                },                    
                "Advantage Condition": "Attack has Advantage if target doesn't have all its Hit Points."
            }
        }
    },
    "Swarm of Rats": {
        "Name": "Swarm of Rats",
        "Size": "Medium",
        "Type": "Swarm of Tiny Beasts",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 14,
        "Hit Dice": "4d8 - 4",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 9,
            "DEX": 11,
            "CON": 9,
            "INT": 2,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": -1,
        "DEX Save": 2,
        "CON Save": -1,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -4,
        "Resistances": ["Bludgeoning", "Piercing", "Slashing"],
        "Immunities": ["Charmed", "Frightened", "Grappled", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned"],
        "Senses": {
            "Darkvision": 30,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Swarm": "The swarm can occupy another creature’s space and vice versa, and can move through any opening large enough for a Tiny rat. The swarm can’t regain Hit Points or gain Temporary Hit Points."
        },
        "Actions": {
            "Bites": {
                "Name" : "Bites",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "2d4",
                "Damage Type": "Piercing",
                "Conditional Extra": {
                    "Condition": "Bloodied",
                    "Damage": "1d4",
                    "Damage Average": 2
                }  
            }
        }
    },
    "Swarm of Ravens": {
        "Name": "Swarm of Ravens",
        "Size": "Medium",
        "Type": "Swarm of Tiny Beasts",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {"Walk": 10, "Fly": 50},
        "Ability Scores": {
            "STR": 6,
            "DEX": 14,
            "CON": 12,
            "INT": 5,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": -2,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -3,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {"Perception": 5},
        "Resistances": ["Bludgeoning", "Piercing", "Slashing"],
        "Immunities": ["Charmed", "Frightened", "Grappled", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned"],
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Swarm": "The swarm can occupy another creature’s space and vice versa, and can move through any opening large enough for a Tiny raven. The swarm can’t regain Hit Points or gain Temporary Hit Points."
        },
        "Actions": {
            "Beaks": {
                "Name" : "Beaks",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Piercing",
                "Conditional Extra": {
                    "Condition": "Bloodied",
                    "Damage": "1d4",
                    "Damage Average": 2
                }  
            },
            "Cacophony": {
                "Name": "Cacophany",
                "Attack Type": "Saving Throw", 
                "Range": "Target within self space",
                "Recharge": 6,
                "Effect": {
                    "Name": "Deafened",
                    "Type": "WIS",
                    "DC": 11,
                    "Expires": "StartOfSourceTurn",
                    "Description": "While Deafened, the target has Disadvantage on ability checks and attack rolls."
                },
            }
        }
    },
    "Swarm of Venomous Snakes": {
        "Name": "Swarm of Venomous Snakes",
        "Size": "Medium",
        "Type": "Swarm of Tiny Beasts",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": 4,
        "HP": 36,
        "Hit Dice": "8d8",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 8,
            "DEX": 18,
            "CON": 11,
            "INT": 1,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": -1,
        "DEX Save": 4,
        "CON Save": 0,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Resistances": ["Bludgeoning", "Piercing", "Slashing"],
        "Immunities": ["Charmed", "Frightened", "Grappled", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned"],
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 2,
        "XP": 450,
        "Proficiency Bonus": 2,
        "Traits": {
            "Swarm": "The swarm can occupy another creature’s space and vice versa, and can move through any opening large enough for a Tiny snake. The swarm can’t regain Hit Points or gain Temporary Hit Points."
        },
        "Actions": {
            "Bites": {
                "Name" : "Bites",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 8,
                "Damage": "1d8 + 4",
                "Damage Type": "Piercing",
                "Damage Components": [
                    {"Dice": "1d8", "Modifier": "4", "Type": "Piercing"},
                    {"Dice": "3d6", "Type": "Poison"}
                ],    
                "Bloodied Damage": "1d4 + 4",            
            }
        }
    },
    "Tiger": {
        "Name": "Tiger",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 30,
        "Hit Dice": "4d10 + 8",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 17,
            "DEX": 16,
            "CON": 14,
            "INT": 3,
            "WIS": 12,
            "CHA": 8,
        },
        "STR Save": 3,
        "DEX Save": 3,
        "CON Save": 2,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -1,
        "Skills": {"Perception": 3, "Stealth": 7},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 1,
        "XP": 200,
        "Proficiency Bonus": 2,
        "Actions": {
            "Rend": {
                "Name" : "Rend",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Target Size": "Large",
                "Hit Average": 10,
                "Damage": "2d6 + 3",
                "Damage Type": "Slashing",
                "Effect": "If the target is a Large or smaller creature, it is knocked Prone."
            }
        },
        "Bonus Actions": {
            "Nimble Escape": "The tiger takes the Disengage or Hide action."
        }
    },
    "Triceratops": {
        "Name": "Triceratops",
        "Size": "Huge",
        "Type": "Beast (Dinosaur)",
        "Alignment": "Unaligned",
        "AC": 14,
        "Initiative": -1,
        "HP": 114,
        "Hit Dice": "12d12 + 36",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 22,
            "DEX": 9,
            "CON": 17,
            "INT": 2,
            "WIS": 11,
            "CHA": 5,
        },
        "STR Save": 6,
        "DEX Save": -1,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Senses": {
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": 5,
        "XP": 1800,
        "Proficiency Bonus": 3,
        "Actions": {
            "Multiattack": {
                "Description": "The triceratops makes two Gore attacks.",
                "Sequence": ["Gore", "Gore"],
                "Attacks": {
                    "Gore": {
                        "Name" : "Gore",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 9,
                        "Reach": "5 ft.",
                        "Hit Average": 19,
                        "Damage": "2d12 + 6",
                        "Damage Type": "Piercing",
                        "Extra Effect": "If the triceratops moved 20+ ft straight toward the target, it takes an extra 9 (2d8) piercing damage and is knocked prone (if Huge or smaller)."
                    }
                }
            }
        }
    },
    "Tyrannosaurus Rex": {
        "Name": "Tyrannosaurus Rex",
        "Size": "Huge",
        "Type": "Beast (Dinosaur)",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 0,
        "HP": 136,
        "Hit Dice": "13d12 + 52",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 25,
            "DEX": 10,
            "CON": 19,
            "INT": 2,
            "WIS": 12,
            "CHA": 9,
        },
        "STR Save": 10,
        "DEX Save": 0,
        "CON Save": 4,
        "INT Save": -4,
        "WIS Save": 4,
        "CHA Save": -1,
        "Skills": {"Perception": 4},
        "Senses": {
            "Passive Perception": 14
        },
        "Languages": [],
        "Challenge": 8,
        "XP": 3900,
        "Proficiency Bonus": 3,
        "Actions": {
            "Multiattack": {
                "Description": "The tyrannosaurus makes one Bite attack and one Tail attack.",
                "Sequence": ["Bite", "Tail"],
                "Attacks": {
                    "Bite": {
                        "Name" : "Bite",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 10,
                        "Reach": "10 ft.",
                        "Target Size": "Large",
                        "Hit Average": 33,
                        "Damage": "4d12 + 7",
                        "Damage Type": "Piercing",
                        "Effect": {
                            "Name": "Grappled (Restrained)",
                            "Escape Modifier": "STR",
                            "Escape DC": 17,
                        }                               
                    },
                    "Tail": {
                        "Name" : "Tail",
                        "Attack Type": "Melee Weapon Attack",
                        "Attack Bonus": 10,
                        "Target Size": "Huge",
                        "Reach": "15 ft.",
                        "Hit Average": 25,
                        "Damage": "4d8 + 7",
                        "Damage Type": "Bludgeoning",
                        "Effect": "If the target is Huge or smaller, it is knocked prone."
                    }
                }
            }
        }
    },
    "Venomous Snake": {
        "Name": "Venomous Snake",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 5,
        "Hit Dice": "2d4",
        "Speed": {"Walk": 30, "Swim": 30},
        "Ability Scores": {
            "STR": 2,
            "DEX": 15,
            "CON": 11,
            "INT": 1,
            "WIS": 10,
            "CHA": 3,
        },
        "STR Save": -4,
        "DEX Save": 2,
        "CON Save": 0,
        "INT Save": -5,
        "WIS Save": 0,
        "CHA Save": -4,
        "Senses": {
            "Blindsight": 10,
            "Passive Perception": 10
        },
        "Languages": [],
        "Challenge": Fraction(1, 8),
        "XP": 25,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Reach": "5 ft.",
                "Hit Average": 4,
                "Damage Components": [
                    {"Dice": "1d4", "Modifier": "2", "Type": "Piercing"},
                    {"Dice": "1d6", "Type": "Poison"}
                ],   
            }
        }
    },
    "Vulture": {
        "Name": "Vulture",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 10,
        "Initiative": 0,
        "HP": 5,
        "Hit Dice": "1d8 + 1",
        "Speed": {"Walk": 10, "Fly": 50},
        "Ability Scores": {
            "STR": 7,
            "DEX": 10,
            "CON": 13,
            "INT": 2,
            "WIS": 12,
            "CHA": 4,
        },
        "STR Save": -2,
        "DEX Save": 0,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -3,
        "Skills": {"Perception": 3},
        "Senses": {
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The vulture has advantage on an attack roll against a creature if at least one of the vulture’s allies is within 5 feet of the creature and the ally isn’t incapacitated."
        },
        "Actions": {
            "Beak": {
                "Name" : "Beak",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 2,
                "Reach": "5 ft.",
                "Hit Average": 2,
                "Damage": "1d4",
                "Damage Type": "Piercing"
            }
        }
    },
    "Warhorse": {
        "Name": "Warhorse",
        "Size": "Large",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 11,
        "Initiative": 1,
        "HP": 19,
        "Hit Dice": "3d10 + 3",
        "Speed": {"Walk": 60},
        "Ability Scores": {
            "STR": 18,
            "DEX": 12,
            "CON": 13,
            "INT": 2,
            "WIS": 12,
            "CHA": 7,
        },
        "STR Save": 4,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 3,
        "CHA Save": -2,
        "Skills": {},
        "Senses": {
            "Passive Perception": 11
        },
        "Languages": [],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 2,
        "Actions": {
            "Hooves": {
                "Name" : "Hooves",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 9,
                "Damage": "2d4 + 4",
                "Damage Type": "Bludgeoning",
                "Additional Effect": "If the target is Large or smaller and the horse moved 20+ feet straight toward it, the target takes an extra 5 (2d4) Bludgeoning damage and is knocked Prone."
            }
        }
    },
    "Weasel": {
        "Name": "Weasel",
        "Size": "Tiny",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 13,
        "Initiative": 3,
        "HP": 1,
        "Hit Dice": "1d4 - 1",
        "Speed": {"Walk": 30, "Climb": 30},
        "Ability Scores": {
            "STR": 3,
            "DEX": 16,
            "CON": 8,
            "INT": 2,
            "WIS": 12,
            "CHA": 3,
        },
        "STR Save": -4,
        "DEX Save": 3,
        "CON Save": -1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -4,
        "Skills": {
            "Acrobatics": 5,
            "Perception": 3,
            "Stealth": 5
        },
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 13
        },
        "Languages": [],
        "Challenge": 0,
        "XP": 10,
        "Proficiency Bonus": 2,
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 1,
                "Damage": "1",
                "Damage Type": "Piercing"
            }
        }
    },
    "Winter Wolf": {
        "Name": "Winter Wolf",
        "Size": "Large",
        "Type": "Monstrosity",
        "Alignment": "Neutral Evil",
        "AC": 13,
        "Initiative": 1,
        "HP": 75,
        "Hit Dice": "10d10 + 20",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 18,
            "DEX": 13,
            "CON": 14,
            "INT": 7,
            "WIS": 12,
            "CHA": 8,
        },
        "STR Save": 4,
        "DEX Save": 1,
        "CON Save": 2,
        "INT Save": -2,
        "WIS Save": 1,
        "CHA Save": -1,
        "Skills": {
            "Perception": 5,
            "Stealth": 3
        },
        "Senses": {
            "Passive Perception": 15
        },
        "Languages": ["Common", "Giant", "Winter Wolf"],
        "Resistances": ["Cold"],
        "Challenge": 3,
        "XP": 700,
        "Proficiency Bonus": 3,
        "Traits": {
            "Keen Hearing and Smell": "The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Pack Tactics": "The wolf has Advantage on attack rolls against a creature if at least one of the wolf’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition.",
            "Snow Camouflage": "The wolf has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 6,
                "Reach": "5 ft.",
                "Hit Average": 11,
                "Damage": "2d6 + 4",
                "Damage Type": "Piercing",
                "Effect": {
                    "Name": "Prone",
                    "Save Type": "STR",
                    "Save DC": 14,
                },                
                "Additional Effect": "If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked Prone."
            },
            "Cold Breath": {
                "Recharge": "5-6",
                "Attack Type": "Dexterity Saving Throw",
                "Save DC": 12,
                "Range": "15 ft. cone",
                "Effect": "Each creature in that area takes 18 (4d8) cold damage on a failed save, or half as much damage on a successful save."
            }       
        }
    },        
    "Wolf": {
        "Name": "Wolf",
        "Size": "Medium",
        "Type": "Beast",
        "Alignment": "Unaligned",
        "AC": 12,
        "Initiative": 2,
        "HP": 11,
        "Hit Dice": "2d8 + 2",
        "Speed": {"Walk": 40},
        "Ability Scores": {
            "STR": 14,
            "DEX": 15,
            "CON": 12,
            "INT": 3,
            "WIS": 12,
            "CHA": 6,
        },
        "STR Save": 2,
        "DEX Save": 2,
        "CON Save": 1,
        "INT Save": -4,
        "WIS Save": 1,
        "CHA Save": -2,
        "Skills": {
            "Perception": 5,
            "Stealth": 4
        },
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 15
        },
        "Languages": [],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Pack Tactics": "The wolf has Advantage on attack rolls against a creature if at least one of the wolf’s allies is within 5 feet of the creature and the ally doesn’t have the Incapacitated condition."
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 4,
                "Target Size": "Medium",
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d6 + 2",
                "Damage Type": "Piercing",
                "Effect": "If the target is Medium or smaller, it is knocked Prone."
            }
        }
    },     
    "Worg": {
        "Name": "Worg",
        "Size": "Large",
        "Type": "Monstrosity",
        "Alignment": "Neutral Evil",
        "AC": 13,
        "Initiative": 1,
        "HP": 26,
        "Hit Dice": "4d10 + 4",
        "Speed": {"Walk": 50},
        "Ability Scores": {
            "STR": 16,
            "DEX": 13,
            "CON": 13,
            "INT": 7,
            "WIS": 11,
            "CHA": 8,
        },
        "STR Save": 3,
        "DEX Save": 1,
        "CON Save": 1,
        "INT Save": -2,
        "WIS Save": 0,
        "CHA Save": -1,
        "Skills": {
            "Perception": 4,
        },
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 14
        },
        "Languages": ["Goblin", "Worg"],
        "Challenge": Fraction(1, 2),
        "XP": 100,
        "Proficiency Bonus": 3,
        "Traits": {
            "Keen Hearing and Smell": "The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
        },
        "Actions": {
            "Bite": {
                "Name" : "Bite",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 5,
                "Reach": "5 ft.",
                "Hit Average": 10,
                "Damage": "2d6 + 3",
                "Damage Type": "Piercing",
                "Effect": {
                    "Name": "Prone",
                    "Save Type": "STR",
                    "Save DC": 13,
                },                
                "Description": "If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked Prone."
            }
        }
    },     
    "Zombie": {
        "Name": "Zombie",
        "Size": "Medium",
        "Type": "Undead",
        "Alignment": "Neutral Evil",
        "AC": 8,
        "Initiative": -2,
        "HP": 15,
        "Hit Dice": "2d8+6",
        "Speed": {
            "Walk": 20
        },
        "Ability Scores": {
            "STR": 13,
            "DEX": 6,
            "CON": 16,
            "INT": 3,
            "WIS": 6,
            "CHA": 5
        },
        "STR Save": 1,
        "DEX Save": -2,
        "CON Save": 3,
        "INT Save": -4,
        "WIS Save": 0,
        "CHA Save": -3,
        "Skills": {},
        "Senses": {
            "Darkvision": 60,
            "Passive Perception": 8
        },
        "Languages": ["Understands Common and one other language (can’t speak)"],
        "Challenge": Fraction(1, 4),
        "XP": 50,
        "Proficiency Bonus": 2,
        "Traits": {
            "Undead Fortitude": {
                "Description": "If damage reduces the zombie to 0 HP, it makes a Constitution saving throw (DC 5 + damage taken) unless the damage is Radiant or from a Critical Hit. On a success, it drops to 1 HP instead."
            }
        },
        "Gear": [],
        "Actions": {
            "Slam": {
                "Name": "Slam",
                "Attack Type": "Melee Weapon Attack",
                "Attack Bonus": 3,
                "Reach": "5 ft.",
                "Hit Average": 5,
                "Damage": "1d8+1",
                "Damage Type": "Bludgeoning"
            }
        }
    },   
}