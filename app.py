from flask import Flask, render_template

app = Flask(__name__)

# Sample data: A list of car dictionaries
cars_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2024, "price": 28000, "status": "Available"},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2023, "price": 25000, "status": "Sold"},
    {"id": 3, "make": "Ford", "model": "F-150", "year": 2024, "price": 45000, "status": "Available"},
    {"id": 4, "make": "Tesla", "model": "Model 3", "year": 2023, "price": 38000, "status": "Available"}
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars_inventory)

if __name__ == '__main__':
    app.run(debug=True)