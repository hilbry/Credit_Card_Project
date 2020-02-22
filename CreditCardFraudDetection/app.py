
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
    


@app.route('/credit_card_usage')
def credit_card_usage():
    return render_template('credit_card_usage.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
#     

if __name__ == "__main__":
    app.run()   