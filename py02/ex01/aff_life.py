from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff_life(df: pd.DataFrame):
    """
    Plots the life expectancy of a specific country over time.
    A DataFrame where the index represents country names
    and the columns represent years with life expectancy data.
    """

    c = "France"
    china = df.loc[c]

    china.index = china.index.astype(int)
    # print(china_data)
    # print('_'*30)
    # print(china_data.index)
    # print('_'*30)
    # print(china_data.values)
    # print('_'*30)
    plt.figure(figsize=(10, 5))
    plt.plot(china.index, china.values, linestyle="-", color="b", label=c)

    plt.title(f" {c} Life Expectancy Projections", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)
    plt.legend()
    # plt.grid(True)
    plt.show()


def main():
    """
    loads life expectancy data and visualizes it for a specific country.
    """
    df = load('../CSV/life_expectancy_years.csv')

    if df is not None:
        aff_life(df)


if __name__ == "__main__":
    main()
