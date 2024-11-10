from varasto import Varasto


def luo_varastot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    return mehua, olutta

def nayta_getterit(varasto, nimi):
    print(f"{nimi} getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def varaston_toiminnot(varasto, nimi):
    print(f"{nimi}: {varasto}")
    print(f"{nimi}.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    print(f"{nimi}: {varasto}")
    print(f"{nimi}.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    print(f"{nimi}: {varasto}")

def varaston_otto(varasto, nimi, maara):
    print(f"{nimi}.ota_varastosta({maara})")
    saatiin = varasto.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"{nimi}: {varasto}")

def main():
    mehua, olutta = luo_varastot()
    nayta_getterit(olutta, "Olutvarasto")
    mehu_setterit(mehua)
    virhetilanteet()
    varaston_toiminnot(olutta, "Olutvarasto")
    varaston_otto(olutta, "Olutvarasto", 1000.0)
    varaston_otto(mehua, "Mehuvarasto", -32.9)

if __name__ == "__main__":
    main()
