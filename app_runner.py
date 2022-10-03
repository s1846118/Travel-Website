from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def render_home():        
    return render_template('home.html')

@app.route('/map.html')
def render_map():        
    return render_template('map.html')

@app.route('/Colombia.html')
def render_colombia():        
    return render_template('todocolombia.html')

@app.route('/Medellin.html')
def render_medellin():        
    return render_template('Medellin.html')

@app.route('/Guatape.html')
def render_guatape():        
    return render_template('Guatape.html')

@app.route('/Santa.html')
def render_santa():        
    return render_template('Santa.html')

@app.route('/Burataca.html')
def render_buritaca():        
    return render_template('Burataca.html')

@app.route('/Palomino.html')
def render_palomino():        
    return render_template('Palomino.html')

@app.route('/Minca.html')
def render_minca():        
    return render_template('Minca.html')

@app.route('/Cartagena.html')
def render_cartagena():        
    return render_template('Cartagena.html')

@app.route('/Chinachina.html')
def render_chinchina():        
    return render_template('Chinchina.html')

@app.route('/SantaRosa.html')
def render_santaR():        
    return render_template('SantaRosa.html')

@app.route('/Manizales.html')
def render_manizales():        
    return render_template('Manizales.html')
	
if __name__ == '__main__':
    app.run(debug = True)  