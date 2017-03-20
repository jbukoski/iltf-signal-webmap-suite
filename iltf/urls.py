from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from tamaya.admin import tamaya_admin
from comanche.admin import comanche_admin

admin.autodiscover()

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^tamaya/', include('tamaya.urls')),
url(r'^tamaya/admin/', include(tamaya_admin.urls)),
url(r'^comanche/', include('comanche.urls')),
url(r'^comanche/admin/', include(comanche_admin.urls)),]

urlpatterns += staticfiles_urlpatterns()

