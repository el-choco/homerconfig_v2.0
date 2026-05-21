# 🛠️ Homer Config Manager v2.1 (Web UI)

*[🇩🇪 Deutsche Version unten](#-deutsche-version)*

A lightweight, web-based Python tool for comfortably managing your [Homer](https://github.com/bastienwirtz/homer) dashboard configuration. 

Instead of manually editing YAML files, this tool provides a sleek, dark-themed Web Interface (GUI) to add, delete, and reorder services within your `config.yml` quickly and without formatting errors.

---

## 🇬🇧 English Version

### ✨ Features & Updates
* 🌐 **Web-based UI:** Say goodbye to the terminal! Input is now handled via a clean, local web form (powered by Flask).
* 📊 **Live Service Overview:** Displays a comprehensive, structured table of all currently configured categories and services directly beneath the form.
* 🗑️ **Native Delete Function:** Remove services from your `config.yml` instantly with a single click using the integrated trash icon and a safety confirmation prompt.
* ↕️ **Up/Down Sorting:** Move services up or down within their categories using visual arrow buttons to reorder your dashboard layout on the fly.
* 🗂️ **Clean Architecture:** Separated into a Python backend (`serviceconfig.py`) and a HTML template (`templates/index.html`) for professional code maintainability.
* 🎨 **FontAwesome Dropdown:** An integrated dropdown menu containing the most common icons for Home-Labs (Network, Cloud, Docker, VPN, etc.).
* ✏️ **Custom Icons:** Easily input your own FontAwesome classes (e.g., `fas fa-cat`) using a dynamically expanding text field.
* 🧹 **One-Click Clear:** A handy "Clear Form" button to reset all input fields instantly without losing your pre-configured `config.yml` path.
* 🌍 **Full UTF-8 Support:** Special characters and umlauts (ä, ö, ü, ß) are written cleanly and natively into the YAML (no more broken unicode characters).
* 🧠 **Smart Category Management:** The script recognizes existing categories (ignoring case and leading/trailing spaces) and integrates new services seamlessly without creating duplicate categories.
* 🛡️ **Anti-F5 Protection:** Implemented the robust Post-Redirect-Get pattern to completely prevent accidental duplicate entries when refreshing the page.
* 📝 **Clean YAML Formatting:** Outputs the perfect Homer format with clean blank lines between items for maximum readability.

### 📁 Project Structure
Ensure your project folder is set up like this:
```text
/homerconfig/
├── serviceconfig.py
└── templates/
    └── index.html
```

### 🚀 Installation & Requirements

The script requires **Python 3** as well as the YAML and Flask modules.

**For Debian / Ubuntu / DietPi:**
```bash
sudo apt update
sudo apt install python3-yaml python3-flask -y
```

**Alternative via pip (for other systems):**
```bash
pip3 install pyyaml flask
```

### 💻 How to Run

1. Make sure the `templates/index.html` file is inside the `templates` subfolder.
2. **Start the script:**
   ```bash
   python3 serviceconfig.py
   ```
   *(Tip: To keep the web server running in the background even after you close the SSH terminal, use `nohup` or `screen`):*
   ```bash
   nohup python3 serviceconfig.py &
   ```
3. The terminal will indicate that the server is running (Default: Port `5000`).
4. Open your web browser and navigate to your server's IP address:
   ```text
   http://<YOUR-SERVER-IP>:5000
   ```
5. Management: Enter new services using the form, reorder them using the arrow buttons, or remove them using the delete button. The script updates the `config.yml` instantly!
6. Refresh your Homer dashboard in the browser (F5) – you're done!

### ⚙️ Configuration

You can change the default path to your `config.yml` directly within the script so you don't have to type it out every time.

Open `serviceconfig.py` and modify this line at the top:
```python
DEFAULT_PATH = '/path/to/your/homer/assets/config.yml'
```

---

## 🇩🇪 Deutsche Version

Ein leichtgewichtiges, webbasiertes Python-Tool zur komfortablen Verwaltung deines [Homer](https://github.com/bastienwirtz/homer) Dashboards.

Anstatt YAML-Dateien händisch zu bearbeiten, bietet dieses Tool ein schickes, dunkles Web-Interface, um neue Services blitzschnell einzutragen, zu löschen oder die Reihenfolge direkt in deiner `config.yml` zu ändern.

### ✨ Features & Neue Updates
* 🌐 **Web-basierte Benutzeroberfläche:** Verabschiede dich vom Terminal! Die Eingabe erfolgt nun über ein übersichtliches, lokales Web-Formular (powered by Flask).
* 📊 **Live-Service-Übersicht:** Zeigt eine vollständige, strukturierte Tabelle aller aktuell konfigurierten Kategorien und Dienste direkt unter dem Formular an.
* 🗑️ **Native Löschfunktion:** Entferne Dienste im Handumdrehen über ein Mülleimer-Symbol direkt aus der `config.yml` (inklusive Sicherheitsabfrage).
* ↕️ **Hoch/Runter-Sortierung:** Verschiebe Dienste innerhalb ihrer Kategorie ganz einfach über Pfeiltasten, um die Reihenfolge im Dashboard sofort anzupassen.
* 🗂️ **Saubere Architektur:** Strikt getrennt in ein Python-Backend (`serviceconfig.py`) und ein HTML-Template (`templates/index.html`) für professionelle Wartbarkeit des Codes.
* 🎨 **FontAwesome Dropdown:** Ein integriertes Dropdown-Menü mit den wichtigsten Icons für Home-Labs (Netzwerk, Cloud, Docker, VPN etc.).
* ✏️ **Custom Icons:** Möglichkeit, jederzeit eigene FontAwesome-Klassen (z.B. `fas fa-cat`) über ein dynamisch aufklappendes Textfeld einzugeben.
* 🧹 **Ein-Klick-Reset:** Ein praktischer "Clear Form"-Button, um alle Eingabefelder sofort zu leeren, ohne dass dein vorkonfigurierter Pfad zur `config.yml` verloren geht.
* 🌍 **Vollständiger UTF-8 Support:** Umlaute und Sonderzeichen (ä, ö, ü, ß) werden sauber und nativ in die YAML geschrieben.
* 🧠 **Smartes Kategorie-Management:** Das Skript erkennt bestehende Kategorien (ignoriert Groß-/Kleinschreibung und Leerzeichen) und fügt neue Services nahtlos ein, ohne Kategorien zu duplizieren.
* 🛡️ **Anti-F5-Schutz:** Durch das "Post-Redirect-Get"-Muster wird das versehentliche, doppelte Eintragen von Services beim Neuladen der Seite (F5) komplett verhindert.
* 📝 **Saubere YAML-Formatierung:** Output im perfekten Homer-Format mit sauberen Leerzeilen zwischen den Items – für maximale Lesbarkeit.

### 📁 Projektstruktur
Achte darauf, dass deine Ordnerstruktur auf dem Server wie folgt aussieht:
```text
/homerconfig/
├── serviceconfig.py
└── templates/
    └── index.html
```

### 🚀 Installation & Voraussetzungen

Das Skript benötigt **Python 3** sowie die Module für YAML und Flask.

**Für Debian / Ubuntu / DietPi:**
```bash
sudo apt update
sudo apt install python3-yaml python3-flask -y
```

### 💻 Starten & Verwendung

1. Stelle sicher, dass sich die Datei `index.html` im Unterordner `templates` befindet.
2. **Starte den Webserver:**
   ```bash
   python3 serviceconfig.py
   ```
   *(Tipp: Damit das Skript dauerhaft im Hintergrund weiterläuft, auch wenn du das SSH-Fenster schließt, nutze `nohup` oder `screen`):*
   ```bash
   nohup python3 serviceconfig.py &
   ```
3. Das Terminal zeigt an, dass der Server läuft (Standard: Port `5000`).
4. Öffne deinen Webbrowser und navigiere zur IP-Adresse deines Servers:
   ```text
   http://<DEINE-SERVER-IP>:5000
   ```
5. Verwaltung: Neue Dienste über das Formular eintragen, über die Pfeiltasten verschieben oder mit dem Mülleimer-Button löschen. Das Skript aktualisiert die `config.yml` sofort!
6. Lade dein Homer-Dashboard im Browser neu (F5) – fertig!

### ⚙️ Konfiguration anpassen

Du kannst den Standardpfad zu deiner `config.yml` direkt im Skript anpassen, damit du ihn im Web-Interface nicht jedes Mal neu eintippen musst.

Öffne die `serviceconfig.py` und ändere diese Zeile ganz oben:
```python
DEFAULT_PATH = '/pfad/zu/deinem/homer/assets/config.yml'
```

---

# Homer Service Configuration Tool README

## Overview
This tool is designed to help manage and update the Homer service configuration file. It automates the process of adding new services to the Homer dashboard.

## Prerequisites
- Python installed on your system.
- Homer installed on your system:  https://github.com/bastienwirtz/homer
- An existing Homer service configuration file (usually in YAML format).
- Basic familiarity with running Python scripts and editing YAML files.

## Installation
1. Ensure Python is installed on your machine.
2. Install the `PyYAML` library, necessary for the script. Use the following command:
```
pip install pyyaml
```


## Configuration File Path
Before running the script, make sure to update the `config_file_path` variable in `serviceconfig.py` to point to your actual Homer configuration file. Replace `'path/to/your/homer/config.yml'` with the correct path.

## Backup Your Configuration
It's advised to back up your existing Homer configuration file before running this script to prevent any accidental loss of data. Create a backup of your configuration file using this command:

```
cp path/to/your/homer/config.yml path/to/your/homer/config.yml.bkup
```

## Usage
1. Place `serviceconfig.py` in a convenient location on your computer.
2. Open a terminal or command prompt.
3. Navigate to the directory where `serviceconfig.py` is located.
4. Run the script using Python:

```
python3 serviceconfig.py
```
5. Follow the on-screen prompts to input details for the new service.

### Inputs
When running `serviceconfig.py`, you will be prompted to enter:
- **Category Name**: The name of the category under which the service will be listed (e.g., 'Apps').
- **Category Icon**: The icon for the category (leave blank for default 'fas fa-cloud').
- **Service Name**: The name of the new service.
- **URL**: The URL for the new service.
- **Logo URL or Path**: The URL or path to the logo for the new service (leave blank for default logo).
- **Tags**: Tags for the new service, separated by commas (leave blank if none).
- **Keywords**: Keywords for the new service, separated by commas (leave blank if none).

The script will update your Homer service configuration file with the provided details.
