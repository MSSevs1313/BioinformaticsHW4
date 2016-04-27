import math


def find_rmsd(a, b):
    print "The RMSD of set1 and set2 is: %f" % rmsd(a, b)

    centroidA = align_to_origin(a, find_centroid(a))
    centroidB = align_to_origin(b, find_centroid(b))

    print "Both sets are aligned to the origin."
    print "Set1's centroid: %s" % round_centroid(centroidA)
    print "Set2's centroid: %s" % round_centroid(centroidB)

    print "The optimal RMSD of set1 and set2 after translation is: %f" % rmsd(a, b)


# find the distance between two points a and b
def distance(a, b):
    total = 0
    for ptA, ptB in zip(a, b):
        total += (ptA - ptB) ** 2
    return total


# find the rmsd between two lists of points using the distance
# between each point
def rmsd(a, b):
    total = 0
    for (ptA, ptB) in zip(a, b):
        total += distance(ptA, ptB)
    total /= len(a)
    return math.sqrt(total)


# aligns a given list to the origin by subtracting
# the centroid from each point
def align_to_origin(listA, centroid):
    # centroid = find_centroid(listA)
    for pt in listA:
        if not pt == centroid:
            pt[6] = float(pt[6]) - float(centroid[6])
            pt[7] = float(pt[7]) - float(centroid[7])
            pt[8] = float(pt[8]) - float(centroid[8])
    centroid[6] = 0.0
    centroid[7] = 0.0
    centroid[8] = 0.0
    # return find_centroid(listA)


# finds the centroid of a list, ie the average of each coordinate
def find_centroid(aList):
    xAv, yAv, zAv = (0,)*3
    for pt in aList:
        xAv += pt[0]
        yAv += pt[1]
        zAv += pt[2]
    xAv /= len(aList)
    yAv /= len(aList)
    zAv /= len(aList)
    return [xAv, yAv, zAv]


# rounds and absolute values the centroid
# otherwise returns just really small numbers (####e^-18, etc.)
def round_centroid(centroid):
    return [abs(round(x, 5)) for x in centroid]
