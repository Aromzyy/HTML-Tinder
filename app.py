from flask import Flask, render_template

app = Flask(__name__)

cards = [
    {
        'name': 'Sushi',
        'price': '$$',
        'image': 'https://s3-media0.fl.yelpcdn.com/bphoto/-1BWnyjrsDmTmXH_3wZl_w/ls.jpg'
    },
    {
        'name': 'Ramen',
        'price': '$$',
        'image': 'https://s3-media0.fl.yelpcdn.com/bphoto/5n8QBzhfaf6jnAjgrBZjAg/ls.jpg'
    },
    {
        'name': 'Pizza',
        'price': '$$',
        'image': 'https://s3-media0.fl.yelpcdn.com/bphoto/_ctgOKFOE8MxNjklaNtuag/348s.jpg'
    }
]


@app.route('/')
def index():
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
