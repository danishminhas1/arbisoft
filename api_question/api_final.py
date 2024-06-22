import sys
import requests as req

#Read command line arguments
x = sys.argv[1]
with open(x) as f:
    teams = str(f.readline()).split(",")

#Team 1
main_team = teams[0]

#Team 2
other_team = teams[1]

#Obtain response from API
res = req.get("https://3rbxmjydt1.execute-api.eu-north-1.amazonaws.com/default/icc_matches_played_records").json()

#Initialize list of matches we are interested in
interesting_matches = list()
for match in res:
    if (match["team1"] == main_team) and (match["team2"] == other_team) or (match["team1"] == other_team) and (match["team2"] == main_team):
        interesting_matches.append(match)

#Weighted dictionary for team matches
weight_dict = {}

#Weighted dictionary for all matches
weight_total_dict = {}

for match in interesting_matches:

    #Extract date
    year = int(match["date"][-4:])

    #Extract weight
    if year == 2024:
        weight = 10
    if (2015 <= year) and (year <= 2023):
        weight = year - 2014
    if year < 2015:
        weight = 0.5
    main_team_score = 0
    other_team_score = 0

    #Initialize team scores
    #We need to handle both cases of our main team being team 1 or team 2
    if main_team == match["team1"]:
        for player in match["scoreCardTeam1"]:
            main_team_score += player["score"]
        for player in match["scoreCardTeam2"]:
            other_team_score += player["score"]
    if main_team == match["team2"]:
        for player in match["scoreCardTeam2"]:
            main_team_score += player["score"]
        for player in match["scoreCardTeam1"]:
            other_team_score += player["score"]

    #Make sure a draw didn't occur
    if not main_team_score == other_team_score:
        #Add to total weight
        if weight in weight_total_dict.keys():
            weight_total_dict[weight] += 1
        else:
            weight_total_dict[weight] = 1
    
    #Add to weighted dictionary for the team we are interested in
    if main_team_score > other_team_score:
        if weight in weight_dict.keys():
            weight_dict[weight] += 1
        else:
            weight_dict[weight] = 1
    
#Calculate the weighted average
numerator = 0
denomenator = 0
for weight, no in weight_dict.items(): 
    numerator += weight * no
for weight, no in weight_total_dict.items():
    denomenator += weight* no

#Round answer, add % signs, and display output
print(str(round((numerator/denomenator) * 100, 2)) + "%," + str(100-round((numerator/denomenator) * 100, 2)) + "%")