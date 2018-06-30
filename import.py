# -*- coding: utf-8 -*-
from peewee import *

from datamodel import *


# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("data.tsv", "r"):
    (time, title, manager, published_at, recorded, edited, reviewed, drew_thumbnail, reserved, released, drew_comic,
     tweeted, folder_id, record_url, thumbnail_url, comic_url) = tuple(line[:-1].split("\t"))

    Tasks.create(
        time=time
        title=title
        manager=manager
        published_at=published_at
        recorded=recorded
        edited=edited
        reviewed=reviewed
        drew_thumbnail=drew_thumbnail
        reserved=reserved
        released=released
        drew_comic=drew_comic
        tweeted=tweeted
        folder_id=folder_id
        record_url=record_url
        thumbnail_url=thumbnail_url
        comic_url=comic_url
    }
