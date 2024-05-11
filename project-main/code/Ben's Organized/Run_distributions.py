
import os
import matplotlib.pyplot as plt
import pandas as pd
from primary_functions import get_innings
from primary_functions import runcounter



    


def get_ob_states(inning,totalruns,matrix_dict_new):
    bases = [0, 0, 0]
    runs = 0
    outs = 0
    for play in inning:
        info = play[6]
        if "1-"  in info:
            bases[0] = 0
        if "2-" in info:
            bases[1] = 0
        if "3-" in info:
            bases[2] = 0
        if "-1" in info:
            bases[0] = 1
        if "-2" in info:
            bases[1] = 1
        if "-3" in info:
            bases[2] = 1
        runs += info.count("-H")
        if info[0] in ["S", "W"] or info[:2] in ["HP", "IW"]:
            bases[0] = 1
        elif info[0] == "D":
            bases[1] = 1
        elif info[0] == "T":
            bases[2] = 1
        elif info[:2] == "HR":
            runs += 1
        elif info[:2] in ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'SB', 'NP', 'PB', 'IW']:
            bases[0] = bases[0]
        else:
            outs += 1
        if "CS" in info:
            if "POCS" in info:
                margin = 4
            else:
                margin = 2
            if info[margin] == '2':
                bases[0] = 0
            if info[margin] == '3':
                bases[1] = 0
            if info[margin] == 'H':
                bases[2] = 0
        if "PO" in info and "CS" not in info:
            if info[2] == 1:
                bases[0] = 0
            if info[2] == 2:
                bases[1] = 0
            if info[2] == 3:
                bases[2] = 0
        if info[:2] == "SB":
            if info[2] == '2':
                bases[0] = 0
                bases[1] = 1
            if info[2] == '3':
                bases[1] = 0
                bases[2] = 1
            if info[2] == 'H':
                bases[2] = 0
                runs += 1
        if "DP" in info:
            outs += 1
            split_line = info.split('/')
            fielders = split_line[0]
            baserunners = split_line[1]
            if "GDP" in info:
                if fielders[-1] == '3':
                    bases[0] = 0
                if fielders[-1] in ['4', '6']:
                    bases[1] = 0
                if fielders[-1] == '5':
                    bases[2] = 0
                if fielders[-5] == '3':
                    bases[0] = 0
                if fielders[-5] in ['4', '6']:
                    bases[1] = 0
                if fielders[-5] == '5':
                    bases[2] = 0
            if "LDP" in info or "FDP" in info:
                try:
                    bases[eval(baserunners[4]) - 1] = 0
                except IndexError:
                    bases[0] = bases[0]

                    #end of loop two

        play_key = ''.join(str(num) for num in bases)+str(outs)
        #print(play_key)
        #print([bases, totalruns-runs, outs])

    
        try:
            if totalruns-runs in matrix_dict_new[play_key]:
                matrix_dict_new[play_key][totalruns-runs] +=1
            else:
                matrix_dict_new[play_key][totalruns-runs] = 1

        except:
            continue



def propcounter(freq_dict,needed_runs):
    ret = {}
    for base_state in freq_dict:
        total = sum(freq_dict[base_state].values())
        less = 0
        current_dict = freq_dict[base_state]
        for runs in current_dict:
            if runs<needed_runs:
                less+=current_dict[runs]
        ret[base_state] = 1-less/total
    return ret




#creates dictionary mapping each base state to its distribution of runs scored
#show_plots lets user control whether they want to see histograms for each base state
def distribution_dict(show_plots = False):
    matrix_dict_new = {
        '0000':{},
        '0001': {},
        '0002': {},
        '1000': {},
        '1001': {},
        '1002': {},
        '0100': {},
        '0101': {},
        '0102': {},
        '1100': {},
        '1101': {},
        '1102': {},
        '0010': {},
        '0011': {},
        '0012': {},
        '1010': {},
        '1011': {},
        '1012': {},
        '0110': {},
        '0111': {},
        '0112': {},
        '1110': {},
        '1111': {},
        '1112': {},
    }
    
    for filename in os.listdir("events"):
        path = "events/" + filename
        innings = get_innings(path)
        get_innings(path)
        for inning in innings:
            try:
                get_ob_states(inning,runcounter(inning),matrix_dict_new)
            except:
                continue
    if (show_plots == True):
        for string in matrix_dict_new.keys():
            print("State:", string)
            plt.bar(list(matrix_dict_new[string].keys()), matrix_dict_new[string].values(), color='g')
            plt.show()
    return matrix_dict_new



#takes in dict of frequencies and number of runs needed,
#returns dictionary mapping base state to probability that that number of runs can be attained
def prop_dict(freq_dict,needed_runs):
    ret = {}
    for base_state in freq_dict:
        total = sum(freq_dict[base_state].values())
        less = 0
        current_dict = freq_dict[base_state]
        for runs in current_dict:
            if runs<needed_runs:
                less+=current_dict[runs]
        ret[base_state] = 1-less/total
    return ret



