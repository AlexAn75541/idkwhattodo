from flask import Flask, request

app = Flask(__name__)


@app.route("/prime_number")


def prime_number():
    
    
    def is_prime(n):
        n = int(request.args.get("number")) #I'll be for real for this one, I'm not sure if this is okay or not, its red all over the place 
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    response = {
        "Number": n,
        "Is Prime": is_prime(n)
    }
    return response


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

