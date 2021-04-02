from flask import Flask, request, redirect, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        start_value = 1
        end_value = 50
        magic_number = random.randint(start_value, end_value)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()