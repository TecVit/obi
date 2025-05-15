from decimal import Decimal, getcontext
import math

# Define precisão suficiente (ex: 15 casas decimais)
getcontext().prec = 25

# Entrada
x_str, y_str, theta_str = input().split()
x = Decimal(x_str)
y = Decimal(y_str)
theta = Decimal(theta_str)

# Conversão de Decimal para float para usar com sin/cos
theta_f = float(theta)
cos_theta = Decimal(str(math.cos(theta_f)))
sin_theta = Decimal(str(math.sin(theta_f)))

# Rotação
x_rot = x * cos_theta - y * sin_theta
y_rot = x * sin_theta + y * cos_theta

# Impressão com 6 casas decimais (arredondamento controlado)
print(f"{x_rot:.6f} {y_rot:.6f}")
