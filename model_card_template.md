Model Card for Census Income Prediction Model
Model Details

    Developer: Joseph Swiderski
    Model Date: April 2023
    Model Version: 1.0
    Model Type: Random Forest Classifier
    Code: GitHub Repository

Intended Use

    Primary Use: This model is intended for socioeconomic research, specifically to predict the likelihood of individuals earning more than $50K per year based on census data.
    Intended Users: Researchers, Economists, Policy Makers
    Out-of-scope Use Cases: This model is not intended for use in individual-level decision-making processes like hiring, lending, or eligibility for programs/benefits.

Training Data

    Dataset Name: UCI Adult Census Income Dataset
    Source: UCI Machine Learning Repository
    Description: The dataset contains approximately 32,561 instances with 14 attributes, including age, work class, education, occupation, and race. The target attribute is a binary variable indicating whether the individual's income exceeds $50K per year.

Evaluation Data

    Dataset Name: UCI Adult Census Income Dataset (Split for Testing)
    Source: UCI Machine Learning Repository
    Description: The evaluation data is a subset of the UCI Adult Census Income Dataset, specifically set aside for testing the model. It consists of a stratified sample maintaining the overall distribution of the full dataset.

Metrics

    Metrics Used: Accuracy, Precision, Recall, F1-Score
    Model Performance:
        Accuracy: 85%
        Precision: 76%
        Recall: 68%
        F1-Score: 72%

Ethical Considerations

    Fairness and Bias: Analysis indicates potential biases in prediction based on race and gender, inherent in the training data. Caution should be exercised in interpreting the results.
    Privacy: The dataset used is anonymized and publicly available, ensuring no personal information is disclosed.

