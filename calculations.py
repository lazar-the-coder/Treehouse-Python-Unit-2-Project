import constants
import math
import pdb

exp_players_list = []
unexp_players_list = []
teams_list = constants.TEAMS
teams_sorted = {}

def main():
    convert_team_data()
    sort_to_teams()

def convert_team_data():
    for player in constants.PLAYERS:
        player_fixed = {}
        player_fixed['name'] = player['name']
        player_fixed['guardians'] = player['guardians'].split(" and ")
        player_fixed['height'] = int(player['height'][0:2])
        if player['experience'].lower() == 'yes':
            player_fixed['experience'] = True
            exp_players_list.append(player_fixed)
        else:
            player_fixed['experience'] = False
            unexp_players_list.append(player_fixed)

def limit_calc(list_of_type):
    return math.floor(len(list_of_type)/len(teams_list))

def list_popper(player_list, limit):
    team_player_list = []
    for num in range(limit):
        new_player = player_list.pop()
        team_player_list.append(new_player)
    return team_player_list

def assign_players(exp_limit, unexp_limit):
    full_player_list = list_popper(exp_players_list, exp_limit) +  list_popper(unexp_players_list, unexp_limit)
    return full_player_list
    

def sort_to_teams():
    exp_limit = limit_calc(exp_players_list)
    unexp_limit = limit_calc(unexp_players_list)
    for team in teams_list:
        set_of_players = assign_players(exp_limit, unexp_limit)
        teams_sorted[team] = set_of_players

def display_team_stats(team):
    player_count = len(teams_sorted[team])
    player_names = []
    for player in teams_sorted[team]:
        player_names.append(player["name"])
    exp_players = sum(1 for player in teams_sorted[team] if player["experience"] is True)
    inexp_players = sum(1 for player in teams_sorted[team] if player["experience"] is False)
    ave_height = (sum(player["height"] for player in teams_sorted[team])/len(teams_sorted[team]))
    guardian_names = []
    for player in teams_sorted[team]:
        guardian_names.extend(player["guardians"])
    return player_count, player_names, exp_players, inexp_players, ave_height, guardian_names

if __name__ == "__main__":
    main()
