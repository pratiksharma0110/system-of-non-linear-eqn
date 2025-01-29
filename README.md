# Numerical Methods for Solving Systems of Nonlinear Equations

This project implements numerical methods to solve systems of nonlinear equations using Python. The solution leverages Newton's method for approximating the roots of the system, and MATLAB is used for plotting equations based on metadata.

## Features

- **Dynamic Equation Input:** Users can input up to 2 or 3 nonlinear equations.
- **Jacobian Calculation:** Automatically computes the Jacobian matrix for the system.
- **Root Calculation:** Implements Newton's method to find the solution.
- **File Management:** Saves results in `results.csv` and equation metadata in `metadata.txt`.
- **MATLAB Integration:** Reads metadata and results to generate plots.

## File Structure

- `main.py`: Main entry point for the application. Handles user inputs and coordinates between functions.
- `functions.py`: Contains helper functions for equation parsing, Jacobian computation, and root finding.
- `metadata.txt`: Stores variable and equation information for MATLAB plotting.
- `results.csv`: Contains computed roots of the system.
- `plot.m`: MATLAB script for plotting equations using data from `metadata.txt` and `results.csv`.

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/pratiksharma0110/system-of-non-linear-eqn
   cd system-of-non-linear-eqn
   ```

2. Install dependencies:

   ```bash
   pip install sympy
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

4. Follow the prompts to input equations, initial guesses, and desired tolerance.

5. Use the generated `metadata.txt` and `results.csv` in MATLAB/OCTAVE with `plot.m` to visualize the equations.

## Example

### Input

- Number of equations: 2
- Equations:
  - `x**2 + y**2 - 4`
  - `x**2 - y**2 - 1`
- Initial guess: `x = 1.0, y = 1.0`
- Tolerance: `0.001`

### Output

- Roots: `[x = 1.65, y = 0.98]` (example output)
- Files:
  - `results.csv`:
    ```csv
    1.65,0.98
    ```
  - `metadata.txt`:
    ```
    Variables:
    x, y
    Equations:
    x^2 + y^2 - 4
    x^2 - y^2 - 1
    ```

### MATLAB Plot

Run `plot.m` in MATLAB to visualize the equations.

## Error Handling

- Ensures the number of equations is 2 or 3.
- Validates input equation format.
- Checks if the Jacobian matrix is singular and raises an error if so.

## Requirements

- Python 3.8+
- MATLAB (for plotting)

## Contributing

Feel free to fork this repository and submit pull requests.

## License

