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
    pass

@app.route('/add', methods=['PUT'])
def edit_reminder():
    pass

@app.route('/remove', methods=['DELETE'])
def remove_reminder():
    pass



if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)