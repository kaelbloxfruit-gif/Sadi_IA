from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    ip_address = request.remote_addr  # Get the user's IP address
    response = get_groq_ai_response(user_input, ip_address)
    return {'response': response}

def get_groq_ai_response(user_input, ip_address):
    # Here you would implement the integration with Groq AI
    # This is just a placeholder for the actual implementation
    return f'Processed input: {user_input} from IP: {ip_address}'

if __name__ == '__main__':
    app.run(debug=True)