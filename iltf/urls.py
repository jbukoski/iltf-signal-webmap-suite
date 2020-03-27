from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from bmic.admin import bmic_admin
from comanche.admin import comanche_admin
from jskt.admin import jskt_admin
from lbst.admin import lbst_admin
from rcbc.admin import rcbc_admin
from shbt.admin import shbt_admin
from ssmt.admin import ssmt_admin
from tamaya.admin import tamaya_admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='iltf_index'),
    url(r'^accounts/login/', views.custLogin, name='custLogin'),
    url(r'^admin/', admin.site.urls),
    url(r'^calc/', include('calc.urls'), name='calc'),
    url(r'^bmic/', include('bmic.urls'), name='bmic'),
    url(r'^bmic/admin', include(bmic_admin.urls)),
    url(r'^comanche/', include('comanche.urls'), name='comanche'),
    url(r'^comanche/admin', include(comanche_admin.urls)),
    url(r'^jskt/', include('jskt.urls'), name='jskt'),
    url(r'^jskt/admin', include(jskt_admin.urls)),
    url(r'^lbst/', include('lbst.urls')),
    url(r'^lbst/admin', include(lbst_admin.urls)),
    url(r'^rcbc/', include('rcbc.urls'), name='rcbc'),
    url(r'^rcbc/admin/', include(rcbc_admin.urls)),
    url(r'^shbt/', include('shbt.urls'), name='shbt'),
    url(r'^shbt/admin/', include(shbt_admin.urls)),
    url(r'^ssmt/', include('ssmt.urls'), name='ssmt'),
    url(r'^ssmt/admin/', include(ssmt_admin.urls)),
    url(r'^tamaya/', include('tamaya.urls'), name='tamaya'),
    url(r'^tamaya/admin/', include(tamaya_admin.urls)),
]

urlpatterns += staticfiles_urlpatterns()

