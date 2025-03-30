from datetime import date
from typing import List, Optional
from rechnungen.rechnung import Patient, Ziffer, Position,Rechnung,  Sitzung, Behandlungsfall

class Patient:
    def __init__(self, geschlecht: str, alter: int, vorerkrankungen: List[str]):
        self.geschlecht = geschlecht
        self.alter = alter
        self.vorerkrankungen = vorerkrankungen

class Behandlungsfall:
    def __init__(
        self,
        ziffer_string: str,
        ziffer_beschreibung: str,
        regelhoechstfaktor: float,
        ausschluss_ziffern: List[str],
        abschnitt: str,
        ausschluss_abschnitt: Optional[List[str]] = None,
    ):
        self.ziffer_string = ziffer_string
        self.ziffer_beschreibung = ziffer_beschreibung
        self.regelhoechstfaktor = regelhoechstfaktor
        self.ausschluss_ziffern = ausschluss_ziffern
        self.abschnitt = abschnitt
        self.ausschluss_abschnitt = ausschluss_abschnitt

class Behandlungsfall:
    def __init__(self, diagnose: str):
        self.diagnose = diagnose
        self.sitzungen: List["Sitzung"] = []

class Sitzung:
    def __init__(self, datum: date, uhrzeit: str):
        self.datum = datum
        self.uhrzeit = uhrzeit
        self.positionen: List["Position"] = []

class Position:
    def __init__(
        self,
        ziffer: Ziffer,
        id: str,
        anzahl: int,
        faktor: float,
        begruendung: str,
        beschreibung: str,
        indikation: str,
        gesamtbetrag: float,
        uhrzeit_angegeben: bool,
    ):
        self.ziffer = ziffer
        self.id = id
        self.anzahl = anzahl
        self.faktor = faktor
        self.begruendung = begruendung
        self.beschreibung = beschreibung
        self.indikation = indikation
        self.gesamtbetrag = gesamtbetrag
        self.uhrzeit_angegeben = uhrzeit_angegeben
        self.auslagen: List["Auslage"] = []

class Auslage:
    def __init__(self, bezeichnung: str, gesamtbetrag: float):
        self.bezeichnung = bezeichnung
        self.gesamtbetrag = gesamtbetrag

class Rechnung:
    def __init__(self, datum: date, betrag: float, patient: Patient):
        self.datum = datum
        self.betrag = betrag
        self.patient = patient
        self.behandlungsfall: List["Behandlungsfall"] = []

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