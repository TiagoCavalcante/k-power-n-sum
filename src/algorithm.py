from sympy import Matrix, Symbol, linsolve

# Creates a row containing the powers of the
# line-number from the 1st to the (k + 1)th.
def row(x, k):
  return [x ** a for a in range(1, k + 2)]

# Sum the kth power of the first n natural numbers
# "the hard way".
# This is used as an auxiliary function to create
# a linear system for the formula.
def power_sum(n, k):
  return sum([x ** k for x in range(1, n + 1)])

# Creates the x-th row for the augmented matrix
# using the powers of the line-number and the
# equivalent sum.
def complete_row(x, k):
  return [*row(x, k), power_sum(x, k)]

# Creates the augmented matrix for the linear
# system of the formula.
def augmented_matrix(k):
  return Matrix([
    complete_row(x, k) for x in range(1, k + 2)
  ])

# Generates the formula for the sum of the kth
# power of the first n natural numbers using the
# augmented matrix of its linear system assuming
# that the sum of the kth power is a polynomial
# over n of degree k + 1.
def formula(k):
  matrix = augmented_matrix(k)
  coefficients, = linsolve(matrix)

  n = Symbol('n')
  return sum([
    coefficient * n ** (x + 1)
    for x, coefficient in enumerate(coefficients)
  ])
