# Wir nutzen ein extrem schlankes, offizielles Python-Image
FROM python:3.11-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Flask und YAML installieren
RUN pip install --no-cache-dir flask pyyaml

# Unser Skript und den templates-Ordner in den Container kopieren
COPY . /app

# Port 5000 nach außen freigeben
EXPOSE 5000

# Den Startbefehl festlegen
CMD ["python", "serviceconfig.py"]
