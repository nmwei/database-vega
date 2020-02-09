from db.mongo_db import client


class MongoNewsDao:
    # 添加新闻纪录
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
