# FangTianXia

--->抓取房天下网站全国已开通658个城市的新房以及二手房数据
<网站链接：[https://www.fang.com/SoufunFamily.htm]>

备注：
* 演示了使用scrapy框架抓取新房二手房相关数据信息
* 将数据保存到MongoDB数据库
* 将数据保存到MySQL数据库
* 反爬处理：1. 通过下载器中间件设置UA池 2. 通过全局配置文件设置自定义Cookie值等

# 安装
## python versions: >=3.0+
## mysql versions: >=5.7.21  安装并启动
## mongodb versions: >=3.6.11  安装并启动

# 三方依赖库安装
```
cd FangTianXia
pip install -r requirements.txt
```

# FangTianXia项目相关配置
## 打开 models.py 配置mysql数据库连接
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://数据库用户名:数据库连接密码@数据库所在宿主机ip:3306/数据库名称'
e.g.
 SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qcl123@127.0.0.1:3306/fang_tian_xia'
 
```
## 手动创建数据库
```
mysql -u数据库用户名 -p数据库连接密码

mysql> create database fang_tian_xia default charset="utf8";

```
## 创建迁移仓库
### 这个命令会创建migrations文件夹，所有迁移文件都放在里面。
```
python models.py db init
```
## 创建迁移脚本
### 创建自动迁移脚本
```
python models.py db migrate -m 'initial migration'
```

## 更新数据库
```
python models.py db upgrade
```

## 启动程序
```
python start.py
```
