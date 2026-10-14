import limb

class Creature:
    def __init__(self):
        self.limbs = []

    def add_limb(self, given_limb: limb.Limb):
        if isinstance(given_limb, limb.Limb):
            self.limbs.append(given_limb)
        else:
            raise TypeError(f"The given_limb is {type(given_limb)} not limb.Limb")