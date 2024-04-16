inning1 = [['play', '9', '0', 'zunim001', '22', '.BSBSFFS', 'K'], ['play', '9', '0', 'almoa001', '12', 'FBSS', 'K'], ['play', '9', '0', 'millb002', '00', 'X', 'S6/G'], ['play', '9', '0', 'canor001', '11', 'BCX', 'D9/L.1-3'], ['play', '9', '0', 'smoaj001', '11', 'FBX', 'HR/9/F.3-H;2-H'], ['play', '9', '0', 'morrl001', '31', 'CBBBB', 'W'], ['play', '9', '0', 'seagk001', '22', 'BCBFF>B', 'SB2'], ['play', '9', '0', 'seagk001', '32', 'BCBFF>B.>B', 'W'], ['play', '9', '0', 'saunm001', '32', '.CBFBB>B', 'W.2-3;1-2'], ['play', '9', '0', 'ackld001', '12', 'CCBX', 'T9/L.3-H;2-H;1-H'], ['play', '9', '0', 'zunim001', '02', 'SSC', 'K']]
#, [['play', '9', '1', 'kendh001', '32', '.CSBFBBX', '63/G'], ['play', '9', '1', 'iannc001', '02', 'FSS', 'K'], ['play', '9', '1', 'aybae001', '32', 'BBBCCFX', '3/G']]


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
    

    totalruns = runs
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

                    #end of loop two
        print(bases,runs,outs)


get_ob_states(inning1)