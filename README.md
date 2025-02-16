The code in the provided file performs the following steps to predict customer churn using a Decision Tree model:

1. **Import Libraries**:
   - `pandas` for data manipulation.
   - `matplotlib.pyplot` and `seaborn` for data visualization.
   - `sklearn` for machine learning tasks.

2. **Load Dataset**:
   - Load the dataset from a CSV file using `pd.read_csv`.

3. **Initial Data Exploration**:
   - Display the first few rows of the dataset.
   - Check the shape of the dataset.
   - Check column data types and missing values.
   - Display summary statistics for numerical columns.
   - Check unique values in each column.

4. **Visualize Churn Distribution**:
   - Plot a countplot to visualize the distribution of the target variable `Churn`.
   - Calculate and print the percentage of churned vs. retained customers.

5. **Data Preprocessing**:
   - Convert the `Churn` column to numeric (0 for "No", 1 for "Yes").
   - Identify categorical and numerical columns.
   - Plot a heatmap to show correlations between numerical features.
   - Check for missing values.

6. **Feature Engineering**:
   - Apply label encoding to categorical columns.

7. **Split Data into Train and Test Sets**:
   - Define input features (`X`) and target (`y`).
   - Split the data into training (80%) and testing (20%) sets using `train_test_split`.

8. **Train Decision Tree Model**:
   - Initialize and train a `DecisionTreeClassifier`.
   - Make predictions on the test set.
   - Evaluate the model using accuracy, classification report, and confusion matrix.
   - Plot the decision tree.

9. **Feature Importance**:
   - Calculate and display feature importance scores.
   - Plot the feature importance.

10. **Hyperparameter Optimization using Grid Search**:
    - Define a hyperparameter grid.
    - Initialize and fit a `GridSearchCV` to find the best parameters.
    - Train a new Decision Tree model with the optimized parameters.
    - Evaluate the optimized model.

11. **Compare Initial and Optimized Models**:
    - Compare the accuracy of the initial and optimized models.

This code provides a comprehensive workflow for loading, exploring, preprocessing, training, and evaluating a machine learning model for customer churn prediction.
