from movements import app
from flask import render_template
import random

@app.route('/') 
def listaMovimientos():
    return render_template("movementlists.html")






    