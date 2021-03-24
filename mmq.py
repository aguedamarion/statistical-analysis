# -*- coding: utf-8 -*-
"""
@author: Águeda Marion
"""

import numpy as np
import matplotlib.pyplot as plt

# O arquivo “dados_osciloscopio.txt”, contém dados reais de uma medida de tensão (a segunda
# coluna, em volts) em função do tempo (a primeira coluna, em segundos) feita com um 
# osciloscópio digital ligado a um gerador de sinais programado para gerar um sinal senoidal
# de frequência 2Hz. É razoável considerar que o tempo não tenha incerteza e que as medições
# de tensão tenham incertezas iguais para todos os dados,com valor igual à menor divisão 
# (resolução) das medições de tensão do osciloscópio digital, 𝜎𝑖=0.06𝑉.

# Escreva uma rotina para ajustar esses dados pelo Método dos Mínimos Quadrados por um modelo
# que considere uma onda senoidal, isto é, F(t) = a * cos(2pi*f*t) + b*sin(2pi*f*t), com f = 2Hz.

data = np.genfromtxt('activity24_dados_osciloscopio.txt', delimiter=';')
[t, y] = np.transpose(data)
sy = np.array([0.06] * len(y))  # V

plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Y')
plt.savefig('activity24_1stplot.png')

# função senoidal: F(t) = a * cos(2pi*f*t) + b*sin(2pi*f*t) com f = 2Hz
freq = np.array([2.0] * len(t))  # Hz -> g1

D = np.zeros((2, 1), dtype='float')
M = np.zeros((2, 2), dtype='float')
G = np.array([freq, t], dtype='float')

for i in range(len(D)):  # linhas
    D[i] = sum((y * G[i]) * (1 / sy ** 2))  # G[i] = G[0] e G[1], que seriam g1 e g2 respectivamente
    for j in range(len(M[0, :])):
        M[i, j] = sum((G[i] * G[j]) / sy ** 2)
        
# Obtenha o valor dos parâmetros ajustados 𝑎̃1 e 𝑎̃2 com suas respectivas incertezas.
# Determine a covariância, 𝑐𝑜𝑣(𝑎̃1,𝑎̃2), e a matriz de correlação.

V_A = np.linalg.inv(M)  # matriz de covariância é a inversa de M
A = np.dot(V_A, D)  # multiplicação de matrizes que me devolve os parâmetros A
sa, sb = np.sqrt((V_A[0, 0], V_A[1, 1]))  # incertezas de a e b (parâmetros)
Rho = V_A[0, 1] / (sa * sb)  # coeficiente de correlação

print('V_A', V_A)
print('matriz de correlação', A)
print('incertezas de a e b', sa, sb)
print('rho', Rho)
