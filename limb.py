import json

"""
This file is to create and organize limbs for the creature class.
"""

class Limb:
    def __init__(self):
        self.name = "Limb"
        self.attributes = [] # Describes the state or look of the limb
        self.extremities = []  # These will be hands, feets, claws, etc.
        self.description = "This is a limb"

    def add_attribute(self, given_attribute: str) -> None:
        self.attributes.append(given_attribute)

    def add_extremities(self, given_extremity: str) -> None:
        self.extremities.append(given_extremity)

    def set_name(self, given_name: str) -> None:
        self.name = given_name

    def describe(self) -> None:
        print(self.description)

def create_limb(name="Limb", attributes=[]) -> Limb:
    if not attributes and name == "limb":
        return Limb()
    new_limb = Limb()
    new_limb.attributes = attributes
    new_limb.set_name(name)
    return new_limb

def create_limb_from_file(limb_name: str, attributes=[]) -> Limb:
    """
    The attributes parameter is for when creating a creature the creature attributes will be able to transfer to the limbs. 
    """
    with open(f"Limbs/{limb_name}.json", "r") as file:
        limb_data = json.load(file)
    new_limb = create_limb(limb_name, attributes)
    new_limb.add_extremities(limb_data["extremities"])
    return new_limb