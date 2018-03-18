def calc_d(a, b, c, universal_set):
    s1 = a | b
    not_a = universal_set - a
    not_b = universal_set - b
    s2 = not_a & b
    s3 = not_b | c
    not_s3 = universal_set - s3
    s4 = s2 | not_s3
    not_s4 = universal_set - s4
    s5 = s1 & not_s4
    return s5
