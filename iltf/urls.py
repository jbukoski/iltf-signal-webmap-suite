from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from comanche.admin import comanche_admin
from lbst.admin import lbst_admin
from tamaya.admin import tamaya_admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='iltf_index'),
    url(r'^accounts/login/', views.custLogin, name='custLogin'),
    url(r'^admin/', admin.site.urls),
    url(r'^comanche/', include('comanche.urls'), name='comanche'),
    url(r'^comanche/admin', include(comanche_admin.urls)),
    url(r'^lbst/', include('lbst.urls')),
    url(r'^lbst/admin', include(lbst_admin.urls)),
    url(r'^tamaya/', include('tamaya.urls'), name='tamaya'),
    url(r'^tamaya/admin/', include(tamaya_admin.urls)),
]

urlpatterns += staticfiles_urlpatterns()

