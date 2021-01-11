import pandas as pd


class BayesianClassifier:
    """This class contain all required methods for reading, cleaning
    calculating initial probabilities and predicting new incoming symptoms
    This class is the coded implementation of Bayesian Rule
    ATTRIBUTES:

    Functions:

    """
    def __init__(self):

        # divided data into sets based on disease in the data set
        self.processedData = {}
        # processedData = {
        #    disease1 = {
        #        all symptoms
        #    }
        #    disease2 = {
        #        all symptoms
        #    }
        # }

        # a data structure to store all disease and there respective counts of symptoms
        # i.e. how many people have symptom 1 from all the people having disease 1
        # and so on
        self.countedData = {}
        # countedData = {
        #     "disease0" : {
        #         "Symptom0": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         "Symptom1": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         .
        #         .
        #         .
        #         "SymptomN": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #     }
        #     .
        #     .
        #     .
        #     "diseaseN" : {
        #         "Symptom0": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         "Symptom1": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         .
        #         .
        #         .
        #         "SymptomN": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #     }
        # }

        # main pandas data frame to store all the data read from given data file
        self.dataFrame = pd.DataFrame

        # a list to store all columns number which have diseases in them
        self.statusColumns = []

        # a list to store all the columns number which have symptoms in them
        self.symptomsColumns = []

        # a pandas data frame to store all the columns which have diseases in them
        self.status = pd.DataFrame

        # a pandas data frame to store all the columns which have symptoms in them
        self.symptoms = pd.DataFrame

        #
        self.diseaseList = []

        # to store all the initial probabilities
        self.diseaseProbabilityList = {}
        # diseaseProbabilityList = {
        #              disease0: probability,
        #              disease1: probability,
        #              .
        #              .
        #              .
        #              diseaseN: probability,
        # }

    def getData(self, fileName, missingValues, sep):
        """
        this function reads the given data file for training and stores the read data in 'self.dataFrame'
        in pandas dataframe format it also replace the missing data with 'NaN', data file should be in CSV format

        :param fileName:
        file name with path in string format eg. '../training.csv'
        :param missingValues:
        a list of all the missing values which could be found in given file eg. ['na', '--']
        :param sep:
        character by which different values in given data file is separate eg. spe = ','
        :return:
        it returns nothing. it read data from the given file and stores that data in pandas data frame
        in 'self.dataFrame'
        """
        # reading given file
        self.dataFrame = pd.read_csv(fileName, na_values=missingValues, sep=sep)

    def cleanGivenData(self):
        """
        this function cleans the read data by 'self.getData()', replace or completely remove
        that row which contain 'NaN' values in the data and update data in 'self.dataFrame'
        with cleaned data
        :return:
        it returns nothing,
        but after cleaning data it update the 'self.dataFrame' with cleaned data
        """
        # dropping all the rows which contain any 'NaN' values
        self.dataFrame = self.dataFrame.dropna()

    def train(self, statusColumns, symptomsColumns):
        """
        this function trains the classifier and stores the trained data into there respective
        class attributes.
        This function divides the data set into two groups 1st is diseases, 2nd one is symptoms
        on the bases of given parameters. Than counts the respective values in the data set which
        may be useful in calculating different probabilities in future during prediction i.e. probabilities
        of having a disease from all the given diseases in the data set.

        :param statusColumns:
        a list containing integers, of column numbers in the given data set which contain diseases i.e [1, 2, 3]
        :param symptomsColumns:
        a list containing integers, of column numbers in the given data set which contain symptoms i.e [1, 2, 3]
        :return:
        this function does not return any thing.
        """
        # setting variables
        self.statusColumns = statusColumns
        self.symptomsColumns = symptomsColumns

        # separating data frame into status & symptoms
        self.status = self.dataFrame.iloc[:, self.statusColumns]
        self.symptoms = self.dataFrame.iloc[:, self.symptomsColumns]

        # getting all the unique value in status columns
        # so that could be divided (1st division)
        # status[status.columns[0]].unique() = list of all the unique values in status columns (disease)
        # all the different disease in given data
        self.diseaseList = self.status[self.status.columns[0]].unique()

        # arranged data structure to store all the counts

        # separating data on the bases of uniqueStatusValues & arranging
        # for eachStatusColumn in statusColumns:
        #    # for every selected status column
        #    for eachUniqueValue in uniqueStatusValues:
        #        processedData[eachUniqueValue] = df[status.columns[eachStatusColumn]].count(eachUniqueValue)

        # df.columns[statusColumns][0] = exact column header to select
        # df[df[df.columns[statusColumns][0]] == 'Fungal infection']
        # to extract all the rows which have 'Fungal infection' in it
        for eachDisease in self.diseaseList:
            self.processedData[eachDisease] = self.dataFrame[self.dataFrame[self.dataFrame.columns[self.statusColumns][0]] == eachDisease]

        # After this processing processedData would be like
        # processedData = {
        #    disease1 = {
        #        all symptoms
        #    }
        #    disease2 = {
        #        all symptoms
        #    }
        # }

        # now we have to count the data respectively
        for eachDisease, symptomsList in self.processedData.items():  # traversing over all Disease

            # for all symptoms of select Disease
            for eachSymptom in symptomsList:
                # getting unique value from selected symptoms column (eachSymptom)
                uniqueValuesInSymptomList = self.processedData[eachDisease][eachSymptom].unique()
                # uniqueValuesInSymptomList is a list containing all unique value

                # for all Unique values of selected symptoms
                for eachUniqueValue in uniqueValuesInSymptomList:

                    # checking weather disease(key) exist or not
                    # if not add one & initial with empty dict
                    if eachDisease not in self.countedData.keys():
                        self.countedData[eachDisease] = {}
                    # checking weather Symptom(sub-key) exist or not
                    # if not add one & initial with empty dict
                    if eachSymptom not in self.countedData[eachDisease].keys():
                        self.countedData[eachDisease].update({eachSymptom: {}})
                    # checking weather unique value(sub-sub-key) exist or not
                    # if not add one & initial with 0 (as initial count)
                    if eachUniqueValue not in self.countedData[eachDisease][eachSymptom].keys():
                        self.countedData[eachDisease][eachSymptom].update({eachUniqueValue: 0})

                    # counting and updating the count in countedData
                    self.countedData[eachDisease][eachSymptom][eachUniqueValue] = list(
                        self.processedData[eachDisease][eachSymptom]).count(eachUniqueValue)

        # after this processing countedData will be like
        # countedData = {
        #     "disease0" : {
        #         "Symptom0": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         "Symptom1": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         .
        #         .
        #         .
        #         "SymptomN": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #     }
        #     .
        #     .
        #     .
        #     "diseaseN" : {
        #         "Symptom0": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         "Symptom1": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #         .
        #         .
        #         .
        #         "SymptomN": {
        #             "status0":count,
        #             "status1":count,
        #             .
        #             .
        #             .
        #             "statusN":count,
        #         }
        #     }
        # }

        # Now, initial probabilities have to be calculated
        # for a single Disease
        # P(Disease) = (number of entries of that Disease)/(total entry in th data)

        # we have a list of all the disease in "self.diseaseList"

        # len(status) = total entries in th data
        # total entry in data set
        totalEntries = len(self.status)

        # traversing for all listed diseases in "diseaseList" & calculating probabilities
        for eachDiseases in self.diseaseList:
            # list(status)[0] gives the header value which is passed to the data frame to select that column
            # list(status[list(status)[0]]).count(eachDiseases) = number of entries of that Disease(eachDiseases)
            # len(status) = total entries in th data

            # calculating probability
            probability = list(self.status[list(self.status)[0]]).count(eachDiseases) / totalEntries

            # storing it
            self.diseaseProbabilityList[eachDiseases] = probability

    def getCount(self, disease: str, symptom: str, status: int) -> float:
        """
        It search tha countedData and returns the count for given parameters.
        :param disease:
        disease in string format for which count is required.
        :param symptom:
        for a selected disease which symptom is to select to get respective count.
        :param status:
        for a selected disease & symptom which status (yes or not) is to be counted
        :return:
        it returns the count for the selected attributes if not found returns the minimum number
        """
        # this functions returns the count by searching counted data
        if status in self.countedData[disease][symptom].keys():
            return self.countedData[disease][symptom][status]
        else:
            # minimum number possible
            return 0.000000000000000001

    def runTests(self, givenSymptomsList: list) -> dict:
        """
        it takes a list of all the symptoms by which patient is effected, calculate all the probabilities
        and returns the dict containing all the disease with there respective probabilities

        :param givenSymptomsList:
        A list of symptoms patient is effected with i.e. ["fiver", "vomiting"]
        :return:
        a dict containing all the disease with there respective probabilities
        """

        # an empty dict which will temporarily store all the probabilities
        # by which it could be predicted which is th most likely disease
        probabilityResultsList = dict()

        for eachDisease in self.diseaseList:
            # initializing to avoid any error in calculation
            probability = 1
            # calculating probability of having a disease based in symptoms
            for eachGivenSymptom in givenSymptomsList:
                probability = probability * (self.getCount(eachDisease, eachGivenSymptom, 1) / len(
                    self.status[self.status[list(self.status)[0]] == eachDisease]))

                # multiplying the probability of having disease P(disease)
                probability = probability * self.diseaseProbabilityList[eachDisease]

                # storing the data
                probabilityResultsList[eachDisease] = probability

        # finding sum of all the calculated probability
        prob_sum = 0
        for eachDisease, diseaseProbability in probabilityResultsList.items():
            prob_sum = prob_sum + diseaseProbability

        # dividing all calculated probabilities to there sum for normalization
        for eachDisease, diseaseProbability in probabilityResultsList.items():
            probabilityResultsList[eachDisease] = diseaseProbability / prob_sum

        # returning the calculated probabilities
        return probabilityResultsList

    def mostProbably(self, probabilityResultsList:dict) -> str:
        """
        it takes results from self.runTests and returns the most likely disease.
        :param probabilityResultsList:
        a dict with all disease like {disease: probability}
        :return: most likely disease
        """

        # making decision what is the most probability the disease
        disease = str()
        lastProbability = int()

        for eachDisease, diseaseProbability in probabilityResultsList.items():
            # printing results
            print(f"For disease {eachDisease} calculated probability is: {diseaseProbability}")
            # making decision
            if lastProbability < diseaseProbability:
                lastProbability = diseaseProbability
                disease = eachDisease
        return disease



