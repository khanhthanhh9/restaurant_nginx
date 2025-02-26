import os 
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# --- Static Content ---
@app.route('/static/<path:filename>')
def serve_static(filename):
    static_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(static_dir, filename)

# --- Routes ---
@app.route('/')
def index():
    menu_items = [
        {"name": "Pizza Margherita", "description": "Classic tomato and mozzarella pizza", "image": "/static/restaurant.jpg"},
        {"name": "Pasta Carbonara", "description": "Creamy pasta with eggs, bacon, and cheese", "image": "/static/restaurant.jpg"},
        {"name": "Tiramisu", "description": "Italian coffee-flavored dessert", "image": "/static/restaurant.jpg"}
    ]
    return render_template('index.html', menu_items=menu_items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # Run on all interfaces for Docker
