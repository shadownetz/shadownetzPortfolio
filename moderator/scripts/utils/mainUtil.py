from django.conf import settings
import os


def get_custom_blog_pictures(category=""):
    images_path = []
    main_images_path = settings.CUSTOM_IMAGES
    static_file_path = ""
    if category:
        if category == 'developershub':
            static_file_path = '/static/moderator/custom/images/custom_images/blog_content/developers_hub/'
            main_images_path = settings.CUSTOM_IMAGES_DEVELOPERS_HUB
        elif category == 'sociallife':
            static_file_path = '/static/moderator/custom/images/custom_images/blog_content/socialife/'
            main_images_path = settings.CUSTOM_IMAGES_SOCIAL_LIFE
        for filename in os.listdir(main_images_path):
            if filename.endswith('.jpg'):
                final_file_path = static_file_path + filename
                images_path.append(final_file_path)
    return images_path
