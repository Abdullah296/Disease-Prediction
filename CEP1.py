# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:15:35 2021

@author: Abdullah
"""
import pandas as pd
import numpy 

sym = [3,4,5,6]                                                    # Symptoms you want to analyse
missing_values = ["n/a", "na", "--"]                
myData = pd.read_csv("41disease.csv", na_values = missing_values)
myData = numpy.array(myData)

Disease = {'Fungal infection': 1,                                   # making distionary to change it into number
          'Allergy': 2,
          'GERD':3,
          'Chronic cholestasis':4,
          'Drug Reaction':5,
          'Peptic ulcer diseae':6,
          'AIDS':7,
          'Diabetes ':8,
          'Gastroenteritis':9,
          'Bronchial Asthma':10,
          'Hypertension ':11,
          'Migraine':12,
          'Cervical spondylosis':13,
          'Jaundice':14,
          'Malaria':15,
          'Chicken pox':16,
          'Dengue':17,
          'Typhoid':18,
          'hepatitis A':19,
          'Hepatitis B':20,
          'Hepatitis C':21,
          'Hepatitis D':22,
          'Hepatitis E':23,
          'Alcoholic hepatitis':24,
          'Tuberculosis':25,
          'Common Cold':26,
          'Pneumonia':27,
          'Heart attack':28,
          'Varicose veins':29,
          'Hypothyroidism':30,
          'Hyperthyroidism':31,
          'Hypoglycemia':32,
          'Osteoarthristis':33,
          'Arthritis':34,
          'Acne':35,
          'Urinary tract infection':36,
          'Psoriasis':37,
          'Impetigo':38,
          'Paralysis (brain hemorrhage)':39,
          'Dimorphic hemmorhoids(piles)':40,
          '(vertigo) Paroymsal  Positional Vertigo':41,
          }


print(myData[:, 0])

Dis = list(myData[:, 0])
One = []

for i in range(0, len(Dis)):
    One.append ( Disease[Dis[i]])

myData[:, 0]=One;                                               # converted it into Number


# some list neede

D1 = []                                                      # Disease1 List
D2 = []                                                      # Disease2 List
T = []                                                      # Total
sympercentageD1 = []                                         # D1 symptoms percentage
sympercentageD2 = []                                         # D2symptoms percentage
sympercentageT = []                                         #total symptoms percentage

totalD1 = list(myData[0:, 0]).count(1)                    # Total D1 person
totalD2 = list(myData[0:, 0]).count(2)                    # Total D2 person

D1.append(totalD1)
D2.append(totalD2)
# selecting all rows that contans 2 in class column
# all died

HaveD1 = myData[myData[:, 0] == 1]                         # Seperate all D1 person attributes
# selecting all rows that contans 2 in class column
# all live
HaveD2 = myData[myData[:, 0] == 2]                         # Seperate all D2 person attributes


# Counting of Disease 1 and 2
for i in sym:
    D1.append(list(HaveD1[:, i]).count(1))                  # count symptoms of all D1 people

for i in sym:
    D2.append( list(HaveD2[:, i]).count(1))                 # count symptoms of all D2 people

# total Counting Add one and two
for (item1, item2) in zip(D1, D2):
    T.append(item1+item2)                                   # Add symptoms of all Died & live people

# Calculating Percentages of Symptoms

for i in range(1, len(sym)+1):   
    sympercentageD1.append(D1[i]/D1[0])                        # calculate symptoms percentage of live people


for i in range(1, len(sym)+1):      
    sympercentageD2.append(D2[i]/D2[0])                        # calculate symptoms percentage of Died people

# Total Percentage
for i in range(1, len(sym)+1):     
    sympercentageT.append(T[i]/T[0])                        # calculate symptoms pertange total
    
#people have D1 percentange out of total

D1percentage = totalD1/len(myData)                      # D1 percentage
D2percentage = totalD2/len(myData)                      # D2 percentage


# Contional Probability i-e multiplying with D1

sympercentageD11 = [i * D1percentage for i in sympercentageD1]  # calculating Live person Conditional probability
sympercentageD21 = [i * D2percentage for i in sympercentageD2]  # calculating Died person Conditional probability



# If There is 0 replace it with 0.01

for i in range(0, len(sympercentageD11)):
    if(sum(sympercentageD11) != 0):
        if(sympercentageD11[i] == 0):
            sympercentageD11[i] = 0.01;
 
for i in range(0, len(sympercentageD21)):
    if(sum(sympercentageD21) != 0):
        if(sympercentageD21[i] == 0):
            sympercentageD21[i] = 0.01;       

# Multiplying all conditional Probabilites 
ProbabilityD1 = numpy.prod(sympercentageD11)                   # multiplying all live conditional probability
ProbabilityD1 = ProbabilityD1*D1percentage                # multiplying conditional probability with live percentage

ProbabilityD2 = numpy.prod(sympercentageD21)                   # multiplying all Died conditional probability
ProbabilityD2 = ProbabilityD2*D2percentage                # multiplying conditional probability with Died percentage



# Calculating percentage of D1 and D2

PT = ProbabilityD1+ProbabilityD2                           # total probability
P1 = ProbabilityD1/PT                                        # percentage live
P2 = ProbabilityD2/PT                                        # percentage died

print("Probability of disease 1 is ", P1)
print("Probability of disease 2 is ", P2)

if(P1>P2):
    print("You have Disease 1")
else:
    print("You have Disease 2")



