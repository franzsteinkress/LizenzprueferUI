# Copyright (c) 2025 Franz Steinkress
# Licensed under the MIT License - see LICENSE for details
#
# lizenzprueferui.py
# Lizenzprüfungssystem mit auswählbarem UI-Design

import os
import sys
import subprocess
import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style
from ttkbootstrap.window import Window
from ttkbootstrap import ttk


# Fenster erstellen
fenster = Window(themename="flatly")
fenster.title("LizenzprüferUI")
try:
    fenster.iconbitmap('resources/fs.ico')
except Exception as e:
    print(f"Fehler beim Laden des Icons: {e}")
fenster.geometry("600x600")

# Style-Instanz nach Fenster erzeugen
style = Style(theme="flatly")

fenster.columnconfigure(0, weight=1)
fenster.rowconfigure([0, 1, 2, 3], weight=1)

# Benutzerdefinierte Styles definieren
def configure_custom_styles():
    style.configure("neon.TButton", background="#00ff00", foreground="#000000", bordercolor="#00ff00", lightcolor="#00ff00", darkcolor="#00ff00")
    style.configure("neon.TLabel", background="#1a1a1a", foreground="#00ff00")
    style.configure("neon.TEntry", fieldbackground="#333333", foreground="#00ff00")
    style.configure("neon.TLabelframe", background="#1a1a1a", foreground="#00ff00")
    style.configure("neon.TLabelframe.Label", background="#1a1a1a", foreground="#00ff00")

    #style.configure("glass.TButton", background="#ffffff80", foreground="#000000", bordercolor="#ffffff", lightcolor="#ffffffcc", darkcolor="#ffffff99", relief="flat")
    #style.configure("glass.TLabel", background="#ffffff80", foreground="#000000")
    #style.configure("glass.TEntry", fieldbackground="#ffffff80", foreground="#000000", bordercolor="#ffffff")
    #style.configure("glass.TLabelframe", background="#ffffff80", foreground="#000000")
    #style.configure("glass.TLabelframe.Label", background="#ffffff80", foreground="#000000")
    # Statt: "#ffffff80" (ungültig)
    style.configure("glass.TButton", background="#f8f8f8", foreground="#000000", bordercolor="#cccccc", lightcolor="#ffffff", darkcolor="#dddddd", relief="flat")
    style.configure("glass.TLabel", background="#f0f0f0", foreground="#000000")
    style.configure("glass.TEntry", fieldbackground="#ffffff", foreground="#000000", bordercolor="#cccccc")
    style.configure("glass.TLabelframe", background="#f0f0f0", foreground="#000000")
    style.configure("glass.TLabelframe.Label", background="#f0f0f0", foreground="#000000")

    style.configure("neumo.TButton", background="#e0e0e0", foreground="#333333", bordercolor="#b0b0b0", lightcolor="#ffffff", darkcolor="#b0b0b0", relief="flat")
    style.configure("neumo.TLabel", background="#e0e0e0", foreground="#333333")
    style.configure("neumo.TEntry", fieldbackground="#e0e0e0", foreground="#333333", bordercolor="#b0b0b0")
    style.configure("neumo.TLabelframe", background="#e0e0e0", foreground="#333333")
    style.configure("neumo.TLabelframe.Label", background="#e0e0e0", foreground="#333333")

    #style.configure("claymo.TButton", background="#e0e0e0", foreground="#333333", bordercolor="#a0a0a0", lightcolor="#ffffff", darkcolor="#a0a0a0", relief="flat", borderwidth=2)
    #style.configure("claymo.TLabel", background="#e0e0e0", foreground="#333333")
    #style.configure("claymo.TEntry", fieldbackground="#e0e0e0", foreground="#333333", bordercolor="#a0a0a0")
    #style.configure("claymo.TLabelframe", background="#e0e0e0", foreground="#333333")
    #style.configure("claymo.TLabelframe.Label", background="#e0e0e0", foreground="#333333")
    # Claymorphism: Stärkere Schatten, runde Ecken, plastischer Look
    style.configure("claymo.TButton", background="#d0e1f9", foreground="#333333", bordercolor="#7aa7d2", lightcolor="#ffffff", darkcolor="#a0bcd0", relief="raised", borderwidth=4)
    style.configure("claymo.TLabel", background="#d0e1f9", foreground="#333333")
    style.configure("claymo.TEntry", fieldbackground="#ffffff", foreground="#000000", bordercolor="#7aa7d2")
    style.configure("claymo.TLabelframe", background="#d0e1f9", foreground="#333333")
    style.configure("claymo.TLabelframe.Label", background="#d0e1f9", foreground="#333333")
    
    # Aurora Art Style
    style.configure("aurora.TButton", background="#00FFFF", foreground="#FFFFFF", bordercolor="#70FF00", lightcolor="#FF00FF", darkcolor="#2E003E", relief="flat")
    style.configure("aurora.TLabel", background="#2E003E", foreground="#FFFFFF")
    style.configure("aurora.TEntry", fieldbackground="#4B006E", foreground="#FFFFFF", bordercolor="#70FF00")
    style.configure("aurora.TLabelframe", background="#2E003E", foreground="#FFFFFF")
    style.configure("aurora.TLabelframe.Label", background="#2E003E", foreground="#FFFFFF")

    # Neo-Brutal
    style.configure("neo.TButton", background="#000000", foreground="#F8D300", bordercolor="#000000", lightcolor="#000000", darkcolor="#000000", relief="flat", borderwidth=3)
    style.configure("neo.TLabel", background="#F8D300", foreground="#000000")
    style.configure("neo.TEntry", fieldbackground="#ffffff", foreground="#000000", bordercolor="#000000")
    style.configure("neo.TLabelframe", background="#F8D300", foreground="#000000")
    style.configure("neo.TLabelframe.Label", background="#F8D300", foreground="#000000")

    style.configure("flatly_midblue.TButton", background="#2D74B2", foreground="#ffffff", bordercolor="#1f5a8c", lightcolor="#438ecc", darkcolor="#1e4c72", relief="groove", borderwidth=2)
    style.configure("flatly_midblue.TLabel", background="#e9ecef", foreground="#2D74B2")
    style.configure("flatly_midblue.TEntry", fieldbackground="#ffffff", foreground="#2D74B2")
    style.configure("flatly_midblue.TLabelframe", background="#e9ecef", foreground="#2D74B2")
    style.configure("flatly_midblue.TLabelframe.Label", background="#e9ecef", foreground="#2D74B2")

    style.configure("litera_midblue.TButton", background="#2D74B2", foreground="#ffffff", bordercolor="#235c91", lightcolor="#4a95d6", darkcolor="#1a4b6f", relief="ridge", borderwidth=1)
    style.configure("litera_midblue.TLabel", background="#ffffff", foreground="#2D74B2")
    style.configure("litera_midblue.TEntry", fieldbackground="#fdfdfd", foreground="#2D74B2")
    style.configure("litera_midblue.TLabelframe", background="#ffffff", foreground="#2D74B2")
    style.configure("litera_midblue.TLabelframe.Label", background="#ffffff", foreground="#2D74B2")

    style.configure("yeti_midblue.TButton", background="#2D74B2", foreground="#ffffff", bordercolor="#245e8f", lightcolor="#3e8dd0", darkcolor="#1a4d77", relief="raised", borderwidth=1)
    style.configure("yeti_midblue.TLabel", background="#f8f9fa", foreground="#2D74B2")
    style.configure("yeti_midblue.TEntry", fieldbackground="#ffffff", foreground="#2D74B2", bordercolor="#245e8f")
    style.configure("yeti_midblue.TLabelframe", background="#f8f9fa", foreground="#2D74B2")
    style.configure("yeti_midblue.TLabelframe.Label", background="#f8f9fa", foreground="#2D74B2")

