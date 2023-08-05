from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('page1.html')

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    region = None
    image_path = None

    if request.method == 'POST':
        region = request.form['region']
        image_path = url_for('static', filename=f'{region}_image.jpg') # Change filename according to your images

    return render_template('page2.html', region=region, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
