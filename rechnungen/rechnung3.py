from datetime import date
from rechnungen.rechnung import Patient, Ziffer, Position,Rechnung,  Sitzung, Behandlungsfall



ziffer_beratung = Ziffer(
    ziffer_string="1",
    ziffer_beschreibung="Beratung",
    regelhoechstfaktor=2.3,
    ausschluss_ziffern=[],
    abschnitt="Allgemeine Leistungen"
)

rechnung = Rechnung(
    datum=date(2023, 1, 15),
    betrag=300.00,
    patient=Patient(geschlecht="m", alter=30, vorerkrankungen=[])
)

behandlungsfall = Behandlungsfall(diagnose="Testdiagnose")
sitzung = Sitzung(datum=date(2023, 1, 15), uhrzeit="10:00")

sitzung.positionen.append(
    Position(
        ziffer=ziffer_beratung,
        id="pos1",
        anzahl=1,
        faktor=1.0,
        begruendung="Erstberatung",
        beschreibung="Beratungsgespräch 1",
        indikation="Allgemein",
        gesamtbetrag=50.00,
        uhrzeit_angegeben=True
    )
)

sitzung.positionen.append(
    Position(
        ziffer=ziffer_beratung,
        id="pos2",
        anzahl=1,
        faktor=1.0,
        begruendung="Zweitberatung",
        beschreibung="Beratungsgespräch 2",
        indikation="Allgemein",
        gesamtbetrag=50.00,
        uhrzeit_angegeben=True
    )
)

sitzung.positionen.append(
    Position(
        ziffer=ziffer_beratung,
        id="pos3",
        anzahl=1,
        faktor=1.0,
        begruendung="Drittberatung",
        beschreibung="Beratungsgespräch 3",
        indikation="Allgemein",
        gesamtbetrag=50.00,
        uhrzeit_angegeben=True
    )
)

behandlungsfall.sitzungen.append(sitzung)
rechnung.behandlungsfall.append(behandlungsfall)