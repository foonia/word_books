from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Word
from .forms import WordForm
import random

class WordList(ListView):
    model = Word

    def get(self, request):

        queryset = Word.objects.all().order_by('-id')
        paginator = Paginator(queryset, 15)

        if 'page' in request.GET:
            page = request.GET.get('page')
            word_list = paginator.get_page(page)
            return render(request, 'word/word_list.html', {'word_list':word_list})


        for key, value in request.GET.items():
            query = Word.objects.get(word=key) 
            Word.objects.filter(word=query.word).delete()


        word_list = paginator.get_page(1)
        return render(request, 'word/word_list.html', {'word_list':word_list})


@login_required
def word_add(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            Word(**form.cleaned_data).save()
            return redirect('word:word_list')
    else:
        form = WordForm()

    return render(request, 'word/word_add.html', {'form':form})

@login_required
def word_test(request):
    if request.GET:
        word, mean = list(request.GET.items())[0]
        inst = Word.objects.get(word=word)
        split_words = inst.meaning.split(',')
        split_words = [ s.strip() for s in split_words ]

        if mean in split_words:
            count = inst.count
            if count >= 5:
                inst.delete()
            else:
                inst.count = count + 1
                inst.save()

            messages.success(request, 'the answer is True! {} is {}'.format(word, inst.meaning))
        else:
            messages.warning(request, 'the answer is False! {} is {}'.format(word, inst.meaning))

    word = Word.objects.all()[random.randrange(0,Word.objects.count())]

    return render(request, 'word/word_test.html', {'word': word})
