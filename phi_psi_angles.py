import Bio.PDB
# calculating the Psi and phi angles by using BioPython:
# https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/ramachandran/calculate/
for model in Bio.PDB.PDBParser().get_structure("1HMP", "1HMP.pdb") :
    for chain in model :
        poly = Bio.PDB.Polypeptide.Polypeptide(chain)
        print("Model %s Chain %s" % (str(model.id), str(chain.id)))
        print(poly.get_phi_psi_list())