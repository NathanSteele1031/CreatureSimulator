"""
This file is to create and organize limbs for the creature class.
"""

class Limb:
    def __init__(self):
        self.name = "Limb"
        self.attributes = [] # Describes the state or look of the limb
        self.extremities = []  # These will be hands, feets, claws, etc.
        self.description = "This is a limb"

    def add_attribute(self, given_attribute: str):
        self.attributes.append(given_attribute)

    def set_name(self, given_name: str):
        self.name = given_name

    def describe(self):
        print(self.description)

def create_limb(name="Limb", attributes=[]) -> Limb:
    if not attributes and name == "limb":
        return Limb()
    new_limb = Limb()
    new_limb.attributes = attributes
    new_limb.set_name = name
    return new_limb