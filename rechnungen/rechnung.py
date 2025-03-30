from datetime import date
from typing import List, Optional


class Patient:
    def __init__(self, geschlecht: str, alter: int, vorerkrankungen: List[str]):
        self.geschlecht = geschlecht
        self.alter = alter
        self.vorerkrankungen = vorerkrankungen


class Ziffer:
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
        self.id = id  # Jede ID ist eindeutig.
        self.anzahl = anzahl
        self.faktor = faktor
        self.begruendung = begruendung
        self.beschreibung = beschreibung
        self.indikation = indikation
        self.gesamtbetrag = gesamtbetrag
        self.uhrzeit_angegeben = uhrzeit_angegeben
        #todo analoge positionen hinzufügen
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
        #todo ambulant oder stationär


# Assoziationen zwischen Klassen definieren
Rechnung.behandlungsfall = []
Behandlungsfall.sitzungen = []
Sitzung.positionen = []
Position.auslagen = []