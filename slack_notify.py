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


def notify(obj):
    time = obj['time']
    title = obj['title']
    manager = obj['manager']
    published_at = parser.parse(obj['published_at']).date(
    ) if obj['published_at'] != '' else '未定'
    recorded = '✓' if obj['recorded'] else '✗'
    edited = '✓' if obj['edited'] else '✗'
    reviewed = '✓' if obj['reviewed'] else '✗'
    drew_thumbnail = '✓' if obj['drew_thumbnail'] else '✗'
    reserved = '✓' if obj['reserved'] else '✗'
    released = '✓' if obj['released'] else '✗'
    drew_comic = '✓' if obj['drew_comic'] else '✗'
    tweeted = '✓' if obj['tweeted'] else '✗'

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
