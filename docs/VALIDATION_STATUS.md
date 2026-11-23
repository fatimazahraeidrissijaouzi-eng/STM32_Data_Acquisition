# Release and validation notes

## Available project artifacts

The project source bundle contains:
- KiCad schematic and routed two-layer PCB (ADC4 revision)
- 10 Gerber/drill fabrication files
- STM32CubeIDE configuration and project metadata
- Application source files under `Core/`
- STM32 HAL/CMSIS under `Drivers/`
- FreeRTOS under `Middlewares/`
- `tests/test_adc.c` and KiCad automation scripts
- Historical ERC reports, labeled as historical (not the final validation report)

## Engineering status

- Firmware build previously completed with 0 reported errors and 0 warnings.
- PCB routed; prior DRC reported no violations or unconnected pads, with some checks ignored.
- ERC reports in `docs/erc_history` are from earlier iterations and contain errors; they are not proof of the final design state.
- No board-level hardware testing has been performed.
- A 3D PCB view is a mechanical/placement visualization, not functional proof.
- Decoupling capacitor placement should be reviewed before manufacturing.

## Publication note

This repository is being populated. The full curated source archive is prepared separately for upload; this note does not imply that the archive or all source files have already been pushed to GitHub.
