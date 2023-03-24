def get_min_avg_max(sequence):

    larg = max(sequence)
    minim = min(sequence)
    avg = sum(sequence)/len(sequence)
    print(larg,minim,avg)


get_min_avg_max(sequence=[3,4,6,7])