import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

#paths
CLEANED_DATA_PATH = "../data/processed/cleaned_frailty_data.csv"
PLOTS_FOLDER = "../analysis/plots"
RESULTS_FILE = "../analysis/results.md"

#ensure plots folder exists
os.makedirs(PLOTS_FOLDER, exist_ok=True)

def plot_violin_grip_by_frailty(df):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="Frailty", y="Grip_Strength", data=df, palette={"N": "skyblue", "Y": "lightcoral"})

    plt.title("Grip Strength Distribution by Frailty")
    plt.xlabel("Frailty Status")
    plt.ylabel("Grip Strength (kg)")

    plt.grid(axis='y')
    plt.savefig(f"{PLOTS_FOLDER}/violin_grip_by_frailty.png")
    plt.close()

def plot_scatter_grip_vs_age_with_trendline(df):
    plt.figure(figsize=(8, 6))

    #color Mapping
    colors = {'N': 'skyblue', 'Y': 'lightcoral'}

    for frailty_status in ['N', 'Y']:
        subset = df[df['Frailty'] == frailty_status]
        plt.scatter(subset['Age'], subset['Grip_Strength'], label=f"Frailty = {frailty_status}", color=colors[frailty_status])

    #add Overall Trendline (ignoring frailty status)
    z = np.polyfit(df['Age'], df['Grip_Strength'], 1)
    p = np.poly1d(z)
    plt.plot(df['Age'], p(df['Age']), color='darkorange', linestyle='--', label='Overall Trendline')

    plt.title("Grip Strength vs Age (Colored by Frailty)")
    plt.xlabel("Age (years)")
    plt.ylabel("Grip Strength (kg)")
    plt.legend()
    plt.grid(True)

    plt.savefig(f"{PLOTS_FOLDER}/scatter_grip_vs_age_trendline.png")
    plt.close()

def calculate_summary(df):
    frail_mean = df[df['Frailty'] == 'Y']['Grip_Strength'].mean()
    non_frail_mean = df[df['Frailty'] == 'N']['Grip_Strength'].mean()

    summary_text = f"""
    ## Analysis Summary - Frailty Data

    - Average Grip Strength (Frail): {frail_mean:.2f} kg
    - Average Grip Strength (Non-Frail): {non_frail_mean:.2f} kg

    **Observation:** 
    - Non-frail individuals tend to have a higher average grip strength.
    - Frail individuals show lower grip strength, which supports the hypothesis that reduced physical strength is correlated with frailty.

    ## Generated Visualizations

    1. Violin Plot - Grip Strength by Frailty: `violin_grip_by_frailty.png`
    2. Scatter Plot - Grip Strength vs Age with Trendline: `scatter_grip_vs_age_trendline.png`
    """

    with open(RESULTS_FILE, "w") as file:
        file.write(summary_text)

    print(f"Results saved at {RESULTS_FILE}")

def main():
    df = pd.read_csv(CLEANED_DATA_PATH)

    plot_violin_grip_by_frailty(df)
    plot_scatter_grip_vs_age_with_trendline(df)
    calculate_summary(df)

if __name__ == "__main__":
    main()