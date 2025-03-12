from load_csv import load
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# print(load('../CSV/life_expectancy_years.csv'))

def aff_life(df: pd.DataFrame):
    # Load dataset
    # df = load('../CSV/life_expectancy_years.csv')

    # Select the data for China
    country_name = "France"  # Adjust this if needed
    china_data = df.loc[country_name]

    # Convert index (years) to integers
    china_data.index = china_data.index.astype(int)
    # print(china_data)
    # print('_'*30)
    # print(china_data.index)
    # print('_'*30)
    # print(china_data.values)
    # print('_'*30)
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(china_data.index, china_data.values, linestyle="-", color="b", label=country_name)

    # Titles and labels
    plt.title(f"Life Expectancy in {country_name} Over Time", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life Expectancy (years)", fontsize=12)
    plt.legend()
    # plt.grid(True)

    # Show the plot
    plt.show()

aff_life(load('../CSV/life_expectancy_years.csv'))