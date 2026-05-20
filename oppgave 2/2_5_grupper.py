# 2.5 Inndeling i grupper - tilfeldig fordeling
import random

deltakere = [
    "Sebastian", "Montadar", "Susanna", "Sivert", "Sondre",
    "Bror", "Ludvig", "Endre", "Bilal", "Hans",
    "Harun", "Fredrik", "Dan", "Oscar", "Ninni",
    "Sindre", "Christian", "Simen"
]

# Anbefal antall grupper (ca. 4 per gruppe)
anbefalt = len(deltakere) // 4
print("Det er", len(deltakere), "deltakere.")
print("Anbefalt antall grupper:", anbefalt)

antall = int(input("Hvor mange grupper vil du ha? "))

# Bland deltakerne tilfeldig
random.shuffle(deltakere)

# Lag tomme grupper
grupper = []
for i in range(antall):
    grupper.append([])

# Fordel deltakerne rundt
for i in range(len(deltakere)):
    grupper[i % antall].append(deltakere[i])

# Skriv ut
for i in range(antall):
    print("\nGruppe", i + 1, ":")
    for navn in grupper[i]:
        print(" -", navn)
