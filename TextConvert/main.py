from flask import Flask, request, send_file, render_template, redirect, session
from flask_mysqldb import MySQL
from gtts import gTTS
import shutil
import docx
import PyPDF2

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Aas231@2711'
app.config['MYSQL_DB'] = 'speechlogin'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template("dashboard.html")
    # '''
#    <form method="POST" action="/convert">
#     <input type="text" name="text">
#     <input type="submit" value="Convert to mp3">
#    </form>
#    '''

@app.route('/convert', methods=['POST'])            #main page
def convert():
    text = request.form['text']
    tts = gTTS(text, lang='en', tld='co.in',slow=False)
    if 'username' in session:
        # Get the username of the currently logged-in user from the session
        username = session['username']
        cursor = mysql.connection.cursor()
        query = "INSERT INTO history (text, username) VALUES (%s, %s)"
        cursor.execute(query, (text, username))
        mysql.connection.commit()
        cursor.close()
    else:
        return render_template('login1.html')
    # fname = 'audio.mp3'
    tts.save("audio.mp3")
    # playsound.playsound(fname)
    shutil.move('audio.mp3', 'E:/Projects Python YT/TextConvert/audio.mp3')
    return download()

@app.route('/extmain')
def base():
    return render_template('base.html')


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
    return text

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ' '.join([page.extract_text() for page in pdf_reader.pages])
        return text

@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    file_path = 'uploads/' + file.filename
    file.save(file_path)

    if file_path.endswith('.docx'):
        extracted_text = extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_path)
    else:
        extracted_text = 'Unsupported file format'

    return render_template('result.html', text=extracted_text)

@app.route('/download')         #download
def download():
    return send_file('audio.mp3', as_attachment=True, download_name='audio.mp3')


# @app.route('/')
# def home():
#     return render_template('dashboard.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        # Create cursor
        cur = mysql.connection.cursor()
        # Execute query
        cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, password))
        # Commit to DB
        mysql.connection.commit()
        # Close connection
        cur.close()
        return 'Signup successful!' + render_template('login1.html')

    return render_template('signup1.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        # Create cursor
        cur = mysql.connection.cursor()
        # Execute query
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        # Fetch one record
        user = cur.fetchone()
        # Close connection
        cur.close()
        if user:
            # Store user session
            session['username'] = user['username']
            return redirect('/dashboard')
        else:
            return 'Invalid login credentials!'
    return render_template('login1.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect('/login')
    

@app.route('/history')
def history():
    username = session['username']
    cur = mysql.connection.cursor()
    # Execute query
    cur.execute("SELECT * FROM history WHERE username = %s", (username,))
    # Fetch one record
    user = cur.fetchall()
    return render_template('history.html', user=user)
    # Close connection
    cur.close()
       


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/about')        #about section
def about():
    company_name = "about"
    return render_template('about.html', company=company_name)

@app.route('/home')
def home():
    company_name = "home"
    return render_template('index.html', company=company_name)

@app.route('/docextract')
def docextract():
    company_name = "docextract"
    return render_template('base.html', company=company_name)

@app.route('/engus', methods=['POST'])            #main page
def engus():
    text = request.form['text']
    tts = gTTS(text, lang='en', tld='com',slow=False)
    if 'username' in session:
        # Get the username of the currently logged-in user from the session
        username = session['username']
        cursor = mysql.connection.cursor()
        query = "INSERT INTO history (text, username) VALUES (%s, %s)"
        cursor.execute(query, (text, username))
        mysql.connection.commit()
        cursor.close()
    else:
        return render_template('login1.html')
    tts.save("audio.mp3")
    shutil.move('audio.mp3', '/home/converterio/mysite/audio.mp3')
    return download()

@app.route('/frenchk', methods=['POST'])            #main page
def frenchk():
    text = request.form['text']
    tts = gTTS(text, lang='fr', tld='fr',slow=False)
    if 'username' in session:
        # Get the username of the currently logged-in user from the session
        username = session['username']
        cursor = mysql.connection.cursor()
        query = "INSERT INTO history (text, username) VALUES (%s, %s)"
        cursor.execute(query, (text, username))
        mysql.connection.commit()
        cursor.close()
    else:
        return render_template('login1.html')
    tts.save("audio.mp3")
    shutil.move('audio.mp3', '/home/converterio/mysite/audio.mp3')
    return download()

@app.route('/spanishk', methods=['POST'])            #main page
def spanishk():
    text = request.form['text']
    tts = gTTS(text, lang='es', tld='es',slow=False)
    if 'username' in session:
        # Get the username of the currently logged-in user from the session
        username = session['username']
        cursor = mysql.connection.cursor()
        query = "INSERT INTO history (text, username) VALUES (%s, %s)"
        cursor.execute(query, (text, username))
        mysql.connection.commit()
        cursor.close()
    else:
        return render_template('login1.html')
    tts.save("audio.mp3")
    shutil.move('audio.mp3', '/home/converterio/mysite/audio.mp3')
    return download()

@app.route('/englishus')
def englishus():
    return render_template("engus.html")

@app.route('/frenchre')
def frenchre():
    return render_template("french.html")

@app.route('/spanishre')
def spanishre():
    return render_template("spanish.html")

if __name__ == '__main__':
    app.run()
