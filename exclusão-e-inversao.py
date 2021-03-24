import numpy as np
import matplotlib.pyplot as plt

# Considere a função densidade de probabilidade 𝑓(𝑥) = 𝐴(1−|𝑥|^𝐺) para |𝑥| ≤ 1 (com 𝐺 > 0), onde por simetria é fácil perceber que 〈𝑥〉 = 0.
# Mostre  analiticamente  que:
# (i)  a  constante  de  normalização  é 𝐴=(𝐺+1)/2𝐺
# (ii)  o  desvio-padrão verdadeiro é 𝜎0=√(𝐺+1)/(3𝐺+9).
# Gerar conjuntos de 𝑁 valores  de 𝑥 que  sigam  essa  função  densidade  de  probabilidade  para  uma  dada  escolha  do expoente 𝐺.
# Parâmetros de entrada devem ser os valores de 𝐺 e 𝑁, e deve retornar um vetor com 𝑁 valores de 𝑥.

N = 1000


def sigma_0_1(G): return ((G + 1) / (3 * G + 9)) ** (1 / 2)


G = 10

# NxN candidatos a amostras
x_s = np.random.default_rng().uniform(-1, 1, 2 * N)
f_s = np.random.default_rng().uniform(0, (G + 1) / (2 * G), 2 * N)


def f(x, G): return (G + 1) * (1 - np.abs(x) ** G) / (2 * G)


filtro_exclusao = f_s <= f(x_s, G)
x_raw = x_s[filtro_exclusao]
np.shape(x_raw)

# Separando simulação completa
x = x_raw[:N]
np.shape(x)
plt.hist(x)
plt.savefig('a8_1stplot.png')

sigma_x = x.std(ddof=1)
print('x', np.mean(x))
print('sigma_x', sigma_x)
print('F1', np.sum(np.abs(x)<sigma_0_1(G))/N)
