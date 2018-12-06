# -*- coding: utf-8 -*-

# Scrapy settings for dados project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dados'

SPIDER_MODULES = ['dados.spiders']
NEWSPIDER_MODULE = 'dados.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dados (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'dados.pipelines.MongoDBPipeline':300,
                  }
#mongodb://<dbuser>:<dbpassword>@ds149672.mlab.com:49672/prouni
MONGODB_SERVER = "ds149672.mlab.com"
MONGODB_PORT = 49672
MONGODB_DB = "prouni"
MONGODB_COLLECTION = "seguranca"
MONGODB_USER = 'banco1'
MONGODB_PW = 'banco1'