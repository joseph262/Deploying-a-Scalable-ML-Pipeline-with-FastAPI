Model Details

    Developer: Joseph Swiderski
    Model Date: April 2023
    Model Version: 1.0
    Model Type: Random Forest Classifier
    Code Availability: Available on GitHub Repository

Intended Use

    Primary Use:
        For socioeconomic research, aimed at predicting the probability of individuals earning over $50K annually based on census data.
    Intended Users:
        Targeted at Researchers, Economists, and Policy Makers.
    Out-of-scope Use Cases:
        Not recommended for individual-level decisions such as hiring, lending, or determining program/benefit eligibility.

Training Data

    Dataset Name: UCI Adult Census Income Dataset
    Source: UCI Machine Learning Repository
    Description:
        The dataset includes around 32,561 instances with 14 attributes, including age, work class, education, etc. The key target attribute is income exceeding $50K per year.

Evaluation Data

    Dataset Name: UCI Adult Census Income Dataset (Split for Testing)
    Source: UCI Machine Learning Repository
    Description:
        This is a subset of the main dataset, specifically reserved for testing the model. It represents a stratified sample.
    Evaluation Data Percentage:
        The percentage of data used for evaluation is 80% training and 20% testing.

Metrics

    Metrics Used: Accuracy, Precision, Recall, F1-Score
    Model Performance:
        Accuracy: 85%
        Precision: 76%
        Recall: 68%
        F1-Score: 72%

Ethical Considerations

    Fairness and Bias:
        There is evidence of potential biases based on race and gender in the predictions, reflecting the training data's inherent biases.
    Privacy:
        The dataset is anonymized and publicly accessible, safeguarding personal information.

Caveats and Recommendations

    Model Limitations:
        The model's predictions are based on historical data, which may not accurately represent current or future trends.
        Bias in the data can lead to skewed predictions, particularly affecting underrepresented groups.
    Usage Recommendations:
        Users should interpret the model's predictions in the context of its limitations and inherent biases.
      
        Regular updates and re-evaluations of the model are recommended to ensure its relevance and accuracy.
        
