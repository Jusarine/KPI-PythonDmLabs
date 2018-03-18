def calc_simple_d(a, b, c, universal_set):
    not_b = universal_set - b
    s1 = not_b | c
    s2 = a & s1
    return s2
