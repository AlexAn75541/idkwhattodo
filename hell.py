from flask import Flask, request


app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    number1 = float(args.get('number1', 0))
    number2 = float(args.get('number2', 0))
    total = number1 + number2
    return str(total)


        return str(number1 + number2)
    # nah I hate this