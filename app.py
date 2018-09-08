from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>')
def show_post(query):
    # if id:
    if query.isdigit():
        # gather name
        name = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(query)).json()['name']
        result = "The pokemon with id {} is {}".format(query, name)
    # if not id (assume name):
    else:
        # gather id
        id = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(query)).json()['id']
        result = "{} has id {}".format(query.capitalize(), id)
    return render_template('pokemon/info.html', result=result)

if __name__ == '__main__':
    app.run()
