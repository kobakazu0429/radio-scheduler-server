# -*- coding: utf-8 -*-
#
# +-------------------------------------------------------------------+
# | radio_scheduler - DataBase Info                                   |
# | CREATE TABLE `tasks` (`id` int(11) NOT NULL AUTO_INCREMENT,       |
# |                       `time` int(11) DEFAULT NULL,                |
# |                       `title` text CHARACTER SET utf8,            |
# |                       `manager` text CHARACTER SET utf8,          |
# |                       `published_at` date DEFAULT NULL,           |
# |                       `recorded` tinyint(1) NOT NULL,             |
# |                       `edited` tinyint(1) NOT NULL,               |
# |                       `reviewed` tinyint(1) NOT NULL,             |
# |                       `drew_thumbnail` tinyint(1) NOT NULL,       |
# |                       `reserved` tinyint(1) NOT NULL,             |
# |                       `released` tinyint(1) NOT NULL,             |
# |                       `drew_comic` tinyint(1) NOT NULL,           |
# |                       `tweeted` tinyint(1) NOT NULL,              |
# |                       `folder_id` text CHARACTER SET utf8,        |
# |                       `record_url` text CHARACTER SET utf8,       |
# |                       `thumbnail_url` text CHARACTER SET utf8,    |
# |                       `comic_url` text CHARACTER SET utf8,        |
# |                       PRIMARY KEY(`id`)                           |
# |                       ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 |
# +-------------------------------------------------------------------+

from peewee import *
import settings


db = MySQLDatabase(
    database=settings.DB_NAME,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT)


class Tasks(Model):
    time = IntegerField(null=True, default='')
    title = TextField(null=True, default='')
    manager = TextField(null=True, default='')
    published_at = DateField(null=True, default='')
    recorded = BooleanField(default=False)
    edited = BooleanField(default=False)
    reviewed = BooleanField(default=False)
    drew_thumbnail = BooleanField(default=False)
    reserved = BooleanField(default=False)
    released = BooleanField(default=False)
    drew_comic = BooleanField(default=False)
    tweeted = BooleanField(default=False)
    folder_id = TextField(null=True, default='')
    record_url = TextField(null=True, default='')
    thumbnail_url = TextField(null=True, default='')
    comic_url = TextField(null=True, default='')

    class Meta:
        database = db
