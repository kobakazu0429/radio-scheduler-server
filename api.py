# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request, redirect, url_for
from flask_cors import CORS
from dateutil import parser
from peewee import *
import json

from datamodel import *


api = Flask(__name__)
CORS(api)


# 404の時は以下を返す
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# 処理する前にdbへ接続する
@api.before_request
def before_request_handler():
    db.connect()


# 処理した後にdbを切断する
@api.teardown_request
def after_request_handler(exc):
    if not db.is_closed():
        db.close()


# ルートへのアクセスをapiへリダイレクトさせる
@api.route('/', methods=['GET'])
def redirect_api():
    return redirect('/api/v2/tasks/', code=303)


# 全件取得
@api.route('/api/v2/tasks/', methods=['GET'])
def get_tasks():
    datas = []

    query = Tasks.select().dicts().order_by(Tasks.id.desc())

    for task in query:
        datas.append(task)

    return make_response(jsonify(datas))


# 1件取得
@api.route('/api/v2/tasks/<string:id>/', methods=['GET'])
def get_task(id):
    datas = []

    query = Tasks.select().where(Tasks.id == id).dicts()

    for task in query:
        datas.append(task)

    return make_response(jsonify(datas))


# 新規作成
@api.route('/api/v2/tasks/', methods=['POST'])
def create_task():
    Tasks.create(
        time=request.form['time'],
        title=request.form['title'],
        manager=request.form['manager'],
        published_at=parser.parse(request.form['published_at']).date(
        ) if request.form['published_at'] != '' else '',
        recorded=int(request.form['recorded']),
        edited=int(request.form['edited']),
        reviewed=int(request.form['reviewed']),
        drew_thumbnail=int(request.form['drew_thumbnail']),
        reserved=int(request.form['reserved']),
        released=int(request.form['released']),
        drew_comic=int(request.form['drew_comic']),
        tweeted=int(request.form['tweeted']),
        folder_id=request.form['folder_id'],
        record_url=request.form['record_url'],
        thumbnail_url=request.form['thumbnail_url'],
        comic_url=request.form['comic_url'])

    return make_response(jsonify({'result': 'Uploaded'}), 200)


# 編集
@api.route('/api/v2/tasks/<string:id>/', methods=['PATCH'])
def update_task(id):
    updating_task = Tasks.get(Tasks.id == id)

    updating_task.time = request.form['time']
    updating_task.title = request.form['title']
    updating_task.manager = request.form['manager']
    updating_task.published_at = parser.parse(request.form['published_at']).date(
    ) if request.form['published_at'] != '' else ''
    updating_task.recorded = int(request.form['recorded'])
    updating_task.edited = int(request.form['edited'])
    updating_task.reviewed = int(request.form['reviewed'])
    updating_task.drew_thumbnail = int(request.form['drew_thumbnail'])
    updating_task.reserved = int(request.form['reserved'])
    updating_task.released = int(request.form['released'])
    updating_task.drew_comic = int(request.form['drew_comic'])
    updating_task.tweeted = int(request.form['tweeted'])
    updating_task.folder_id = request.form['folder_id']
    updating_task.record_url = request.form['record_url']
    updating_task.thumbnail_url = request.form['thumbnail_url']
    updating_task.comic_url = request.form['comic_url']

    updating_task.save()

    return make_response(jsonify({'result': 'Updated'}), 200)


# 削除
@api.route('/api/v2/tasks/<string:id>/', methods=['DELETE'])
def delete_task(id):
    deleting_task = Tasks.get(Tasks.id == id)

    deleting_task.delete_instance()

    return make_response(jsonify({'result': 'Deleted'}), 200)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
