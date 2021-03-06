"""
The `compat` module provides support for backwards compatibility with older
versions of django and python.
"""
# flake8: noqa
from __future__ import unicode_literals

# urlparse in python3 has been renamed to urllib.parse
try:
    from urlparse import parse_qs, parse_qsl, urlparse, urlsplit, urlunparse, urlunsplit
except ImportError:
    from urllib.parse import parse_qs, parse_qsl, urlparse, urlsplit, urlunsplit, urlunparse

try:
    from urllib import urlencode, quote_plus, unquote_plus
except ImportError:
    from urllib.parse import urlencode, quote_plus, unquote_plus

# changed in Django 1.10 (broken in Django 2.0)
try:
    from django.urls import reverse, reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse, reverse_lazy

# Added in Django 1.9, required as long as 1.8 is supported
try:
    from django.contrib.auth.mixins import LoginRequiredMixin
except ImportError:
    from braces.views import LoginRequiredMixin

# bastb Django 1.10 has updated Middleware. This code imports the Mixin required to get old-style
# middleware working again
# More?
#  https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
