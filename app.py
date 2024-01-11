import socket
import os
from dotenv import load_dotenv

from pymongo import MongoClient
from flask import Flask, request
from bson import json_util, ObjectId
import json

app = Flask(__name__)

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
client = MongoClient(MONGODB_URI)

@app.route('/', methods=['GET'])
def default_route():
    return 'Landing page for to-do-list project'

@app.route('/get-all', methods=['GET'])
def get_all_reminders():
    db = client.todolist
    reminders_collection = db.reminders_test
    cursor = reminders_collection.find()
    result = []
    for document in cursor:
        document_cleaned = json.loads(json_util.dumps(document))
        result.append(document_cleaned)
    return result    

@app.route('/get-one', methods=['GET'])
def get_one_reminder():
    oid = request.args.get('oid')
    db = client.todolist
    reminders_collection = db.reminders_test
    document_to_find = {"_id": ObjectId(oid)}
    result = reminders_collection.find_one(document_to_find)
    return json.loads(json_util.dumps(result))

@app.route('/add', methods=['POST'])
def add_reminder():
    db = client.todolist
    reminders_collection = db.reminders_test
    title = request.args.get('title')
    new_reminder = {
        "title": title,
        "completed": False
    }
    result = reminders_collection.insert_one(new_reminder)
    return f"_id of inserted document: {result.inserted_id}"

@app.route('/update', methods=['PUT'])
def edit_reminder():
    db = client.todolist
    reminders_collection = db.reminders_test
    oid = request.args.get('oid')
    title = request.args.get('title')
    completed = request.args.get('completed')

    reminder_to_update = {"_id": ObjectId(oid)}
    updates = {}
    if title:
        updates["title"] = title
    if completed != None:
        updates["completed"] = completed
    
    result = reminders_collection.update_one(reminder_to_update, {"$set": updates})

    return f"Documents updated: {str(result.modified_count)}"


@app.route('/remove', methods=['DELETE'])
def remove_reminder():
    db = client.todolist
    reminders_collection = db.reminders_test
    oid = request.args.get('oid')
    document_to_delete = {"_id": ObjectId(oid)}

    result = reminders_collection.delete_one(document_to_delete)
    return f"Documents deleted: {str(result.deleted_count)}"


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)