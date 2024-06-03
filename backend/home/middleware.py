# home/middleware.py

from django.shortcuts import redirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class AdminRedirectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/admin/':
            return redirect(f'/{settings.LANGUAGE_CODE}/admin/')
        return None
