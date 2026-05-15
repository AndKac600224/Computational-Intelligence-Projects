
#######################################################################
#--------------------------PROBLEM KOMIWOJAŻERA -----------------------
#######################################################################

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import time

SEED_VAL = 42
POLE = 300
K = 500 #warunek stopu
N = 50 #ilość punktów (genów w każdym chromosomie)
M = 30 #ilość chromosomów w populacji
P_cross = 75 #prawdopodobieństwo krzyżowania
P_mut = 25 #prawdopodobieństwo mutacji

random.seed(SEED_VAL)
np.random.seed(SEED_VAL)
# Obszar do analizy i losowanie punktów -----------------------------------------------------------------------------

df_points = pd.DataFrame(0, columns = ['x', 'y'], index=range(1, N+1))
points = []
for i in range(0,N):
    x_curr = random.randint(0, POLE+1)
    y_curr = random.randint(0, POLE+1)

    while [x_curr, y_curr] in points:
        x_curr = random.randint(0, POLE+1)
        y_curr = random.randint(0, POLE+1)

    points.append([x_curr, y_curr])
    df_points.iloc[i, :] = [x_curr, y_curr]

# print(df_points)


# Tworzenie M-osobowej populacji dla N osobników-----------------------------------------------------------------------

nr_list = [f'pt_{i}' for i in range(1, N+1)]
df_population = pd.DataFrame(0, index=range(1, M+1), columns=[*nr_list, 'sum_dist', 'population_nr'])

nr_list = [int(i) for i in range(1,N+1)]
for k in range(0,M):
    temp_list = nr_list.copy()
    random.shuffle(temp_list)
    df_population.iloc[k, 0:N] = temp_list
    df_population.loc[k+1, 'population_nr'] = k+1

# print(df_population)

# tworzenie funkcji dystansu euklidesowego i jej wdrożenie ------------------------------------------------------------

def dist_calc(x_1, y_1, x_2, y_2):
    dist = np.sqrt((x_2-x_1)**2 + (y_2 - y_1)**2)
    return dist

def dist_calc_for_gens(df, M, N):
    for i in range(0,M):
        sum_curr_pop = 0
        for j in range(0, N-1):
            nr_curr = df.iloc[i, j]
            nr_curr_next = df.iloc[i, j+1]

            x_1_curr = df_points.loc[nr_curr, 'x']
            y_1_curr = df_points.loc[nr_curr, 'y']
            x_2_curr = df_points.loc[nr_curr_next, 'x']
            y_2_curr = df_points.loc[nr_curr_next, 'y']

            dist_curr = dist_calc(x_1_curr, y_1_curr, x_2_curr, y_2_curr)
            sum_curr_pop += dist_curr

        comeback_dist = dist_calc(df_points.loc[df_population.iloc[i, 0], 'x'], df_points.loc[df_population.iloc[i, 0], 'y'],
                                  df_points.loc[df_population.iloc[i, N-1], 'x'], df_points.loc[df_population.iloc[i, N-1], 'y'])
        df.loc[i+1, 'sum_dist'] = int(sum_curr_pop + comeback_dist)
    return df


def dist_calc_for_single_child(child_list, N):
    sum_curr_pop = 0
    for j in range(0,N-1):
        nr_curr = child_list[j]
        nr_curr_next = child_list[j + 1]
        x_1_curr = df_points.loc[nr_curr, 'x']
        y_1_curr = df_points.loc[nr_curr, 'y']
        x_2_curr = df_points.loc[nr_curr_next, 'x']
        y_2_curr = df_points.loc[nr_curr_next, 'y']

        dist_curr = dist_calc(x_1_curr, y_1_curr, x_2_curr, y_2_curr)
        sum_curr_pop += dist_curr

    comeback_dist = dist_calc(df_points.loc[child_list[0], 'x'], df_points.loc[child_list[0], 'y'],
                              df_points.loc[child_list[N-1], 'x'], df_points.loc[child_list[N-1], 'y'])
    return int(sum_curr_pop + comeback_dist)

df_population = dist_calc_for_gens(df_population, M, N)
# print(df_population)


# Selekcja rankingowa + sukcesja elitarna + krzyzowanie + mutacja + nowe pokolenia aż warunek stopu == TRUE -----------


def crossover(p1, p2):
    size = len(p1)
    child = [0] * size

    locus1 = random.randint(0, size-2)
    locus2 = random.randint(locus1+1, size-1)
    child[locus1:locus2+1] = p1[locus1:locus2+1] #tu są teraz kopie

    p2_rest = [k for k in p2 if k not in child] #tu biezremy reszte z p2 - niekopie
    p2_idx = 0
    for i in range(size):
        if child[i] == 0:
            child[i] = p2_rest[p2_idx]
            p2_idx +=1

    return child



