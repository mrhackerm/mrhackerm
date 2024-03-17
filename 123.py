from flask import Flask, request, jsonify, render_template
import base64
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save_frame', methods=['POST'])
def save_frame():
    try:
        image_data = request.form['image_data']

        decoded_image_data = base64.b64decode(image_data.split(",")[1])

        save_dir = "frames"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        file_name = os.path.join(save_dir, f'frame_{len(os.listdir(save_dir))}.png')
        with open(file_name, "wb") as f:
            f.write(decoded_image_data)

        return jsonify({'status': 'success', 'message': 'Frame saved successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
