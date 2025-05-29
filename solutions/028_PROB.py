# Basically finds the probability that a motif will occur through random chance in 
# a DNA sequence given its GC content
# Takes the log base 10 of each probability, so higher numbers (less negative) mean
# a higher probability


def probRandomString(s: str, gc_arr: list[float]):
    for gc in gc_arr:
        g = gc/2
        a = (1-gc)/2
        prob = 1.0
        for base in s:
            match base:
                case "A" | "T":
                    prob *= a
                case "C" | "G":
                    prob *= g
        yield math.log10(prob)
