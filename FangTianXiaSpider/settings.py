# -*- coding: utf-8 -*-

# Scrapy settings for FangTianXiaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FangTianXiaSpider'

SPIDER_MODULES = ['FangTianXiaSpider.spiders']
NEWSPIDER_MODULE = 'FangTianXiaSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'FangTianXiaSpider (+http://www.yourdomain.com)'

# mongodb数据库相关配置信息
MONGO_URI = "localhost"
MONGO_DB = "fang_tian_xia"

# mysql数据库相关配置信息
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "qcl123"
MYSQL_DATABASE = "fang_tian_xia"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "cookie": "Integrateactivity=notincludemc; global_cookie=17kijhurz2h9vm365ltm7ct412uk8sorg7d; new_search_uid=b72c"
              "61f515372e749de47dc0bdb60cc2; __utmc=147393320; xfAdvLunbo=; searchConN=1_1586434558_3487%5B%3A%7C%40%"
              "7C%3A%5D1f8fcecd705d62e6e809eef94a988b89; logGuid=0bc536d2-f141-4d34-bb7b-3d400dc62cf5; newhouse_user_"
              "guid=3E539168-B610-AD4A-1B69-2F3EF69A312E; newhouse_chat_guid=7E7D939E-8139-DE52-AEB9-A9EA4E6CB149; __"
              "utma=147393320.828304232.1586434571.1586434571.1586438385.2; __utmz=147393320.1586438385.2.2.utmcsr=hf"
              ".fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; Captcha=6A722F6F33626B657162567456373741646B697A5"
              "44A4D64784A492B7174577579557376364B464E542F2F307455516967445375636A6C53314B33523771477A754652704C497837"
              "336D733D; csrfToken=PeLPpRGyX04T2ZcpUf1dfo9c; g_sourcepage=esf_fy%5Elb_pc; city=www; unique_cookie=U_17"
              "kijhurz2h9vm365ltm7ct412uk8sorg7d*52; __utmb=147393320.118.10.1586438385",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.132 Safari/537.36"
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'FangTianXiaSpider.middlewares.FangtianxiaspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'FangTianXiaSpider.middlewares.RandomUADownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'FangTianXiaSpider.pipelines.FangTianXiaMongoDBPipeline': 300,
   'FangTianXiaSpider.pipelines.FangTianXiaMySQLPipeline': 303,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
