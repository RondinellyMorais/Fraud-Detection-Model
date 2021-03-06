# Fraud Detection
![Wellcome](/imagen/fraud.png?raw=True)
[![author](https://img.shields.io/badge/author-rondinelly-red.svg)](https://www.linkedin.com/in/rondinellyoliveiradatascience)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/gallery)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/scikit-learn/badges/version.svg)](https://anaconda.org/conda-forge/scikit-learn)
## 1. Bussines Problem.
<p align="justify"> Let's take Blocker Fraude Company as an example to analyze our business problem. Blocker Fraude Company is a company specialized in the detection of fraud in financial transactions made through mobile devices. The company has a service called “Blocker Fraud” which guarantees the blocking of fraudulent transactions. </p>

<p align="justify"> And the company's business model is of the Service type, with monetization made by the performance of the service provided, that is, the user pays a fixed fee on the success in detecting fraud in the client's transactions. </p>

<p align="justity"> However, Blocker Fraud Company is expanding in Brazil and in order to acquire customers more quickly, it has adopted a very aggressive strategy. The strategy works as follows: </p>

 1. **The company will receive 25% of the value of each transaction that is truly detected as fraud.** 

 2. **The company will receive 5% of the value of each transaction detected as fraud, however the transaction is truly legitimate.** 

 3. **The company will return 100% of the value to the customer for each transaction detected as legitimate, however the transaction is truly a fraud.**

<p align="justity"> With this aggressive strategy, the company assumes the risks of failing to detect fraud and is remunerated for assertively detecting fraud. </p>

## 2. Bussines Assumptions.

 * Currently fraud rates remain at record highs all the world, with total cost of these crimes are around US$42 billion.
 * And 13% of companies and other organizations those who’d experienced a fraud said they’d lost US$50 million-plus.
 * A small proportion of these losses are ever recovered, compromised financial institutions and personal impact for bank clients.
 * The global data protection market, valued at 15 billion US dollars in 2020, is forecast to grow by more than 30 percent between 2020 and 2027 annually, [according to Grand View Research](https://www.grandviewresearch.com/industry-analysis/data-protection-as-a-service-market).
 * Due to the large amount of fraud and large volume of company losses, solutions for detecting fraudulent events become extremely necessary.
 
 ## 3. Solution Strategy
 **Step 01. Data Description** Firstly, we loading the dataset and take overview about columns and rows. </p>
 **Step 02. Data filtering** We checking for missing data in dataset  and checking possible useless columns that do not contain information to modeling.</p>
 **Step 03. Exploratory Data Analysis** We explore the data to find outliers, insights to understand better the data and other points relevant to modeling. </p>
 **Step 04. Data Preparation** Prepare the date so that machine learning models can learn the specific behavior. </p>
 **Step 05. Feature Selection** Selection of the most significant attributes to train model. </p>
 **Step 06. Machine Learning Modelling** Building machine learning train </p>
 **Step 07. Choose the Best Machine Learning Model** Training some machine learning models and choose the model with best performance. </p>
 **Step 08. Convert Model Performance to Bussines Values** Convert the metrics scores of model performance in business practical results. </p>
 **Step 09. Deploy the Model to Production** Publish the model in cloud environment so the other people or services can use the results to improve th bussines decision.</p>
 **Note: We can get the full exploratory data analysis on the notebook**
 [Code | Fraud-Detection-notebook](https://github.com/RondinellyMorais/Fraud-Detection-App/blob/master/Fraud-Detection-notebook.ipynb) 
 
## 4. Top 3 Data Insight
**Hypothese 01** Fraudulent transaction events have an average amount monetary greater than  average non-fraudulent events.</p>
**True** The hypothesis is confirmed, the average monetary value for fraudulent transactions is much higher than the average for non-fraudulent transactions.</p>
**Hypothese 02** The average of the time values that occur between transactions, 'step', for fraudulent events must be less than the observed average for non-fraudulent events.</p>
**False** The average of the time values that occur between transactions for fraudulent events is greater than the average observed for non-fraudulent events.</p>
**Hypothese 03** All types of payment must take place in the event of fraudulent transactions. </p>
**False** The 'CASH_OUT' and 'TRANSFER' are the only forms of payment in fraudulent transaction events. </p>

## 5. Machine Learning Model Applied
Test three type machine learning models: **CatBoostClassifier, RandomForestClassifier and XGBClassifier**.

## 6. Machine Learning Model performance
**CatBoostClassifier:**
The best model found was **CatBoostClassifier** because this model fit the data very well. We can see the values of the evaluation metrics in the tables below.

|Classe |precision | recall | f1-score |       
|-------|--------- | ------ | -------- |       
|   0   | 0.99     | 0.98   |  0.98    |        
|   1   |0.98      | 0.99   |  0.98    |        

|Accuracy |ROC-AUC |
|---------|--------|
|0.98     |0.983   |

Confusion Matrix

|   |0        |1       |
|---|---------|--------|
| 0 |2400     |26      |
| 1 |10       |2500    |

We can think that this model was overfitted, but the **CatBoostClassifier** uses the 'Overfitting detector is active' feature which stops the model's evolution when overfitting occurs.</p>

**RandomForestClassifier:**
The secund model tested was the RandomForesClassifier and we can the values of the evaluation metrics in the tables below. </p>

|Classe |precision | recall | f1-score |       
|-------|--------- | ------ | -------- |       
|   0   | 0.91     | 0.93   |  0.92    |        
|   1   | 0.93     | 0.91   |  0.92    |   

|Accuracy |ROC-AUC |
|---------|--------|
|0.92     |0.9199  |

Confusion Matrix

|   |0        |1       |
|---|---------|--------|
| 0 |2300     |170     |
| 1 |220      |2200    |




**XGBClassifier:**
The XGBClassifier model showed too an impressive  performance in the classification task.
|Classe |precision | recall | f1-score |       
|-------|--------- | ------ | -------- |       
|   0   | 0.93     | 0.99   |  0.96    |        
|   1   | 0.99     | 0.92   |  0.95    |   

|Accuracy |ROC-AUC |
|---------|--------|
|0.95     |0.9541  |

Confusion Matrix

|   |0        |1       |
|---|---------|--------|
| 0 |2000     |28      |
| 1 |200      |2000    |

## 7. Bussines Results.

Lets recap the bussines model: the company will receive 25% of the value of the transactions classified as truly fraud. the company receives 5% of the value of transactions classified as fraud but these transactions are legitimate. The company will pay the customer 100% of the value of transactions classified as legitimate, but these transactions are truly fraudulent. </p>

|Truly Fraud |False Fraud | False No Fraud |      
|------------|----------- | -------------- |      
|25% of gain | 5% of gain | 100% of loss   |   

We must multiply all fraudulent events correctly classified as legitimate by the win percentage (25%) and then subtract all fraudulent events wrongly classified as non-fraudulent multiplied by the loss percentage (100%). Then we owe previous result by the average value of fraudulent transactions and finally we add with average of non-truly non-fraudulent transactions multiplied the amount of fraudulent misclassified transactions and the percentage of gain (5%).</p> 

**PS1:** The average of fraudulent transaction amounts is 1.467.967 and The average of no fraudulent transaction amounts is 178.197.

Summarizing the revenue, loss and profit due to classification  all test data by **CatBoostClassifier**  model
|Truly Fraud      |False Fraud   | False No Fraud |Revenues        | Loss           |  Profit        |
|-----------------|--------------|----------------|----------------|----------------|----------------|
|0.25X2.500x1.467.967|0.05X26x178197| 1x10x1467.967   |917.711.031     |14.679.670      |903.031.361     |

 The **CatBoostClassifier** model was trained using 30% of all fractious records. Then, if we classific all fraudulent transaction records we get revenue, loss and  total profits.
 |Total Revenues  | Total Loss     | Total Profit   |
 |----------------|----------------|----------------|
 |3.059.036.770   |48.883.301      |3.010.153.469   |
 
 remembering that all values are given in local currency where the data was obtained.
 
 Using **RandomForestClassifier**  model, the bussines results will be
 
 |Total Revenues  |Total Loss      |Total Profit    |
 |----------------|----------------|----------------|
 |2.693.625.424   |1.074.432.624   |1.619.192.800   |
 
 And **XGBClassifier** model 
 
 |Total Revenues  |Total Loss      |Total Profit    |
 |----------------|----------------|----------------|
 |2.444.995.806   |977.666.022     |1.467.329.784   |
 
## 8. Conclusion.
Based on exploratory data analysis and machine learning models, we can reach the following conclusions about business strategyod Blocked Fraud Company. </p>
* The model with best peformance was **CatBoostClassifier**.
* the ROC-AUC metric shows that this model has a reliability around **98%**.
* Using  **CatBoostClassifier** model to classific all fraud records we get **3.059.036.770** of profit in local currency.
* The profit spect is the around **3.010.153.469** in local currency.
*  In case the model not be better then the random predictions, we expect that Blocked Fraud Company will have a loss of about **5.416.798.230** in local currency.</p>
**We simulate the detection of fraudulent transactions by selecting dataset features through a simple application, link below.** 
[ Fraud-Detection-App.py](https://share.streamlit.io/rondinellymorais/fraud-detection-app/Fraud-Detection-App.py)
## 9. Lessons Learned.
The main points learned in this task were:
* The high performance of the machine learning model is essential for the company to make good profits.
* Classification problems where classes are too unbalanced significantly affect the prediction model. therefore we must balance the classes.
* An exploratory analysis of basic data can provide key insights.

## 10. Next Steps to Improve.
* To improve the performance and reliability of machine learning models, new datasets can be used as a test.
* Always is possible make hyperparameter tunning and improve your models.
* Apply these models to new types of business problems.
