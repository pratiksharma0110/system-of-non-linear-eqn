from sympy import Matrix, sympify, symbols, diff
import csv


def compute_tolerance():
    num = int(input("Enter the number of decimals: "))
    if num <= 0:
        raise ValueError("Number of decimals must be positive.")
    return 0.5 * 10**-num


def create_variables(num):
    if num == 2:
        return symbols("x y")
    elif num == 3:
        return symbols("x y z")
    else:
        raise ValueError("Only supports 2 or 3 equations")


def create_eqns(num):
    eqns = []
    for i in range(1, num + 1):
        while True:
            try:
                eqn = input(f"Equation {i}: ")
                eqns.append(sympify(eqn))
                break
            except Exception as e:
                print(f"Invalid equation format. Please try again. Error: {e}")
    return Matrix(eqns)


def initial_guess(vars):
    guess = []
    for var in vars:
        g = float(input(f"Initial Guess {var}: "))
        guess.append(g)
    return Matrix(guess)


def compute_jacobian(eqns, vars):
    jacobian = []
    for eqn in eqns:
        j = [diff(eqn, var) for var in vars]
        jacobian.append(j)
    jacobian_matrix = Matrix(jacobian)
    if jacobian_matrix.det() == 0:
        raise ValueError("Jacobian matrix is singular.")
    return jacobian_matrix


def compute_root(guess, eqns, j, vars, tol):
    max_iter = 1000
    jacobian_matrix = Matrix(j)
    f_matrix = Matrix(eqns)
    for i in range(max_iter):
        jacobian = Matrix(jacobian_matrix.subs(dict(zip(vars, guess))))

        if jacobian.det() == 0:
            raise ValueError(
                f"Jacobian matrix is singular at iteration {i}. Unable to proceed."
            )

        j_inv = jacobian.inv()
        f_value = Matrix(f_matrix.subs(dict(zip(vars, guess))))
        delta = j_inv * f_value
        guess = guess - delta

        if delta.norm() < tol:
            print(f"Converged in {i + 1} iterations.")
            return guess

    raise ValueError(
        "Newton's method did not converge within the maximum number of iterations."
    )


def save_results(variables, equations, root, filename="results.csv"):

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(root)
    print(f"Root saved to {filename}")

    with open("metadata.txt", mode="w") as file:
        file.write("Variables:\n")
        file.write(", ".join(map(str, variables)) + "\n")
        file.write("Equations:\n")
        file.write("\n".join(map(str, equations)) + "\n")
    print("Variables and equations saved to metadata.txt")
