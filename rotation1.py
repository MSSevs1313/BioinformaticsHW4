import math
import rmsd
import linear_ops


def rotation1():
    pdb_list = list_from_file("2ezm.pdb")
    last_n_ca_vector = get_vector(pdb_list)

    stripped_vector = list_stripper(last_n_ca_vector)
    print linear_ops.dihedral_angle(stripped_vector)

    rmsd.align_to_origin(pdb_list, last_n_ca_vector[1])

    pdb_sub_list = pdb_list[pdb_list.index(last_n_ca_vector[0])::]
    # rotate(pdb_sub_list, math.radians(30))


# def rotate(pdb_sub_list, angle):
#     for atom in pdb_sub_list:


def list_stripper(list):
    x = [map(float, atom[6:9]) for atom in list]
    return x


def list_from_file(pdb_file):
    pdb_file = open(pdb_file)
    x = [line.split() for line in pdb_file if line.startswith("ATOM")]
    return x


def get_vector(pdb_list):
    vector = []
    vector.append(pdb_list[1476])
    vector.append(pdb_list[1495])
    vector.append(pdb_list[1496])
    vector.append(pdb_list[1497])
    return vector

rotation1()
