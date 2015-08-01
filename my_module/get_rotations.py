def get_rotations(n):
    rotations = []
    for i in xrange(len(str(n))):
        rotations.append(int(str(n)[i:] + str(n)[0:i]))
    return(rotations)
