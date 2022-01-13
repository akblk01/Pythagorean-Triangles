def pisagor():
    listPisagor = list()
    for i in range(1,100):
        for j in range(1,100):
            for k in range(1,100):
                if (i**2) + (j**2) == k**2 and i<j:
                    listPisagor.append((i,j,k))
    for i in listPisagor:
        print(i)
pisagor()