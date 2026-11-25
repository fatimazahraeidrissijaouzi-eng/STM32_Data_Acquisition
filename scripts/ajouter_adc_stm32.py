
from pathlib import Path
import uuid
import subprocess
import re

DOSSIER = Path(__file__).resolve().parent

SOURCE = DOSSIER / "STM32_Data_Acquisition_corrige.kicad_sch"
SORTIE = DOSSIER / "STM32_Data_Acquisition_ADC4.kicad_sch"
RAPPORT = DOSSIER / "rapport_ERC_ADC4.txt"

if not SOURCE.is_file():
    raise SystemExit("ERREUR : schema corrige introuvable.")

texte = SOURCE.read_text(encoding="utf-8")

# Configuration : 4 entrees ADC
adc = [
    ("ADC_IN0", 90.17, 66.04),
    ("ADC_IN1", 90.17, 68.58),
    ("ADC_IN2", 90.17, 71.12),
    ("ADC_IN3", 90.17, 73.66),
]

# Oscillateur interne HSI :
# PD0 et PD1 restent inutilisees
pins_nc = [
    (54.61, 76.20),
    (54.61, 78.74),
]

elements = []

# Ajouter les etiquettes ADC
for nom, x, y in adc:
    if re.search(
        r'\(label\s+"' + re.escape(nom) + r'"',
        texte
    ):
        print("Etiquette deja presente :", nom)
        continue

    elements.append(
        f'''
    (label "{nom}"
        (at {x:.2f} {y:.2f} 0)
        (effects
            (font (size 1.27 1.27))
            (justify left bottom)
        )
        (uuid "{uuid.uuid4()}")
    )
'''
    )

    print("ADC ajoute :", nom)

# Ajouter No Connect sur PD0 et PD1
for x, y in pins_nc:
    motif = (
        r'\(no_connect\s*'
        r'\(at\s+' + re.escape(f"{x:.2f}") +
        r'\s+' + re.escape(f"{y:.2f}") + r'\)'
    )

    if re.search(motif, texte):
        continue

    elements.append(
        f'''
    (no_connect
        (at {x:.2f} {y:.2f})
        (uuid "{uuid.uuid4()}")
    )
'''
    )

    print("No Connect ajoute :", x, y)

# Inserer les elements avant la fermeture du schema
position = texte.rfind(")")

if position < 0:
    raise SystemExit("ERREUR : schema invalide.")

texte = (
    texte[:position]
    + "".join(elements)
    + texte[position:]
)

SORTIE.write_text(texte, encoding="utf-8")

print("\nNouveau schema :", SORTIE.name)

# Lancer la verification ERC
cli = Path(
    r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
)

if not cli.is_file():
    print("KiCad CLI introuvable.")
    raise SystemExit(1)

commande = [
    str(cli),
    "sch",
    "erc",
    "--output",
    str(RAPPORT),
    str(SORTIE),
]

resultat = subprocess.run(
    commande,
    capture_output=True,
    text=True,
    errors="replace"
)

print("\nRESULTAT ERC")
print(resultat.stdout)
print(resultat.stderr)
print("Code retour :", resultat.returncode)
print("Rapport :", RAPPORT.name)
print("\nSchema original conserve.")
