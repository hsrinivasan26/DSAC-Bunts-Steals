# Fun with the Baseball Run-Expectancy Matrix

## Description
This project provides a variety of functions to construct and play with Run-Expectancy Matrices using box-scores from the past __ major league seasons. All the data comes from Retrosheet. Below is an overview of the different files in the code folder and the functionalities of each. To use, simply clone the repository. We hope that others interested in sabermetrics will enjoy exploring the game through these functions.

## Files

### primary_functions.py:
  Contains several functions important to constructing the matrix that are called in the rest of the files.

### Run_distributions.py:
  This file takes in runs needed as an input and displays a matrix showing the probability of scoring that number of runs for each game state. Also displays a histogram of the distribution of total runs scored for each game state.

### Probability_of_Steal_Needed.py:
  calculates required success rate for a steal attempt to be profitable by evaluating given base state and potential runner using the run expectancy matrix. 
  
### Matrix_Visualization.py:
  Displays created run-expectancy dictionaries as presentable matrices.

### Is_Steal_Beneficial.py:
  Takes in game state and steal success probability as inputs and returns whether or not a steal increases expected number of runs scored.
    
### Difference_Between_League_and_Team_Run_Expectancy_in_Dictionary_and_Matrix.py:
  Takes in a team as input and displays a matrix showing the difference between league and team expected runs for each game state.
  
### Create_Team_Specific_Dictionary_and_Visualize_Matrix.py:
  Takes in a specific team and displays their individual run expectancy matrix.

