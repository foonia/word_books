from django.conf.urls import url
from .views import *

app_name = 'word'

urlpatterns = [
    url(r'^$', WordList.as_view(), name='word_list'),        
    url(r'^add$', word_add, name='word_add'),
    url(r'^test$', word_test, name='word_test'),
]
