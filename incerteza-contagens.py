import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# gerar um  conjuntode 𝑁 = 200 dados  que  sigam  a função  densidade  de  probabilidade 𝑓 (𝑥) = (3/125)𝑥^2, para 𝑥 ∈ [0,5].
# rodar o programa 3 vezes e guardar os outputs.

ind = pd.Index(['[0, 1[', '[1, 2[', '[2, 3[', '[3, 4[', '[4, 5['],
               name='[x_a,x_b[')
df = pd.DataFrame(index=ind,
                  columns=['(1) P(x_a<=x<=x_b)', '(2) n_0', '(3) n', '(4) n',
                           '(5) n', '(6) nh', '(7) sig_nh', '(8) s_n'])

def cum_f(x): return (x ** 3) / 125


df['(1) P(x_a<=x<=x_b)'] = [cum_f(i + 1) - cum_f(i) for i in range(5)]

df['(2) n_0'] = df['(1) P(x_a<=x<=x_b)'] * 200

rng = np.random.default_rng()
N = 200
b = [0, 1, 2, 3, 4, 5]

c1_3 = (125 * rng.random(N)) ** (1 / 3)
df['(3) n'] = plt.hist(c1_3, bins=b)[0]
plt.savefig('hist_c1_3.png')

c2_4 = (125 * rng.random(N)) ** (1 / 3)
df['(4) n'] = plt.hist(c2_4, bins=b)[0]
plt.savefig('hist_c2_4.png')

c2_5 = (125 * rng.random(N)) ** (1 / 3)
df['(5) n'] = plt.hist(c2_5, bins=b)[0]
plt.savefig('hist_c2_5.png')


def binarize(a): return np.histogram(a, bins=b)[0]

# Gere 𝑛𝑅𝐸𝑃 = 10.000 conjuntos de 𝑁=200 dados e guarde os resultados

n_rep = 10000

x = (125 * rng.random((n_rep, N))) ** (1 / 3)
d = np.apply_along_axis(binarize, axis=1, arr=x)

df['(6) nh'] = d.mean(axis=0)
d_std = d.std(axis=0, ddof=1)
df['(7) sig_nh'] = d_std / (d.shape[0] ** (1 / 2))

# gerar 𝑛̅, esua respectiva incerteza (escreva esses valores com o número correto de algarismos significativos)

df['(8) s_n'] = d_std

df.to_csv('activity11.csv')

print('df', df)
