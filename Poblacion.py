def poblacion():
    poblacionA = 35000000
    poblacionB = 19900000
    lim = 1
    i = 0
    while i < lim:
        if poblacionA < poblacionB:
            i = lim + 1
        else:
            incrementoA = poblacionA * 0.20
            poblacionA = incrementoA + poblacionA
            incrementoB = poblacionB * 0.30
            poblacionB = incrementoB + poblacionB
            lim = lim +1
            incrementoA = 0
            incrementoB = 0
            print('El limite',lim)
            print('El limite',poblacionA)
            print('El limite',poblacionB)
    i=i+1
poblacion()
