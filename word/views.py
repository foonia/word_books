from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Word
from .forms import WordForm
import random

class WordList(ListView):
    model = Word

    def get(self, request):
        for key, value in request.GET.items():
            query = Word.objects.get(word=key) 
            Word.objects.filter(word=query.word).delete()

        queryset = Word.objects.all().order_by('-id')
        return render(request, 'word/word_list.html', {'word_list':queryset})


def word_add(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            Word(**form.cleaned_data).save()
            return redirect('word:word_list')
    else:
        form = WordForm()

    return render(request, 'word/word_add.html', {'form':form})


def word_test(request):
    if request.GET:
        word, mean = request.GET.items[0]
        word = Word.objects.get(word=word)
        split_words = word.meaning.split(',')
        split_words = [ s.strip() for s in split_words ]

        if value in split_words:
            count = word.count
            if count >= 5:
                word.delete()
            else:
                word.count = count + 1
                word.save()

            messages.success(request, 'the answer is True! {} is {}'.format(key, word.meaning))
        else:
            messages.warning(request, 'the answer is False! {} is {}'.format(key, word.meaning))

    word = Word.objects.all()[random.randrange(0,Word.objects.count())]

    return render(request, 'word/word_test.html', {'word': word})
