# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:55:24 2021

@author: Abdullah
"""

import pandas as pd
import numpy

sym = [4,5,6]

myData = pd.read_csv("hepatitis.csv", sep=',')
myData = numpy.array(myData)

print(numpy.shape(myData))
D = []
L = []


totalLive = list(myData[0:, 0]).count(2)
totalDied = list(myData[0:, 0]).count(1)
D.append(totalDied)
L.append(totalLive)
# selecting all rows that contans 2 in class column
# all died

allDied = myData[myData[:, 0] == 1]
# selecting all rows that contans 2 in class column
# all live
allLive = myData[myData[:, 0] == 2]


# All died with steriod
D.append( list(allDied[:, sym[0]]).count(2))
# All died with antiviral
D.append( list(allDied[:, sym[1]]).count(2))
# All died with fatigue
D.append( list(allDied[:, sym[2]]).count(2))
# All live with steriod
L.append( list(allLive[:, sym[0]]).count(2))
# All live with antiviral
L.append( list(allLive[:, sym[1]]).count(2))
# All live with fatigue
L.append( list(allLive[:, sym[2]]).count(2))


T = []
for (item1, item2) in zip(L, D):
    T.append(item1+item2)
    
sympercentageL = []    
sympercentageL.append(L[1]/L[0])
sympercentageL.append(L[2]/L[0])
sympercentageL.append(L[3]/L[0]) 

sympercentageD = []    
sympercentageD.append(D[1]/D[0])
sympercentageD.append(D[2]/D[0])
sympercentageD.append(D[3]/D[0]) 

sympercentageT = []    
sympercentageT.append(T[1]/T[0])
sympercentageT.append(T[2]/T[0])
sympercentageT.append(T[3]/T[0]) 

livepercentage = totalLive/142
Diedpercentage = totalDied/142

sympercentageL1 = [i * livepercentage for i in sympercentageL]
sympercentageD1 = [i * Diedpercentage for i in sympercentageD]

Probabilitylive = numpy.prod(sympercentageL1)
Probabilitylive = Probabilitylive*livepercentage

ProbabilityDied = numpy.prod(sympercentageD1)
ProbabilityDied = ProbabilityDied*Diedpercentage

PT = Probabilitylive+ProbabilityDied
PL = Probabilitylive/PT
PD = ProbabilityDied/PT

print(PL)
print(PD)

if(PL>PD):
    print("Conguration You will remain Live")
else:
    print("Bad luck! according to our prediction you will not survive")


