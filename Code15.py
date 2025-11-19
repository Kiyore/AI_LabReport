import random
import math

def simulatedannealing(cities, initialtemperature, stoppingtemp, coolingrate, totaldistance):
    currenttour = cities[:]
    besttour = currenttour[:]
    n = len(cities)
    temperature = initialtemperature
    iteration = 0

    while temperature > stoppingtemp:
        i, j = sorted(random.sample(range(n), 2))
        newtour = currenttour[:]
        newtour[i:j+1] = reversed(newtour[i:j+1])
        currentdistance = totaldistance(currenttour)
        newdistance = totaldistance(newtour)
        if newdistance < currentdistance:
            currenttour = newtour
            if newdistance < totaldistance(besttour):
                besttour = newtour
        elif random.random() < math.exp((currentdistance - newdistance) / temperature):
            currenttour = newtour
        temperature *= coolingrate
        iteration += 1

    return besttour, totaldistance(besttour)
