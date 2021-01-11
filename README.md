# Disease-Prediction
  Make a module of Baysain inference which you can import it in your own code
  
  
  Make another File to use the above module
 Class has following functions
 *  .Clean (which find all NAN in data and drop that row from whole Data).
 *  .Train (which Find the probabilities of all Disease given following Symptoms, 
      Train Find all diseases probabilities with symptoms)
 *  .predict(Which tell the Disease having greater Probability,
      Predict Tell disease name having highest probability)

Following is Explanation of baysain inference with Example 


**Bayes Rule:**


Bayes’ Theorem finds the probability of an event occurring given the probability of another event that has already occurred. Bayes’ theorem is stated mathematically as the following equation:


         P(y|X) = P(X|y)P(y)
                    P(X)
             
        X = [x1, x2 ... xn]
  
  
        P(y|x1, x2 ... xn) = P(x1|y)P(x2|y)...P(xn|y)*P(y)
                                 P(x1)P(x2)...P(xn)
  
  
  
**Example:

 Here is corona and viral infection symptoms Table 
  
| Disease | Total | Fever | Tastelessness | Fatigue |
| :--- | :----: | :---: | :----: | :---: |
| Corona | 116 | 95 | 49 | 81 |
| viral Infection | 26 | 11 | 2 | 7 |

After analysing Data, calculating Symptoms Percentages
| Disease | Total | Fever | Tastelessness | Fatigue |
| :--- | :----: | :---: | :----: | :---: |
| Corona | 0.81 | 0.66 | 0.33 | .55 |
| viral Infection | 0.19 | 0.15 | 0.08 | 0.13 |



Then calculate conditional Probabilities of Corona or Viral Infection symptoms and put it in Bayes Formula



> P(Corona|Fever,Tastelessness,Fatigue) = (0.66)(0.34)(0.55)(0.81)/
                                           P(x1)P(x2)...P(xn)



> P(Corona|Fever,Tastelessness,Fatigue) = 0.099


Same Calculate for Viral Infection 


> P(Viral infection|Fever,Tastelessness,Fatigue) = 0.00187



These numbers can be converted into a probability by making the sum equal to 1 (normalization):
S0, 



>  P(Corona|Fever,Tastelessness,Fatigue) = 0.099/0.099+0.00187


> P(Viral infection|Fever,Tastelessness,Fatigue) = 0.00187/0.099+0.00187



> P(Corona|Fever,Tastelessness,Fatigue) = 0.98


>  P(Viral infection|Fever,Tastelessness,Fatigue) = 0.018

 So doing bayseain inference we know which disease have greater probability, So we predict greater probability disease which is corona in this Case




 If you want to learn more about Baysain inference, you can [learn](https://www.geeksforgeeks.org/naive-bayes-classifiers/#:~:text=Naive%20Bayes%20classifiers%20are%20a,is%20independent%20of%20each%20other.) from here
