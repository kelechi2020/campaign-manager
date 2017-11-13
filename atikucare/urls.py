from django.conf.urls import include, url
from django.contrib import admin

from buharisupport.view import generatestate,getdetails,localgovanalysis,visualize
from buharisupport import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'atikucare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.page, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^visualize/', visualize.page , name='visualize'),
    url(r'^index', views.page, name='home'),
    url(r'^getdetails/', getdetails.getdetails, name='states'),
    url(r'^getward/', getdetails.get_ward, name='wards'),
    url(r'^getpoolingunit/', getdetails.get_pooling_unit, name='pooling_unit'),
    url(r"^localgov/(?P<state>[^/]+)$", localgovanalysis.page, name='local'),
]
