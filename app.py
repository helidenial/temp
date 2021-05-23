from db import writeNotes
from flask import Flask, render_template, request, redirect
from db import getNotes, writeNotes
app = Flask(__name__)


@app.route('/')
def fun():
    return render_template('index.html',notes=getNotes())


@app.route('/write', methods=["POST"])
def writeNote():
    note = request.form.get('note-input')
    writeNotes(note)
    return redirect('/',302)

app.run()


