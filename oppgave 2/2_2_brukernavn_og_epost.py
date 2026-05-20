# 2.2 Brukernavn og epost

def lag_brukernavn(navn):
    navn = navn.lower()
    deler = navn.split()
    fornavn = deler[0]
    etternavn = deler[1]
    return fornavn + etternavn[0]


def lag_epost(navn, domene):
    brukernavn = lag_brukernavn(navn)
    return brukernavn + domene


# Test
print(lag_brukernavn("Jo Brochmann"))
print(lag_epost("Jo Brochmann", "@lotus.no"))
