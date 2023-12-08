import matplotlib.pyplot as plt
import random
import numpy as np

#comment/uncomment certain tasks and stanzas of certain tasks depending on interest of simulation

def getNormalSamplesOfSize(n):
    #return a list of samples from normal distribution(mu=0, sigma=1) of size n
    return np.random.normal(0, 1, n)

def task1():
    #1.plot histogram of samples
    samples = list(getNormalSamplesOfSize(10000)) 
    #2.plot line graph of mean v.s. sample size
    n = [i for i in range(1,10001)]
    means = [np.mean(list(getNormalSamplesOfSize(i))) for i in n]
    assert (len(n) == 10000) and (len(means) == 10000), f"len(n) == {len(n)}, len(means) == {len(means)}"
    fig,ax = plt.subplots(1,2)
    ax[0].hist(samples, bins=500)
    ax[1].plot(n,means)
    ax[0].set_xlabel('X_n\'s from normal distibution')
    ax[0].set_ylabel('frequencies')
    ax[0].set_title('X_n value histogram')
    ax[1].set_xlabel('sample sizes (n)')
    ax[1].set_ylabel('mean value')
    ax[1].yaxis.set_label_position('right')
    ax[1].set_title('mean value vs sample size')
    plt.show()


def getUniformSamplesOf(n):
    return list(np.random.uniform(-1,1,n))

def task2():
    #1.plot three histograms using C_1 to C_n
    U_n = getUniformSamplesOf(10000)
    while np.median(U_n) < 0.0 or np.mean(U_n) < 0.0:
        U_n = getUniformSamplesOf(10000)

    print(f'median(U_n) == {np.median(U_n)}')
    print(f'mean(U_n) == {np.mean(U_n)}')
    n = [i for i in range(1,10001)]
    C_n = [np.tan(np.pi * u) for u in U_n]
    means_C = [np.mean(random.sample(C_n, i)) for i in n]
    fig,ax = plt.subplots()

    ax.hist(C_n[0:int(10000/100)], bins=100, range = (-5,5))
    ax.set_xlabel('Cauchy Random Variable (C_n)')
    ax.set_ylabel('frequencies')
    ax.set_title(f'n = 10000/100 = {int(10000/100)}')
    plt.show()

    ax.hist(C_n[0:int(10000/100)], bins=100, range=(-5,5))
    ax.set_xlabel('Cauchy Random Variable (C_n)')
    ax.set_ylabel('frequencies')
    ax.set_title(f'n = 10000/10 = {int(10000/10)}')
    plt.show()

    ax.hist(C_n, bins=100, range=(-5,5))
    ax.set_xlabel('Cauchy Random Variable (C_n)')
    ax.set_ylabel('frequencies')
    ax.set_title(f'n = 10000')
    plt.show()

    #2.plotting the mean
    ax.plot(n, means_C)
    ax.set_xlabel('sample size (n)')
    ax.set_ylabel('Mean of Cauchy Random Variable')
    ax.set_title('Mean of Cauchy Random Variable vs Sample Size (n)')
    plt.show()

def task3():
    Xn = getNormalSamplesOfSize(10000)
    Yn = getNormalSamplesOfSize(10000)
    Zn = [y/x for y,x in zip(Yn, Xn)]
    fig,ax = plt.subplots()
    
    #1. histograms
    ax.hist(Zn[0:int(10000/100)], bins=100, range = (-5,5))
    ax.set_xlabel('Cauchy Random Variable (Zn)')
    ax.set_ylabel('frequencies')
    ax.set_title(f'n = 10000/100 = {int(10000/100)}')
    plt.show()

    ax.hist(Zn[0:int(10000/10)], bins=100, range = (-5,5))
    ax.set_xlabel('Cauchy Random Variable (Zn)')
    ax.set_ylabel('frequencies')
    ax.set_title(f'n = 10000/10 = {int(10000/10)}')
    plt.show()

    ax.hist(Zn, bins=100, range = (-5,5))
    ax.set_xlabel('Cauchy Random Variable (Zn)')
    ax.set_ylabel('frequencies')
    ax.set_title(f'n = 10000')
    plt.show()

    #2. plotting mean vs sample size
    n  = [i for i in range(1, 10001)]
    means = [np.mean(random.sample(Zn, i)) for i in n]
    ax.plot(n, means)
    ax.set_xlabel('sample size (n)')
    ax.set_ylabel('Mean of Cauchy Random Variable (Zn)')
    ax.set_title('Mean of Cauchy Random Variable (Zn) vs Sample Size (n)')
    plt.show()
        
if __name__ == '__main__':
    task1()
    task2()
    task3()
