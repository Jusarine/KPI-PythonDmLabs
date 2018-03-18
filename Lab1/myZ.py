def calc_my_z(b, c, universal_set):
    not_b = complement(b, universal_set)
    z = difference(c, not_b)
    return z


def complement(x, universal_set):
    not_x = difference(universal_set, x)
    return not_x


def difference(x, y):
    dif = set()

    for i in x:
        exist = False
        for j in y:
            if i == j:
                exist = True

        if not exist:
            dif.add(i)

    return dif
