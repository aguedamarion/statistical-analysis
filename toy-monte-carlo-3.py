import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.rcParams['figure.figsize'] = 15,7

# gere 10 000 dados z com distribuição triangular no intervalo entre -1 e +1 a partir da soma  de  dois  dados  com
# distribuição  uniformeno  intervalo  entre -0.5  e  +0.5, isto é, valor de z pode ser gerado como a soma de dois
# valores gerados como no exercício anterior[no Octave, z= -1+ rand(1e4,1) + rand(1e4,1)]

N = 10000
dist = np.random.uniform(low=-0.5, high=0.5, size=N) + np.random.uniform(low=-0.5, high=0.5, size=N)

media = np.mean(dist)
desvio = np.std(dist, ddof=1)

plt.hist(dist, edgecolor='k', bins=30)
plt.axvline(x=media, color='black', ls='--', label='Média')
plt.axvline(x=media-desvio, color='purple', ls='--', label=r'intervalo de $1 \sigma$')
plt.axvline(x=media+desvio, color='purple', ls='--')
plt.axvline(x=media-2*desvio, color='#14855D', ls='--', label=r'intervalo de $2 \sigma$')
plt.axvline(x=media+2*desvio, color='#14855D', ls='--')
plt.axvline(x=media-3*desvio, color='blue', ls='--', label=r'intervalo de $3 \sigma$')
plt.axvline(x=media+3*desvio, color='blue', ls='--')
plt.legend()
plt.savefig('a5_3rdplot.png')

# 1.1 calcular z_mean e sua incerteza, desv_pad_z;
# 1.2 calcular o desvio-padrão amostral de z (sigma_z)
# 1.3 calcular o número de dados z dentro de um sigma_z
# 1.4 calcular o número de dados z dentro de 2 sigma_z
# 1.5 calcular o número de dados z dentro de 3 sigma_z

print(f'''
média: {media:.4f}
desvio padrão: {desvio:.4f}
qtde no intervalo de 1 sigma: {sum(abs(x-media) < desvio for x in dist)}
qtde no intervalo de 2 sigma: {sum(abs(x-media) < 2*desvio for x in dist)}
qtde no intervalo de 3 sigma: {sum(abs(x-media) < 3*desvio for x in dist)}
''')
