# -*- coding: utf-8 -*-
"""
@author: Águeda Marion
"""
import numpy as np
import matplotlib.pyplot as plt

# Nesta atividade iremos considerar dados estatisticamente independentes com função 
# densidade de probabilidade gaussiana, de valor verdadeiro 𝑥0=0 e desvio-padrão 
# verdadeiro 𝜎0=1. Gere 𝑀=10.000 conjuntos de 𝑁=5 dados cada e, para cada conjunto,
# calcule o desvio-padrão amostral, 𝑠, e a variância amostral, 𝑉.

M = 10000
x0 = 0
s0 = 1
Ns = [2, 3, 4, 5, 10, 50, 100]

for j in range(len(Ns)):
    sx = np.zeros(M)  # matriz dos desvios-padrão de cada simulação
    Vx = np.zeros(M)  # matriz dos valores médios de cada simulação
    x = np.zeros((M, Ns[j]))  # array que recebe os xi simulados
    for i in range(M):
        for k in range(Ns[j]):
            xi = x0 + s0 * np.random.randn()
            x[i, k] = xi

    sx = np.std(x, axis=1, ddof=1)  # desvios-padrão
    Vx = sx ** 2  # variância
    
    # Faça histogramas dos 𝑀 valores de 𝑠 e de 𝑉

    if Ns[j] == 2:
        plt.figure(figsize=(8, 8))
        plt.hist(sx, bins=50)
        plt.title('s para N=2')
        plt.ylabel(f'N = {Ns[j]}')
        plt.savefig('N2_s.png')

        plt.figure(figsize=(8, 8))
        plt.hist(Vx, bins=50)
        plt.title('V para N=2')
        plt.ylabel(f'N = {Ns[j]}')
        plt.savefig('N2_V.png')
        print(f'sx:\n{np.average(sx):.4f} ({np.std(sx):.4f})')
        print(f'Vx:\n{np.average(Vx):.4f} ({np.std(Vx):.4f})')

    if Ns[j] == 3:
        print(f'sx:\n{np.average(sx):.4f} ({np.std(sx):.4f})')
