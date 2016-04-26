import math


def dihedral_angle(atoms):
    vec_b_a = vector_difference(atoms[1], atoms[0])
    vec_c_b = vector_difference(atoms[2], atoms[1])
    abc_normal = normalize(cross_product(vec_b_a, vec_c_b))

    vec_d_c = vector_difference(atoms[3], atoms[2])
    bcd_normal = normalize(cross_product(vec_c_b, vec_d_c))

    if dot_product(abc_normal, normalize(vec_d_c)) > 0:
        return math.degrees(angle_btw_vectors(dot_product(abc_normal, bcd_normal)))
    else:
        return -math.degrees(angle_btw_vectors(dot_product(abc_normal, bcd_normal)))


def vector_difference(vec1, vec2):
    return [vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2]]


def cross_product(vec1, vec2):
    c_x = vec1[1]*vec2[2] - vec1[2]*vec2[1]
    c_y = vec1[2]*vec2[0] - vec1[0]*vec2[2]
    c_z = vec1[0]*vec2[1] - vec1[1]*vec2[0]
    return [c_x, c_y, c_z]


def normalize(vec):
    magnitude = math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    normalized = [a/magnitude for a in vec]
    return normalized


def dot_product(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]


def angle_btw_vectors(vec_dot_prod):
    return math.acos(vec_dot_prod)
