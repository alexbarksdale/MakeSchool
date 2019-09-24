from random import choice
from flask import Flask, request
from flask import render_template
from random import sample, choice

app = Flask(__name__)


@app.route('/')
def index():
    # Show the homepage and ask the user's name
    section = 'BEW 1.1 Section A'
    greeting = 'Good morning class'
    return render_template(
        'index.html',
        section=section,
        greeting=greeting)


# compliments = ['dope', 'nice', 'sick', 'rad']
# wisdom_list = ['Use both feet to walk',
#                'Use your eyes to see', 'Make sure to breath']


# @app.route('/compliment')
# def get_compliment():
#     # Give the user a compliment
#     name = request.args.get('name')
#     show_compliments = request.args.get('show_compliments')
#     compliments_to_show = sample(compliments, 3)

#     return render_template(
#         'compliments.html',
#         name=name,
#         show_compliments=show_compliments,
#         compliments=compliments_to_show)

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']


def get_compliment():
    compliment = compliments[0]
    return f'Hello there, user! You are so {compliment}!'


# def get_horoscope():
#     wisdom = choice(wisdom_list)
#     return f'Here\'s some widsom: {wisdom}'


if __name__ == "__main__":
    app.run(debug=True)
