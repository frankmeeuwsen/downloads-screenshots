from flask import Flask, render_template, send_file, jsonify, request
import os
from pathlib import Path
import mimetypes
from PIL import Image
import io
import base64

app = Flask(__name__)

# Path naar Downloads folder
DOWNLOADS_PATH = Path.home() / "Downloads"

# Ondersteunde afbeeldingsformaten
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff'}

def is_image(filepath):
    """Check of bestand een afbeelding is"""
    return filepath.suffix.lower() in IMAGE_EXTENSIONS

def get_images():
    """Haal alle afbeeldingen uit Downloads folder"""
    images = []
    for file in DOWNLOADS_PATH.iterdir():
        if file.is_file() and is_image(file):
            images.append({
                'name': file.name,
                'path': str(file),
                'size': file.stat().st_size,
                'modified': file.stat().st_mtime
            })
    # Sorteer op wijzigingsdatum (nieuwste eerst)
    images.sort(key=lambda x: x['modified'], reverse=True)
    return images

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/images')
def get_images_list():
    """API endpoint om lijst met afbeeldingen te krijgen"""
    images = get_images()
    return jsonify(images)

@app.route('/api/thumbnail/<path:filename>')
def get_thumbnail(filename):
    """Genereer en stuur thumbnail"""
    filepath = DOWNLOADS_PATH / filename
    
    if not filepath.exists() or not filepath.is_file():
        return "File not found", 404
    
    try:
        # Open afbeelding en maak thumbnail
        img = Image.open(filepath)
        img.thumbnail((300, 300))
        
        # Converteer naar bytes
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/api/delete/<path:filename>', methods=['DELETE'])
def delete_image(filename):
    """Verwijder afbeelding"""
    filepath = DOWNLOADS_PATH / filename
    
    if not filepath.exists() or not filepath.is_file():
        return jsonify({'error': 'File not found'}), 404
    
    try:
        filepath.unlink()  # Verwijder bestand
        return jsonify({'success': True, 'message': f'{filename} verwijderd'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)