def mutation(ch1):

    loc1 = random.randint(0, len(ch1)-1)
    value = ch1[loc1]
    while (loc1 + value)% len(ch1) == loc1:
        value = random.randint(1, len(ch1)-1)
        ch1[loc1] = value
    #zeby nie trafic w to samo mieejsce bo bez sensu mutacja

    loc2 = (loc1 + value) % len(ch1) # jesli by wyszedl poza zakres to nawrotka
    ch1[loc1], ch1[loc2] = ch1[loc2], ch1[loc1]
    return ch1

############# WYKRES ANIMOWANY
# plt.ion()
# fig, ax = plt.subplots(figsize=(8, 8))
# ax.set_xlim(-10, POLE + 10)
# ax.set_ylim(-10, POLE + 10)
# ax.set_title("Ewolucja trasy Komiwojażera")
# line, = ax.plot([], [], 'ro-', lw=1, markersize=4, alpha=0.6)
# base_point, = ax.plot([], [], 'bs', markersize=8, label='Start/Meta')
# info_text = ax.set_title('', fontsize=12, fontweight='bold')
# plt.legend(loc='upper right')
# ############# WYKRES ANIMOWANY

best_scores = pd.DataFrame(columns=['Population number', 'Lowest total distance in population',
                                    'Average total distance in population', 'Highest total distance in population'], index=range(0,500))

count_all = 0
while count_all < K:

    if count_all >= 1:
        df_population = df_population.sort_values(by='sum_dist')

    parents = df_population.iloc[:int(0.25*M), :] #wybieramy 25% najlepszych
    new_population = parents.iloc[:2, :].values.tolist() #sukcesja elitarna

    while len(new_population) != M:  #poki nie stworzy M-elementowej nowej populacji

        n1 = random.randint(0, int(0.25*M)-1)
        n2 = random.randint(0, int(0.25*M)-1)
        while n1 == n2:
            n2 = random.randint(0, int(0.25*M)-1)
        parent1 = parents.iloc[n1, 0:N].tolist()
        parent2 = parents.iloc[n2, 0:N].tolist()

        #prawdopodob. krzyzowania
        help_list = [1] * P_cross + [0] * (100-P_cross)
        help_nr = random.choice(help_list)
        if help_nr == 1:
            child = crossover(parent1, parent2)
        else:
            child = random.choice([parent1, parent2]).copy() #wybiera randomowego rodzica - klon gdy nie trafi P crossover

        #prawdopodob. mutacji
        help_list2 = [1] * P_mut + [0] * (100-P_mut)
        help_nr = random.choice(help_list2)
        if help_nr == 1:
            child = mutation(child)

        curr_dist = dist_calc_for_single_child(child, N)
        full_child = child + [curr_dist, len(new_population)+1]
        new_population.append(full_child)

    df_population = pd.DataFrame(new_population, columns=df_population.columns)

    ############# WYKRES ANIMOWANY
    # best_chromosome = df_population.iloc[0, 0:N].tolist()
    # best_dist = df_population.iloc[0, -2]
    # ordered_points = best_chromosome + [best_chromosome[0]]
    # x_coords = [df_points.loc[pt, 'x'] for pt in ordered_points]
    # y_coords = [df_points.loc[pt, 'y'] for pt in ordered_points]
    # line.set_data(x_coords, y_coords)
    # base_x = df_points.loc[best_chromosome[0], 'x']
    # base_y = df_points.loc[best_chromosome[0], 'y']
    # base_point.set_data([base_x], [base_y])
    # ax.set_title(f'Generacja: {count_all} | Najlepszy dystans: {best_dist}', color='darkblue')
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    # plt.pause(0.001)
    # ############# WYKRES ANIMOWANY

    if count_all == 0:
        first_dist = df_population.iloc[0, -2]
    df_population = df_population.sort_values(by='sum_dist')
    if count_all % 25 == 0:
        time.sleep(0.25)
        print(f'Najlepszy osobnik w {count_all} populacji to chromosom nr {df_population.iloc[0, -1]} z wynikiem dystansu: {df_population.iloc[0, -2]}.')
    best_scores.iloc[count_all,:] = [count_all, df_population.iloc[0, -2], np.mean(df_population.iloc[:,-2]), df_population.iloc[-1, -2]]
    count_all += 1

end_dist = df_population.iloc[0, -2]

print(f'Po {K} populacjach spadek wartości funkcji dystansu nastąpił o {round(((first_dist - end_dist) / first_dist) * 100, 2)}%.')

################### WYKRES LINEPLOT
# fig, ax= plt.subplots(figsize=(14,8))
# sns.lineplot(best_scores, x='Population number', y='Lowest total distance in population', ax=ax, linewidth=2, color='green', label='Lowest')
# sns.lineplot(best_scores, x='Population number', y='Average total distance in population', ax=ax, linewidth=2, color='orange', label='Average')
# sns.lineplot(best_scores, x='Population number', y='Highest total distance in population', ax=ax, linewidth=2, color='red', label='Highest')
# ax.set_title('Total distance trend by the population number (COUNT_GENERATION=500, P_cross = 75%, P_mut = 25%)', fontsize=16)
# ax.grid(True, linestyle='--', alpha=0.6)
# ax.legend()
# plt.show()
################### WYKRES LINEPLOT


