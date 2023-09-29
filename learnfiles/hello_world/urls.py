from django.urls import path , re_path , register_converter
from . import views

from extensions import converters

register_converter(converters.Four_digit_year_maker, 'yyyy' )

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>", views.detail, name="detail"), #ersal mohtavay url be safhe asli
    # path("archive/<int:year>", views.archive_posts, name="archive")
    # re_path(r"^archive/(?P<year>[0-9]{4})/$", views.archive_posts, name="archive")
    path("archive/<yyyy:year>/", views.archive_posts, name="archive")

]

# {?P} baray eshare be yek variable pythoni estefade mishava. 