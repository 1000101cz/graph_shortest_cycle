import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming


# Example usage
vertices = ['Jihlava', 'Telc', 'Trebic', 'Dacice', 'JHradec', 'NBystrice', 'MBudejovice', 'Zirovnice', 'Slavonice']
edges = [('Jihlava', 'Telc', 30.1),
         ('Jihlava', 'Trebic', 33.8),
         ('Jihlava', 'Dacice', 42.4),
         ('Jihlava', 'JHradec', 58.9),
         ('Jihlava', 'NBystrice', 65.7),
         ('Jihlava', 'MBudejovice', 46.4),
         ('Jihlava', 'Zirovnice', 38.6),
         ('Jihlava', 'Slavonice', 54.6),
         ('Telc', 'Trebic', 35.2),
         ('Telc', 'Dacice', 12.2),
         ('Telc', 'JHradec', 40.8),
         ('Telc', 'NBystrice', 40.9),
         ('Telc', 'MBudejovice', 32.5),
         ('Telc', 'Zirovnice', 26.1),
         ('Telc', 'Slavonice', 24.5),
         ('Trebic', 'Dacice', 41.9),
         ('Trebic', 'JHradec', 76),
         ('Trebic', 'NBystrice', 71.1),
         ('Trebic', 'MBudejovice', 23),
         ('Trebic', 'Zirovnice', 60.8),
         ('Trebic', 'Slavonice', 54.7),
         ('Dacice', 'JHradec', 35.8),
         ('Dacice', 'NBystrice', 29.7),
         ('Dacice', 'MBudejovice', 30.9),
         ('Dacice', 'Zirovnice', 31.6),
         ('Dacice', 'Slavonice', 13.3),
         ('JHradec', 'NBystrice', 16.8),
         ('JHradec', 'MBudejovice', 67.9),
         ('JHradec', 'Zirovnice', 20.4),
         ('JHradec', 'Slavonice', 37),
         ('NBystrice', 'MBudejovice', 59.3),
         ('NBystrice', 'Zirovnice', 33),
         ('NBystrice', 'Slavonice', 21.1),
         ('MBudejovice', 'Zirovnice', 59.5),
         ('MBudejovice', 'Slavonice', 38.6),
         ('Zirovnice', 'Slavonice', 36.1)
]

distance_matrix = []
for i in range(9):
    row = []
    for j in range(9):
        row.append([])
    distance_matrix.append(row)

for row, city_row in enumerate(vertices):
    for column, city_column in enumerate(vertices):
        if row == column:
            distance_matrix[row][column] = 0
        else:
            for edge in edges:
                if city_row in edge and city_column in edge:
                    distance_matrix[row][column] = edge[-1]
                    break
            else:
                print("Exception")

distance_matrix = np.array(distance_matrix)

permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
print("\nSolution")
solution = ""
for per in permutation:
    solution += vertices[per]
    solution += ' - '
print(solution)
print("Distance ", distance)
