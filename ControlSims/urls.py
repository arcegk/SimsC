from django.conf.urls import patterns, include, url
from django.contrib import admin
from control.views import VentaListView , VentaCreateView, SimListViewtoUp ,\
 SimUpdateView , VentaUpdateView , MesListView , ConsultaAjax


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ControlSims.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sim/(?P<pk>\d+)/editar/$' , SimUpdateView.as_view() , name='sim_update'),
    url(r'^ventas/(?P<pk>\d+)/editar/' , VentaUpdateView.as_view() , name='venta_update'),
    url(r'^$' ,  SimListViewtoUp.as_view() , name='list_simstoUp'),
    url(r'^ventas/' , VentaListView.as_view() , name='list_ventas'),
    url(r'^register/' , VentaCreateView.as_view() , name = 'registrar'),
    url(r'^consulta/' , MesListView.as_view() , name="consulta"),
    url(r'^consulta-ajax/' , ConsultaAjax.as_view() , name = "consulta-ajax")
   

)