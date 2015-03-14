from django.conf.urls import patterns, include, url
from django.contrib import admin
from control.views import SimListView , VentaListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ControlSims.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$' , SimListView.as_view() , name='listSims'),
)