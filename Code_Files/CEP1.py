import pandas as pd
import numpy 

#Row you want to Predict
TT = 4              #which row you want to predict from testing.csv
F = 41              # Total Disease you want to add

sym = []            # Symptoms you want to analyse

# Data cleaning

missing_values = ["n/a", "na", "--"]                  
myData1 = pd.read_csv("testing.csv", na_values = missing_values)

myData1 = numpy.array(myData1)

Test = myData1[TT,:]

for i in range(0,len(Test)):
    if(Test[i] == 1):
        sym.append(i+1)
print(sym)      # Sym contains Row number which new patient have symptoms


myData = pd.read_csv("Dataset.csv", na_values = missing_values)

# Data cleaning of training data
FindingNAN = myData.isnull()

dropingrow = []

NAN_index = FindingNAN.any(axis=1)                              # finding index of NAN row

for i in range(0,len(myData)):
    if(NAN_index[i] == True):
         dropingrow.append(i)
         
myData = myData.drop(dropingrow)        # Drop rows which contain NAN
##################################33

myData = numpy.array(myData)

# converting String into number

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



Dis = list(myData[:, 0])
One = []

for i in range(0, len(Dis)):
    One.append ( Disease[Dis[i]])

myData[:, 0]=One;                                               # converted it into Number


# some list needed in code

D = []
totalD = []
HaveD = []
D1 = []
sympercentageD1 = []
sympercentageT = []
Dpercentage = []
sympercentage1 = []
P = []
ProbabilityD = []

for i in range(1,F+1):
    totalD.append( list(myData[0:, 0]).count(i))                    # TotalD contains how many people have Disease 1 to N

#Seperating Attributes of all diseases  

for i in range(1,F+1):
    HaveD.append( myData[myData[:, 0] == i])                        # 3d list contain Disease 1 Symptoms to disease N


# Counting Symptoms
 
for a in range(0,F):
    D1 = []
    D1.append(totalD[a])
    for b in sym:
        Extra = []
        for i in range(0, 120):
            Extra.append(HaveD[a][i][b])
        D1.append(Extra.count(1))
    D.append(D1)                                                    # count Symptoms of Disease 1 to Disease N


T = [ sum(x) for x in zip(*D) ]         # Total people having these symptoms


# Calculating Percentage of Symptoms

for a in range(0,F):
    sympercentageD = []
    for i in range(1, len(sym)+1):   
        sympercentageD.append(D[a][i]/D[a][0])
    sympercentageD1.append(sympercentageD)                  # Calculating percentage of all symptoms
    
for i in range(1, len(sym)+1):     
    sympercentageT.append(T[i]/T[0])                        # total Percentage 


for a in range(0,F):
    Dpercentage.append(D[a][0]/T[0])                     # each disease probability

# Calculating Conditional Probability

for a in range(0,F):
    sympercentage = []
    sympercentage = [i * Dpercentage[a] for i in sympercentageD1[a]]    
    sympercentage1.append(sympercentage)                # Multiply each Symptoms Percentage with disease probability

# If 0 replace it with 0.0001 so Error don't occur

for a in range(0,F):    
    for i in range(0, len(sym)):
        if(sum(sympercentage1[a]) != 0):
            if(sympercentage1[a][i] == 0):
                sympercentage1[a][i] = 0.0001;

# Muliplying all Conditional probabilities

for a in range(0,F):  
    ProbabilityD1 = numpy.prod(sympercentage1[a])                   # multiplying all live conditional probability
    ProbabilityD.append( ProbabilityD1*Dpercentage[a])

#Calculating Total Probability
    
PT = sum(ProbabilityD)


for a in range(0,F):
    P.append(ProbabilityD[a]/PT )
    print("Probability of disease", a+1 ," is ", P[a])

print("You have Disease ", P.index(max(P))+1)
Getdisease =[k for k,v in Disease.items() if v == P.index(max(P))+1]
print("You are diagonose with ", Getdisease[0])   


 
