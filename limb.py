class Limb:
    def __init__(self):
        self.attributes = []

    def add_attribute(self, given_attribute: str):
        self.attributes.append(given_attribute)

    def describe(self):
        if self.attributes:
            print(f"This limb is {self.attributes}")
        else:
            print("This limb is blank")

def create_limb(attributes=[]) -> Limb:
    if not attributes:
        return Limb()
    new_limb = Limb()
    new_limb.attributes = attributes
    return new_limb