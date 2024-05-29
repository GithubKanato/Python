import matplotlib.pyplot as plt
import pandas

def read_csv():
    df = pandas.read_csv('day5/data.csv')
    return df

def print_graph(data):
    plt.plot(data['date'],data['temperature'],data['humidity'])
    plt.show()

def main():
    # csv読み込み
    data = read_csv()
    # グラフを書く
    print_graph(data)


if __name__ == "__main__":
    main()