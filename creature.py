import limb
import json

"""
This file is used to create and organize the creature class.
"""

class Creature:
    def __init__(self):
        self.limbs = []
        self.attributes = [] # These attributes will count towards all other limbs. Ex. hairy, all limbs will be hairy. 

    def add_limb(self, given_limb: limb.Limb):
        if isinstance(given_limb, limb.Limb):
            self.limbs.append(given_limb)
        else:
            raise TypeError(f"The given_limb is {type(given_limb)} not limb.Limb")

    def describe(self):
        for selected_limb in self.limbs:
            selected_limb.describe()

def create_creature_from_file(file_path: str):
    """
    Order of how to get creature data.
    1. Place the attributes in the creature class
    2. Loop through Limbs, create and add them to the creature.
    3. Make sure the attributes of the creature are also on the Limbs.
    """
    with open(file_path, "r") as file:
        creature_data = json.load(file)
    new_creature = Creature()
    new_creature.attributes = creature_data["attributes"]

    for selected_limb in creature_data["limbs"]:
        new_creature.add_limb(limb.create_limb_from_file(selected_limb, new_creature.attributes))

    return new_creature