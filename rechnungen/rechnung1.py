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
    abschnitt="Abschnitt A"
)

pos_sitzung_1 = Position(
    ziffer=ziffer_1,
    id="pos_sitzung_1",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="Beratung",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)

pos_sitzung_2 = Position(
    ziffer=ziffer_1,
    id="pos_sitzung_2",
    anzahl=1,
    faktor=1.0,
    begruendung="",
    beschreibung="Beratung",
    indikation="",
    gesamtbetrag=10.0,
    uhrzeit_angegeben=True
)

sitzung_1 = Sitzung(
    datum=date(2023, 1, 15),
    uhrzeit="10:00"
)
sitzung_1.positionen.append(pos_sitzung_1)

sitzung_2 = Sitzung(
    datum=date(2023, 1, 15),
    uhrzeit="11:00"
)
sitzung_2.positionen.append(pos_sitzung_2)

behandlungsfall = Behandlungsfall(
    diagnose="Testdiagnose"
)
behandlungsfall.sitzungen.append(sitzung_1)
behandlungsfall.sitzungen.append(sitzung_2)

rechnung = Rechnung(
    datum=date(2023, 1, 15),
    betrag=20.0,
    patient=patient
)
rechnung.behandlungsfall.append(behandlungsfall)