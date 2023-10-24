L1 = [1, 3, 6, 78, 35, 88, 55]
    L2 = [12, 24, 35, 24, 88, 120, 155]

    L3 = intersection_listes(L1, L2)

def intersection_listes(L1, L2):
    ensemble_L1 = set(L1)
    ensemble_L2 = set(L2)
    L3 = list(ensemble_L1 & ensemble_L2)
    return L3

    print("L1 =", L1)
    print("L2 =", L2)
    print("L3 (Intersection) =", L3)
