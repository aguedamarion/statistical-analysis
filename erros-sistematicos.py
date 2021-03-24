# -*- coding: utf-8 -*-
"""
@author: Águeda Marion
"""

# Suponha duas medições (𝑥 e 𝑦) sujeitas a erros de calibração com desvio-padrão scal 
# e a erros (aleatórios) de leitura de desvio-padrão sl, de modo que as incertezas são
# s_𝑥 = s_𝑦 = √[(scal^2) + (sl^2)]. Considerando que os erros sejam gaussianos, a 
# geração dos dados 𝑥 e 𝑦 pode ser feita a partir de 3 números aleatórios gaussianos de
# valor esperado 0 e desvio-padrão verdadeiro 1 (𝑟𝐶, 𝑟𝑥 e 𝑟𝑦) por:
# 𝜀𝐶 = scal ∗ rc
# 𝑥 = 𝑥0 + sl ∗ 𝑟𝑥 + 𝜀𝐶
# 𝑦 = 𝑦0 + sl ∗ 𝑟𝑦 + 𝜀𝐶

import numpy as np
import matplotlib.pyplot as plt

x0 = 110
y0 = 100

scal = 4  # incert de calibração (sistematico)
sl = 3  # incert de leitura (aleatorio)

N = 1000


def gera(N, x0, y0, scal, sl):
    rc = np.random.randn(N)
    rx = np.random.randn(N)
    ry = np.random.randn(N)

    ecal = scal * rc
    x = x0 + (sl * rx) + ecal
    y = y0 + (sl * ry) + ecal

    return x, y


x, y = gera(N, x0, y0, scal, sl)
print('\n-------------- 1 ---------------')
print(f' sCal = {scal} e sLeit = {sl}')
# GRAFICO
plt.scatter(x, y)
plt.title('Dispersão X x Y')
plt.xlabel('Dados x')  # nomeando eixo x
plt.ylabel('Dados y')
plt.savefig('a19_1stplot.png')

# Determine a frequência relativa com que os erros de 𝑥 e 𝑦 têm o mesmo sinal e, usando 
# seus conhecimentos sobre a binomial, estime a incerteza dessa  frequência relativa.

print('-------------- 1-A ---------------')

# erros
erro_x = x - x0
erro_y = y - y0

mul = erro_x * erro_y  # o array já multiplica naturalmente elemento por elemnto
n = np.count_nonzero(mul > 0)

# frequencia relativa de dados gerados positivos ao mesmo tempo
freq = n / N
sn = np.sqrt(N * freq * (1 - freq))
sfreq = (1 / N) * sn

print(f'Freq relativa de erros com mesmo sinal:\n{freq:.3f}({sfreq:.3f})')

# Calcule a covariância amostral, 𝑉𝑥𝑦, e a correspondente correlação amostral, 𝑅, dos 𝑁 
# pares de valores de 𝑥 e 𝑦 gerados.

print('-------------- 1-B ---------------')
# calculo da COVARIANCIA AMOSTRAL e seu coeficiente

s_x = np.std(x, ddof=1)  # incerteza de a
s_y = np.std(y, ddof=1)  # incerteza de b
xm = np.mean(x)  # média dos dados de a
ym = np.mean(y)  # média dos dados de a
er_x = np.zeros(N)
er_y = np.zeros(N)
for i in range(N):
    er_x[i] = (x[i] - xm)
    er_y[i] = (y[i] - ym)

cov = (1 / (N - 1)) * (np.sum((er_x) * (er_y)))  # COVARIANCIA
R = cov / (s_x * s_y)  # coef de CORRELAÇÃO AMOSTRAL

scov = s_x * s_y * (np.sqrt((1 + R ** 2) / (N - 1)))
sR = (1 - R ** 2) / np.sqrt(N - 1)

print(f'Covariância amostal (e incerteza):\n{cov:+.2f}({scov:.2f})')
print(f'Correlação amostral (e incerteza):\n{R:+.3f}({sR:.3f})')

# Para cada um dos 𝑁 pares de valores de 𝒙 e 𝒚, calcule a soma correspondente, 𝑤 = 𝑥 + 𝑦. 
# Determine o desvio-padrão amostral de 𝒘 (a incerteza de cada valor de 𝒘).

print('-------------- 1-C ---------------')
w = x + y
sw = np.std(w, ddof=1)
inc_sw = sw / (np.sqrt(2 * (N - 1)))  # incerteza da incerteza
print(f'Desvpad de w=(x + y) e sua incerteza:\n{sw:.2f}({inc_sw:.2f})')

# Repita o item anterior para o caso da diferença entre 𝒙 e 𝒚, 𝑧 = 𝑥−𝑦.

print('-------------- 1-D ---------------')

z = x - y
sz = np.std(z, ddof=1)
inc_sz = sz / (np.sqrt(2 * (N - 1)))  # incerteza da incerteza
print(f'Desvpad de z=(x - y) e sua incerteza:\n{sz:.2f}({inc_sz:.2f})')

# Considere agora o caso de várias medições sujeitas a erros sistemáticos, 𝜀𝑆 (igual para 
# todos os dados), e aleatórios, 𝜀𝐴 (que diferem de dado para dado):
# 𝑑𝑖 = 𝑑0 + Ss + Sa onde 𝑑0=200 é o valor verdadeiro da grandeza. Suponha que os erros 
# sistemáticos sejam gaussianos e tenham desvio-padrão Ss0=4 e os aleatórios também sejam
# gaussianos com desvio-padrão Sa0=3. Gere 𝑴=𝟏𝟎.𝟎𝟎𝟎 conjuntos de 𝑵=𝟐𝟓 dadoscom essas 
# características e registre os 𝑀 valores médios de cada conjunto. Estime numericamente a 
# incerteza dos valores médios dos 𝑁 dados, 𝑠𝑑𝑚.

print('\n-------------- 2 ---------------')

M = 10000
N_ = 25
d0 = 200
Ss0 = 4  # incerteza devida aos erros sistemáticos
Sa0 = 3  # incerteza devida aos erros aleatórios

media_simu = np.zeros(M)
for i in range(M):
    Ss = Ss0 * np.random.randn()
    recebe_num = []
    for j in range(N_):
        Sa = Sa0 * np.random.randn()
        d = d0 + Ss + Sa
        recebe_num.append(d)

    media_simu[i] = np.mean(recebe_num)

inc_simu = np.std(media_simu, ddof=1)
s_inc_simu = inc_simu / np.sqrt(2 * (M - 1))

print(f'Incerteza dos valores medios:\n{inc_simu:.3f} ({s_inc_simu:.3f})')
