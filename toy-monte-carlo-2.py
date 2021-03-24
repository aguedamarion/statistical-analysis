import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.rcParams['figure.figsize'] = 15, 7

# gerar 10 000 dados y com distribuição uniforme no intervalo entre -0,5  e  +0,5

N = 10000
dist = np.random.uniform(low=-0.5, high=0.5, size=N)

media = np.mean(dist)
desvio = np.std(dist, ddof=1)

plt.hist(dist, edgecolor='k', bins=30)
plt.axvline(x=media, color='black', ls='--', label='Média')
plt.axvline(x=media - desvio, color='purple', ls='--', label=r'intervalo de $1 \sigma$')
plt.axvline(x=media + desvio, color='purple', ls='--')
plt.axvline(x=media - 2 * desvio, color='#14855D', ls='--', label=r'intervalo de $2 \sigma$')
plt.axvline(x=media + 2 * desvio, color='#14855D', ls='--')
plt.axvline(x=media - 3 * desvio, color='blue', ls='--', label=r'intervalo de $3 \sigma$')
plt.axvline(x=media + 3 * desvio, color='blue', ls='--')
plt.legend()
plt.savefig('a5_2ndplot.png')

# 1.1 calcular y_mean e sua incerteza, desv_pad_y;
# 1.2 calcular o desvio-padrão amostral de y (sigma_y)
# 1.3 calcular o número de dados y dentro de um sigma_y
# 1.4 calcular o número de dados y dentro de 2 sigma_y
# 1.5 calcular o número de dados y dentro de 3 sigma_y
print(f'''
média: {media:.4f}
desvio padrão: {desvio:.4f}
qtde no intervalo de 1 sigma: {sum(abs(x - media) < desvio for x in dist)}
qtde no intervalo de 2 sigma: {sum(abs(x - media) < 2 * desvio for x in dist)}
qtde no intervalo de 3 sigma: {sum(abs(x - media) < 3 * desvio for x in dist)}
''')
