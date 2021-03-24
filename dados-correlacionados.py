import numpy as np
import matplotlib.pyplot as plt

# Gerar pares de dados, 𝑎 e 𝑏, gaussianos com valores verdadeiros 𝑎0 e 𝑏0, desvios-padrões s_a0 e s_b0 e coeficiente decorrelação 𝜌 
# (ou seja, com covariância, 𝑐𝑜𝑣 (𝑎,𝑏) = 𝜌*s_a0*s_b0). Esses dados podem ser gerados a partir de dois números aleatórios gaussianos
# descorrelacionados, com valores verdadeiros nulos e desvios-padrão unitários, 𝑟1e 𝑟2,da seguinte forma:
# 𝑎=𝑎0+ (s_a0*𝑟1) e 𝑏=𝑏0+s_b0.(𝜌.𝑟_1+√(1−𝜌^2).𝑟_2

# os  valores  verdadeiros  de 𝑎 e 𝑏 sejam, respectivamente, 𝒂𝟎=𝟑𝟎 e 𝒃𝟎=𝟐𝟎 e que os desvios-padrões verdadeiros sejamiguais: s_a0=s_b0=𝟐,
# de modo que as simulações a seguir só irão diferirpelo coeficiente de correlação, 𝝆.
a0 = 30
s_a0 = 2

b0 = 20
s_b0 = 2

Ps = [+0.75, -0.75, 0, -0.25, +0.5, -0.9, +0.95]
Faz = [1, 1, 0, 0, 0, 0, 0]

# Gere 𝑵=𝟓𝟎𝟎 pares  de  dadoscom 𝝆=+0.75 e os represente em  um  gráfico de  dispersão. Avalie qualitativamente se é fácil perceber alguma relação
# entre os valores de 𝑏 de acordo com os valores de 𝑎. Usando  seus conhecimentos  sobre  binomial,  estime  a incerteza de 𝑛.

N = 500


def gera_dados(p, N):
    r1 = np.random.randn(N)
    r2 = np.random.randn(N)

    a = a0 + s_a0 * r1
    b = b0 + s_b0 * (p * r1 + np.sqrt(1 - p ** 2) * r2)

    return a, b  # me devolve dois arrays



fig = plt.figure()
axs = fig.subplots(3,4)
lin = 0
col = 0

for i in range(len(Ps)):

    p = Ps[i]
    qP = i + 1

    print(f'\n---------({qP}) Letra a:----------')
    print(f'p = {p:+}')
    # grafico de dispersao
    a, b = gera_dados(p, N)
    if i in (3,7,11):
        lin += 1
        col = 0
    elif i != 0:
        col += 1
    axs[lin,col].plot(a, b)
    #axs[0,0].title(f'({qP}) p = {p:+}')
    #axs[0,0].xlabel('Dados a')  # nomeando eixo x
    #axs[0,0].ylabel('Dados b')
    
    # determine  a frequência  relativa  com  que  os  erros  de 𝑎 e 𝑏 têm  o  mesmo  sinal, 𝑓 = 𝑛/𝑁, com sua  respectiva incerteza.
    
    if Faz[i] == 1:
        print(f'---------({qP}) Letra a1: ----------')
        '''Conte o número de vezes, 𝑛,
         em que os erros de 𝑎 e 𝑏 tem o mesmo sinal '''
        n = 0
        for i in range(N):
            erro_a = a[i] - a0
            erro_b = b[i] - b0
            if erro_a * erro_b > 0:  # se os dois tiverem mesmo sinal
                n += 1
        print(f'No. vezes que a e b têm o mesmo sinal:\n n = {n}')

        freq = n / N
        s_n = np.sqrt(N * freq * (1 - freq))
        print(f'Incerteza de n: {s_n:.0f}')

        print(f'---------({qP}) Letra a2: ----------')

        s_freq = ((1 / N)) * (s_n)
        print(f'freq relativa n/N: \n {freq:.3f}({s_freq:.3f})')
        
        # Calcule a  covariância  amostral, 𝑉𝑎𝑏, e  a  correspondente  correlação  amostral, 𝑅, dos 𝑁 pares  de valores de 𝑎 e 𝑏 gerados.
        
        print(f'---------({qP}) Letra a3: ----------')

        # calculo da COVARIANCIA AMOSTRAL e seu coeficiente
        a, b = gera_dados(p, N)
        s_a = np.std(a, ddof=1)  # incerteza de a
        s_b = np.std(b, ddof=1)  # incerteza de b
        am = np.mean(a)  # média dos dados de a
        bm = np.mean(b)  # média dos dados de b
        er_a = np.zeros(N)
        er_b = np.zeros(N)
        for i in range(N):
            er_a[i] = (a[i] - am)
            er_b[i] = (b[i] - bm)

        cov = (1 / (N - 1)) * (np.sum((er_a) * (er_b)))  # COVARIANCIA
        R = cov / (s_a * s_b)  # coef de CORRELAÇÃO AMOSTRAL

        scov = s_a * s_b * (np.sqrt((1 + R ** 2) / (N - 1)))
        sR = (1 - R ** 2) / np.sqrt(N - 1)

        print(f'Covariância amostral (e incerteza): \n{cov:+.2f}({scov:.2f})')
        print(f'Correlação amostral (e incerteza): \n{R:+.3f}({sR:.3f})')

        print(f'---------({qP}) Letra a4: ----------')

        w = np.zeros(N)
        for i in range(N):
            w[i] = a[i] + b[i]

        sw = np.std(w, ddof=1)
        inc_sw = sw / (np.sqrt(2 * (N - 1)))  # incerteza do desvio-padrão amostral
        print(f'Desvpad de w=(a + b) e sua incerteza:\n{sw:.2f}({inc_sw:.2f})')

        print(f'---------({qP}) Letra a5: ----------')

        z = np.zeros(N)
        for i in range(N):
            z[i] = a[i] - b[i]

        sz = np.std(z, ddof=1)
        inc_sz = sz / (np.sqrt(2 * (N - 1)))  # incerteza do desvio-padrão amostral
        print(f'Desvpad de z=(a - b) e sua incerteza:\n{sz:.2f}({inc_sz:.2f})')

fig.savefig('a18_0plot.png')
