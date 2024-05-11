```python

import os
import matplotlib.pyplot as plt
import pandas as pd
from primary_functions import get_innings
from primary_functions import runcounter
from primary_functions import get_ob_states


def calculate_steal_expected_value(base_state, success_prob, matrix_dict):
    runner_positions = (base_state[:3])
    outs = int(base_state[3])
    
    if runner_positions == "100":
        successful_steal_state = "010"
        failed_steal_state = "000"
    elif runner_positions == "010":
        successful_steal_state = "001"
        failed_steal_state = "000"
    elif runner_positions == "001":
        successful_steal_state = "000"
        failed_steal_state = "000"
    else:
        steal_runner = input("Multiple runners on base. Enter the runner stealing (1 for first, 2 for second, 3 for third): ")
        if runner_positions == "110":
            if steal_runner == "2":
                successful_steal_state = "101"
                failed_steal_state = "100"
        elif runner_positions == "101":
            if steal_runner == "1":
                successful_steal_state = "011" 
                failed_steal_state = "001"
            if steal_runner == "3":
                successful_steal_state = "100" 
                failed_steal_state = "100"
        elif runner_positions == "011":
            if steal_runner == "3":
                successful_steal_state = "010"
                failed_steal_state = "010"


    successful_steal_key = successful_steal_state + str(outs)
    failed_steal_key = failed_steal_state + str(outs+1)
    
    success_value = matrix_dict[successful_steal_key]
    if runner_positions[2] == "1":
        success_runs = (success_value[1] / success_value[0])+1
    else:
        success_runs = (success_value[1] / success_value[0])

    if outs <=1:
        failed_value = matrix_dict[failed_steal_key]
        failed_runs = failed_value[1] / failed_value[0]
    else:
        failed_runs = 0
    original_value = matrix_dict[base_state]
    original_runs = original_value[1]/original_value[0]

    expected_runs = success_runs*success_prob + failed_runs*(1-success_prob)
    if expected_runs > original_runs:
        return "This steal is beneficial", success_runs, failed_runs
    else: return "This steal is not beneficial", success_runs, failed_runs

    

base_state = input("Enter the current base state (e.g., 1000 for runner on first and no outs): ")
success_prob = float(input("Enter the probability of success of the steal (between 0 and 1): "))

result = calculate_steal_expected_value(base_state, success_prob, matrix_dict)
print(result)
    
```
