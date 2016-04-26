import math


def get_energy():
    pdb_file = open("2ezm.pdb")
    pdb_list = list_from_file(pdb_file)
    high_energy = []
    total_energy = 0
    for entry in pdb_list:
        for index in range(pdb_list.index(entry) + 5, len(pdb_list)):
            energ = energy(entry, pdb_list[index])
            total_energy += energ
            if energ > 20:
                high_energy.append([entry, pdb_list[index], energ])
    print total_energy
    print "Number of steric clashes: " + str(len(high_energy))
    for entry in high_energy:
        print "Energy: " + str(entry.pop(2))
        print "Distance: " + str(distance(entry[0], entry[1]))
        print "Atoms: "
        for element in entry:
            print element


def list_from_file(pdb_file):
    x = [line.split() for line in pdb_file if line.startswith("ATOM")]
    return x


def distance(atom1, atom2):
    return math.sqrt((float(atom1[6]) - float(atom2[6]))**2 +
                     (float(atom1[7]) - float(atom2[7]))**2 +
                     (float(atom1[8]) - float(atom2[8]))**2)


def energy(atom1, atom2):
    dist = distance(atom1, atom2)
    if dist < 3.4:
        return 100/dist**2
    else:
        return 0


get_energy()
