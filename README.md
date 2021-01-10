# Disease-Prediction
  Make a class of Baysain inference which you can import it in your own code
  Make another File to use the above file functions
 Class has following functions
 *  .Clean (which find all NAN in data and drop that row from whole Data).
 *  .Train (which Find the probabilities of all Disease given following Symptoms )
 *  .predict(Which tell the Disease having greater Probability)


###Bayes Rule:
Bayes’ Theorem finds the probability of an event occurring given the probability of another event that has already occurred. Bayes’ theorem is stated mathematically as the following equation:


  P(y|X) = P(X|y)P(y)
              P(X)
              
              
              
              
  X = [x1, x2 ... xn]
  
  
  P(y|x1, x2 ... xn) = P(x1|y)P(x2|y)...P(xn|y)*P(y)
                               P(x1)P(x2)...P(xn)
  
  
            
            
| Disease | Total | Fever | Tastelessness | Fatigue |
| :--- | :----: | :---: | :----: | :---: |
| Corona | 116 | 95 | 49 | 81 |
| viral Infection | 26 | 11 | 2 | 7 |


 If you want to learn Baysain inference, you can [learn](https://www.geeksforgeeks.org/naive-bayes-classifiers/#:~:text=Naive%20Bayes%20classifiers%20are%20a,is%20independent%20of%20each%20other.) from here
