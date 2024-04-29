import streamlit as st
import pandas as pd
from get_team_data import find_games

st.title("NBA Team Data")

nba_teams = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]

user_team = st.selectbox(label="Choose your NBA Team", options=nba_teams)

find_games(user_team)

df = pd.DataFrame(find_games(user_team))
STATS = ['GAME_DATE', 'MATCHUP', 'WL', 'PTS', 'FG_PCT', 'FG3_PCT', 'FTM', 'FTA', 'REB', 'AST', 'STL', 'BLK', 'TOV']
data = df[STATS].head()

st.dataframe(data)
