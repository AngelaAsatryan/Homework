# create class Chemical element
class Chemical_element:
    def __init__(self, Chemical_symbol, Chemical_name, Atomic_number, Atomic_mass, Chemical_properties, Phase, Melt_boil_points, Densities):
        self.Chemical_symbol = Chemical_symbol
        self.Chemical_name = Chemical_name
        self.Atomic_number = Atomic_number
        self.Atomic_mass = Atomic_mass
        self.Chemical_properties = Chemical_properties
        self.Phase = Phase
        self.Melt_boil_points = Melt_boil_points
        self.Densities = Densities
    #methods
    def transform(mol):
        print("The" + " "+ mol.Chemical_name + " " +"has been transformed to.")
    def form_mol(mol):
        print(mol.Chemical_symbol + " "+ "+" + " "+mol.Chemical_symbol+ " "+"="+ " "+str(mol.Chemical_symbol)+"2")
    def radiate(mol):
        print(int(mol.Atomic_number) - 1)
    def boil(mol):
        print("The temperature of" + " " + mol.Chemical_name + " " + "increased to the boiling point.")

#instance, e.g Hydrogen
H = Chemical_element("H", "Hydrogen", "1", "1.00784u", "Non metal", "Gas", "-259.14 C, -252.87 C", "0.0763 g/cm3")
print(H.Densities)
H.transform()
H.form_mol()
H.radiate()
H.boil()
