
from pathlib import Path
import re
import uuid
import subprocess

DOSSIER = Path(__file__).resolve().parent

SOURCE = DOSSIER / "STM32_Data_Acquisition.kicad_sch"
SORTIE = DOSSIER / "STM32_Data_Acquisition_corrige.kicad_sch"

if not SOURCE.exists():
    raise SystemExit("ERREUR : schema KiCad introuvable.")

texte = SOURCE.read_text(encoding="utf-8")

# Broches reservees pour ADC, oscillateur et autres fonctions
# Seules les broches actuellement considerees inutilisees
# recevront un marqueur No Connect.

broches = [
    (54.61, 83.82),
    (54.61, 86.36),
    (54.61, 88.90),
    (54.61, 93.98),
    (54.61, 96.52),
    (54.61, 99.06),
    (54.61, 101.60),
    (54.61, 104.14),
    (54.61, 106.68),
    (54.61, 114.30),
    (54.61, 116.84),
    (54.61, 119.38),
    (54.61, 121.92),
    (54.61, 124.46),
    (54.61, 127.00),
    (54.61, 129.54),
    (54.61, 132.08),
    (90.17, 86.36),
    (90.17, 93.98),
    (90.17, 96.52),
    (90.17, 104.14),
]

# Supprimer le marqueur No Connect isole
motif = (
    r'\(no_connect\s*'
    r'\(at 146\.05 102\.87\)\s*'
    r'\(uuid "[^"]+"\)\s*\)'
)

texte, supprimes = re.subn(motif, "", texte)

# Eviter les doublons
marqueurs = []

for x, y in broches:
    position_nc = f"(at {x:.2f} {y:.2f})"

    if re.search(
        r'\(no_connect\s*' + re.escape(position_nc),
        texte
    ):
        continue

    marqueurs.append(
        '\n(no_connect\n'
        f'  (at {x:.2f} {y:.2f})\n'
        f'  (uuid "{uuid.uuid4()}")\n'
        ')\n'
    )

# Inserer les marqueurs dans le schema
position = texte.rfind(")")

if position == -1:
    raise SystemExit("ERREUR : format KiCad invalide.")

texte = (
    texte[:position]
    + "".join(marqueurs)
    + texte[position:]
)

SORTIE.write_text(texte, encoding="utf-8")

print("Schema genere :", SORTIE.name)
print("Marqueurs ajoutes :", len(marqueurs))
print("Marqueurs isoles supprimes :", supprimes)

# Verification ERC avec KiCad 10
cli = Path(
    r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
)

if cli.exists():
    rapport = DOSSIER / "rapport_ERC_corrige.txt"

    commande = [
        str(cli),
        "sch",
        "erc",
        "--output",
        str(rapport),
        str(SORTIE)
    ]

    resultat = subprocess.run(
        commande,
        capture_output=True,
        text=True,
        errors="replace"
    )

    print(resultat.stdout)
    print(resultat.stderr)
    print("Code retour :", resultat.returncode)
    print("Rapport :", rapport)
else:
    print("KiCad CLI introuvable.")

print("Termine : fichier original conserve.")
