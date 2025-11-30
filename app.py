from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="db",
            port="5432"
        )
        return "Connection to PostgreSQL: OK!"
    except Exception as e:
        return f"Database error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

