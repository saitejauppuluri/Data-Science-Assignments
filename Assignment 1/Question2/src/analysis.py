import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

"""
This script reads cleaned student performance data and creates 5 visualizations to better understand the data.

1. Math Score Distribution - This plot shows how all students scored in math. It helps us see if most students are doing well or struggling. Without this, we would have to go through hundreds of rows to understand overall performance.
2. Parental Education vs Math Score - This shows if students with more educated parents get better math scores. It helps us see the connection between family background and student success.
3. Lunch Type vs Math Score - This checks if students who get free or reduced lunch score differently from those with standard lunch. It helps us see if economic factors affect performance.
4. Test Preparation vs Math Score - This compares students who took a test preparation course with those who didn’t. It helps us see if the prep course actually helps students score better.
5. Gender vs Math Score - This compares average math scores between male and female students. It helps us see if there is any performance gap between genders.

These visualizations make it easier to spot patterns, compare groups, and find what factors might influence student performance, which would be much harder if we only looked at raw numbers.
"""

#paths
CLEANED_PATH = "../data/processed/cleaned_student_data.csv"
PLOTS_FOLDER = "../analysis/plots"
RESULTS_PATH = "../analysis/results.md"

os.makedirs(PLOTS_FOLDER, exist_ok=True)

def plot_math_score_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['math_score'], kde=True, color='skyblue')
    plt.title("Distribution of Math Scores")
    plt.xlabel("Math Score")
    plt.ylabel("Count")
    plt.grid(True)
    plt.savefig(f"{PLOTS_FOLDER}/math_score_distribution.png")
    plt.close()

def plot_parent_education_vs_math_score(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='parental_level_of_education', y='math_score', data=df, palette='Set2')
    plt.title("Parental Education Level vs Math Score")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f"{PLOTS_FOLDER}/parent_education_vs_math_score.png")
    plt.close()

def plot_lunch_vs_math_score(df):
    plt.figure(figsize=(6, 6))
    sns.barplot(x='lunch', y='math_score', data=df, palette='pastel')
    plt.title("Average Math Score by Lunch Type")
    plt.grid(True)
    plt.savefig(f"{PLOTS_FOLDER}/lunch_vs_math_score.png")
    plt.close()

def plot_test_prep_vs_math_score(df):
    plt.figure(figsize=(6, 6))
    sns.boxplot(x='test_preparation_course', y='math_score', data=df, palette='muted')
    plt.title("Test Preparation Course vs Math Score")
    plt.grid(True)
    plt.savefig(f"{PLOTS_FOLDER}/test_prep_vs_math_score.png")
    plt.close()

def plot_gender_vs_math_score(df):
    plt.figure(figsize=(6, 6))
    sns.barplot(x='gender', y='math_score', data=df, palette='coolwarm')
    plt.title("Average Math Score by Gender")
    plt.grid(True)
    plt.savefig(f"{PLOTS_FOLDER}/gender_vs_math_score.png")
    plt.close()

def generate_summary(df):
    avg_math = df['math_score'].mean()
    median_math = df['math_score'].median()

    summary = f"""
    # Student Performance - Analysis Summary

    ## Key Observations

    - Average Math Score: {avg_math:.2f}
    - Median Math Score: {median_math:.2f}

    ---

    ## Visualizations and Analysis

    ### 1. Distribution of Math Scores
    - **File:** math_score_distribution.png
    - Most students score between 60 and 80.
    - There are a few students with much lower scores, but overall performance is fairly balanced.

    ---

    ### 2. Parental Education Level vs Math Score
    - **File:** parent_education_vs_math_score.png
    - Students whose parents have higher education (college degree or higher) tend to have slightly better math scores.
    - However, the differences between groups are not very large, meaning parental education is not the only factor.

    ---

    ### 3. Average Math Score by Lunch Type
    - **File:** lunch_vs_math_score.png
    - Students who receive standard lunch (indicating better economic background) tend to score higher on average.
    - This suggests economic factors may play a role in performance.

    ---

    ### 4. Test Preparation Course Completion vs Math Score
    - **File:** test_prep_vs_math_score.png
    - Students who completed a test preparation course tend to have slightly better scores.
    - Some students who did not complete the course still scored high, so test prep helps, but it’s not the only factor.

    ---

    ### 5. Average Math Score by Gender
    - **File:** gender_vs_math_score.png
    - Male and female students have very similar average math scores.
    - There is no strong evidence of a gender gap in math performance based on this dataset.

    ---

    ## Conclusion

    These visualizations helped us understand how different factors might influence student performance. Without these plots, spotting these patterns would have been much harder. By summarizing data visually, we could quickly identify trends related to parental education, lunch type, test preparation, and gender.
    """

    with open(RESULTS_PATH, "w") as f:
        f.write(summary)

    print(f"Summary saved at {RESULTS_PATH}")

def main():
    df = pd.read_csv(CLEANED_PATH)

    plot_math_score_distribution(df)
    plot_parent_education_vs_math_score(df)
    plot_lunch_vs_math_score(df)
    plot_test_prep_vs_math_score(df)
    plot_gender_vs_math_score(df)

    generate_summary(df)

if __name__ == "__main__":
    main()