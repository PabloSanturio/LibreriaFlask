from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Note, Libro
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    librito = Libro.query.all()
    return render_template("home.html", librito=librito)


@views.route('/nuevolibro', methods=['GET', 'POST'])
def libroForm():
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        nombre = request.form.get('nombre')
        autor = request.form.get('autor')
        tema = request.form.get('tema')
        idioma = request.form.get('idioma')
        encuadernacion = request.form.get('encuadernacion')
        paginas = request.form.get('paginas')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        libro = Libro.query.filter_by(nombre=nombre).first()
        if libro:
            flash('El libro ya está agregado.', category='error')
        else:
            nuevoLibro = Libro(isbn=isbn, nombre=nombre, autor=autor, tema=tema, idioma=idioma,
                               encuadernacion=encuadernacion, paginas=paginas, precio=precio, stock=stock)
            db.session.add(nuevoLibro)
            db.session.commit()
            flash('Libro agregado!', category='success')
            return redirect(url_for('views.Todoslibros'))

    return render_template("libroform.html")


@views.route('/todoslibros', methods=['GET', 'POST'])
def Todoslibros():

    librito = Libro.query.all()
    return render_template("todoslibros.html", librito=librito)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # this function expects a JSON from the INDEX.js file
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
