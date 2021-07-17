!pip install flask-ngrok 
from flask import Flask, render_template, request, redirect
from flask_ngrok import run_with_ngrok
import matplotlib.pyplot as plt
app = Flask(__name__)
run_with_ngrok(app)

import cv2 as cv



@app.route('/')
def index():
    return render_template('base.html')

@app.route('/transformation', methods=['POST', 'GET'])
def transformation():
  if request.method == "POST":
    img_file = request.form.get('image_file')

    # factors
    x = int(request.form.get("width"))
    y = int(request.form.get("height"))

    # operation
    operation = request.form.get("operation")

    if operation == 'scaling':
      img = cv.imread(img_file)
      res = cv2.resize(img, (x, y), interpolation = cv2.INTER_NEAREST)
      cv2.imwrite('sample_output.jpg', res)



    message = "your given image"
    return render_template('result.html', message = message)
  
  message = "Please enter correct information"
  return render_template('base.html', message = message)



if __name__ == '__main__':
    app.run()