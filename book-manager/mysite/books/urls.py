from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^create_book$', views.create_book),
    url(r'^edit_book/(?P<id>\d+)$', views.edit_book),
    url(r'^update_book/(?P<id>\d+)$', views.update_book),
    url(r'^delete_book/(?P<id>\d+)$', views.destroy_book),

    url(r'^add_review_to_book/(?P<id>\d+)$', views.add_review_to_book, name='add_review_to_book'),
    url(r'^book_detail/(?P<id>\d+)$', views.book_detail, name='book_detail'),

    url(r'^create_author$', views.create_author),
    url(r'^edit_author/(?P<id>\d+)$', views.edit_author),
    url(r'^update_author/(?P<id>\d+)$', views.update_author),
    url(r'^delete_author/(?P<id>\d+)$', views.destroy_author),
    url(r'^authors_index/$', views.authors_index, name='authors'),

    url(r'^search/$', views.search),
]
