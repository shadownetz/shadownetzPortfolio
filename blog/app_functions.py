from developershub.models import DevelopersHubBlog
from food.models import FoodBlog
from movies.models import MovieBlog
from sociallife.models import SocialLifeBlog
from sports.models import SportBlog
from trending.models import TrendingBlog
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)


class BlogClass:

    def __init__(self):
        pass

    @staticmethod
    def get_all_model_objects(filter_by=''):
        main_objects = []
        # get singular model objects each and store sequentially
        if len(filter_by) <= 0:
            obj1 = [i for i in DevelopersHubBlog.objects.all()]
            obj2 = [i for i in FoodBlog.objects.all()]
            obj3 = [i for i in MovieBlog.objects.all()]
            obj4 = [i for i in SocialLifeBlog.objects.all()]
            obj5 = [i for i in SportBlog.objects.all()]
            obj6 = [i for i in TrendingBlog.objects.all()]
        else:
            obj1 = [i for i in DevelopersHubBlog.objects.filter(title__icontains=filter_by)]
            obj2 = [i for i in FoodBlog.objects.filter(title__icontains=filter_by)]
            obj3 = [i for i in MovieBlog.objects.filter(title__icontains=filter_by)]
            obj4 = [i for i in SocialLifeBlog.objects.filter(title__icontains=filter_by)]
            obj5 = [i for i in SportBlog.objects.filter(title__icontains=filter_by)]
            obj6 = [i for i in TrendingBlog.objects.filter(title__icontains=filter_by)]
        # save sequentially as list items
        main_objects.extend(obj1)
        main_objects.extend(obj2)
        main_objects.extend(obj3)
        main_objects.extend(obj4)
        main_objects.extend(obj5)
        main_objects.extend(obj6)
        return main_objects

    @staticmethod
    def fetch_number_developer_hub_post():
        return DevelopersHubBlog.objects.count()

    @staticmethod
    def fetch_number_food_post():
        return FoodBlog.objects.count()

    @staticmethod
    def fetch_number_movies_post():
        return MovieBlog.objects.count()

    @staticmethod
    def fetch_number_social_life_post():
        return SocialLifeBlog.objects.count()

    @staticmethod
    def fetch_number_trending_post():
        return TrendingBlog.objects.count()

    @staticmethod
    def fetch_number_sport_post():
        return SportBlog.objects.count()

    def fetch_blog_items(self, page, number_per_page, query=''):
        if len(query) <= 0:
            main_objects = self.get_all_model_objects()
        else:
            main_objects = self.get_all_model_objects(query)

        final_objects = []
        # save index of each list item
        main_objects_len = [i for i in range(len(main_objects))]
        # rearranging order
        even_numbers = list(filter(lambda x: x % 2 == 0, main_objects_len))
        odd_numbers = list(filter(lambda x: x % 2 != 0, main_objects_len))
        # get each model singular object according to rearranging order
        list_one = [main_objects[i] for i in even_numbers]
        list_two = [main_objects[i] for i in odd_numbers]
        list_one.extend(list_two)
        # final list items rearranged
        final_objects.extend(list_one)
        # paginate
        paginator = Paginator(final_objects, number_per_page)
        blogs = ''
        try:
            blogs = paginator.get_page(page)
        except PageNotAnInteger:
            blogs = paginator.get_page(1)
        except EmptyPage:
            blogs = ''
        finally:
            return blogs

    @staticmethod
    def fetch_popular_post_developers_hub():
        return DevelopersHubBlog.objects.all().order_by('date_created')[::-1][0]

    @staticmethod
    def fetch_popular_post_food():
        return FoodBlog.objects.all().order_by('date_created')[::-1][0]

    @staticmethod
    def fetch_popular_post_movies():
        return MovieBlog.objects.all().order_by('date_created')[::-1][0]

    @staticmethod
    def fetch_popular_post_social_life():
        return SocialLifeBlog.objects.all().order_by('date_created')[::-1][0]

    @staticmethod
    def fetch_popular_post_trending():
        return TrendingBlog.objects.all().order_by('date_created')[::-1][0]

    @staticmethod
    def fetch_popular_post_sport():
        return SportBlog.objects.all().order_by('date_created')[::-1][0]

    @staticmethod
    def populate_list(*args):
        main_object = []
        for item in args:
            main_object.extend(item)
        return main_object
