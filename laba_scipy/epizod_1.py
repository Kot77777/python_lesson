import sympy
from sympy import symbols

rho = symbols('ρ')
mu = symbols('μ')
lamda = symbols('λ')

matrix = sympy.Matrix(9, 9, lambda i, j: 0)
matrix[0, 3] = matrix[1, 4] = matrix[2, 5] = -1/rho
matrix[3, 0] = -(lamda + 2*mu)
matrix[4, 1] = matrix[5, 2] = -mu
matrix[6, 0] = matrix[8, 0] = -lamda

eig = matrix.eigenvals()
for eig, num in eig.items():
    print(f"eigen values: {eig}, multiplicity: {num}")
