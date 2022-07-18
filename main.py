# Get the number of teams playing
num_teams = int(input("Please enter the number of teams: "))
teams_counter = 1 
teams_list = []

# Get sports teams from user
while teams_counter <= num_teams:
  team = input("{}. Team name: ".format(teams_counter))
  teams_list.append(team)
  teams_list.sort()
  teams_counter += 1

# Create schedule from the sports team list
print("\nYour schedule is:")
for home_team in teams_list:
  for away_team in teams_list:
    if home_team != away_team:
      print(home_team + " vs " + away_team)