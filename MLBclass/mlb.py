class Team:
    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.pct = wins / losses

    def stats(self):
        return "{} {} {}".format(self.name, self.wins, self.losses)


# NL Central
cubs = Team("Chicago Cubs", 38, 30)
brewers = Team("Milwaukee Brewers", 38, 30)
reds = Team("Cincinatti Reds", 35, 31)
cards = Team("St.Louis Cardinals", 35, 33)
pirates = Team("Pittsburgh Pirates", 23, 44)

# NL East
mets = Team("New York Mets", 35, 25)
phillies = Team("Philidelphia Phillies", 33, 33)
nats = Team("Washington Nationals", 30, 35)
braves = Team("Atlanta Braves", 30, 35)
marlins = Team("Miami Marlins", 29, 39)

# NL West
giants = Team("San Francisco Giants", 44, 25)
dodgers = Team("L.A. Dodgers", 41, 27)
padres = Team("San Diego Padres", 38, 32)
rockies = Team("Colorado Rockies", 28, 41)
dbacks = Team("Arizona Diamondbacks", 20, 50)

# AL East
rays = Team("Tampa Bay Rays", 43, 26)
redsox = Team("Boston Red-Sox", 42, 27)
yankees = Team("New York Yankees", 35, 32)
jays = Team("Toronto Blue Jays", 33, 33)
orioles = Team("Baltimore Orioles", 22, 46)

# AL Central
whitesox = Team("Chicago White-Sox", 43, 25)
indians = Team("Cleveland Indians", 38, 28)
royals = Team("Kansas City Royals", 30, 37)
tigers = Team("Detroit Tigers", 29, 39)
twins = Team("Minnesota Twins", 27, 41)

# AL West
atheletics = Team("Oakland Atheletics", 43, 27)
astros = Team("Houston Astros", 39, 28)
mariners = Team("Seattle Mariners", 34, 36)
angels = Team("L.A. Angels", 33, 35)
rangers = Team("Texas Rangers", 25, 43)

print("-----NL Central-----")
print(cubs.stats())
print(brewers.stats())
print(reds.stats())
print(cards.stats())
print(pirates.stats())
print("-----NL East-----")
print(mets.stats())
print(phillies.stats())
print(nats.stats())
print(braves.stats())
print(marlins.stats())
print("-----NL West-----")
print(giants.stats())
print(dodgers.stats())
print(padres.stats())
print(rockies.stats())
print(dbacks.stats())
print("-----AL East-----")
print(rays.stats())
print(redsox.stats())
print(yankees.stats())
print(jays.stats())
print(orioles.stats())
print("-----AL Central-----")
print(whitesox.stats())
print(indians.stats())
print(royals.stats())
print(tigers.stats())
print(twins.stats())
print("-----AL West-----")
print(atheletics.stats())
print(astros.stats())
print(mariners.stats())
print(angels.stats())
print(rangers.stats())
