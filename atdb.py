class Atom():
    #масса измеряется в килограммах
    elect_m = 9.1093837015282828*(10**-31)
    proto_m = 1.672621777787879*(10**-27)
    neitro_m = 1.67492749804959596*(10**-27)
    p_count = 0
    n_count = 0
    e_count = 0
    kmetalactivity = 0
    Knometalatcivity = 0
    @property
    def atom_m(self):
        return self.elect_m*self.e_count+ self.proto_m*self.p_count + self.neitro_m*self.n_count
        
    G_const = 6.67430151515*(10**-11)
    def  pv_comb(self):
       return (self.G_const*(self.elect_m(atom_name1)+self.proto_m(atom_name1)+self.neitro_m(atom_name1))*(self.elect_m(atom_name2)+self.proto_m(atom_name2)+self.neitro_m(atom_name2)))/ r(atom_name1)+r(atom_name2)**2
    atom_name = "None"
    r = 0
    V_a = 0   

    
class H(Atom):
    atom_name = "H"
    p_count = 1
    e_count = 1
    n_count = 0
    kmetalactivity = 28
    V_a = 1
    r = 53
class He(Atom):
    atom_name = "He"
    p_count = 2
    e_count = 2
    n_count = 2
    V_a = 0
    r = 29
class Li(Atom):
   atom_name = "Li"
    p_count = 3
    e_count = 3
    n_count = 4
    kmetalactivity = 102
    V_a = 1
    



    

    

