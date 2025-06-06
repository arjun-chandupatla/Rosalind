# Find the ratio of transitions to transversions in a string of DNA
# Both transitions and transversions are types of point mutations,
# but transitions are purine-purine or pyrimidine-pyrimidine substitutions,
# while transversions are purine-pyrimidine substitutions

def ratio(s1: str, s2: str) -> float:
    ts, tv = 0, 0
    for i in range(len(s1)):
        b1, b2 = s1[i], s2[i]
        if b1 == b2:
            continue
        match b1, b2:
            case "A" | "G", "A" | "G":
                ts += 1
            case "C" | "T", "C" | "T":
                ts += 1
            case _:
                tv += 1
    return ts/tv
