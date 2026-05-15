
### --------------------------------------- ESTYMACJA LICZBY π Z UŻYCIEM MONTE CARLO -----------------------------###


import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#########################
N_ITER = 1000
#########################
n_iters = [100, 1000, 10000, 100000]
data_for_boxplots = []
r = 1
pts = pd.DataFrame(columns=['X', 'Y', 'isIn', 'estPi'])
list_pts = [pts.copy() for v in range(10)]

for j in range(1,11):
    k=0
    for i in range(1, N_ITER+1):
        x = random.random()
        y = random.random()

        if (x**2 + y**2) <= r**2:
            k += 1
            list_pts[j-1].loc[i-1] = [x, y, 'In', 4 * k / i]
        else:
            list_pts[j-1].loc[i-1] = [x, y, 'Out', 4 * k / i]

sumAll = sum(df['estPi'].iloc[-1] for df in list_pts)
pi_est = sumAll / len(list_pts)


line_x = np.linspace(0, r, 500)
line_y = np.sqrt(r**2-line_x**2)

### Wykres grid -----------------------------------------------------------

# fig, ax = plt.subplots(figsize=(6,6))
# sns.scatterplot(list_pts[0], x='X', y='Y', hue='isIn', palette='coolwarm', legend=True, ax=ax, s=8)
# sns.lineplot(x=line_x, y=line_y, color='black', linewidth=2, label='y_teo')
# plt.title(f"Random X and Y, est. π: {round(pi_est,4)}")
# plt.legend(loc='upper left', title="Point distribution", markerscale=2)
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.grid(True)
# plt.show()

### Wykres path -------------------------------------------------------------

# fig2, ax2 = plt.subplots(figsize=(10,6))
# for j in range(1,9):
#     sns.lineplot(data=list_pts[j-1], x=list_pts[j-1].index, y='estPi', linewidth=1, color='orange',ax=ax2)
# sns.lineplot(data=list_pts[9], x=list_pts[j-1].index, y='estPi', linewidth=1, color='orange', label='est. PI path',ax=ax2)
# sns.lineplot(x=range(1,N_ITER+1), y=3.1416, linewidth=1.5, color='black', label='PI=3.1415',ax=ax2)
# plt.title(f'PI estimation after 10k draws: {round(pi_est,4)} for 10 processes')
# plt.legend(loc='upper right')
# plt.xlabel('n')
# plt.ylim(2, 4)
# plt.xlim(0, N_ITER)
# plt.ylabel('PI estimated')
# plt.show()


### Wykres boxplot -----------------------------------------------------------

for n in n_iters:
    for m in range(10):
        k=0
        for i in range(1, n+1):
            x = random.random()
            y= random.random()
            if (x**2 + y**2) <= r**2:
                k+=1
        pi_est_n = 4*k/n
        data_for_boxplots.append({'N': n, 'PiEst': pi_est_n})

df_final = pd.DataFrame(data_for_boxplots)

plt.figure(figsize=(10,6))
sns.boxplot(data=df_final, x='N', y='PiEst', palette='coolwarm', showmeans=True)
plt.axhline(3.1416, color='red', linewidth=2, label = 'π ≈ 3.1416' )
plt.title('Pi distribution for each N draws')
plt.xlabel('N')
plt.ylabel('Pi est.')
plt.legend()

plt.show()



