from pathlib import Path
import pcbnew

dossier = Path(__file__).resolve().parent

source = dossier / "STM32_Data_Acquisition_ADC4.kicad_pcb"
sortie = dossier / "STM32_Data_Acquisition_ADC4_auto.kicad_pcb"

if not source.exists():
    raise FileNotFoundError(f"PCB introuvable : {source}")

board = pcbnew.LoadBoard(str(source))

positions = {
    "U1": (110, 100),
    "C1": (100, 90),
    "C2": (105, 90),
    "C3": (110, 90),
    "C4": (115, 90),
    "C5": (120, 90),
    "C6": (125, 90),
    "R1": (95, 105),
    "R2": (95, 110),
    "R3": (95, 115),
    "R4": (95, 120),
    "SW1": (85, 105),
    "J1": (140, 100),
    "J2": (140, 115),
    "J3": (80, 125),
    "J4": (140, 130),
    "J5": (80, 140),
}

trouves = set()

for fp in board.GetFootprints():
    ref = fp.GetReference()
    if ref in positions:
        x, y = positions[ref]
        fp.SetPosition(pcbnew.VECTOR2I(
            pcbnew.FromMM(x),
            pcbnew.FromMM(y)
        ))
        trouves.add(ref)
        print(f"Place : {ref}")

pcbnew.SaveBoard(str(sortie), board)

print(f"\nEmpreintes placees : {len(trouves)}")
print(f"PCB genere : {sortie}")
print("PCB original conserve.")