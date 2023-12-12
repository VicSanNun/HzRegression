import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np

def plot(X, Y, Sigma, rec, drec, title, d2rec=None, d3rec=None ):

    x = np.linspace(0,2.5,1000)
    y = 70*np.sqrt(0.3*(1+x)**3+0.7)

    plt.xlim(0, 2.5)
    plt.fill_between(rec[:, 0], rec[:, 1] + rec[:, 2], rec[:, 1] - rec[:, 2],
                     facecolor='lightblue')
    plt.plot(rec[:, 0], rec[:, 1], label='Reconstrução')
    plt.plot(x,y, linestyle="dashed", label="LCDM", color="black")
    plt.errorbar(X, Y, Sigma, color='red', fmt='_', label="Observações")
    plt.legend()
    plt.xlabel('z')
    plt.ylabel('H(z)')
        
    plt.savefig(f'{title}')

if __name__=="__main__":
    (X,Y,Sigma) = loadtxt("../inputdata.txt", unpack='True')
    rec = loadtxt("f.txt")
    drec = loadtxt("df.txt")
    
    plot(X, Y, Sigma, rec, drec)
