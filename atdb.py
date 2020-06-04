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
    chemical_class = None

    @property
    def atom_mass(self):
        return self.elect_m * self.e_count + self.proto_m * self.p_count + self.neitro_m * self.n_count

    @property
    def get_radius_mm(self):
        return self.radius / 1000000000000
        

    
class H(Atom):
    chemical_class = "Хуй знает"
    proton_count = 1
    neutron_count = 0
    electron_count = 1
    metal_activity_coef = 28
    valence = 1
    radius = 53

class He(Atom):
    chemical_class = "Nonmetal"
    proton_count = 2
    neutron_count = 2
    electron_count = 2
    valence = 0
    radius = 29

class Li(Atom):
    chemical_class = "Metal"
    proton_count = 3
    neutron_count = 4
    electron_count = 3
    metal_activity_coef = 102
    valence = 1
    radius = 159