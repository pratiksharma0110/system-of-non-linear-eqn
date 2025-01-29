from sympy import Matrix, plot, pprint
from functions import (
    compute_jacobian,
    compute_tolerance,
    create_variables,
    create_eqns,
    initial_guess,
    compute_root,
    save_results,
)


def main():
    try:
        num = int(input("Enter the number of equations: "))
        if num < 2:
            raise ValueError("Number of equations must be at least 2.")

        variables = create_variables(num)
        print(f"Variables: {variables}")
        print("Please refer to the above list before writing equation")

        eqns = create_eqns(num)
        guess = initial_guess(variables)
        jacobian_matrix = compute_jacobian(eqns, variables)
        print("Jacobian Matrix")

        pprint(jacobian_matrix)
        n = int(input("Enter the number of decimals: "))

        tolerance = compute_tolerance(n)

        print(f"Tolerance: {tolerance}")

        root = compute_root(guess, eqns, jacobian_matrix, variables, tolerance, n)
        save_results(variables, eqns, root)
        pprint(root)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
