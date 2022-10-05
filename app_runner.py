from flask import Flask,render_template,redirect

with open("MapsAPIKey.txt","r") as f:
    key = f.read()

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')

@app.route('/home.html')
def return_home():
    return redirect('/')

@app.route('/map.html')
def render_map():        
    return render_template('map.html', key_data = key)

@app.route('/todocolombia.html')
def render_colombia():        
    return render_template('todocolombia.html', key_data = key)

@app.route('/Medellin.html')
def render_medellin():        
    return render_template('Medellin.html', key_data = key)

@app.route('/Guatape.html')
def render_guatape():        
    return render_template('Guatape.html', key_data = key)

@app.route('/Santa.html')
def render_santa():        
    return render_template('Santa.html', key_data = key)

@app.route('/Burataca.html')
def render_buritaca():        
    return render_template('Burataca.html', key_data = key)

@app.route('/Palomino.html')
def render_palomino():        
    return render_template('Palomino.html', key_data = key)

@app.route('/Minca.html')
def render_minca():        
    return render_template('Minca.html', key_data = key)

@app.route('/Cartagena.html')
def render_cartagena():        
    return render_template('Cartagena.html', key_data = key)

@app.route('/Chinchina.html')
def render_chinchina():        
    return render_template('Chinchina.html', key_data = key)

@app.route('/SantaRosa.html')
def render_santaR():        
    return render_template('SantaRosa.html', key_data = key)

@app.route('/Manizales.html')
def render_manizales():        
    return render_template('Manizales.html', key_data = key)
	
if __name__ == '__main__':
    app.run(debug = True)  