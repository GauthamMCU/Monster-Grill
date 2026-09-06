import os
from flask import Flask, render_template

# Ensure Flask looks in the correct templates directory
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    menu_items = [
        {"name": "Monster Beef Burger", "price": "$12.99", "desc": "Double patty with extra melted cheese"},
        {"name": "Smoked BBQ Ribs", "price": "$18.50", "desc": "Slow-cooked pork ribs with house marinade"},
        {"name": "Grilled Chicken Wings", "price": "$9.99", "desc": "Spicy buffalo glazed wings"}
    ]
    return render_template('index.html', menu=menu_items)

if __name__ == '__main__':
    app.run(debug=True, port=8000)