import datetime

aktuelles_datum_und_zeit = datetime.datetime.now()
formatiertes_datum_und_zeit = aktuelles_datum_und_zeit.strftime("%d.%m.%Y um %H:%M")
benutzername = "Abi"

nachricht = f"Das ist {benutzername}'s App. Du nutzt sie am {formatiertes_datum_und_zeit}."

print(nachricht)

