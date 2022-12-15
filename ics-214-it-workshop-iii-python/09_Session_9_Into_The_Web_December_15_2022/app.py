# Flask code goes here.

from flask import Flask, render_template
import sqlite3

# Create a Flask instance - holds name of the current Python module.
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# Decorate the function to define the URL Route - helps in making the return value get served as HTTP response.
@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    # Serve the index.html page from the templates.
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8999, debug=True)
