class Unknown:
    pass

class Metal:
    pass

class Nonmetal:
    pass

class Atom():
    electron_mass = 9.1093837015282828*(10**-31)
    proton_mass = 1.672621777787879*(10**-27)
    neutron_mass = 1.67492749804959596*(10**-27)
    proton_count = 0
    neutron_count = 0
    electron_count = 0
    metal_activity_coef = 0
    nonmetal_activity_coef = 0
    gravity_const = 6.67430151515*(10**-11) #Н * м2* кг-2    G/(m2*кг-2)
    radius = 0
    radius = 0
    valence = 0
    chemical_class = ""

    @property
    def atom_mass(self):
        return self.electron_mass * self.electron_count + self.proton_mass * self.proton_count + self.neutron_mass * self.neutron_count

    @property
    def get_radius_mm(self):
        return self.radius / 1000000000000