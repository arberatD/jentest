import subprocess
import datetime

def test_hi_output():
    # Führe das Skript hi.py aus und fange die Ausgabe auf
    result = subprocess.run(['python3', 'hi.py'], stdout=subprocess.PIPE, text=True)
    output = result.stdout

    # Baue die erwartete Zeichenkette auf, die in der Ausgabe enthalten sein sollte
    aktuelles_datum_und_zeit = datetime.datetime.now()
    formatiertes_datum_und_zeit = aktuelles_datum_und_zeit.strftime("%d.%m.%Y um %H:%M")
    expected_string = f"Das ist Abi's App. Du nutzt sie am {formatiertes_datum_und_zeit[:16]}"

    # Überprüfe, ob der erwartete String in der Ausgabe enthalten ist
    assert expected_string in output[:50], "Die Ausgabe entspricht nicht dem erwarteten Format."
