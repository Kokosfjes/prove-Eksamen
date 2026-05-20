# 2.4 Feilhåndtering

def fjern_falske_brukere(brukere, nokkelord):
    resultat = []
    for b in brukere:
        if nokkelord not in b:
            resultat.append(b)
    return resultat


def finn_duplikater(deltakere):
    resultat = {}
    for navn in deltakere:
        if navn in resultat:
            resultat[navn] = resultat[navn] + 1
        else:
            resultat[navn] = 1

    # Returner kun de som har mer enn 1
    duplikater = {}
    for navn in resultat:
        if resultat[navn] > 1:
            duplikater[navn] = resultat[navn]
    return duplikater


# Test
print(fjern_falske_brukere(["thorc", "ravim", "ceciliet", "fredrikg"], "fred"))

print(finn_duplikater(["Ole", "Kari", "Ole", "Per", "Kari", "Ole"]))
