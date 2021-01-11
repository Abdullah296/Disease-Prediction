from baysianClasifier import BayesianClassifier
import sys
import pandas

myClasifier = BayesianClassifier()

try:
    myClasifier.getData("../DataSet/Training.csv", ["n/a", "na", "--"], ',')
except:
    print("file not found")
    sys.exit()

print("Cleaning data ...")
myClasifier.cleanGivenData()

print("training on given data ...")
myClasifier.train([132], list(range(0, 132)))

testingFile = sys.argv[1]

testingSymptoms = sys.argv[2]
print(testingSymptoms)
try:
    testingdata = pandas.read_csv(testingFile)
except:
    print("Enter a correct file name")
    sys.exit()

# getting all the symptoms from the mentioned row
userIn = int(testingSymptoms)
index = 0
testingSymptoms = []
for i in list(testingdata.iloc[userIn, :]):
    # if status is 1 add to list
    if i == 1:
        testingSymptoms.append(testingdata.columns[index])
    index = index + 1

# predicting for given symptoms
Disease =myClasifier.predict(myClasifier.runTests(testingSymptoms))
print("")
print(Disease)
print("")
print("You can find medicine of your disease using the link below")

from googlesearch import search

for i in search(Disease +" Medicine" ,   lang='en', num=1, start=0, stop=1, pause=2.0):
        print (i)
        
print("")
print("You can find Doctor using Link below")

for i in search(Disease +" Doctor in Islamabad" ,   lang='en', num=1, start=0, stop=1, pause=2.0):
        print (i)