from datetime import date
from rechnungen.rechnung import Patient, Ziffer, Position,Rechnung,  Sitzung, Behandlungsfall

patient = Patient(
    geschlecht="m",
    alter=30,
    vorerkrankungen=[]
)

ziffer_1 = Ziffer(
    ziffer_string="1",
    ziffer_beschreibung="Beratung",
    regelhoechstfaktor=2.3,
    ausschluss_ziffern=[],
    abschnitt="Allgemeine Leistungen"
)

rechnung = Rechnung(
    datum=date(2023, 1, 1),
    betrag=200.0,
    patient=patient
)

behandlungsfall_1 = Behandlungsfall(diagnose="Erkältung")
sitzung_1_bf1 = Sitzung(datum=date(2023, 1, 2), uhrzeit="10:00")

pos1_1_bf1_s1 = Position(
    ziffer=ziffer_1,
    id="bf1_s1_pos1",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)

pos1_2_bf1_s1 = Position(
    ziffer=ziffer_1,
    id="bf1_s1_pos2",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)

sitzung_1_bf1.positionen.append(pos1_1_bf1_s1)
sitzung_1_bf1.positionen.append(pos1_2_bf1_s1)

sitzung_2_bf1 = Sitzung(datum=date(2023, 1, 3), uhrzeit="11:00")
pos1_1_bf1_s2 = Position(
    ziffer=ziffer_1,
    id="bf1_s2_pos1",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)
sitzung_2_bf1.positionen.append(pos1_1_bf1_s2)

behandlungsfall_1.sitzungen.append(sitzung_1_bf1)
behandlungsfall_1.sitzungen.append(sitzung_2_bf1)

rechnung.behandlungsfall.append(behandlungsfall_1)

behandlungsfall_2 = Behandlungsfall(diagnose="Kopfschmerz")
sitzung_1_bf2 = Sitzung(datum=date(2023, 1, 4), uhrzeit="09:00")

pos1_1_bf2_s1 = Position(
    ziffer=ziffer_1,
    id="bf2_s1_pos1",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)

pos1_2_bf2_s1 = Position(
    ziffer=ziffer_1,
    id="bf2_s1_pos2",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)

sitzung_1_bf2.positionen.append(pos1_1_bf2_s1)
sitzung_1_bf2.positionen.append(pos1_2_bf2_s1)

sitzung_2_bf2 = Sitzung(datum=date(2023, 1, 5), uhrzeit="10:00")

behandlungsfall_2.sitzungen.append(sitzung_1_bf2)
behandlungsfall_2.sitzungen.append(sitzung_2_bf2)

rechnung.behandlungsfall.append(behandlungsfall_2)