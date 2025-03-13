from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
        relation between incomes and life expectancy
    """
    income = '../CSV/income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    life_expectancy_path = '../CSV/life_expectancy_years.csv'

    income_data = load(income)
    life_expectancy = load(life_expectancy_path)
    x = income_data['1900']
    y = life_expectancy['1900']

    plt.scatter(x, y)
    plt.xlabel("Gross domestic product")
    plt.title("1900")
    plt.ylabel("Life Expectancy")
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.xlim(left=300)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
