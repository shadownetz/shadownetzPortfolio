from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from .models import (FoodBlog, FoodBlogComment)
from django.core.exceptions import ObjectDoesNotExist


class FoodBlogClass:

    def __init__(self):
        self.blog_model = FoodBlog

    def get_model_content(self, order_by="date_created"):
        return self.blog_model.objects.all().order_by(order_by)

    def filter_model_content(self, title="", order_by="date_created"):
        return self.blog_model.objects.filter(title__icontains=title).order_by(order_by)

    def get_single_model_content(self, model_id):
        try:
            return self.blog_model.objects.get(pk=model_id) if model_id else None
        except ObjectDoesNotExist:
            return

    def get_blog_content(self, page, per_page_number):
        FoodBlogs = self.get_model_content()
        paginator = Paginator(FoodBlogs, per_page_number)
        blogs = ''

        try:
            blogs = paginator.get_page(page)
        except PageNotAnInteger:
            blogs = paginator.get_page(1)
        except EmptyPage:
            blogs = ''
        finally:
            return blogs

    def get_single_blog_content(self, blog_id):
        single_blog = self.get_single_model_content(blog_id)
        return single_blog if single_blog else ''

    def get_previous_single_blog_content(self, main_blog_id):
        main_blog = self.get_single_model_content(main_blog_id)
        if main_blog:
            tmp_main_blog_id = int(main_blog_id) - 1    # start fetch from previous blog content
            while tmp_main_blog_id > 0:
                prev_blog = self.get_single_model_content(tmp_main_blog_id)
                if prev_blog:
                    return prev_blog
                tmp_main_blog_id -= 1
                continue
        return

    def get_next_single_blog_content(self, main_blog_id):
        main_blog = self.get_single_model_content(main_blog_id)
        if main_blog:
            tmp_main_blog_id = int(main_blog_id) + 1    # start fetch from next blog content
            all_blog_count = self.get_model_content().count()
            while tmp_main_blog_id <= all_blog_count:
                next_blog = self.get_single_model_content(tmp_main_blog_id)
                if next_blog:
                    return next_blog
                tmp_main_blog_id += 1
        return

    def post_comment(self, blog_id, email, message):
        if blog_id and email and message:
            main_blog = self.get_single_blog_content(blog_id=blog_id)
            if main_blog:
                tmp_object = FoodBlogComment.objects.create(
                    user=email, blog=main_blog, message=message
                )
                if tmp_object:
                    main_blog.comments += 1
                    main_blog.save()
                    return True
        return False

    def get_comments(self, blog_id):
        """
        Get comments for a selected blog
        :param blog_id: id of blog to fetch comment from
        :return: list of comments, total number of comments
        """
        if blog_id:
            main_blog = self.get_single_blog_content(blog_id=blog_id)
            if main_blog:
                selected_comments = FoodBlogComment.objects.filter(blog=main_blog).order_by('id')[::-1]
                no_of_comments = len(selected_comments)
                return [selected_comments, no_of_comments]
        return ['', 0]

    def get_comment_greater_than_id(self, blog_id, tmp_id):
        if blog_id:
            last_comment_id = int(tmp_id)
            main_blog = self.get_single_blog_content(blog_id=blog_id)
            if main_blog:
                selected_comments = FoodBlogComment.objects.filter(blog=main_blog, id__gt=last_comment_id)
                return selected_comments
        return ''

    def get_total_no_of_comment(self, blog_id):
        if blog_id:
            main_blog = self.get_single_blog_content(blog_id=blog_id)
            if main_blog:
                return FoodBlogComment.objects.filter(blog=main_blog).count()
        return 0

    def filter_blog_content_by_search(self, query, page, per_page_number, context="title"):
        """
        Display blog contents based on search parameter
        :param context: search based on context parameter i.e tags
        :param query: search query
        :param page: page number to display
        :param per_page_number: number of pages per page
        :return:
        """
        if context == 'title':
            FoodBlogs = self.filter_model_content(title=query)
        else:
            FoodBlogs = self.filter_model_content()

        paginator = Paginator(FoodBlogs, per_page_number)
        blogs = ''
        try:
            blogs = paginator.get_page(page)
        except PageNotAnInteger:
            blogs = paginator.get_page(1)
        except EmptyPage:
            blogs = ''
        finally:
            return blogs
