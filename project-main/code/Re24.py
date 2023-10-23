filename = "events/2004OAK.EVA"
f = open(filename, 'r')
lines = f.readlines()
plays = []
for l in lines:
    if "play" in l:
        currentline = l.split(',')
        currentline[6] = currentline[6][:-1]
        plays.append(currentline)

innings = []
inning = []
for i in range(100):
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

print(innings[2])

def get_ob_states(inning):
    bases = [0, 0, 0]
    runs = 0
    for play in inning:
        info = play[6]
        if "1-"  in info:
            bases[0] = 0
        if "2-" in info:
            bases[1] = 0
        if "3-" in info:
            bases[2] = 0
        if "-2" in info:
            bases[1] = 1
        if "-3" in info:
            bases[2] = 1
        if "-H" in info:
            runs += 1
        if info[0] in ["S", "W"] or info[:2] == "HP":
            bases[0] = 1
        if info[0] == "D":
            bases[1] = 1
        if info[0] == "T":
            bases[2] = 1
        if info[:2] == "HR":
            runs += 1
        print([bases, runs])
        
        
    
get_ob_states(innings[2])

    
    
