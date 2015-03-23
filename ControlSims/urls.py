from django.conf.urls import patterns, include, url
from django.contrib import admin
from control.views import  SimCreateView, SimListViewtoUp ,\
 SimUpdateView , MesListView , ConsultaAjax


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ControlSims.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sim/(?P<pk>\d+)/editar/$' , SimUpdateView.as_view() , name='sim_update'),
    url(r'^$' ,  SimListViewtoUp.as_view() , name='list_simstoUp'),
    url(r'^register/' , SimCreateView.as_view() , name = 'registrar'),
    url(r'^consulta/' , MesListView.as_view() , name="consulta"),
    url(r'^consulta-ajax/' , ConsultaAjax.as_view() , name = "consulta-ajax"),
    url(r'^login/' , 'django.contrib.auth.views.login' , { 'template_name' : 'login.html'  }) ,
   

)