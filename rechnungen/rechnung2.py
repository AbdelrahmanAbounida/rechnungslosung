from datetime import date
from rechnungen.rechnung import Patient, Ziffer, Position,Rechnung,  Sitzung, Behandlungsfall

patient = Patient(
    geschlecht="männlich", # gender 
    alter=30,
    vorerkrankungen=["Diabetes"] # preexisiting condition 
)

ziffer_1 = Ziffer(
    ziffer_string="1",
    ziffer_beschreibung="Beratung",
    regelhoechstfaktor=2.3,
    ausschluss_ziffern=[],
    abschnitt="Abschnitt1"
)

ziffer_4 = Ziffer(
    ziffer_string="4",
    ziffer_beschreibung="Andere Leistung",
    regelhoechstfaktor=2.3,
    ausschluss_ziffern=[],
    abschnitt="Abschnitt2"
)

position_1_day1 = Position(
    ziffer=ziffer_1,
    id="pos1_day1",
    anzahl=1,
    faktor=1.0,
    begruendung="Beratung",
    beschreibung="Beratung mit Zeitangabe",
    indikation="Allgemeine Beratung",
    gesamtbetrag=20.0,
    uhrzeit_angegeben=True
)

position_2_day1 = Position(
    ziffer=ziffer_4,
    id="pos2_day1",
    anzahl=1,
    faktor=1.0,
    begruendung="Andere Leistung",
    beschreibung="Andere berechnungsfähige Leistung",
    indikation="Allgemeine Behandlung",
    gesamtbetrag=40.0,
    uhrzeit_angegeben=False
)

position_1_day2 = Position(
    ziffer=ziffer_1,
    id="pos1_day2",
    anzahl=1,
    faktor=1.0,
    begruendung="Beratung",
    beschreibung="Beratung mit Zeitangabe 1",
    indikation="Allgemeine Beratung",
    gesamtbetrag=20.0,
    uhrzeit_angegeben=True
)

position_2_day2 = Position(
    ziffer=ziffer_1,
    id="pos2_day2",
    anzahl=1,
    faktor=1.0,
    begruendung="Beratung",
    beschreibung="Beratung mit Zeitangabe 2",
    indikation="Allgemeine Beratung",
    gesamtbetrag=20.0,
    uhrzeit_angegeben=True
)

position_3_day2 = Position(
    ziffer=ziffer_1,
    id="pos3_day2",
    anzahl=1,
    faktor=1.0,
    begruendung="Beratung",
    beschreibung="Beratung ohne Zeitangabe",
    indikation="Allgemeine Beratung",
    gesamtbetrag=20.0,
    uhrzeit_angegeben=False
)

sitzung_day1 = Sitzung(datum=date(2023, 3, 1), uhrzeit="10:00")
sitzung_day1.positionen.append(position_1_day1)
sitzung_day1.positionen.append(position_2_day1)

sitzung_day2 = Sitzung(datum=date(2023, 3, 2), uhrzeit="10:30")
sitzung_day2.positionen.append(position_1_day2)
sitzung_day2.positionen.append(position_2_day2)
sitzung_day2.positionen.append(position_3_day2)

behandlungsfall = Behandlungsfall(diagnose="Testdiagnose")
behandlungsfall.sitzungen.append(sitzung_day1)
behandlungsfall.sitzungen.append(sitzung_day2)

rechnung = Rechnung(datum=date(2023, 3, 3), betrag=200.0, patient=patient)
rechnung.behandlungsfall.append(behandlungsfall)