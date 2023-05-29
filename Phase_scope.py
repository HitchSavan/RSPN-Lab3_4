import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Задаем длительность шага, амплитуду и подгружаем данные
datas = pd.read_excel('new_data.xlsx') # считывание координат перемещений
time = [i for i in range(len(datas['X']))] # индекс времени в пределах одного шага

# Разбиваем данные по осям
x_move = pd.Series(datas['X']).rolling(5).mean() # перемещение по оси X
z_move = pd.Series(datas['Z']).rolling(5).mean() # перемещение по оси Z

# Определяем значения скорости и ускорения
x_speed = np.gradient(x_move, time) # скорость по оси X
z_speed = np.gradient(z_move, time) # скорость по оси Z

x_acceleration = np.gradient(x_speed, time) # ускорение по оси X
z_acceleration = np.gradient(z_speed, time) # ускорение по оси Z

phase_scope = [] # индекс фаз шага
item = len(time)
while len(phase_scope) != 4:
    if np.gradient(z_acceleration, time)[item-1]*np.gradient(z_acceleration, time)[item-2] <= 0: # нахождение локальных экстремумов
        phase_scope.append(item-1) # добавление индекса фазы шага
    item = item - 1
phase_scope.reverse() # разворот вектора индексов