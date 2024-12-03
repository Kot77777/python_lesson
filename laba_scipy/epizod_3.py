import sympy as sp
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt


x = sp.symbols('x')
y = sp.Function('y')
equation = sp.Eq(y(x).diff(x), -2 * y(x))
solution = sp.dsolve(equation, y(x), ics={y(0): sp.sqrt(2)})
solut = solution.rhs


def numerical_solver():
    def dydx(y, x):
        return -2 * y

    x_values = np.linspace(0, 10, 100)
    y0 = np.sqrt(2)
    y_values = sc.integrate.odeint(dydx, y0, x_values).flatten()
    return x_values, y_values


x_vals = np.linspace(0, 10, 100)
y_analytical = sp.lambdify(sp.symbols('x'), solut, 'numpy')(x_vals)
x_numerical, y_numerical = numerical_solver()

plt.scatter(x_vals, y_analytical, label='Аналитическое решение', color='blue', s=30)
plt.scatter(x_numerical, y_numerical, marker='*' , label='Численное решение', color='green', s=30)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.title('Решение dy/dx = -2y при y(0) = √2')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.minorticks_on()
plt.savefig('Epizod_3a.png', dpi=300)
plt.show()

x_vals = np.linspace(0, 10, 100)
y_analytical = sp.lambdify(sp.symbols('x'), solut, 'numpy')(x_vals)
_, y_numerical = numerical_solver()

plt.scatter(x_vals, np.abs(y_analytical - y_numerical), label='Разность решений', color='red')
plt.plot(x_vals, np.abs(y_analytical - y_numerical), color='gray', linestyle='-')
plt.xlabel('x')
plt.ylabel('|Аналитическое - численное|')
plt.legend()
plt.title('Разность аналитического и численного решений')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.minorticks_on()
plt.savefig('Epizod_3b.png', dpi=300)
plt.show()

solution = solut
print(f'Символьное решение: {solution}')
