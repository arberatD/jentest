import subprocess
import datetime
import re

def test_hi_output():
    # Führe das Skript hi.py aus und fange die Ausgabe auf
    result = subprocess.run(['python3', 'hi.py'], stdout=subprocess.PIPE, text=True)
    output = result.stdout

    # Überprüfe, ob die Ausgabe dem erwarteten Muster entspricht
    # Beispiel: "Das ist Abi's App. Du nutzt sie am 09.02.2024 um 14:05."
    pattern = r"Das ist Abi's App. Du nutzt sie am \d{2}\.\d{2}\.\d{4} um \d{1,2}:\d{2}"
    assert re.search(pattern, output), "Die Ausgabe entspricht nicht dem erwarteten Format."
