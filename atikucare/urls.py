from django.conf.urls import include, url
from django.contrib import admin
from buharisupport import views
from buharisupport.view import getdetails, localgovanalysis, visualize, pooling_unit_analysis,ward_analysis
from buharisupport.view.jsonviews import allmembersdatatable

urlpatterns = [
    # Examples:
    # url(r'^$', 'atikucare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.page, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^visualize/', visualize.page, name='visualize'),
    url(r'^index', views.page, name='home'),
    url(r'^getdetails/', getdetails.getdetails, name='states'),
    url(r'^getward/', getdetails.get_ward, name='wards'),
    url(r'^getpoolingunit/', getdetails.get_pooling_unit, name='pooling_unit'),
    url(r"^localgov/(?P<state>[^/]+)$", localgovanalysis.page, name='local'),
    url(r'^members$', allmembersdatatable.peopleajax, name='table'),
    url(r'^members/view$', allmembersdatatable.peopleview, name='members'),
    url(r"^ward_analysis/(?P<localgov>[^/]+)$", ward_analysis.page, name='ward_analysis'),
    url(r"^pooling_unit_analysis/(?P<ward>[^/]+)$", pooling_unit_analysis.page, name='pooling_unit_analysis'),

]
