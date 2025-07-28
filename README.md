# LizenzprueferUI

![Python](https://img.shields.io/badge/Python-3.13-blue) ![VS Code](https://img.shields.io/badge/Editor-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white) ![UI Framework](https://img.shields.io/badge/UI%20Framework-ttkbootstrap-2D74B2?style=flat-square&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green)

Ein Python-basiertes Lizenzprüfungssystem, das Lizenzdateien mit RSA-Signaturen validiert und ein modernes grafisches Benutzerinterface mit anpassbarem Design bietet.

## Voraussetzungen
- Python 3.13.4 oder höher
- Bibliotheken:
  - `cryptography` – zur digitalen Signaturprüfung
  - `ttkbootstrap` – für moderne Themes und GUI-Komponenten
  - `Pillow` – für Icon-/Bildverarbeitung in der GUI

## Installation
1. Klone das Repository oder kopiere die Dateien.
   ```bash
   git clone https://github.com/dein-name/LizenzprueferUI.git
   cd ./LizenzprueferUI
   ```
2. Stelle sicher, dass Python 3.13.4 installiert ist:
   ```bash
   python --version
   ```
3. Erstelle und aktiviere eine virtuelle Umgebung:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
4. Installiere die Abhängigkeit:
   ```bash
   pip install cryptography pillow ttkbootstrap
   ```
5. Starte die Anwendung:
   ```bash
   python lizenzpruefer.py --help
   ```

## Nutzung
- **Schlüsselpaar generieren**:
   ```bash
   python lizenzpruefer.py --generiere-schluessel
   ```
- **Lizenzdatei erstellen**:
   ```bash
   python lizenzpruefer.py --erstelle-lizenz --lizenznehmer "Max Mustermann" --ablaufdatum "2026-12-31" --produkt-id "PROD123" --lizenz-datei config/licenses/lizenz.json
   ```
- **Lizenzdatei prüfen**:
   ```bash
   python lizenzpruefer.py --pruefe-lizenz --lizenz-datei config/licenses/lizenz.json
   ```
- Ausgabe zeigt, ob die Lizenz gültig ist, und gibt Lizenznehmer, Produkt-ID und Ablaufdatum an.

### Grafische Benutzeroberfläche (GUI)

![LizenzprueferUI](.screenshots/lizenzprueferui.png)

### Übersicht

Das Projekt bietet zusätzlich zur Kommandozeile eine intuitive, visuell anpassbare Benutzeroberfläche in `lizenzprueferui.py`. Die GUI ist vollständig mit [ttkbootstrap](https://ttkbootstrap.readthedocs.io/) gestaltet und unterstützt:

* Dynamische Theme-Auswahl
* Integration von benutzerdefinierten Styles (Custom Styles)
* Visuelle Rückmeldungen (MessageBox, Popups)
* Pfadauswahl für Lizenzdateien (mit Voreinstellungen)
* Unterstützung moderner GUI-Designs wie Glassmorphism und Neumorphism

Neben der Kommandozeilen-Nutzung bietet das Projekt eine grafische Benutzeroberfläche, die in `lizenzpruefer_gui.py` implementiert ist. Diese ermöglicht eine intuitive Bedienung der folgenden Funktionen:

### GUI-Funktionen
* **Schlüsselpaar generieren**
  Erzeugt RSA-Schlüsselpaare über einen Button

* **Lizenzdatei erstellen**
  Eingabefelder für:

  * Lizenznehmer
  * Ablaufdatum (Format: `YYYY-MM-DD`)
  * Produkt-ID
  * Lizenzdatei-Zielpfad (voreingestellt, aber veränderbar)

* **Lizenz prüfen**
  Öffnet eine Datei, prüft die digitale Signatur und zeigt die Gültigkeit visuell an

### Start der GUI
1. Aktiviere die virtuelle Umgebung:

   ```bash
   .venv\Scripts\Activate.ps1
   ```
2. Starte die GUI:

   ```bash
   python lizenzprueferui.py
   ```
3. Voraussetzungen:

   * Datei `fs.ico` muss im selben Verzeichnis liegen
   * Styles werden automatisch erkannt

## Design & Theme-System

Die Anwendung unterstützt eine Vielzahl von Design-Themes aus `ttkbootstrap` und erweitert diese durch individuell gestaltete **Custom Styles** (z. B. Neon, Glass, Mid Blue).

### Designauswahl im Code

```python
from ttkbootstrap import Style
style = Style(theme="flatly")  # oder: "neon", "glass", etc.
```

### Verfügbare Themes

```python
themes = {
    "Flatly (Material Design)": "flatly",
    "Flatly (Mid Blue)": "flatly_midblue",
    "Journal (Minimal UI)": "journal",
    "Cyborg (Dark Mode)": "cyborg",
    "Vapor (Modern Flat)": "vapor",
    "Solar (Retro)": "solar",
    "Superhero (Neo-Brutal)": "superhero",
    "Darkly (Dark Flat)": "darkly",
    "Litera (Clean Light)": "litera",
    "Litera (Mid Blue)": "litera_midblue",
    "Lumen (Soft Light)": "lumen",
    "Cosmo (Modern Light)": "cosmo",
    "Minty (Fresh Light)": "minty",
    "Pulse (Vibrant)": "pulse",
    "United (Bold)": "united",
    "Yeti (Soft Blue)": "yeti",
    "Yeti (Mid Blue)": "yeti_midblue",
    "Dark Neon Mode": "neon",
    "Glassmorphism": "glass",
    "Neumorphism": "neumo",
    "Claymorphism": "claymo",
    "Aurora Art Style": "aurora",
    "Neo-Brutal (Gelb)": "neo"
}
```

### Eigene Styles (Beispiel: Neon)

In der GUI werden Custom Styles über `style.configure(...)` definiert, z. B.:

```python
style.configure("neon.TButton",
    background="#00ff00",
    foreground="#000000",
    bordercolor="#00ff00",
    lightcolor="#00ff00",
    darkcolor="#00aa00",
    borderwidth=2,
    relief="flat"
)
```

Weitere Designsysteme wie **Glasmorphism (transparente UI-Felder)** und **Neumorphism (weiche 3D-Effekte)** sind ebenfalls integriert und über das Theme-Auswahlmenü nutzbar.

## Lizenz
Die Anwendung ist unter der [MIT-Lizenz](./LICENSE) lizenziert.