## End to end Machine Learning Project

* Created a tool that estimates data science salaries (MAE ~ $ 14K) to help data scientists / data analyst / data engineers negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium 
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Random Forest Regressor, Adaboost, Xgboost and many other using GridsearchCV to reach the best model.
* Built a client facing API using flask (CLient/End-User can use Front End UI and/or shared drive location to put theor test data)

## Code and Resources Used
* Python Version: 3.11
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* For Web Framework Requirements: pip install -r requirements.txt
* Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium

## Data Ingestion
* Client can use a Front End website to enter customer data to predict churn
* Client can also use a shared drive location to put the raw bulk data. The Machine Learning Pipeline would automatically run the pre-processing tasks and give the ouput in a shared location.

## Data Validation
* I used python scripts to validate the raw data sent by client.
* This is done by verifying the __Name of File__ and __Number of Columns__ in the file. More such checks can be added if needed
* Data that doesn't pass the validation check goes to __folder__ : bad_data_archived , while data that passes all checks goes to __folder__ : good_data

## Data Logging and Custom Exception handling
* Every step is logged and a separate folder is created for logging. Such process can help identify problems in the code
* Every error is logged in the logger file with a Custom Error Handling exception message


## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

1. Job title
2. Salary Estimate
3. Job Description
4. Rating
5. Company
6. Location
7. Company Headquarters
8. Company Size
9. Company Founded Date
10. Type of Ownership
11. Industry
12. Sector
13. Revenue
14. Competitors

## Data Cleaning 
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

* Parsed numeric data out of salary
* Made column for avg salary out min and max salary
* Removed rows without salary
* Parsed rating out of company text
* Cleaned up company state and headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
    1. Python
    2. R
    3. Excel
    4. AWS
    5. Spark
    6. Column for simplified job title and Seniority

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. you can find more details in the assets file


## Model Training
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

Finally, I decided to use Random Forest Regressor

## Front End API
I also developed a front end api use flask
## how to run
```
python app.py
```
then click on the url, you can see the homepage, then enter /predict after the url, you can enter several infos, then the model can give you the predicted salary based on the training results

