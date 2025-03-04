# Metadata - Student Performance Visualization

## Dataset Overview

- **Source:** Kaggle - Students Performance in Exams Dataset
- **File Name:** StudentsPerformance.csv
- **Number of Records:** 1000 students
- **Number of Columns:** 8

### Column Descriptions

| Column Name                    | Description |
|--------------------------------|-------------|
| gender                         | Student's gender (`male` or `female`). |
| race/ethnicity                 | Categorical group assignment (Group A, B, C, etc.). |
| parental_level_of_education    | Parent's highest education level. |
| lunch                          | Type of lunch received (`standard` or `free/reduced`). |
| test_preparation_course        | Completion status of test prep course (`completed` or `none`). |
| math_score                     | Final math score (0-100). |
| reading_score                  | Final reading score (0-100). |
| writing_score                  | Final writing score (0-100). |

---

## Preprocessing Summary

- Column names were standardized to lowercase and spaces were replaced with underscores.
- All rows with missing values (if any) were removed.
- All score columns (math, reading, writing) were converted to numeric.
- Categorical columns (like gender, parental education, lunch type, etc.) were standardized to lowercase for consistency.
- Cleaned data was saved to:
    ```
    data/processed/cleaned_student_data.csv
    ```

---

## Key Assumptions

- All data is assumed accurate as provided in the original dataset.
- No external data sources were used.
- Analysis focuses mainly on **math scores**, in line with assignment requirements.
- No extreme outliers were removed, as the dataset was considered generally clean.