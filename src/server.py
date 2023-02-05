from flask import Flask, render_template
from sqlite3 import connect as sql_connect

app = Flask(__name__)
db = sql_connect("configuration.db")
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS links (url TEXT, name TEXT, colour TEXT, icon TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS settings (title TEXT, desc TEXT, background BLOB, favicon BLOB, password TEXT, exist BOOLEAN)")

c.execute("SELECT * FROM settings")
settings = c.fetchone()
if settings is None:
    c.execute("INSERT INTO settings VALUES ('Compressify', 'Create your own \"link in bio\" solution', '', '', 'password', 0)")
    db.commit()

links = ["cunt", "twat"] # change on release


@app.route('/')
def index():
    return render_template('index.html', links=links, title=settings[0], desc=settings[1])

app.run(debug=True, use_reloader=True, host="0.0.0.0")
