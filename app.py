from flask import Flask, render_template, request
import rembg
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_background', methods=['POST'])
def remove_background():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        input_image = Image.open(uploaded_file).convert("RGBA")
        output_image = rembg.remove(input_image)
        output_image_path = os.path.join('static', 'output.png')
        output_image.save(os.path.join(app.root_path, output_image_path), format="PNG")
        return render_template('result.html', output_image=output_image_path)
    return "No file selected."

if __name__ == '__main__':
    app.run(debug=True)
