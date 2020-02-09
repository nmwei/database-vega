from db.mongo_db import client
from bson.objectid import ObjectId


class MongoNewsDao:
    # 添加新闻记录
    def insert(self, title, content):
        try:
            client.school.news.insert_one({'title': title, 'content': content})
        except Exception as e:
            print(e)

    # 查找新闻正文的主键值
    def search_id(self, title):
        try:
            news = client.school.news.find_one({'title': title})
            return str(news["_id"])
        except Exception as e:
            print(e)

    # 新闻修改
    def update(self, id, title, content):
        try:
            client.school.news.update_one({'_id': ObjectId(id)}, {
                '$set': {
                    'title': title,
                    'content': content
                }
            })
        except Exception as e:
            print(e)

    # 查找新闻正文
    def search_content_by_id(self, id):
        try:
            news = client.school.news.find_one({'_id': ObjectId(id)})
            return news['content']
        except Exception as e:
            print(e)