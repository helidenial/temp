import pymongo

client = pymongo.MongoClient('mongodb+srv://atg:greg@cluster0.uypjm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


def getNotes():
    col = client['db']['notes']
    return col.find()

    
def writeNotes(Note:str):
    col = client['db']['notes']
    col.insert_one({ "text": Note })