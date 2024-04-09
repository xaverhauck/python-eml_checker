#! ~/usr/bin/env python3

import os
from email import message_from_file


def update_status(count, total_amount):
    status = f"searching: {count} of {total_amount}"
    print(status, end='\r')


# Gibt Array mit allen Suchbegriffen zurück
def read_search_terms(file_path):
    with open(file_path, 'r') as file:
        # Extrahiere Suchbegriffe aus der Datei
        return [line.strip() for line in file if line.strip()]

# Prüft, welcher Suchbegriff in welcher E-Mail vorkommt. Rückgabewert = Array
def search_in_email(search_terms, eml_file_path):
    with open(eml_file_path, 'r', encoding='utf-8') as file:
        email = message_from_file(file)


    c = 0
    for st in search_terms:
        c += 1
        update_status(c, len(search_terms))
        if st.lower() in str(email).lower():
            found_term = st
            search_terms.remove(found_term)
            return found_term

# Ordnet die Suchbegriffe den Emails zu, gibt ein Objekt zurück mit
# {"file": filename, "found_term": found_term}
def search_in_folder(search_terms):
    folder_path = "./import"  # Der feste Ordnerpfad ./import

    # Durchsuche alle .eml-Dateien im angegebenen Ordner
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".eml"):
            print("Suche in: " + filename)
            eml_file_path = os.path.join(folder_path, filename)
            found_term = search_in_email(search_terms, eml_file_path)
     
            # Speichere das Ergebnis in einem Array
            results.append({"file": filename, "found_term": found_term})
            print(f"Zugeordnet: {found_term}")
            print("—".center(30, '—'))

    return results


def run_script():
    # Frage nach Bestätigung
    confirmation = input("Möchten Sie das Skript ausführen? Drücken Sie Enter für Ja: ")
    # Überprüfe die Eingabe
    if confirmation == "":
        if __name__ == "__main__":
            # Übergabe: Pfad zur INI-Datei mit den Suchbegriffen
            search_terms = read_search_terms("./searchTerms.ini")
            emails = search_in_folder(search_terms)

            # Ausgabe der .eml-Dateinamen, für die kein Element aus dem Array vorlag
            email_not_found = [result['file'] for result in emails if not result['found_term']]
            if email_not_found:
                print("Zu folgenden E-mails konnte kein Suchbegriff zugeordnet werden:")
                for filename in email_not_found:
                    print(filename)

            else:
                print("Zu allen E-mails wurde mindestens ein Suchbegriff zugeordnet.")
            print("—".center(30, '—'))

            # Ausgabe der search_terms, welche in keiner .eml gefunden wurde
            # [search_term, ...] - [{"file": filename, "found_term": found_term}, ...]:
            print("Folgende Suchbegriffe konnten nicht zugeordnet werden:\n")
            for i in range(len(search_terms)):
                print(f"[{i+1}] {search_terms[i]}")
            print(" DONE ".center(30, '—'))


# Skript aufrufen
run_script()