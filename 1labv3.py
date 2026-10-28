#============================================================
# Лабораторная работа №1. Вариант 3
# Моделирование амплитудной и частотной модуляции (Python)
# ============================================================
import numpy as np
import matplotlib.pyplot as plt

# ---------- 1. Диапазон времени ----------
# t = 1.0 ... 3.0 с шагом 0.001
# np.arange не включает правый конец, поэтому берём 3.0 + 0.001/2
t = np.arange(1.0, 3.0 + 0.0005, 0.001)

# ---------- 2. Модулирующий сигнал ----------
W1 = 2 * np.pi * 0.6       # W1/2pi = 0.6
W2 = 2 * np.pi * 0.9       # W2/2pi = 0.9
A  = np.sin(W1 * t) + np.cos(W2 * t)

# ---------- 3. Амплитудная модуляция ----------
W0   = 2 * np.pi * 10      # несущая: W0/2pi = 10
F_am = (1 + A) * np.cos(W0 * t)

plt.figure(figsize=(11, 5))
plt.plot(t,  A,    color='b', label='A(t) — модулирующий')
plt.plot(t, -A,    color='g', label='−A(t) — отражённый')
plt.plot(t,  F_am, color='r', linewidth=0.8, label='F_am(t) — АМ-сигнал')
plt.grid(True, which='both', linestyle=':')
plt.title('Амплитудная модуляция (вариант 3)')
plt.xlabel('t, с'); plt.ylabel('Амплитуда')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('am_variant3.png', dpi=150)   # сохранить для отчёта
plt.show()

# ---------- 4. Частотная модуляция ----------
K    = 2 * np.pi * 5                       # индекс девиации
F_fm = np.cos((W0 + K * A) * t)

plt.figure(figsize=(11, 5))
plt.plot(t, A,    color='b', label='A(t) — модулирующий')
plt.plot(t, F_fm, color='m', linewidth=0.8, label='F_fm(t) — ЧМ-сигнал')
plt.grid(True, which='both', linestyle=':')
plt.title('Частотная модуляция (вариант 3)')
plt.xlabel('t, с'); plt.ylabel('Сигнал')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('fm_variant3.png', dpi=150)
plt.show()
