import matplotlib.pyplot as plt
import numpy as np
import time

def pi_est(n):
    '''
    Calcula Pi para n puntos que se evaluan viendo cuantos caen dentro y fuera de un circulo circunscrito por un cuadrado.
    '''
    valorPi=4*sum((np.square(np.random.uniform(0, 1, n).tolist()) + np.square(np.random.uniform(0, 1, n).tolist()))<=1)/n
    return(valorPi)

n = 1000
numExperimentos = 100000

# Calcula Pi con map y una funcion
start = time.time()
listaValoresPi=list(map(pi_est, [n]*numExperimentos))
end = time.time()
print(end - start)

print('media= '+str(np.mean(listaValoresPi)))
print ('mediana= '+str(np.median(listaValoresPi)))
#plt.plot(listaValoresPi)

# Calcula pi con map y lambda
start = time.time()
listaValoresPi1=list(map(lambda x : 4*sum((np.square(np.random.uniform(0, 1, x).tolist()) + np.square(np.random.uniform(0, 1, x).tolist()))<=1)/x,  [n]*numExperimentos))
end = time.time()
print(end - start)

print('media= '+str(np.mean(listaValoresPi1)))
print ('mediana= '+str(np.median(listaValoresPi1)))
