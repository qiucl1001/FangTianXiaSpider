# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql


class FangTianXiaMongoDBPipeline(object):
    """将数据保存到MongoDB数据库中"""
    def __init__(self, mongo_uri, mongo_db):
        """
        初始化
        :param mongo_uri: mongodb链接地址
        :param mongo_db: mongodb数据库
        """
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collections].insert_one(dict(item))
        return item

    def close_spider(self):
        self.client.close()


class FangTianXiaMySQLPipeline(object):
    """将数据保存到mysql数据库中"""
    def __init__(self, host, port, user, password, database):
        """
        初始化
        :param host: mysql宿主机所在ip地址
        :param port: mysql端口号
        :param user: 登入mysql所需用户名
        :param password: 登入mysql所需的密码
        :param database: 用来存储数据的数据库
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("MYSQL_HOST"),
            port=crawler.settings.get("MYSQL_PORT"),
            user=crawler.settings.get("MYSQL_USER"),
            password=crawler.settings.get("MYSQL_PASSWORD"),
            database=crawler.settings.get("MYSQL_DATABASE")
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8"
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ", ".join(data.keys())
        values = ", ".join(["%s"]*len(data))
        sql = "insert into %s(%s) values(%s)" % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()

        return item

    def close_spider(self):
        self.cursor.close()
        self.db.close()


