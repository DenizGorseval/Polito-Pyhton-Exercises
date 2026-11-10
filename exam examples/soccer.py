def read_stats(filename):
    try:
        with open(filename, "r") as file:
            stats = [line.strip().split(",") for line in file]
            stats = stats[1:]
    except OSError:
        print("The file cannot be opened")
    
    teams_dict = dict()
    for stat in stats:
        player = stat[0]
        position = stat[1]
        team = stat[2]
        age = 2022 - int(stat[3])
        minutes_played = int(stat[4])
        goals = int(stat[5])
        assists = int(stat[6])
        offsides = int(stat[7])
        reached_crosses = int(stat[8])
        intercepted_balls = int(stat[9])
        recovered_balls = int(stat[12])

        if minutes_played != 0:
            forward_efficiency = float((goals/minutes_played)+(assists/minutes_played)-(offsides/minutes_played))
            if reached_crosses != 0:
                midfield_efficiency = float((intercepted_balls + recovered_balls+(assists/reached_crosses)/minutes_played))
            else:
                midfield_efficiency = 0
        else:
            forward_efficiency = 0
        
        if team not in teams_dict:
            teams_dict[team]={
                "players": {},
                "count": 0
            }
        teams_dict[team]["players"][player] = {
                "age": age,
                "fw": forward_efficiency,
                "mf": midfield_efficiency
            }
        teams_dict[team]["count"] += 1

    return teams_dict
            



def main():
    filename = "player_stats.csv"
    read_stats(filename)
main()