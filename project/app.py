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

@app.route('/convert', methods=['POST'])            #main page
def convert():
    text = request.form['text'] 
    tts = gTTS(text, lang='en', tld='co.in')
    tts.save("audio.mp3")
    shutil.move('audio.mp3', 'G:/Converter/project/audio.mp3')
    return download()

@app.route('/download')         #download
def download():
    return send_file('audio.mp3', as_attachment=True, download_name='audio.mp3')

@app.route('/about')        #about section
def about():
    company_name = "about"
    return render_template('about.html', company=company_name)

@app.route('/home')
def home():
    company_name = "home"
    return render_template('index.html', company=company_name)
 


if __name__ == '__main__':
    app.run()
