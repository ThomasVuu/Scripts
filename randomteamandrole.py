import random

names = ["Thomas", "Eivind", "Markus", "Ask", "David", "Martin", "Emil", "Jonathan", "Sander", "Erik"]

random.shuffle(names)

roles = ["top", "jungle", "mid", "adc", "support"]

team1 = []
team2 = []

team1_roles = roles.copy()
team2_roles = roles.copy()

for i in range(5):
    player = names.pop()
    role = random.choice(team1_roles)
    team1_roles.remove(role)
    team1.append((player, role))

for i in range(5):
    player = names.pop()
    role = random.choice(team2_roles)
    team2_roles.remove(role)
    team2.append((player, role))

team1 = sorted(team1, key=lambda x: roles.index(x[1]))
team2 = sorted(team2, key=lambda x: roles.index(x[1]))

print("Team 1:")
for player, role in team1:
    print(f"{role} - {player}")

print("\nTeam 2:")
for player, role in team2:
    print(f"{role} - {player}")
