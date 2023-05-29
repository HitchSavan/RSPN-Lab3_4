import pandas as pd
import numpy as np
import math
import Phase_scope as Pc # подключение переменных из скрипта Phase_scope.py

# Вводим значения высоты, длительности и количества шагов
#inp_ampl_z = float(input('Введите значение высоты шага: '))
#data_time = float(input('Введите значение длительности шага: '))
#num_of_step = int(input('Введите количество шагов: '))
inp_ampl_z = np.random.random() * 0.3 + 0.1
data_time = np.random.random() + 1
num_of_step = int(np.random.random() * 9 + 1)
print(f'Случайная амплитуда: {inp_ampl_z}\nСлучайное время шага: {data_time}\nСлучайное количество шагов: {num_of_step}')

# Загружаем данные шагов и считываем данные по осям
data = pd.read_excel('new_data.xlsx')
x_move = np.array(data['X'])
z_move = np.array(data['Z'])

# Масштабируем данные
max_z_move = max(z_move) # Максимальная значение высоты по Z из исходных данных
for i in range(len(z_move)):
    x_move[i], z_move[i] = x_move[i]*inp_ampl_z/max_z_move, z_move[i]*inp_ampl_z/max_z_move

# Создаем данные с несколькими шагами и время
some_x_move = [] # Список нескольких значенией по X
some_z_move = [] # Список нескольких значенией по Z
time = [i*data_time/len(x_move) for i in range(len(z_move)*num_of_step)] # Время

for i in range(num_of_step):
    some_z_move.extend(z_move) # Дублируем перемещение по Z
    for j in range(len(x_move)):
        some_x_move.append(x_move[j] + x_move[len(x_move)-1]*i) # Накапливаеи перемещение по X

# Добавляем шумы
for i in range(len(time)):
    some_x_move[i] += (np.random.random() * 2 - 1)*0.001
    some_z_move[i] += (np.random.random() * 2 - 1)*0.001

# Расчитываем скорость
x_speed = np.gradient(some_x_move, time)
z_speed = np.gradient(some_z_move, time)

# Расчитываем ускорение
x_acceleration = np.gradient(x_speed, time)
z_acceleration = np.gradient(z_speed, time)

# Разбиваем ускорения на отдельные шаги
x_acceleration_solo = np.hsplit(x_acceleration, num_of_step)
z_acceleration_solo = np.hsplit(z_acceleration, num_of_step)

# Рассчитываем среднее и СКО шага
short_time = [i*data_time/len(x_move) for i in range(len(x_move))]
x_acc_mean = Pc.x_acceleration # среднее ускорение по оси X
z_acc_mean = Pc.z_acceleration # среднее ускорение по оси Z
x_acc_std = np.std(x_acceleration_solo, axis=0) # СКО ускорения по оси X
z_acc_std = np.std(z_acceleration_solo, axis=0) # СКО ускорения по оси Z
x_acc_plus = x_acc_mean + x_acc_std
x_acc_minus = x_acc_mean - x_acc_std
z_acc_plus = z_acc_mean + z_acc_std
z_acc_minus = z_acc_mean - z_acc_std

# Рассчитываем фазы
phase_scope = Pc.phase_scope
for i in range(len(phase_scope)):
    phase_scope[i] = phase_scope[i]*data_time/len(x_move)

# Расчет значений темпа и ритма
Ritm = 60/data_time
Temp = x_move[len(x_move)-1]*60/(data_time)
print(f'Средний ритм равен: {Ritm}')
print(f'Средний темп равен: {Temp}')

# Расчет параметров шага
g_ampl_z = z_move.max()
print(f'Расчитанная амплитуда шага: {g_ampl_z}')

g_num_of_steps = 0
z_treshold = g_ampl_z * 0.9
flag = False
for z in some_z_move:
    if z >= z_treshold and not flag:
        g_num_of_steps += 1
        flag = True
    if z < z_treshold:
        flag = False

print(f'\nРасчитанное количество шагов: {g_num_of_steps}')

g_step_time = phase_scope[-1]
print(f'Расчитанное время шага: {g_step_time}')

g_step_len = some_x_move[-1] / g_num_of_steps
print(f'Расчитанная длина шага: {g_step_len}')