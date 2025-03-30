"""
# Auggabe1:
Verification of Invoices
check wether the given rechnungen classes comply with 2 rules 
- The consultation is indivisible; it can only be billed once in a session.
- Billing for consultations multiple times on the same day is only justified if the consultations 
  take place at different times. The times must be specified.

  Q: for Rule2 is this for the same sitzung or could be many sitzung a day 

result :
List of ids of the invoice positions that violate these rules 
"""
# Patient has envoices (Rechnug) in which it descripes Behandlungsfall in which he can do multiple sitzungen (sessions) and each 
# sitzung has multiple positionen / services and each position could have addons which infer addition costs (auslagen)
# Patient > Rechnug > Behandlungsfall > Sitzung > Position > Auslagen

from rechnungen.rechnung import Rechnung
from rechnungen.rechnung1 import rechnung as rechnung1
from rechnungen.rechnung2 import rechnung as rechnung2
from rechnungen.rechnung3 import rechnung as rechnung3
from rechnungen.rechnung4 import rechnung as rechnung4


def task1():
  rechnungen: list[Rechnung] = [rechnung1,rechnung2, rechnung3, rechnung4]

  all_violatingpositions = []
  for rechnung in rechnungen:
    all_violatingpositions.extend(rechnung.verify_rechnung())

  print(f"List of violationing positions: {all_violatingpositions}")
  return all_violatingpositions