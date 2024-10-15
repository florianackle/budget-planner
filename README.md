# :page_facing_up: PE-A ATL

Schulprojekt von Florian Ackle

# :bookmark: Current version

v0.1

# :construction_worker: Starting point

Als Software-Entwickler muss man in der Lage sein, ein Softwareprojekt auf- und umzusetzen. Dabei ist es wichtig, dass es von Beginn weg sauber strukturiert, dokumentiert und getestet wird. Um das zu verinnerlichen, ist es am besten, es immer wieder zu machen und von den vorherigen Erfahrungen zu profitieren.

# :sparkles: What can the budget planner do?

Der "Budget-Planner" ist eine App, die es Benutzern ermöglicht, ihre Einnahmen und Ausgaben zu verwalten und ein Budget zu erstellen. 
Jede Transaktion kann Kategorien zugeordnet werden, und Benutzer können ihr Budget basierend auf ihren Finanzaktivitäten aktualisieren und nachverfolgen.

#### Track It, Stack It! :money_with_wings: :money_with_wings: :money_with_wings:

Das Projekt ist wie folgt aufgebaut:
### Frontend
- React mit Material-UI :lipstick:
- Unter ```/frontend/src``` gibt es den Ordner ```/components``` und ```/services``` diese beinhalten folgendes:
- ```/components```: einzelne Frontend Komponente
- ```/services```: Dienste für Abfragen aus dem Frontend an das Backend 

### Backend
- FastAPI :rocket:
- Unter ```/backend/app``` wurde das Projekt in folgende Unterordner aufgeteilt:
- ```/models``` - Datenbank Modelle
- ```/routers``` - Backend Routen
- ```/schemas``` - Datenbank Schemas
- ```/services``` - Dienste für die einzelnen Komponenten (Business-Logik)
- ```/seeders``` - Datenbank Seeder (z.B. vordefinierte Kategorien)
- Die Config für die Verbindung zur Datenbank befindet sich in folgenden Files: ```/dependencies.py``` und ```/database.py```

### Database
- PostgreSQL innerhalb Docker-Container :whale2:
- Das ```docker-compose.yml``` liegt direkt im root Ordner vom Projekt

Der Budget-Planner unterstützt folgende Funktionen:
- Benutzer Registrierung und Login (mit JWT Integration) :closed_lock_with_key:
- Eintragen von Einnahmen und Ausgaben :money_with_wings:
- Kategorisieren von Einnahmen und Ausgaben :bookmark:
- Einnahmen und Ausgaben anzeigen (pro kategorie und typ) :scroll:

# :rocket: clone and run project
[clone and run project](knowledgebase/CLONE-PROJECT.md)

# :hourglass: If I had more time

## Folgende Ergänzungen würde ich noch machen:
- Endpoint hinzufügen, dass ein User seinen Account löschen kann (somit wird sein Budget und alle seine Einnahmen und Ausgaben gelöscht)
- Funktion für das Ausloggen eines Benutzers hinzufügen
- Funktion hinzufügen, dass ein Benutzer seine eigenen Kategorien erstellen kann (Endpoints dafür sind bereits erstellt)
- Projekt erweitern, dass ein Benutzer mehrere Budgets haben kann (z.B. für verschiedene Konten, oder gemeinsames Budget mit einem anderen User)
- Pagination für die Einnahmen & Ausgaben Tabelle ergänzen (damit die Liste nicht unendlich lang wird und bei vielen Einträgen weiterhin schnell lädt)
- Erweiterte Sicherheit (bessere Validierung für Kennwörter für mehr Komplexität)
- Weitere Backend Tests mit erweiterten Cases

# :lock: Copyright

Bitte kopiere diesen Code nicht... ausser du gibst mir einen :cookie:
</br>
Sonst... lass die Finger davon :point_left:.

# :date: Last Update

> 15.10.2024

# Authors

- [@florianackle](https://www.github.com/florianackle)

# :tada: Have fun!