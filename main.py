from flask import Flask, request, redirect, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['low_value'] or guess > session['high_value']:
            message = f'Invalid Selection! Please choose a number between {session['low_value']} and {session['high_value']}!'
        elif guess == session['magic_number']:
            session['still_guessing'] = False
            message = 'A victory message'
        elif guess > session['magic_number']:
            session['high_value'] = guess
            message = 'too high. Try again.'
        elif guess < session['magic_number']:
            session['low_value'] = guess
            message = 'too low. Try again.'
    else:
        low_value = 1
        high_value = 50
        session['still_guessing'] = True
        session['magic_number'] = random.randint(low_value, high_value)
        session['low_value'] = low_value
        session['high_value'] = high_value
        message = ''

    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run()
