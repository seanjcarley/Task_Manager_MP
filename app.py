#!/usr/bin/env python

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import env as config


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html')


# def hello():
#     return 'Hello world ...again!'


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP','0.0.0.0'),
        port=int(os.environ.get('PORT', 8080)),
        debug=True
    )
