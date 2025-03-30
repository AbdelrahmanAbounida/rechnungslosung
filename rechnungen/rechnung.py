from datetime import date
from typing import List, Optional


class Patient:
    """
    Represents a patient with basic demographic information and medical history.
    """
    def __init__(self, geschlecht: str, alter: int, vorerkrankungen: List[str]):
        self.geschlecht = geschlecht
        self.alter = alter
        self.vorerkrankungen = vorerkrankungen # pre conditions


class Ziffer: # billing code 
    """
    Represents a medical billing code with relevant attributes such as description, 
    maximum billing factor, exclusions, and section categorization.
    """
    def __init__(
        self,
        ziffer_string: str, # code >> I will use position id instead of this attr (not sure) ..
        ziffer_beschreibung: str, # description >> we gonna use it to check position type 
        regelhoechstfaktor: float, # maximum billing factor
        ausschluss_ziffern: List[str], # exclusions
        abschnitt: str, # section
        ausschluss_abschnitt: Optional[List[str]] = None, # exclusions sections
    ):
        self.ziffer_string = ziffer_string
        self.ziffer_beschreibung = ziffer_beschreibung
        self.regelhoechstfaktor = regelhoechstfaktor
        self.ausschluss_ziffern = ausschluss_ziffern
        self.abschnitt = abschnitt
        self.ausschluss_abschnitt = ausschluss_abschnitt


class Behandlungsfall: # Treatment Case 
    """
    Represents a medical treatment case associated with a specific diagnosis.
    """
    def __init__(self, diagnose: str):
        self.diagnose = diagnose 
        self.sitzungen: List["Sitzung"] = [] # sessions / appointments 


class Sitzung: # sessions  
    """
    Represents a medical session (appointment) with a specific date and time.
    """
    def __init__(self, datum: date, uhrzeit: str):
        self.datum = datum
        self.uhrzeit = uhrzeit
        self.positionen: List["Position"] = [] # sessions 


class Position:
    """
        This is part of the sitzung or session (patient could have multiple positions / services in a sitzung)
    """
   
    def __init__(
        self,
        ziffer: Ziffer, 
        id: str,
        anzahl: int,
        faktor: float,
        begruendung: str, # reason for the position 
        beschreibung: str,
        indikation: str,
        gesamtbetrag: float, # total cost of the position 
        uhrzeit_angegeben: bool, 
    ):
        self.ziffer = ziffer
        self.id = id  # Jede ID ist eindeutig. >> I dont know what is the diff with ziffer_string > I will use it 
        self.anzahl = anzahl
        self.faktor = faktor
        self.begruendung = begruendung 
        self.beschreibung = beschreibung  
        self.indikation = indikation
        self.gesamtbetrag = gesamtbetrag 
        self.uhrzeit_angegeben = uhrzeit_angegeben
        #todo analoge positionen hinzufügen
        self.auslagen: List["Auslage"] = []


        # How can we check if this position is a beratung
    def ist_beratung(self) -> bool:
        """ check if this position is a beratung
            possible solutions could be in
            return True if this position is a beratung
        """
        # TODO:: could be an LLM sol to check also begruendung, beschreibung depending on the rechnung
        return "beratung" in self.begruendung.lower()  or "beratung" in self.ziffer.ziffer_beschreibung.lower()


class Auslage: 

    def __init__(self, bezeichnung: str, gesamtbetrag: float):
        self.bezeichnung = bezeichnung
        self.gesamtbetrag = gesamtbetrag


class Rechnung:
    """
    Represents a medical invoice for a patient, including total cost and treatment cases.
    """
    def __init__(self, datum: date, betrag: float, patient: Patient):
        self.datum = datum
        self.betrag = betrag
        self.patient = patient
        self.behandlungsfall: List["Behandlungsfall"] = []
        #todo ambulant oder stationär
    
    def verify_rechnung(self) -> list[str]:
        """ Verifies if the rechnung is valid acc.to our 2 main rules (Task1)

        - Bereung can only be billed once per sitzung
        - Multiple Bereungen on the same day require different specified times.

        Returns a list of position IDs that violate the rules.
        """
        violating_positions = set() # List of violating Positions 
        
        # Q: Assuming Rule2 is per all treatment case other than that this should be moved down this for loop
        day_sitzungen : dict[str,dict[str,str]] = {} # Rule2: (day > time > beratung_ziffer)

        for behandlungsfall in self.behandlungsfall:
            
            for sitzung in behandlungsfall.sitzungen:
                sitzung_beratung_ziffers = set() # track it per sitzung for rule1
                
                for position in sitzung.positionen:
                    if position.ist_beratung(): 
                        billing_ziffer = position.ziffer.ziffer_string

                        # Rule 1: Bereung can only be billed once per sitzung >> applied to positions
                        if billing_ziffer in sitzung_beratung_ziffers:
                            violating_positions.add(position.id)
                        else:
                            sitzung_beratung_ziffers.add(billing_ziffer) # Q: Could be position.id ??
                        
                        # Rule 2: billing multiple times for breatung a day, only allowed if beratung is at different times
                        # could be we need to check if it violates perfor going with rule2 checks 
                        day = sitzung.datum.today().strftime("%Y-%m-%d") # YYY-MM-DD
                        time = sitzung.uhrzeit

                        if day not in day_sitzungen:
                            day_sitzungen[day] = {}
                            day_sitzungen[day][time] = billing_ziffer

                        elif time not in day_sitzungen[day]:
                            day_sitzungen[day][time] = billing_ziffer

                        else:
                            violating_positions.add(position.id)
        return list(violating_positions)


# Assoziationen zwischen Klassen definieren
Rechnung.behandlungsfall = [] # treatment casese
Behandlungsfall.sitzungen = [] # appointments
Sitzung.positionen = [] # 
Position.auslagen = []



