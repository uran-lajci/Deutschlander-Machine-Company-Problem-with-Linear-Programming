from ortools.linear_solver import pywraplp

def primalSolution():
    solver = pywraplp.Solver('DMC', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Variables
    x = solver.NumVar(2, solver.infinity(), 'x')
    y = solver.NumVar(2, solver.infinity(), 'y')
    s1 = solver.NumVar(0, solver.infinity(), 's1')
    s2 = solver.NumVar(0, solver.infinity(), 's2')
    s3 = solver.NumVar(0, solver.infinity(), 's3')

    # Objective function
    solver.Maximize(24000 * x + 10000 * y)

    # Constraints
    solver.Add(16 * x + 8 * y + s1 == 100) # Rollers constraint
    solver.Add(30 * x + 12 * y + s2 == 160) # Gear cutting constraint
    solver.Add(8 * x + 3 * y + s3 == 40) # Polishing constraint

    # Solve
    status = solver.Solve()

    # Print the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution:')
        print(f'Number of four-color presses: {x.solution_value()}')
        print(f'Number of two-color presses: {y.solution_value()}')
        print(f'Optimal profit: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

def dualSolution():
    solver = pywraplp.Solver('DMC', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Variables
    s1 = solver.NumVar(0, solver.infinity(), 's1')
    s2 = solver.NumVar(0, solver.infinity(), 's2')
    s3 = solver.NumVar(0, solver.infinity(), 's3')

    # Objective function
    solver.Minimize(100 * s1 + 160 * s2 + 40 * s3)

    # Constraints
    solver.Add(16 * s1 + 30 * s2 + 8 * s3 >= 24000) # Profit constraint for four-color presses
    solver.Add(8 * s1 + 12 * s2 + 3 * s3 >= 10000) # Profit constraint for two-color presses

    # Solve
    status = solver.Solve()

    # Print the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution:')
        print(f'Slack variable for rollers constraint: {s1.solution_value()}')
        print(f'Slack variable for gear cutting constraint: {s2.solution_value()}')
        print(f'Slack variable for polishing constraint: {s3.solution_value()}')
        print(f'Optimal cost: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')


primalSolution()
print("---------------------")
dualSolution()