import numpy as np
import matplotlib.pyplot as plt
from primary_functions import create_matrix
from Update Create_Team_Specific_Dictionary_and_Visualize_Matrix import create_team_matrix(team)

def calculate_difference(team_code):
    # Call the create_team_matrix function to get the dictionary
    matrix_dict_team = create_team_matrix(team_code)

    # Initialize an empty dictionary to store the differences
    difference_dict = {}

    # Iterate through the keys in matrix_dict_team
    for key in matrix_dict_team:
        value1 = matrix_dict_team[key][1] / matrix_dict_team[key][0]
        value2 = matrix_dict[key][1] / matrix_dict[key][0]
        difference_dict[key] = value1 - value2

    # Return the new dictionary with the differences
    return difference_dict

# Example usage:
team_code = input("Enter the three-letter code for the team: ")
differences = calculate_difference(team_code)
print(differences)
