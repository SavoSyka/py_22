import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def task1():
    n, m = map(int, input().split())
    print(n**2-m**2)
def task2():
    s=input()
    k=0
    for el in s:
        if (ord(el)>=48) and (ord(el<=57)):
            k=k+1
    print(k)


def task3():
    s = input().split()
    k = 0
    for el in s:
        if len(el) >= 3 and el[-1] == 's' and el[-2] == 'u' and el[-3] == 'b':
            k = k + 1
    print(k)

def task4(generator):
    # TODO: четвертое задание

def task5(list_of_smth):
    print(list_of_smth[6:-1:2])

def task6(list1, list2, list3, list4):
    a = set(list1) & set(list4)
    b = set(list2) & set(list3)
    c = a | b
    print(list(c))

def task7():
    np.random.seed(12)
    data = np.random.randint(0, 65, 64)
    n_data = data.reshape(8, 8)
    new_data = n_data[0:-1, 1::]
    print(np.linalg.det(new_data))
    return new_data

def task8(f, min_x, max_x, N, min_y, max_y):
    plt.ylim(min_y, max_y)
    plt.xlim(min_x, max_x)

    plt.grid('True')
    plt.yscale('log')
    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.plot(x, y, 'g-.')
    plt.show()
    plt.savefig("function.png")


def task9(data, x_array, y_array, treshold):
    r_data = data.reshape(data.size, 1)
    plt.hist(r_data, 'auto')
    plt.show()
    plt.savefig('histograms_0.png')



def task10(list_of_smth):
    # TODO: ...

def task11(filename="infile.csv"):
    df = pd.read_csv(filename)
    for col in df.columns:
        mask = df.isnull()[col]
        df[mask][col].index.values
        print(col, len(df[mask][col].index.values))


def task12(filename="video-games.csv"):
    f = pd.read_csv(filename)
    d = dict()
    d['n_games'] = [f.iloc[:, 1].nunique()]
    d['mean_price'] = f.groupby(["publisher"]).agg({"price": 'mean'}).loc['EA', 'price']
    df = f[f.max_players <= 2]
    d['mean_raiting_1_2']=df.price.mean()