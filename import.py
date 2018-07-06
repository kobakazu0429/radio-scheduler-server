# -*- coding: utf-8 -*-
from peewee import *

from datamodel import *


# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("data.csv", "r"):
    (time, title, manager, published_at, recorded, edited, reviewed, drew_thumbnail, reserved, released, drew_comic,
     tweeted, folder_id, record_url, thumbnail_url, comic_url) = tuple(line[:-1].split(","))

    Tasks.create(
        time=time,
        title=title,
        manager=manager,
        published_at=published_at,
        recorded=int(recorded),
        edited=int(edited),
        reviewed=int(reviewed),
        drew_thumbnail=int(drew_thumbnail),
        reserved=int(reserved),
        released=int(released),
        drew_comic=int(drew_comic),
        tweeted=int(tweeted),
        folder_id=folder_id,
        record_url=record_url,
        thumbnail_url=thumbnail_url,
        comic_url=comic_url
    )
