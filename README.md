# Employee Retention Prediction

This project predicts whether an employee will stay or leave a company based on various features such as education, city, payment tier, age, and more. The model is built using a Random Forest Classifier and includes preprocessing steps like scaling numerical features and one-hot encoding categorical features.

---

## Features

- **Education**: Employee's highest degree.
- **City**: City where the employee works.
- **PaymentTier**: Payment tier (1 = Low, 2 = Medium, 3 = High).
- **Age**: Employee's age.
- **Gender**: Employee's gender.
- **EverBenched**: Whether the employee has been inactive (benched).
- **ExperienceInCurrentDomain**: Years of experience in the current domain.
- **YearsInCompany**: Total years the employee has been with the company.
- **TenureGroup**: Duration in the current role.

---

## Dataset

The dataset used for this project is `Cleaned_Employee.csv`. It contains the following columns:
- `LeaveOrNot`: Target variable (1 = Leave, 0 = Stay).
- Features: `Education`, `City`, `PaymentTier`, `Age`, `Gender`, `EverBenched`, `ExperienceInCurrentDomain`, `YearsInCompany`, `TenureGroup`.

---

## Steps

1. **Data Preprocessing**:
   - One-hot encoding for categorical features.
   - Standard scaling for numerical features.

2. **Model Training**:
   - Random Forest Classifier with a maximum depth of 10 and 100 estimators.

3. **Evaluation**:
   - Classification report.
   - Confusion matrix.
   - Accuracy score.
   - Stratified cross-validation.

4. **Model Saving**:
   - The trained model is saved as `final_model.pkl` using `joblib`.

---

## Results

- **Classification Report**:
  Provides precision, recall, and F1-score for each class.
- **Confusion Matrix**:
  Displays the number of true positives, true negatives, false positives, and false negatives.
- **Accuracy**:
  - Training Accuracy: ~90%
  - Test Accuracy: ~85%
- **Cross-Validation**:
  - Mean Accuracy: ~85%
  - Standard Deviation: ~2%

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Yusef8812/CC105-django.git
   cd employee-retention-prediction
