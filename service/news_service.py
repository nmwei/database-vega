from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao


class NewsService:
    __news_dao=NewsDao()
    __redis_news_dao=RedisNewsDao()

    # 查询审批新闻列表
    def search_unreview_list(self, page):
        return self.__news_dao.search_unreview_list(page)

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        return self.__news_dao.search_unreview_count_page()

    # 审批新闻
    def update_unreview_news(self, id):
        return self.__news_dao.update_unreview_news(id)

    # 查询所有新闻列表
    def search_list(self, page):
        return self.__news_dao.search_list(page)

    # 查询所有新闻的总页数
    def search_count_page(self):
        return self.__news_dao.search_count_page()

    # 删除新闻
    def delete_by_id(self, id):
        return self.__news_dao.delete_by_id(id)

    # 添加新闻
    def insert(self, title, editor_id, type_id, content_id, is_top):
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    # 查找用户缓存的记录
    def search_cache(self, id):
        return self.__news_dao.search_cache(id)

    # 向Redis保存缓存的新闻
    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)

    # 删除缓存的新闻
    def delete_cache(self, id):
        self.__redis_news_dao.delete_cache(id)

    # 根据id查找新闻
    def search_by_id(self, id):
        return self.__news_dao.search_by_id(id)

    # 更改新闻
    def update(self, id, title, type_id, content_id, is_top):
        self.__news_dao.update(id, title, type_id, content_id, is_top)
        self.delete_cache(id)