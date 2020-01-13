from db.news_dao import NewsDao


class NewsService:
    __news_dao=NewsDao()

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