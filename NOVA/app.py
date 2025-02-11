from flask import Flask, render_template, jsonify, request
import ai_core

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Aquí irá la lógica para procesar el audio
    response = ai_core.process_command(request.get_json()['audio'])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)