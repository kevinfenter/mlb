from sportsreference.nfl.teams import Teams
from sportsreference.nfl.roster import Roster
from sportsreference.nfl.roster import Player

for team in Teams():
    print(team.name)
    schedule = team.schedule  # Request the current team's schedule
    for game in schedule:
        print(game.date, game.points_scored, game.points_allowed)


detroit = Roster('DET')
for player in detroit.players:
    print(player.name, player.games_played)
