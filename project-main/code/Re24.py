filename = "events/2004BOS.EVA"
f = open(filename, 'r')
lines = f.readlines()
plays = []
for l in lines:
    if l[:4] == 'play':
        currentline = l.split(',')
        currentline[6] = currentline[6][:-1]
        plays.append(currentline)
innings = []
inning = []
for i in range(len(plays)):
    if i == 0:
        current_inning = '1'
        current_half = '0'
    else:
        current_inning = plays[i-1][1]
        current_half = plays[i-1][2]
    if plays[i][1] == current_inning and plays[i][2] == current_half:
        inning.append(plays[i])
    else:
        innings.append(inning)
        inning = []
        inning.append(plays[i])


def get_ob_states(inning):
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
        if "-H" in info:
            runs += 1
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
                
            
            
            
                
        print([bases, runs, outs])
        
        
    
for i in range(20, 50):
    print(innings[i])
    get_ob_states(innings[i])
    
    
