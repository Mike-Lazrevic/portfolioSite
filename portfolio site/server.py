from flask import Flask, request, jsonify, render_template
import subprocess
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('firstP.html')

@app.route('/updateInputData', methods=['POST'])
def update_input_data():
    if request.method == 'POST':
        # Execute textChanger.py or perform other tasks as needed
        subprocess.run(['python', 'textChanger.py'])
        return jsonify({'message': 'Input data updated successfully'})
    else:
        return jsonify({'error': 'Method not allowed'}), 405

@app.route('/runMarioGame', methods=['POST'])
def run_mario_game():
    if request.method == 'POST':
        try:
            # Run marioGame.py and return output
            output = subprocess.check_output(['python', 'marioGame.py'], stderr=subprocess.STDOUT, timeout=5)
            return output
        except subprocess.CalledProcessError as e:
            return jsonify({'error': e.output.decode('utf-8')}), 500
        except subprocess.TimeoutExpired:
            return jsonify({'error': 'Timeout: Mario game took too long to execute.'}), 500
    else:
        return jsonify({'error': 'Method not allowed'}), 405

@app.route('/restart', methods=['POST'])
def restart():
    if request.method == 'POST':
        # Copy contents of constInputData.txt to InputData.txt
        shutil.copyfile('constInputData.txt', 'InputData.txt')
        return jsonify({'message': 'Game restarted successfully'})
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
