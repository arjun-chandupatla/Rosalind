# Calculate the expected number of offspring with a dominant phenotype
# given six integers that indicate how many couples have each possible 
# genotype for a certain factor. 

# Calculate the average number of offspring with a dominant phenotype
def getOffspring(n_arr: list[int]) -> float:
    offspring_arr = []
    for i in range(6):
        k = i+1
        n = n_arr[i]
        match k:
        # cases taken from drawing Punnett squares
            case 1 | 2 | 3:
                offspring_arr.append(float(n*2))
            case 4:
                offspring_arr.append(float(2*n*0.75))
            case 5:
                offspring_arr.append(float(n))
            case 6:
                offspring_arr.append(float(0))
            case _:        # theoretically unreachable state
                pass
    num_dominant = sum(offspring_arr)
    return num_dominant


# "Stringify" the float
def formatOutput(num):
    return str(num)


def parseInput(file):
    text = file.read()
    couple_arr = list(map(int, text.split()))
    return couple_arr
