from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request:redirect('word:word_list')),
    path('admin/', admin.site.urls),
    path('word/', include('word.urls')),
]
