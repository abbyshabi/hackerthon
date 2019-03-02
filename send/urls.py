from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('r^',views.index,name = 'welcome'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)