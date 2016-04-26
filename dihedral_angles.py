import linear_ops


def find_dihedral_angles():
    pdb_file = open("2ezm.pdb")
    atoms = list_from_file(pdb_file)

    phi_atoms = atoms[0:4]
    psi_atoms = atoms[1:5]

    print u"\u03d5 angle = " + str(linear_ops.dihedral_angle(phi_atoms))
    print u"\u03a8 angle = " + str(linear_ops.dihedral_angle(psi_atoms))


def list_from_file(pdb_file):
    x = []
    for line in pdb_file:
        temp = line.split()
        # parses just the ATOMS in the tenth amino acid that are C, CA or N
        # also saves the C from the 9th and N from the 11th amino acids
        if temp[0] == "ATOM":
            if (temp[2] in ['C', 'CA', 'N']) and (temp[5] == '10'):
                temp = map(float, temp[6:9])
                x.append(temp)
            elif (temp[2] == 'C') and temp[5] == '9':
                temp = map(float, temp[6:9])
                x.append(temp)
            elif (temp[2] == 'N') and temp[5] == '11':
                temp = map(float, temp[6:9])
                x.append(temp)
    return x


find_dihedral_angles()
