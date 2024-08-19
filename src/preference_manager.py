import json
import os

PREFERENCES_FILE = 'preferences.json'

def load_preferences():
    """Charge les préférences depuis le fichier JSON."""
    if not os.path.exists(PREFERENCES_FILE):
        return {'diet': []}

    try:
        with open(PREFERENCES_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Erreur lors de la lecture du fichier de préférences. Le fichier peut être corrompu.")
        return {'diet': []}
    except Exception as e:
        print(f"Une erreur est survenue lors du chargement des préférences : {e}")
        return {'diet': []}

def save_preferences(preferences):
    """Sauvegarde les préférences dans le fichier JSON."""
    try:
        with open(PREFERENCES_FILE, 'w') as file:
            json.dump(preferences, file, indent=4)
    except IOError:
        print("Erreur lors de l'écriture dans le fichier de préférences.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'enregistrement des préférences : {e}")

def add_preference(preference):
    """Ajoute une nouvelle préférence alimentaire si elle n'existe pas déjà."""
    if not isinstance(preference, str) or not preference.strip():
        print("La préférence doit être une chaîne de caractères non vide.")
        return
    
    preferences = load_preferences()
    if preference not in preferences['diet']:
        preferences['diet'].append(preference)
        save_preferences(preferences)
        print(f"Préférence ajoutée : {preference}")
    else:
        print(f"La préférence '{preference}' existe déjà.")

def list_preferences():
    """Affiche les préférences alimentaires actuelles."""
    preferences = load_preferences()
    if preferences['diet']:
        print("Préférences alimentaires actuelles :")
        for pref in preferences['diet']:
            print(f" - {pref}")
    else:
        print("Aucune préférence alimentaire définie.")
