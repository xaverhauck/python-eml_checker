# eMail Checker - crawl your .eml
Das Skript prüft die Inhalte der .eml Dateien unter `./import` mit der gegebenen Liste in `./searchTerms.ini`

- Alle nicht zugeordneten Elemente aus searchTerm.ini werden zurückgegeben,
- Alle nicht zugeordneteten Elemente aus .eml werden zurückgegeben.
- Wurde alles erfolgreich gefunden, wird eine Erfolgsmeldung zurückgegeben.

## Hinweise
- Wird ein Suchbegriff gefunden, fliegt er aus der Suchliste raus. Duplikate werden eliminert.

## Anwendung
1. eMails in den Ordner `import`ablegen.
2. Suchbegriffe in `searchTerm.ini` schreiben. Je Zeile ein Suchbegriff (z.B. Excel Tabelle kopieren)
3. `run.py` mit Python (z.B. IDLE) ausführen.
4. Start mit ENTER