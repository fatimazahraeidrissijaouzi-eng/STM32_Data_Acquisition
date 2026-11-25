
from pathlib import Path
import pcbnew

dossier = Path(__file__).resolve().parent

source = dossier / "STM32_Data_Acquisition_ADC4_auto.kicad_pcb"
sortie = dossier / "STM32_Data_Acquisition_ADC4_prepare.kicad_pcb"

if not source.exists():
    raise FileNotFoundError(f"PCB introuvable : {source}")

if sortie.exists():
    raise FileExistsError(
        f"Le fichier existe deja : {sortie}\n"
        "Renomme-le avant de relancer le script."
    )

board = pcbnew.LoadBoard(str(source))
footprints = list(board.GetFootprints())

if not footprints:
    raise RuntimeError("Aucune empreinte trouvee.")

# Calculer les limites des composants
xmin = min(fp.GetBoundingBox().GetLeft() for fp in footprints)
ymin = min(fp.GetBoundingBox().GetTop() for fp in footprints)
xmax = max(fp.GetBoundingBox().GetRight() for fp in footprints)
ymax = max(fp.GetBoundingBox().GetBottom() for fp in footprints)

# Ajouter une marge de 5 mm
marge = pcbnew.FromMM(5)

xmin -= marge
ymin -= marge
xmax += marge
ymax += marge

# Creer le contour sur Edge.Cuts
contour = pcbnew.PCB_SHAPE(board)
contour.SetShape(pcbnew.SHAPE_T_RECT)
contour.SetStart(pcbnew.VECTOR2I(xmin, ymin))
contour.SetEnd(pcbnew.VECTOR2I(xmax, ymax))
contour.SetLayer(pcbnew.Edge_Cuts)
contour.SetWidth(pcbnew.FromMM(0.05))

board.Add(contour)

pcbnew.SaveBoard(str(sortie), board)

print("================================")
print("PREPARATION PCB TERMINEE")
print("================================")
print("Composants :", len(footprints))
print("Contour PCB cree sur Edge.Cuts")
print("Fichier :", sortie)
print("PCB original conserve")
print("================================")
