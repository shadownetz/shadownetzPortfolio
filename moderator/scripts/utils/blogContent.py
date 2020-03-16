from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
from django.conf import settings
from requests.exceptions import ConnectionError, ReadTimeout


class Content:

    def __init__(self, title, content, user, image, url, tags, date):
        self.title = title
        self.content = content
        self.user = user
        self.image = image
        self.tags = tags
        self.date = date
        self.url = url

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_user(self):
        return self.user

    def get_image(self):
        return self.image

    def get_tags(self):
        return self.tags

    def get_date(self):
        return self.date

    def get_url(self):
        return self.url


class BlogContentTemplate:

    def __init__(self):
        self.newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)

    def get_content(self, context, tag="", page=1):
        result = []
        try:
            all_articles = self.newsapi.get_everything(q=context, page=page)
        except ConnectionError:
            pass
        except ReadTimeout:
            pass
        except NewsAPIException:
            pass
        else:
            if all_articles['status'] == 'ok':
                articles = all_articles['articles']
                for item in articles:
                    title = item['title']
                    content = item['content']
                    user = item['author']
                    image = item['urlToImage']
                    tags = tag
                    url = item['url']
                    date = item['publishedAt']
                    new_content = Content(title, content, user, image, url, tags, date)
                    result.append(new_content)
        return result
