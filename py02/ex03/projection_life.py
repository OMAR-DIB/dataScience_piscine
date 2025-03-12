from load_csv import load
import matplotlib.pyplot as plt

def main():
    path1= '../CSV/income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    path2 = '../CSV/life_expectancy_years.csv'
    
    try:
        var1 = load(path1)
        var2 = load(path2)
    except:
        print("error")
        exit(0)
    
    value1=var1['1900']
    value2=var2['1900']
    
    plt.scatter(value1,value2)
    plt.xlabel("hi")
    plt.ylabel("hello")
    plt.show()
    
if __name__ == '__main__':
    main()
