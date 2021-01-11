from baysianClasifier import BayesianClassifier

myClasifier = BayesianClassifier()
myClasifier.getData("../DataSet/Training.csv", ["n/a", "na", "--"], ',')
myClasifier.cleanGivenData()
myClasifier.train([132], list(range(0, 132)))
results = myClasifier.runTests([ "red_sore_around_nose"])
print(myClasifier.predict(results))
