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
        
#это важно для плотности атомов:
#Эле́ктроотрица́тельность — фундаментальное химическое свойство атома, количественная характеристика способности атома в молекуле смещать к себе общие электронные пары, то есть способность атомов оттягивать к себе электроны других атомов.
    
class H(Atom):
    chemical_class = "Хуй знает, короче водород"
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
class Be(Atom):
    #Токсичен из-за устойчивого соединения с кислородом BeO#
    chemical_class = "Metal"
    proton_count = 4
    neutron_count = 5
    electron_count = 4
    metal_activity_coef = 61
    valence = 2
    radius = 104
class B(Atom):
    #По своиствам напоминает кремний#
    chemical_class = "Nonmetal"
    proton_count = 5
    neutron_count = 6
    electron_count = 5
    valence = 3
    radius = 98
class C(Atom):
    #Самая непонятная хуйня с 1000 и 1 модификацией...     от дерева до графена блять!!!#
    chemical_class = "Nonmetal"
    proton_count = 6
    neutron_count = 6
    electron_count = 6
    valence = 4
    radius = 77 
class N(Atom):
    #Входит в состав днк#
    chemical_class = "Nonmetal"
    proton_count = 7
    neutron_count = 7
    electron_count = 7
    valence = 5
    radius = 92 
class O(Atom):
    #Это кислород, что те еще блять надо?## я хуй знает, но его радиус варьируется от 45 до 78 так что я хз
    chemical_class = "Nonmetal"
    proton_count = 8
    neutron_count = 8
    electron_count = 8
    valence = 6
    radius = 48 
class F(Atom):
    ##
    chemical_class = "Nonmetal"
    proton_count = 9
    neutron_count = 10
    electron_count = 9
    valence = 7
    radius = 73
class Ne(Atom):
    #(Радиус атома	? (38)[2] пм)   прямо с википедии#
    chemical_class = "Nonmetal"
    proton_count = 10
    neutron_count = 10
    electron_count = 10
    valence = 0
    radius = 38
class Na(Atom):
    #Мой любимчик
    chemical_class = "Metal"
    proton_count = 11
    neutron_count = 12
    electron_count = 11
    metal_activity_coef = 92
    valence = 1
    radius = 171
class Mg(Atom):
    ##
    chemical_class = "Metal"
    proton_count = 12
    neutron_count = 12
    electron_count = 12
    metal_activity_coef = 87
    valence = 2
    radius = 128
class Al(Atom):
    ##
    chemical_class = "Metal"
    proton_count = 13
    neutron_count = 14
    electron_count = 13
    metal_activity_coef = 59
    valence = 3
    radius = 131
class Si(Atom):
    ##
    chemical_class = "Nonmetal"
    proton_count = 14
    neutron_count = 14
    electron_count = 14
    valence = 4
    radius = 132
class P(Atom):
    ##
    chemical_class = "Nonmetal"
    proton_count = 15
    neutron_count = 16
    electron_count = 15
    valence = 5
    radius = 128
class S(Atom):
    ##
    chemical_class = "Nonmetal"
    proton_count = 16
    neutron_count = 16
    electron_count = 16
    valence = 6
    radius = 127
class Cl(Atom):
    ##
    chemical_class = "Nonmetal"
    proton_count = 17
    neutron_count = 18
    electron_count = 17
    valence = 7
    radius = 99
class Ar(Atom):
    ##
    chemical_class = "Nonmetal"
    proton_count = 18
    neutron_count = 20
    electron_count = 18
    valence = 0
    radius = 71
class K(Atom):
    ##
    chemical_class = "Metal"
    proton_count = 19
    neutron_count = 20
    electron_count = 19
    metal_activity_coef = 99
    valence = 1
    radius = 235
class Ca(Atom):
    ##
    chemical_class = "Metal"
    proton_count = 20
    neutron_count = 20
    electron_count = 20
    metal_activity_coef = 94
    valence = 2
    radius = 174
class Sc(Atom):
    ##
    chemical_class = "Metal"
    proton_count = 21
    neutron_count = 23
    electron_count = 21
    metal_activity_coef = 67
    valence = 3
    radius = 162
class Ti(Atom):
    ##
    chemical_class = "Metal"
    proton_count = 22
    neutron_count = 26
    electron_count = 22
    metal_activity_coef = 50
    valence = 4
    radius = 147
#Витошка, ты дурак блин#