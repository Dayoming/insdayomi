import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from insda.forms import Form
from insda.models import Article


# Create your views here.
def board(request):
    article_list = Article.objects.all().order_by('-cdate')
    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        print('PageNotAnInteger')
        items = paginator.page(1)
    except EmptyPage:
        print('EmptyPage')
        items = paginator.page(paginator.num_pages)

    for article in items:
        print(article)

    return render(request, 'insda/board.html', {'items':items, 'pagenator':paginator})


def index(request):
    return render(request, 'insda/index.html')


def upload(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.name = request.POST['name']
            article.photo = request.FILES['photo']
            article.contents = request.POST['contents']
            article.save()

            return redirect('/insda/')
    else:
        form = Form()

    return render(request, 'insda/upload.html', {'form':form})


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = Form(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.name = request.POST['name']
            article.photo = request.FILES['photo']
            article.contents = request.POST['contents']
            article.save()

            return redirect('/insda/')
    else:
        form = Form(instance=article)
    return render(request, 'insda/upload.html', {'form':form})


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('/insda/')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'insda/detail.html', {'article':article})


def like(request):
    pk = request.POST.get('pk', None)
    article = Article.objects.get(pk=pk)
    article.like += 1
    article.save()

    context = {'pk': pk, 'like_count': article.like}

    return HttpResponse(json.dumps(context), content_type='application/json')