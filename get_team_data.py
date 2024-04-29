import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

nba_teams = teams.get_teams()

def find_games(user_team):
    # Select the dictionary for the team, which contains their team ID
    nba_team = [team for team in nba_teams if team['full_name'] == user_team][0]
    nba_team_id = nba_team['id']

    # Query for games where the Celtics were playing
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=nba_team_id)

    # The first DataFrame of those returned is what we want.
    games = gamefinder.get_data_frames()[0]

    return games