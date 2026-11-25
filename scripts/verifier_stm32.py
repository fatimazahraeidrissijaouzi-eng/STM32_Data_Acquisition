
from pathlib import Path
import subprocess
import sys

DOSSIER = Path(__file__).resolve().parent
SCHEMA = DOSSIER / "STM32_Data_Acquisition.kicad_sch"
RAPPORT = DOSSIER / "rapport_ERC.txt"
KICAD_CLI = Path(r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe")

if not SCHEMA.is_file():
    print("ERREUR : schema introuvable :", SCHEMA)
    sys.exit(1)

if not KICAD_CLI.is_file():
    print("ERREUR : kicad-cli introuvable :", KICAD_CLI)
    sys.exit(1)

commande = [
    str(KICAD_CLI), "sch", "erc",
    "--output", str(RAPPORT), str(SCHEMA)
]

resultat = subprocess.run(
    commande, capture_output=True, text=True
)

print(resultat.stdout)
print(resultat.stderr)
print("Code retour :", resultat.returncode)

if RAPPORT.exists():
    print("Rapport cree :", RAPPORT)
else:
    print("Aucun rapport genere.")
