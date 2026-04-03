from flask import Flask, render_template, redirect, url_for, request, jsonify
import mysql.connector
import bcrypt
from login import login_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET')

app.register_blueprint(login_bp)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
        port=os.getenv("DB_PORT")
    )

@app.route('/getTables', methods = ['GET'])
def get_tables():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute('SHOW TABLES;') 
    tables = cursor.fetchall()
    cursor.close()
    con.close()

    table_names = [table[0] for table in tables]
    return jsonify({"tables": table_names}), 200
# -------------------------------------------------
@app.route('/cadastro', methods = ['GET', 'POST'])
def userRegistration():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['senha']

        if not name or not email or not password:
            return 'Dados incompletos', 400

        passwordInBytes = password.encode('utf-8')
        passwordHash = bcrypt.hashpw(passwordInBytes, bcrypt.gensalt())


        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return render_template('registerPage.html', error='Email já está em uso')
        
        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, passwordHash)
            )
            con.commit()
            return redirect(url_for('userRegistration'))  
        except Exception as e:
            con.rollback()
            return f"Erro: {str(e)}"
        finally:
            cursor.close()
            con.close()

    return render_template('registerPage.html')

if __name__ == "__main__":
    print("connecting to database...")
    app.run(debug=True)
