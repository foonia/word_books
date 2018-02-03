from django.conf.urls import url
from .views import WordList

app_name = 'word'

urlpatterns = [
    url(r'^$', WordList.as_view(), name='word_list'),        
]
