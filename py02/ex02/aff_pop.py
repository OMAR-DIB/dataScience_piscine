import matplotlib.pyplot as plt
from load_csv import load


def get_values(row):
    """
        Take an array and return a new array with the values
        as float (replacing human-readable format)
    """
    return [
        float(i.replace('k', 'e3').replace('M', 'e6'))
        for i in row.to_numpy()
    ]


def main():
    """
        Display a graph that compares the population projection
        of France vs Belgium
    """
    df = load("population_total.csv")

    first_country = df.loc['France']
    second_country = df.loc['Belgium']

    try:
        years = first_country.index.astype(int).to_numpy()
    except Exception:
        print("Error: Years must be integers")
        exit(0)

    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f'{x/1e6:.0f}M'))

    years_filtered = years[(years >= 1800) & (years <= 2050)]

    plt.plot(
        years_filtered,
        get_values(first_country.loc[years_filtered.astype(str)]),
        label='France',
        color='g'
    )
    plt.plot(
        years_filtered,
        get_values(second_country.loc[years_filtered.astype(str)]),
        label='Belgium',
        color='b'
    )

    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend()
    plt.xticks([year for year in years_filtered if year % 40 == 0])
    plt.yticks([20_000_000, 40_000_000, 60_000_000])
    plt.show()


if __name__ == "__main__":
    main()
