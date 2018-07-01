import requests
import json
from dateutil import parser


# Config
DEBUG_MODE = False
INCOMING_WEBHOOK_URL = 'https://hooks.slack.com/services/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'
CHANNEL = 'C989JV2NN' if DEBUG_MODE else 'CB10PPRP1'
USERNAME = '進捗どうですか？'
ICON = 'https://i.imgur.com/uWrClZN.png'


def notify(id):
    r = requests.get('http://0.0.0.0:3000/api/v2/tasks/%s/' % id).json()

    time = r[0]['time']
    title = r[0]['title']
    manager = r[0]['manager']
    published_at = parser.parse(r[0]['published_at']).date(
    ) if r[0]['published_at'] != '' else '未定'
    recorded = '✓' if r[0]['recorded'] else '✗'
    edited = '✓' if r[0]['edited'] else '✗'
    reviewed = '✓' if r[0]['reviewed'] else '✗'
    drew_thumbnail = '✓' if r[0]['drew_thumbnail'] else '✗'
    reserved = '✓' if r[0]['reserved'] else '✗'
    released = '✓' if r[0]['released'] else '✗'
    drew_comic = '✓' if r[0]['drew_comic'] else '✗'
    tweeted = '✓' if r[0]['tweeted'] else '✗'

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

    requests.post(INCOMING_WEBHOOK_URL, json.dumps(data))
