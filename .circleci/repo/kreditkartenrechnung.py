import csv
import re


def read_csv(filename: str = "./csv/data.csv", limit: int = 0) -> list:
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=";")
        data = []
        for [line, row] in enumerate(csvreader):
            if limit != 0 and line >= limit:
                break
            data.append(row["kreditkartennummer"])
    return data


def check_prüfziffer(kreditkartennr: str = '') -> bool:
    if kreditkartennr == '':
        kreditkartennr = input("Geben Sie Ihre Kreditkartennummer ein: ")

    kreditkartennr = re.sub(r"[^\d]", '', kreditkartennr)
    if len(kreditkartennr != 16):
        return False
    prüfziffer = kreditkartennr[-1]
    kreditkartennr = kreditkartennr[:-1]

    verdoppelte_werte = []
    for stelle, wert in enumerate(kreditkartennr):
        if stelle % 2 == 0:
            verdoppelte_werte.append(int(wert) * 2)
        else:
            verdoppelte_werte.append(int(wert))

    quersummen = []
    for i in verdoppelte_werte:
        quersumme = 0
        for j in str(i):
            quersumme += int(j)
        quersummen.append(quersumme)

    summe = sum(quersummen)
    zahl = summe % 10
    zahl = 10 - zahl if 10 - zahl != 10 else 0

    return zahl == int(prüfziffer)


kreditkarten = []
for i in read_csv(limit=100):
    kreditkarten.append((i, check_prüfziffer(i)))

korrekt = 0
falsch = 0
text = ""
for [kreditkartennr, bool] in kreditkarten:
    if (bool):
        text += f"{kreditkartennr} ist Korrekt.\n"
        # print(f"Kreditkartennummer {kreditkartennr} is Korrekt!")
        korrekt += 1
    else:
        text += f"{kreditkartennr} ist Falsch.\n"
        # print(f"Kreditkartennummer {kreditkartennr} is Falsch!")
        falsch += 1

print(
    f"Es gab {korrekt} korrekte Kreditkartennummern und {falsch} falsche Kreditkartennummern!"
)

with open("./verarbeitete_kreditkarten/kreditkarten.txt", "w") as f:
    f.writelines(text)
