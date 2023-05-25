# Phishing-url-detection
Project related to machine learning to detect phishing detection


This is an End-to-End Machine Learning Project which focuses on phishing websites to classify phishing and legitimate ones.
Particularly, We focused on content-based features like html tag based features.

inputs
csv files of phishing and legitimate URLs
verified_online.csv --> phishing websites URLs from phishtank.org
tranco_list.csv --> legitimate websites URLs from tranco-list.eu
general flow
Use csv file to get URLs
Send a request to each URL and receive a response by requests library of python
Use the content of response and parse it by BeautifulSoup module
Extract features and create a vector which contains numerical values for each feature
Repeat feature extraction process for all content\websites and create a structured dataframe
Add label at the end to the dataframes | 1 for phishing 0 for legitimate
Save the dataframe as csv and structured_data files are ready!
Check "structured_data_legitimate.csv" and "structured_data_phishing.csv" files.
After obtaining structured data, you can use combine them and use them as train and test data
You can split data as train and test like in the machine_learning.py first part.
Then We implemented different ML models:
Support Vector Machine
Gaussian Naive Bayes
Decision Tree
Random Forest
AdaBoost
You can obtain the confusion matrix, and performance measures: accuracy, precision, recall
Finally, We visualized the performance measures for all models.
Random Forest is the best for my case.
