import datetime
now = datetime.datetime.now()
print("(standings as of): ")
print(now.strftime(" --- %Y-%m-%d %H:%M:%S  ---"))


class Team:
    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.pct = wins / losses

    total_games = 162

    def standings(self):
        return "{} {} {}".format(self.name, self.wins, self.losses)

    def total_played(self):
        return "{} {}".format(self.name, self.wins + self.losses)

    # def best_team(self):
    #     most_wins = wins[0]
    #     for z in wins:
    #         if z > most_wins:
    #             most_wins = z
    #     return most_wins
    # print("the best team is:", best_team(wins))


# NL Central
cubs = Team("Chicago Cubs      ", 38, 30)
brewers = Team("Milwaukee Brewers ", 38, 30)
reds = Team("Cincinatti Reds   ", 35, 31)
cards = Team("St.Louis Cardinals", 35, 33)
pirates = Team("Pittsburgh Pirates", 23, 44)

# NL East
mets = Team("New York Mets        ", 35, 25)
phillies = Team("Philidelphia Phillies", 33, 33)
nats = Team("Washington Nationals ", 30, 35)
braves = Team("Atlanta Braves       ", 30, 35)
marlins = Team("Miami Marlins        ", 29, 39)

# NL West
giants = Team("San Francisco Giants", 44, 25)
dodgers = Team("L.A. Dodgers        ", 41, 27)
padres = Team("San Diego Padres    ", 38, 32)
rockies = Team("Colorado Rockies    ", 28, 41)
dbacks = Team("Arizona Diamondbacks", 20, 50)

# AL East
rays = Team("Tampa Bay Rays    ", 43, 26)
redsox = Team("Boston Red-Sox    ", 42, 27)
yankees = Team("New York Yankees  ", 35, 32)
jays = Team("Toronto Blue Jays ", 33, 33)
orioles = Team("Baltimore Orioles ", 22, 46)

# AL Central
whitesox = Team("Chicago White-Sox ", 43, 25)
indians = Team("Cleveland Indians ", 38, 28)
royals = Team("Kansas City Royals", 30, 37)
tigers = Team("Detroit Tigers    ", 29, 39)
twins = Team("Minnesota Twins   ", 27, 41)

# AL West
atheletics = Team("Oakland Atheletics", 43, 27)
astros = Team("Houston Astros    ", 39, 28)
mariners = Team("Seattle Mariners  ", 34, 36)
angels = Team("L.A. Angels       ", 33, 35)
rangers = Team("Texas Rangers     ", 25, 43)


def allstandings():
    print("============================")
    print("-----NL Central-----")
    print("============================")
    print(cubs.standings())
    print(brewers.standings())
    print(reds.standings())
    print(cards.standings())
    print(pirates.standings())
    print("============================")
    print("-----NL East-----")
    print("============================")
    print(mets.standings())
    print(phillies.standings())
    print(nats.standings())
    print(braves.standings())
    print(marlins.standings())
    print("============================")
    print("-----NL West-----")
    print("============================")
    print(giants.standings())
    print(dodgers.standings())
    print(padres.standings())
    print(rockies.standings())
    print(dbacks.standings())
    print("============================")
    print("-----AL East-----")
    print("============================")
    print(rays.standings())
    print(redsox.standings())
    print(yankees.standings())
    print(jays.standings())
    print(orioles.standings())
    print("============================")
    print("-----AL Central-----")
    print("============================")
    print(whitesox.standings())
    print(indians.standings())
    print(royals.standings())
    print(tigers.standings())
    print(twins.standings())
    print("============================")
    print("-----AL West-----")
    print("============================")
    print(atheletics.standings())
    print(astros.standings())
    print(mariners.standings())
    print(angels.standings())
    print(rangers.standings())


selection = input("enter 1 for all standings or type in specific team ")
if selection == "1":
    print(allstandings())
elif selection == "cubs":
    print(cubs.standings())
elif selection == "brewers":
    print(brewers.standings())
elif selection == "reds":
    print(reds.standings())
elif selection == "cardinals":
    print(cards.standings())
elif selection == "pirates":
    print(pirates.standings())
elif selection == "mets":
    print(mets.standings())
elif selection == "phillies":
    print(phillies.standings())
elif selection == "nationals":
    print(nats.standings())
elif selection == "braves":
    print(braves.standings())
elif selection == "marlins":
    print(marlins.standings())
elif selection == "giants":
    print(giants.standings())
elif selection == "dodgers":
    print(dodgers.standings())
elif selection == "padres":
    print(padres.standings())
elif selection == "rockies":
    print(rockies.standings())
elif selection == "diamondbacks":
    print(dbacks.standings())
elif selection == "dbacks":
    print(dbacks.standings())
elif selection == "rays":
    print(rays.standings())
elif selection == "redsox":
    print(redsox.standings())
elif selection == "yankees":
    print(yankees.standings())
elif selection == "bluejays":
    print(jays.standings())
elif selection == "orioles":
    print(orioles.standings())
elif selection == "whitesox":
    print(whitesox.standings())
elif selection == "indians":
    print(indians.standings())
elif selection == "roayls":
    print(royals.standings())
elif selection == "tigers":
    print(tigers.standings())
elif selection == "twins":
    print(twins.standings())

else:
    print("that is incorrect _  now you have a virus")
