from matplotlib import pyplot as plt
import numpy as np
import Lab_4 as Lab  # подключение переменных из скрипта Lab_4.py

# Графики шагов
fig1, [[axs0, axs1], [axs2, axs3], [axs4, axs5]] = plt.subplots(3, 2)
fig1.subplots_adjust(hspace=0.5, top=0.9, bottom=0.1)
axs0.plot(Lab.time, Lab.some_x_move)
axs0.set_title('Перемещение по X')
axs1.plot(Lab.time, Lab.some_z_move)
axs1.set_title('Перемещение по Z')
axs2.plot(Lab.time, Lab.x_speed)
axs2.set_title('Скорость по X')
axs3.plot(Lab.time, Lab.z_speed)
axs3.set_title('Скорость по Z')
axs4.plot(Lab.time, Lab.x_acceleration)
axs4.set_title('Ускорение по X')
axs5.plot(Lab.time, Lab.z_acceleration)
axs5.set_title('Ускорение по Z')

# Графики средних ускорений, СКО и фаз шага
fig2, [axs0, axs1] = plt.subplots(1, 2)
y_min, y_max = np.nanmin(Lab.x_acceleration) - 1, np.nanmax(Lab.x_acceleration) + 1
axs0.plot(Lab.short_time, Lab.x_acc_mean, label='Среднее', color='red')
axs0.plot(Lab.short_time, Lab.x_acc_plus, label='Среднее + СКО', linewidth=1, linestyle='--', color='gray')
axs0.plot(Lab.short_time, Lab.x_acc_minus, label='Среднее - СКО', linewidth=1, linestyle='--', color='brown')
axs0.fill_between(Lab.short_time, y_min, y_max, where=(np.array(Lab.short_time)<=Lab.phase_scope[0]), alpha=0.2, label='Период опоры')
axs0.fill_between(Lab.short_time, y_min, y_max, where=(np.array(Lab.short_time)>=Lab.phase_scope[0])&(np.array(Lab.short_time)<=Lab.phase_scope[1]), alpha=0.2, label='Фаза переноса 2')
axs0.fill_between(Lab.short_time, y_min, y_max, where=(np.array(Lab.short_time)>=Lab.phase_scope[1]), alpha=0.2, label='Фаза переноса 1')
axs0.margins(x=0, y=0)
axs0.set_title('Ускорение по X')
axs0.legend()
axs0.grid()
axs1.plot(Lab.short_time, Lab.z_acc_mean, label='Среднее', color='red')
axs1.plot(Lab.short_time, Lab.z_acc_plus, label='Среднее + СКО', linewidth=1, linestyle='--', color='gray')
axs1.plot(Lab.short_time, Lab.z_acc_minus, label='Среднее - СКО', linewidth=1, linestyle='--', color='brown')
axs1.fill_between(Lab.short_time, y_min, y_max, where=(np.array(Lab.short_time)<=Lab.phase_scope[0]), alpha=0.2, label='Период опоры')
axs1.fill_between(Lab.short_time, y_min, y_max, where=(np.array(Lab.short_time)>=Lab.phase_scope[0])&(np.array(Lab.short_time)<=Lab.phase_scope[1]), alpha=0.2, label='Фаза переноса 2')
axs1.fill_between(Lab.short_time, y_min, y_max, where=(np.array(Lab.short_time)>=Lab.phase_scope[1]), alpha=0.2, label='Фаза переноса 1')
axs1.margins(x=0, y=0)
axs1.set_title('Ускорение по Z')
axs1.legend()
axs1.grid()

plt.show()