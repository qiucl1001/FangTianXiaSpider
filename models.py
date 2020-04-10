# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    """app配置相关信息类"""

    # SQLAlchemy相关配置选项
    # 设置连接数据库的URL
    # 注意：district_code数据库要事先手动创建
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qcl123@127.0.0.1:3306/fang_tian_xia'

    # 动态跟踪配置
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)


# 创建一个SQLAlchemy数据库连接对象
db = SQLAlchemy(app)

# 创建flask脚本管理工具对象r
manager = Manager(app)

# 创建数据库迁移工具对象
Migrate(app, db)

# 向manager对象中添加数据库操作命令
manager.add_command("db", MigrateCommand)


class NewHouseFang(db.Model):
    """定义一个用来存储房天下新房的数据表"""
    # 定义表名
    __tblname__ = "new_houses"

    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(64))  # 省份
    city = db.Column(db.String(64))  # 市
    name = db.Column(db.String(64))  # 小区名
    price = db.Column(db.String(64))  # 价格
    rooms = db.Column(db.String(64))  # 几居几室
    area = db.Column(db.String(32))  # 面积
    address = db.Column(db.String(128))  # 地址
    district = db.Column(db.String(64))  # 行政区
    sale = db.Column(db.String(64))  # 是否在销售中
    origin_url = db.Column(db.String(255))  # 原url地址

    def __str__(self):
        return 'NewHouseFang:%s' % self.name


class EsfFang(db.Model):
    """定义一个用来存储房天下二手房的数据表"""
    # 定义表名
    __tblname__ = "esf_houses"

    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(64))  # 省份
    city = db.Column(db.String(64))  # 市
    name = db.Column(db.String(64))  # 小区名
    rooms = db.Column(db.String(64))  # 几室几厅
    floor = db.Column(db.String(16))  # 楼层
    toward = db.Column(db.String(16))  # 朝向
    year = db.Column(db.String(32))  # 建筑年代
    address = db.Column(db.String(128))  # 地址
    area = db.Column(db.String(32))  # 建筑面积
    price_total = db.Column(db.String(32))  # 总价
    price_unit = db.Column(db.String(32))  # 单价
    origin_url = db.Column(db.String(255))  # 原url地址

    def __str__(self):
        return 'EsfFang:%s' % self.name


if __name__ == '__main__':
    manager.run()
