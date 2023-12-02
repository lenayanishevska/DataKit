import requests
import pandas as pd
from io import StringIO

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'

# Download the file using requests
response = requests.get(url, verify=False)
data = StringIO(response.text)

# Read the CSV from the downloaded content
df = pd.read_csv(data)

print(df.head())

# b. Select only the Team, Yellow Cards, and Red Cards columns
selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

# c. How many teams participated in the Euro2012?
num_teams = df['Team'].nunique()
print(f"Number of teams participated in Euro2012: {num_teams}")

# d. Filter teams that scored more than 6 goals
high_scorers = df[df['Goals'] > 6]
print("Teams that scored more than 6 goals:")
print(high_scorers[['Team', 'Goals']])