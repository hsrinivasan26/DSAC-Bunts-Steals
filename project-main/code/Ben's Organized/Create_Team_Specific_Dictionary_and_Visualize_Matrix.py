```python
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from primary_functions import get_innings
from primary_functions import runcounter
from primary_functions import get_ob_states

def create_teame_matrix():
    if __name__ == "__main__":
        print("Start")    
        matrix_dict_team = {
            '0000':[0,0],
            '0001': [0, 0],
            '0002': [0, 0],
            '1000': [0, 0],
            '1001': [0, 0],
            '1002': [0, 0],
            '0100': [0, 0],
            '0101': [0, 0],
            '0102': [0, 0],
            '1100': [0, 0],
            '1101': [0, 0],
            '1102': [0, 0],
            '0010': [0, 0],
            '0011': [0, 0],
            '0012': [0, 0],
            '1010': [0, 0],
            '1011': [0, 0],
            '1012': [0, 0],
            '0110': [0, 0],
            '0111': [0, 0],
            '0112': [0, 0],
            '1110': [0, 0],
            '1111': [0, 0],
            '1112': [0, 0],
        }
    # Directory where the files are located
    directory = "events"

    team = input("Three letter code for team (example: New York Mets = NYN):")

    # Filter files containing "NYN"
    files = [file for file in os.listdir(directory) if team in file]

    # Iterate through filtered files
    for filename in files:
        path = os.path.join(directory, filename)
        innings = get_innings(path)
        for inning in innings:
            try:
                get_ob_states(inning, runcounter(inning), matrix_dict_team)
            except Exception as e:
                print(f"Error processing {path}: {e}")
                continue

    print(matrix_dict_team)


matrix = np.zeros((8,3))

for key, value in matrix_dict_team.items():
    row = int(key[0:3], 2)
    col = int(key[3])
    ratio = value[1] / value[0]
    matrix[row, col] = ratio
    print([row,col])

print(matrix)
# Labels for rows and columns
row_labels = [format(i, '03b') for i in range(8)]
col_labels = ['0', '1', '2']

# Plot the table
plt.figure(figsize=(8, 6))
plt.table(cellText=np.round(matrix, 2),
          rowLabels=row_labels,
          colLabels=col_labels,
          loc='center')
plt.axis('off')  # Hide axes
plt.title('Run-expectancy Matrix')
plt.show()
```
