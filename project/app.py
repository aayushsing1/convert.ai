from flask import Flask, request, send_file, render_template
from gtts import gTTS
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    # '''
#    <form method="POST" action="/convert">
#     <input type="text" name="text">
#     <input type="submit" value="Convert to mp3">
#    </form>
#    '''

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    tts = gTTS(text, lang='en', tld='co.in')
    tts.save("example.mp3")
    shutil.move('example.mp3', 'G:/Converter/project/example.mp3')
    return download()

@app.route('/download')
def download():
    return send_file('example.mp3', as_attachment=True, download_name='example.mp3')


if __name__ == '__main__':
    app.run(debug=True)
