from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def aff_pop():
    """Displays population trends for two countries from 1800 to 2050."""
    country_2 = "Angola"
    country_1 = "Albania"
    df = load('../CSV/population_total.csv')
    # print(var)
    # Extract data and handle possible KeyErrors
    try:
        uae_data = df.loc[country_2]
        france_data = df.loc[country_1]
    except KeyError as e:
        print(f"Error: {e} not found in the dataset.")
        return

    # Convert index to integers and filter years
    france_data.index = france_data.index.astype(int)
    uae_data.index = uae_data.index.astype(int)
    france_data = france_data[(france_data.index >= 1800) & (france_data.index <= 2050)]
    uae_data = uae_data[(uae_data.index >= 1800) & (uae_data.index <= 2050)]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(france_data.index, france_data.values, 'b-', label=country_1)
    plt.plot(uae_data.index, uae_data.values, 'r--', label=country_2)

    # Format y-axis to show values in millions
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x/1e6:.0f}M'))

    plt.title("Population Growth Comparison")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="upper left")
    plt.show()

aff_pop()






# from load_csv import load
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# def aff_pop(df: pd.DataFrame):
#     """Displays population trends for two countries from 1800 to 2050."""
#     # Define countries
#     country_1 = "France"  # Change this if needed
#     country_2 = "United Arab Emirates"  # Change this if needed

#     # Extract data
#     country_1_data = df.loc[country_1]
#     country_2_data = df.loc[country_2]

#     # Convert index (years) to integers
#     country_1_data.index = country_1_data.index.astype(int)
#     country_2_data.index = country_2_data.index.astype(int)

#     # Filter data from 1800 to 2050
#     country_1_data = country_1_data[(country_1_data.index >= 1800) & (country_1_data.index <= 2050)]
#     country_2_data = country_2_data[(country_2_data.index >= 1800) & (country_2_data.index <= 2050)]

#     # Plot the data
#     plt.figure(figsize=(12, 6))
#     plt.plot(country_1_data.index, country_1_data.values, linestyle="-", color="b", label=country_1)
#     plt.plot(country_2_data.index, country_2_data.values, linestyle="--", color="r", label=country_2)

#     # Titles and labels
#     plt.title("Population Growth (1800 - 2050)", fontsize=14)
#     plt.xlabel("Year", fontsize=12)
#     plt.ylabel("Population", fontsize=12)
#     plt.legend()
#     # plt.grid(True)

#     # Show the plot
#     plt.show()

# # Load CSV and display the graph
# aff_pop(load('../CSV/population_total.csv'))