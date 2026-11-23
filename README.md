# STM32 Data Acquisition Board & Real-Time Embedded System

**STM32F103C8Tx · KiCad · STM32CubeIDE · Embedded C · FreeRTOS**

A hardware/software engineering project combining a custom two-layer STM32 data-acquisition PCB with embedded firmware for ADC sampling and UART communication.

## Project overview

- **Hardware:** STM32F103C8Tx schematic and 2-layer PCB designed in KiCad, with reset circuitry, decoupling capacitors, and headers for SWD, ADC, UART, I2C and SPI.
- **PCB fabrication outputs:** front/back copper, solder masks, silkscreens, board outline, and plated/non-plated drill files generated from the routed board.
- **Firmware:** STM32CubeIDE project using STM32 HAL, ADC, USART, I2C, SPI, timer configuration and FreeRTOS tasks for acquisition and communication.
- **Verification:** KiCad ERC/DRC checks performed; firmware compiled successfully in STM32CubeIDE; ADC arithmetic test cases exercised separately.

## Repository structure (target layout)

```text
hardware/
  kicad/                KiCad schematic, project and routed PCB
  gerbers/              Fabrication outputs
firmware/
  Core/                 Application sources and headers
  Drivers/              STM32 HAL and CMSIS dependencies
  Middlewares/          FreeRTOS middleware
  tests/                Firmware-related tests
  STM32_Data_Acquisition_FW.ioc
scripts/                KiCad automation scripts
docs/                   Verification reports and project images
```

> **Publication status:** Files are being added progressively. The directory tree above describes the intended complete release; not all paths are necessarily present yet.

## Verification status and limitations

The PCB design was routed and fabrication outputs generated. Earlier checks reported no DRC violations or unrouted connections, with certain check categories ignored; schematic-to-PCB parity was not established by those results. The firmware was reported to compile without errors or warnings. ADC calculations were tested separately, but these are **not** evidence of complete embedded runtime verification.

**No physical STM32 board was manufactured or tested.** Hardware behavior, UART traffic and FreeRTOS scheduling have not been validated on a real device. Component placement, especially proximity of decoupling capacitors to MCU power pins, should be reviewed before fabrication.

## Tools

KiCad 10, STM32CubeIDE, Embedded C, STM32 HAL, FreeRTOS, Python.

## License

See the repository license for original project material. Third-party STM32 HAL, CMSIS and FreeRTOS files retain their own applicable notices and licenses.
