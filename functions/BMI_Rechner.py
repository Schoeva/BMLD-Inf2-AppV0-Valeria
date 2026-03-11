from datetime import datetime
import pytz


def bmi_rechner(gewicht_kg, groesse_m):
    """
    Berechnet den Body Mass Index (BMI), kategorie und timestamp.
    
    Args:
        gewicht_kg: Gewicht in Kilogramm
        groesse_m: Körpergröße in Metern
    
    Returns:
        Der berechnete BMI, kategorie und timestamp.
    """
    if groesse_m <= 0 or gewicht_kg <= 0:
        return "Ungültige Eingabe"
    
    bmi = gewicht_kg / (groesse_m ** 2)
    return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),  # Current swiss time
        "groesse_m": groesse_m,
        "gewicht_kg": gewicht_kg,
        "bmi": round(bmi, 1),
        "bmi_kategorie ": bmi_kategorie(bmi),
    }
    


def bmi_kategorie(bmi):
    """
    Bestimmt die BMI-Kategorie.
    
    Args:
        bmi: Der BMI-Wert
    
    Returns:
        Die entsprechende Kategorie
    """
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"

    