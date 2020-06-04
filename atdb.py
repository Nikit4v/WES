from Helper import *
    
class H(Atom):
    chemical_class = Unknown() #Проще стравнить классы чем строки, зато на класс соединений можно будет спихнуть часть инфы и обработки
    proton_count = 1
    neutron_count = 0
    electron_count = 1
    metal_activity_coef = 28
    valence = 1
    radius = 53

class He(Atom):
    chemical_class = Nonmetal()
    proton_count = 2
    neutron_count = 2
    electron_count = 2
    valence = 0
    radius = 29

class Li(Atom):
    chemical_class = Metal()
    proton_count = 3
    neutron_count = 4
    electron_count = 3
    metal_activity_coef = 102
    valence = 1
    radius = 159