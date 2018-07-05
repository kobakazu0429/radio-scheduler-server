import requests
import json
from dateutil import parser

from datamodel import *
import settings


# Config
DEBUG_MODE = False
CHANNEL = 'C989JV2NN' if DEBUG_MODE else 'CB10PPRP1'
USERNAME = '進捗どうですか？'
ICON = 'https://i.imgur.com/uWrClZN.png'


def notify(id):
    query = Tasks.select().where(Tasks.id == id).dicts()

    data = []

    for task in query:
        data.append(task)

    time = data[0]['time']
    title = data[0]['title']
    manager = data[0]['manager']
    published_at = data[0]['published_at'] if data[0]['published_at'] != '' else '未定'
    recorded = '✓' if data[0]['recorded'] else '✗'
    edited = '✓' if data[0]['edited'] else '✗'
    reviewed = '✓' if data[0]['reviewed'] else '✗'
    drew_thumbnail = '✓' if data[0]['drew_thumbnail'] else '✗'
    reserved = '✓' if data[0]['reserved'] else '✗'
    released = '✓' if data[0]['released'] else '✗'
    drew_comic = '✓' if data[0]['drew_comic'] else '✗'
    tweeted = '✓' if data[0]['tweeted'] else '✗'

    progress = '''\
第%s回
「%s」
担当　　　　: %s
公開予定日　: %s
収録　　　　: %s
編集　　　　: %s
検閲　　　　: %s
サムネ画像　: %s
予約投稿　　: %s
公開　　　　: %s
４コマ漫画　: %s
ツイート　　: %s
''' % (time, title, manager, published_at, recorded, edited, reviewed, drew_thumbnail, reserved, released, drew_comic, tweeted)

    attachments = [{
        "color": "#a3deff",
        "text": progress,
        "actions": [{
            "type": "button",
            "text": "ラジオスケジューラーへ飛ぶ",
            "url": "http://www.scheduler.kure-rad.io:429/"
        }]
    }]

    data = {
        'channel': CHANNEL,
        'username': USERNAME,
        'icon_url': ICON,
        'text': 'ラジオスケジューラーが更新されました',
        'attachments': attachments
    }

    requests.post(settings.INCOMING_WEBHOOK_URL, json.dumps(data))
