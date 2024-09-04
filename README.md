
# ML Project - Credit Score Classification (EN)

My first personal Machine Learning project. 04/2024

Pandaland ML Project: Credit Score Classification

Introduction

In the world of finance, accurately classifying clients based on their creditworthiness is essential for optimizing loan decisions. Pandaland, a leading financial institution, was facing inefficiencies in their manual credit scoring process. To address this, Jaime Inchaurraga led the development of an automated solution using machine learning to streamline client credit classification, improving the decision-making process and reducing costs.
Problem Statement

Pandaland required a robust, automated system to replace their manual classification methods, which consumed extensive resources. The goal was to develop a multi-class classification model that could categorize clients into one of three credit score groups: Poor, Standard, and Good, allowing for more efficient loan approvals.
Dataset

The dataset used in this project consisted of 100,000 client records and included 28 variables. The following preprocessing steps were applied:
Missing Data Imputation: Handled using median for numerical variables and mode for categorical variables.
Outlier Detection: Extreme values were identified and managed using quantiles.
Data Cleaning: Correction of errors such as negative values and errant categories.
Feature Engineering: Essential transformations like encoding categorical variables, feature scaling, and dimensionality reduction.
Modeling Approach

Various models were tested to determine the best fit for the multi-class classification problem, including:
Logistic Regression
Naive Bayes
Random Forest
XGBoost
Initial testing highlighted overfitting and underfitting issues with some models. However, Random Forest proved the most promising, offering a balance between model complexity and accuracy after parameter tuning.
Key Results

Random Forest: Achieved a training accuracy of 95% and test accuracy of 79% after applying cross-validation and synthetic data balancing techniques (SMOTE).
Class Performance:
Class 0 (Poor): High precision, often confused with Class 1.
Class 1 (Standard): Best model performance, with minimal confusion.
Class 2 (Good): Low false negatives, rarely confused with other classes.
Conclusion

This project successfully developed a machine learning model to automate credit score classification for Pandaland. While the model provides solid performance, particularly for Class 1 (Standard), future work will focus on further reducing overfitting and improving the classification accuracy for Class 0 and Class 2.


Directory:
![Credit Score Flowchart](ppt/flujograma%20directorio%20credit%20score%20classification.png)

