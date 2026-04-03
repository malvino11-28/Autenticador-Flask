from flask import request, render_template, redirect, url_for, session, Blueprint
import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

login_bp = Blueprint('login_bp', __name__, template_folder='templates')

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=os.getenv("DB_PORT")
    )

@login_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passwordEntered = request.form['senha'].encode('utf-8')

        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user:
                passwordSaved = user['password'].encode('utf-8')
                if bcrypt.checkpw(passwordEntered, passwordSaved):
                    session['session_id'] = user['id']
                    session['username'] = user['name']
                    return redirect(url_for('login_bp.dashboard'))
                else:
                    return 'Senha incorreta.'
            else:
                return 'Usuário não encontrado.'
        except Exception as e:
            return f'Erro no login: {str(e)}'
        finally:
            cursor.close()
            con.close()
        
    return render_template('login.html')

@login_bp.route('/dashboard')
def dashboard():
    if 'session_id' in session:
        username = session['username']
        return f'Bem-vindo, {username}'
    else:
        return redirect(url_for('login_bp.login'))
    
@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_bp.login'))
