"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.contrib import admin

from tinylinks.tests.views import TestFailedRedirectView, TestRedirectView

try:
    from django.conf.urls import include, patterns, url
except ImportError:  # Django < 1.6 fallback
    from django.conf.urls.defaults import include, patterns, url


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^redirect-test/', TestRedirectView.as_view()),
    url(r'^redirect-fail/', TestFailedRedirectView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tinylinks.urls')),
)
