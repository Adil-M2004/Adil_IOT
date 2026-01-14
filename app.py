from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial data
cars_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2024, "price": 28000},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2023, "price": 25000}
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars_inventory)

@app.route('/add', methods=['POST'])
def add_car():
    # Get data from the form
    new_car = {
        "id": len(cars_inventory) + 1,
        "make": request.form.get("make"),
        "model": request.form.get("model"),
        "year": request.form.get("year"),
        "price": request.form.get("price")
    }
    cars_inventory.append(new_car)
    return redirect(url_for('index'))

@app.route('/delete/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    global cars_inventory
    # Keep all cars EXCEPT the one with the matching ID
    cars_inventory = [car for car in cars_inventory if car['id'] != car_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)