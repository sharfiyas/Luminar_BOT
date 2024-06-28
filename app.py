from flask import Flask, request,render_template,jsonify
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(user_message)
    rasa_response = requests.post(
        'http://localhost:5005/webhooks/rest/webhook',  
        json={"sender": "user", "message": user_message}
    )
    
    messages = rasa_response.json()
    print(messages)

    if messages:
        rasa_message = messages[0]['text']
        print(rasa_message)

    else:
        rasa_message = "Sorry, I didn't understand that."
    return jsonify({"message": rasa_message})



    return user_message