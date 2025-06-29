```markdown
# Downloads Screenshot Manager 📸

Een eenvoudige webapplicatie om screenshots en afbeeldingen in je Downloads folder te beheren. Met thumbnail preview, bulk selectie en directe verwijdering.

## Features

- 🖼️ **Thumbnail preview** van alle afbeeldingen in ~/Downloads
- 🗑️ **Direct verwijderen** met één klik
- ✅ **Bulk selectie** voor het verwijderen van meerdere afbeeldingen tegelijk
- ⌨️ **Volledige keyboard navigatie** met pijltjestoetsen
- 🔍 **Klik op thumbnail** voor grotere weergave
- 🔄 **Automatische refresh** functionaliteit
- 📏 **Bestandsgrootte** weergave
- 📅 **Gesorteerd** op wijzigingsdatum (nieuwste eerst)

## Vereisten

- Python 3.6 of hoger
- pip (Python package manager)

## Installatie

### 1. Clone of download de code

Maak een nieuwe folder en kopieer de bestanden:

```bash
mkdir screenshot-manager
cd screenshot-manager
mkdir templates
```

Kopieer:
- `app.py` naar de hoofdmap
- `index.html` naar de `templates` map

### 2. Virtual environment instellen (aanbevolen)

```bash
# Maak virtual environment
python3 -m venv venv

# Activeer het virtual environment
source venv/bin/activate  # Op macOS/Linux
# of
venv\Scripts\activate     # Op Windows
```

### 3. Installeer dependencies

```bash
pip install flask pillow
```

## Gebruik

### 1. Start de applicatie

```bash
python app.py
```

Je zou moeten zien:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 2. Open in je browser

Ga naar: `http://localhost:5000`

### 3. Afbeeldingen beheren

De applicatie toont automatisch alle afbeeldingen (PNG, JPG, GIF, etc.) uit je `~/Downloads` folder.

## Keyboard Shortcuts ⌨️

| Toets | Actie |
|-------|-------|
| `←` `→` `↑` `↓` | Navigeer door afbeeldingen |
| `Spatie` | Selecteer/deselecteer huidige afbeelding |
| `Enter` | Open afbeelding in preview |
| `Delete` | Verwijder huidige afbeelding |
| `A` | Selecteer alle afbeeldingen |
| `D` | Deselecteer alle afbeeldingen |
| `Shift + Delete` | Verwijder alle geselecteerde afbeeldingen |
| `Esc` | Sluit preview |
| `F5` of `Ctrl/Cmd + R` | Ververs de lijst |

## Muis/Touch Bediening

- **Klik op thumbnail**: Preview in groot formaat
- **Checkbox aanvinken**: Selecteren voor bulk acties
- **Rode knop**: Direct verwijderen
- **Vernieuw knop**: Lijst bijwerken
- **Bulk verwijder knop**: Verschijnt als je items selecteert

## Ondersteunde Bestandsformaten

- PNG
- JPG/JPEG
- GIF
- BMP
- WebP
- TIFF

## Mapstructuur

```
screenshot-manager/
├── app.py                 # Flask backend
├── templates/
│   └── index.html        # Frontend interface
├── venv/                 # Virtual environment (wordt aangemaakt)
└── README.md             # Dit bestand
```

## Veiligheid & Privacy 🔒

- **Lokaal alleen**: De app draait alleen op je eigen computer
- **Geen internet verbinding nodig**: Alle bestanden blijven lokaal
- **Direct verwijderen**: Bestanden worden permanent verwijderd uit je Downloads folder
- **Confirmatie dialogen**: Voor het verwijderen van bestanden

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"

Je virtual environment is niet geactiveerd. Zorg ervoor dat je het activeert:

```bash
source venv/bin/activate  # macOS/Linux
# of
venv\Scripts\activate     # Windows
```

### Applicatie start niet

Controleer of je in de juiste map bent en alle bestanden aanwezig zijn:

```bash
ls -la
# Je zou moeten zien: app.py en templates/
```

### Geen afbeeldingen zichtbaar

- Controleer of er daadwerkelijk afbeeldingen in `~/Downloads` staan
- Klik op "🔄 Vernieuwen" om de lijst bij te werken
- Ondersteunde formaten: PNG, JPG, GIF, BMP, WebP, TIFF

### Poort 5000 al in gebruik

Start de app op een andere poort:

```python
# Wijzig de laatste regel in app.py
app.run(debug=True, port=5001)  # Of andere poort
```

## Customization

### Andere map dan Downloads

Wijzig in `app.py` de regel:

```python
DOWNLOADS_PATH = Path.home() / "Downloads"
```

naar bijvoorbeeld:

```python
DOWNLOADS_PATH = Path.home() / "Pictures" / "Screenshots"
```

### Thumbnail grootte aanpassen

In `app.py`, wijzig:

```python
img.thumbnail((300, 300))  # Verander naar gewenste grootte
```

### Andere poort

In `app.py`, laatste regel:

```python
app.run(debug=True, port=8080)  # Wijzig poort
```

## Toegang vanaf andere apparaten

**Waarschuwing**: Doe dit alleen in een vertrouwde netwerkomgeving!

Wijzig in `app.py` de laatste regel naar:

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

Dan is de app toegankelijk via: `http://[jouw-ip-adres]:5000`

## Stoppen van de Applicatie

- Druk `Ctrl + C` in de terminal waar de app draait
- Of sluit het terminal venster

## Virtual Environment Deactiveren

```bash
deactivate
```

## Bijdragen

Pull requests zijn welkom! Voor grote wijzigingen, open eerst een issue om te bespreken wat je wilt veranderen.

## Licentie

Dit project is gelicenseerd onder de MIT License.

---

**Let op**: Deze applicatie verwijdert bestanden permanent. Zorg ervoor dat je backups hebt van belangrijke bestanden voordat je ze verwijdert.
```