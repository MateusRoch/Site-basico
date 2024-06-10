import pymysql
from flask import Flask, render_template, request, session, make_response, redirect
import pymysql
app = Flask(__name__)

app.secret_key = "kfncoakuhbsjapj"

db = pymysql.connect(host="localhost",user="root",password="mateus12345#",database="cliente")

@app.route("/deletar", methods=["GET", "POST"])
def deletar():
    cursor = db.cursor()
    sql = "DELETE FROM dados WHERE iddados = %s"
    cursor.execute(sql, (request.args.get('iddados'),))
    db.commit()
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
        if request.method == "POST":
            id = request.form.get('iddados')
            nome = request.form.get('nome')
            email = request.form.get('email')

            cursor = db.cursor()
            sql = "UPDATE dados SET nome = %s, email = %s WHERE iddados = %s"

            cursor.execute(sql,(nome,email,id))
            db.commit()

            cursor = db.cursor()
            sql = "SELECT * FROM dados"

            cursor.execute(sql)
            db.commit()
            results = cursor.fetchall()
            print(results)
            return render_template("index.html", content=results)

        else:
            cursor = db.cursor()
            sql = "SELECT * FROM dados"

            cursor.execute(sql)
            db.commit()
            results = cursor.fetchall()
            print(results)
            return render_template("index.html", content =results)

@app.route("/sobre")
def sobre():
    return  "<h2>Sobre</h2>"

@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return "Noticia: "+slug