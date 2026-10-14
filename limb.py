class Limb:
    def __init__(self):
        self.name = "Limb"
        self.attributes = []

    def add_attribute(self, given_attribute: str):
        self.attributes.append(given_attribute)

    def set_name(self, given_name: str):
        self.name = given_name

    def describe(self):
        if self.attributes:
            print(f"This {self.name} is {self.attributes}")
        else:
            print(f"This {self.name} is blank")

def create_limb(attributes=[]) -> Limb:
    if not attributes:
        return Limb()
    new_limb = Limb()
    new_limb.attributes = attributes
    return new_limb