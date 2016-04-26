import math
import rmsd


def translation1():
    pdb_list = list_from_file("2ezm.pdb")
    last_n_ca_vector = find_last_n(pdb_list)
    # rmsd.align_to_origin(pdb_list, last_n_ca_vector)
    # pdb_sub_list = pdb_list[pdb_list.index(last_n_ca_vector)::]
    # rotate(pdb_sub_list, math.radians(30))


# def rotate(pdb_sub_list, angle):
#     for atom in pdb_sub_list:



def list_from_file(pdb_file):
    pdb_file = open(pdb_file)
    x = [line.split() for line in pdb_file if line.startswith("ATOM")]
    return x


def find_last_n(pdb_list):
    ca = 0
    n = 0
    for atom in pdb_list[::-1]:
        if atom[2] == "CA":
            ca = pdb_list.index(atom)
        elif atom[2] == "N":
            n = pdb_list.index(atom)
        if not (ca == 0) and not (n == 0):
            last_n_ca_vector = pdb_list[n:ca+1]
            print last_n_ca_vector
            return last_n_ca_vector



translation1()
