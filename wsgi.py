# from db import writeNotes
from flask import Flask, render_template, request, redirect
# from db import getNotes, writeNotes
app = Flask(__name__)

import pymongo

client = pymongo.MongoClient('mongodb+srv://atg:greg@cluster0.uypjm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


def getNotes():
    col = client['db']['notes']
    return col.find()

    
def writeNotes(Note:str):
    col = client['db']['notes']
    col.insert_one({ "text": Note })

@app.route('/')
def fun():
    return render_template('index.html',notes=getNotes())


@app.route('/write', methods=["POST"])
def writeNote():
    note = request.form.get('note-input')
    writeNotes(note)
    return redirect('/',302)
if __name__ = "__main__":
	app.run()


