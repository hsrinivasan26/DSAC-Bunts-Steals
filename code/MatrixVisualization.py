import numpy as np
import matplotlib.pyplot as plt
from primary_functions import create_matrix


matrix = np.zeros((8,3))

matrix_dict = create_matrix()

for key, value in matrix_dict.items():
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
