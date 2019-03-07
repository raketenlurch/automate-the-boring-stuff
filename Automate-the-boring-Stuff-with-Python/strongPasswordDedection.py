import re

passwordLowerCase = re.compile(r'[a-z]')
passwordUpperCase = re.compile(r'[A-Z]')
passwordDigit = re.compile(r'(\d)')
passwordSpace = re.compile(r'^[a-zA-Z0-9]{8,}$')

def strongPassword():
    while True:
        password = input("Bitte geben Sie ihr neues Passwort ein: ")
        if passwordLowerCase.search(password) == None:
            print("Ihr Passwort muss einen Kleinbuchstaben enthalten.")
            continue
        elif passwordUpperCase.search(password) == None:
            print("Ihr Passwort muss einen Großbuchstaben enthalten.")
            continue
        elif passwordDigit.search(password) == None:
            print("Ihr Passwort muss eine Zahl enthalten.")
            continue
        elif passwordSpace.search(password) == None:
            print("Ihr Passwort muss mindestens 8 Zeichen lang sein und darf kein Leerzeichen enthalten.")
            continue
        else:
            print("Erfolgreich. Ihr Passwort entspricht den Richtlinien.")
            break

strongPassword()