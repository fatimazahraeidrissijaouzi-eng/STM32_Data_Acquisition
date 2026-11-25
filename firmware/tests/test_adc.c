
#include <stdint.h>
#include <stdbool.h>

/* Vérification d'une valeur ADC STM32 12 bits */
bool ADC_IsValid(uint32_t value)
{
    return value <= 4095U;
}

/* Conversion ADC vers millivolts (Vref = 3,3 V) */
uint32_t ADC_ToMillivolts(uint32_t value)
{
    if (!ADC_IsValid(value))
    {
        return 0U;
    }

    return (value * 3300U) / 4095U;
}

/* Tests simples, sans matériel */
int ADC_RunTests(void)
{
    if (!ADC_IsValid(0U)) return 1;
    if (!ADC_IsValid(2048U)) return 2;
    if (!ADC_IsValid(4095U)) return 3;
    if (ADC_IsValid(4096U)) return 4;

    if (ADC_ToMillivolts(0U) != 0U) return 5;
    if (ADC_ToMillivolts(4095U) != 3300U) return 6;

    return 0;
}
