from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import RootView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'keepcalm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RootView.as_view(), name='root' )
)