def reset_custom_styles():
    # Setze alle custom styles auf "leer", damit sie nicht mehr wirken
    for prefix in ["neon", "glass", "neumo", "claymo", "aurora", "neo", "flatly_midblue", "litera_midblue", "yeti_midblue"]:
        style.configure(f"{prefix}.TButton", background="", foreground="", bordercolor="", lightcolor="", darkcolor="", relief="")
        style.configure(f"{prefix}.TLabel", background="", foreground="")
        style.configure(f"{prefix}.TEntry", fieldbackground="", foreground="", bordercolor="")
        style.configure(f"{prefix}.TLabelframe", background="", foreground="")
        style.configure(f"{prefix}.TLabelframe.Label", background="", foreground="")

# Hilfsfunktion für Python-Interpreter-Pfad
def get_python_executable():
    if hasattr(sys, 'frozen'):
        return sys.executable
    venv_path = os.path.join(os.getcwd(), ".venv", "Scripts" if sys.platform == "win32" else "bin", "python.exe" if sys.platform == "win32" else "python")
    return venv_path if os.path.exists(venv_path) else sys.executable

# Lizenz-Subprozesse (gleich wie vorher)
def generate_keypair():
    try:
        result = subprocess.run([
            get_python_executable(),
            "lizenzpruefer.py",
            "--generiere-schluessel"
        ], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Erfolg", "Schlüsselpaar generiert!\n" + result.stdout)
        else:
            messagebox.showerror("Fehler", "Fehler beim Generieren:\n" + result.stderr)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler: {str(e)}")

def choose_license_save_path():
    folder = filedialog.askdirectory(
        initialdir=os.path.join(os.getcwd(), "config", "licenses"),
        title="Zielverzeichnis wählen"
    )
    if folder:
        # Dateiname aus Entry holen
        dateiname = os.path.basename(entry_lizenz_datei.get().strip())

        # Leerer oder ungültiger Dateiname? Fallback
        if not dateiname:
            dateiname = "lizenz.json"
        elif not dateiname.endswith(".json"):
            dateiname += ".json"

        # Neuen Pfad zusammensetzen
        file_path = os.path.join(folder, dateiname)

        # Entry aktualisieren
        entry_lizenz_datei.delete(0, tk.END)
        entry_lizenz_datei.insert(0, file_path)

def create_license():
    lizenznehmer = entry_lizenznehmer.get().strip()
    ablaufdatum = entry_ablaufdatum.get().strip()
    produkt_id = entry_produkt_id.get().strip()
    lizenz_datei = entry_lizenz_datei.get().strip() or "config/licenses/lizenz.json"
    if not all([lizenznehmer, ablaufdatum, produkt_id]):
        messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen!")
        return
    try:
        cmd = [
            get_python_executable(),
            "lizenzpruefer.py",
            "--erstelle-lizenz",
            "--lizenznehmer", lizenznehmer,
            "--ablaufdatum", ablaufdatum,
            "--produkt-id", produkt_id,
            "--lizenz-datei", lizenz_datei
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Erfolg", f"Lizenzdatei erstellt: {lizenz_datei}\n" + result.stdout)
        else:
            messagebox.showerror("Fehler", "Fehler beim Erstellen:\n" + result.stderr)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler: {str(e)}")

def choose_license_load_path():
    file_path = filedialog.askopenfilename(
        defaultextension=".json",
        filetypes=[("JSON-Dateien", "*.json")],
        initialdir=os.path.join(os.getcwd(), "config", "licenses"),
        title="Lizenzdatei auswählen"
    )
    if file_path:
        entry_lizenz_datei_check.delete(0, tk.END)
        entry_lizenz_datei_check.insert(0, file_path)

def check_license():
    lizenz_datei = entry_lizenz_datei_check.get().strip() or "lizenz.json"
    if not lizenz_datei:
        messagebox.showerror("Fehler", "Bitte Lizenzdatei angeben!")
        return
    try:
        result = subprocess.run([
            get_python_executable(),
            "lizenzpruefer.py",
            "--pruefe-lizenz",
            "--lizenz-datei", lizenz_datei
        ], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Erfolg", "Lizenz ist gültig!\n" + result.stdout)
        else:
            messagebox.showerror("Fehler", "Lizenz ungültig:\n" + result.stderr)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler: {str(e)}")

# Themes
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

def change_theme(event=None):
    selected_theme_name = theme_dropdown.get()
    theme_key = themes.get(selected_theme_name)
    if not theme_key:
        messagebox.showerror("Fehler", "Kein gültiges Theme ausgewählt.")
        return
    try:
        #print(f"Versuche Theme '{theme_key}' zu laden")

        if theme_key in ["neon", "glass", "neumo", "claymo", "aurora", "neo", "flatly_midblue", "litera_midblue", "yeti_midblue"]:
            # Custom Themes basieren auf darkly oder litera
            base_theme = "darkly" if theme_key == "neon" else "litera"
            style.theme_use(base_theme)

            # Schriftgewichte bei United (bold)
            if theme_key == "united":
                default_font = ("Segoe UI", 10, "bold")
            else:
                default_font = ("Segoe UI", 10, "normal")
            style.configure(".", font=default_font)

            # Custom Styles setzen
            configure_custom_styles()

            # Widgets mit Custom Styles anpassen
            prefix = theme_key

            # Nur für Glassmorphism Fensterhintergrund setzen
            if theme_key == "neon":
                fenster.configure(bg="#1a1a1a")
            elif theme_key == "glass":
                fenster.configure(bg="#f0f0f0")
            elif theme_key == "neumo":
                fenster.configure(bg="#e0e0e0")
            elif theme_key == "claymo":
                fenster.configure(bg="#d0e1f9")
            elif theme_key == "aurora":
                fenster.configure(bg="#2E003E")
            elif theme_key == "neo":
                fenster.configure(bg="#F8D300")

            for frame in [frame_theme, frame_key, frame_create, frame_check]:
                frame.configure(style=f"{prefix}.TLabelframe")

            for widget in frame_theme.winfo_children() + frame_key.winfo_children() + frame_create.winfo_children() + frame_check.winfo_children():
                if isinstance(widget, ttk.Button):
                    widget.configure(style=f"{prefix}.TButton")
                elif isinstance(widget, ttk.Label):
                    widget.configure(style=f"{prefix}.TLabel")
                elif isinstance(widget, ttk.Entry):
                    widget.configure(style=f"{prefix}.TEntry")
                elif isinstance(widget, ttk.Combobox):
                    widget.configure(style=f"{prefix}.TCombobox")

            if theme_key == "glass":
                fenster.configure(bg="#f0f0f0")
            else:
                fenster.configure(bg=style.lookup(f"{prefix}.TLabel", "background"))

        else:
            # Reset Custom Styles und setze Standard-Theme
            reset_custom_styles()
            style.theme_use(theme_key)

            # Schriftgewichte bei United (bold)
            if theme_key == "united":
                default_font = ("Segoe UI", 10, "bold")
            else:
                default_font = ("Segoe UI", 10, "normal")
            style.configure(".", font=default_font)

            # Widgets auf Standard-Stile setzen
            for frame in [frame_theme, frame_key, frame_create, frame_check]:
                frame.configure(style="TLabelframe")

            for widget in frame_theme.winfo_children() + frame_key.winfo_children() + frame_create.winfo_children() + frame_check.winfo_children():
                if isinstance(widget, ttk.Button):
                    widget.configure(style="TButton")
                elif isinstance(widget, ttk.Label):
                    widget.configure(style="TLabel")
                elif isinstance(widget, ttk.Entry):
                    widget.configure(style="TEntry")
                elif isinstance(widget, ttk.Combobox):
                    widget.configure(style="TCombobox")

            fenster.configure(bg=style.lookup("TLabel", "background"))

    except Exception as e:
        messagebox.showerror("Theme-Fehler", str(e))

# Widgets erstellen
frame_theme = ttk.Labelframe(fenster, text="Theme auswählen")
frame_theme.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
frame_theme.columnconfigure(0, weight=1)

theme_dropdown = ttk.Combobox(frame_theme, values=list(themes.keys()), state="readonly", width=40)
theme_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="")
theme_dropdown.set("Flatly (Material Design)")
theme_dropdown.bind("<<ComboboxSelected>>", change_theme)

# --- Frame: Schlüsselpaar --- #
frame_key = ttk.Labelframe(fenster, text="Schlüsselpaar generieren")
frame_key.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
frame_key.columnconfigure(0, weight=1)
frame_key.rowconfigure(0, weight=1)

btn_generate_key = ttk.Button(frame_key, text="Schlüsselpaar generieren", command=generate_keypair, width=30)
btn_generate_key.grid(row=0, column=0, padx=10, pady=10, sticky="")

# --- Frame: Lizenz erstellen --- #
frame_create = ttk.Labelframe(fenster, text="Lizenzdatei erstellen")
frame_create.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
frame_create.columnconfigure(0, weight=1)
frame_create.columnconfigure(1, weight=1)
frame_create.columnconfigure(2, weight=1)
frame_create.rowconfigure([0, 1, 2, 3, 4], weight=1)

ttk.Label(frame_create, text="Lizenznehmer (Name):", width=27).grid(row=0, column=0, sticky="w", padx=10, pady=2)
entry_lizenznehmer = ttk.Entry(frame_create, width=40)
entry_lizenznehmer.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
entry_lizenznehmer.insert(0, "Max Mustermann")

ttk.Label(frame_create, text="Produkt-ID:", width=27).grid(row=1, column=0, sticky="w", padx=10, pady=2)
entry_produkt_id = ttk.Entry(frame_create, width=40)
entry_produkt_id.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
entry_produkt_id.insert(0, "PROD123")

ttk.Label(frame_create, text="Gültig bis (YYYY-MM-DD):", width=27).grid(row=2, column=0, sticky="w", padx=10, pady=2)
entry_ablaufdatum = ttk.Entry(frame_create, width=40)
entry_ablaufdatum.grid(row=2, column=1, padx=5, pady=2, sticky="ew")
entry_ablaufdatum.insert(0, "2026-12-31")

ttk.Label(frame_create, text="Lizenzdatei (Pfad):", width=27).grid(row=3, column=0, sticky="w", padx=10, pady=2)
entry_lizenz_datei = ttk.Entry(frame_create, width=40)
entry_lizenz_datei.grid(row=3, column=1, padx=5, pady=2, sticky="ew")
entry_lizenz_datei.insert(0, "config/licenses/lizenz.json")
btn_choose_save = ttk.Button(frame_create, text="Pfad wählen", command=choose_license_save_path, width=14)
btn_choose_save.grid(row=3, column=2, padx=10, pady=2, sticky="ew")

btn_create_license = ttk.Button(frame_create, text="Lizenz erstellen", command=create_license, width=30)
btn_create_license.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="")

# --- Frame: Lizenz prüfen --- #
frame_check = ttk.Labelframe(fenster, text="Lizenzdatei prüfen")
frame_check.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
frame_check.columnconfigure(0, weight=1)
frame_check.columnconfigure(1, weight=1)
frame_check.columnconfigure(2, weight=1)
frame_check.rowconfigure([0, 1], weight=1)

ttk.Label(frame_check, text="Lizenzdatei (Inhalt):", width=27).grid(row=0, column=0, sticky="w", padx=10, pady=2)
entry_lizenz_datei_check = ttk.Entry(frame_check, width=40)
entry_lizenz_datei_check.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
entry_lizenz_datei_check.insert(0, "config/licenses/lizenz.json")
btn_choose_check = ttk.Button(frame_check, text="Datei wählen", command=choose_license_load_path, width=14)
btn_choose_check.grid(row=0, column=2, padx=10, pady=2, sticky="ew")

btn_check_license = ttk.Button(frame_check, text="Lizenz prüfen", command=check_license, width=30)
btn_check_license.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="")

# Initiales Theme setzen
change_theme()

fenster.mainloop()
