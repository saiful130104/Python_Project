from bottle import route, run, template, request, view, response

from card_validator.validator import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
@view('index')
def the_real_index():
    return {
        "message": request.query.get('message', 'There was no message'),
        "message1": "I love Python"
    }


@route('/validate')
# @view('validate')
def validate():
    cardNumber = request.query.get('cardNumber', '').strip()
    if cardNumber:
        try:
            issuer = get_issuer(cardNumber)
            return {
                "cardNumber": cardNumber,
                "issuer": issuer,
                "result": "It is a {} card.".format(issuer)
            }
        except ValueError:
            response.status = 400
            return {
                "cardNumber": cardNumber,
                "result": "It is not a valid Credit card number."
            }
    response.status = 400
    return {
        "detail": "The cardNumber is required as a query parameter."
    }


run(host='localhost', port=8080)
