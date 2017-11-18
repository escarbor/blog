from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

                  url(r'^about/$', views.about, name='about'),
                  url(r'^$', views.blog, name='blog'),
                  url(r'^blog/$', views.blog, name='blog'),
                  url(r'^contact/$', views.contact, name='contact'),
                  # url(r'^portfolio/$', views.portfolio, name='portfolio'),
                  url(r'^blog/(?P<slug>[\w-]+)/$', views.blog_post, name='blog_post'),
                  url(r'^blog/filtered/(?P<category>[\w-]+)/$', views.blog_filter, name='blog_filtered'),
                  url(r'^contact/contact_submit/$', views.contact_submit, name="contact_submit"),
                  url(r'^blog/([\w-]+)/comment_submit/$', views.comment_submit, name="comment_submit")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

