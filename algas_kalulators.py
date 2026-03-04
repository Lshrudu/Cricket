# Algas kalkulators (bruto -> neto)
# Pieņemam, ka nodokļu grāmatiņa ir iesniegta:
# piemēro neapliekamo minimumu un atvieglojumu par apgādājamiem.

VSAOI_LIKME = 0.105
IIN_LIKME = 0.255
NEAPLIEKAMAIS_MINIMUMS = 550.0
ATVIEGLOJUMS_APGADAJAMAIS = 250.0


def ievade_bruto():
   
    while True:
        
        try:
            ievade = float(input("Ievadi Bruto algu: "))
            if ievade < 0:
                print("Kļūda: vērtība nedrīkst būt negatīva. Mēģini vēlreiz.")
                continue
            return ievade
        except ValueError:
            print("Kļūda: ievadi skaitli pareizā formātā. Mēģini vēlreiz.")
def ievade_apgad():
   
    while True:
        
        try:
            apgad = int(input("Ievadi apgādājamo skaitu: "))
            if apgad < 0:
                print("Kļūda: vērtība nedrīkst būt negatīva. Mēģini vēlreiz.")
                continue
            return apgad
        except ValueError:
            print("Kļūda: ievadi skaitli pareizā formātā. Mēģini vēlreiz.")

def aprekinat_vsaoi(bruto_alga):
    """Aprēķina darba ņēmēja VSAOI."""
    return bruto_alga * VSAOI_LIKME


def aprekinat_iin(bruto_alga, vsaoi, apgad_skaits):
    """Aprēķina IIN, piemērojot neapliekamo minimumu un atvieglojumus par apgādājamiem."""
    atvieglojums = apgad_skaits * ATVIEGLOJUMS_APGADAJAMAIS
    apliekamais = bruto_alga - vsaoi - NEAPLIEKAMAIS_MINIMUMS - atvieglojums

    if apliekamais < 0:
        apliekamais = 0.0

    return apliekamais * IIN_LIKME


def aprekinat_neto(bruto_alga, vsaoi, iin):
    """Aprēķina neto algu."""
    return bruto_alga - vsaoi - iin



bruto_alga = ievade_bruto()
apgad_skaits = ievade_apgad()

vsaoi = aprekinat_vsaoi(bruto_alga)
iin = aprekinat_iin(bruto_alga, vsaoi, apgad_skaits)
neto = aprekinat_neto(bruto_alga, vsaoi, iin)

print("\n--- Rezultāti ---")
print(f"VSAOI: {vsaoi:.2f} EUR")
print(f"IIN: {iin:.2f} EUR")
print(f"Neto alga: {neto:.2f} EUR")

