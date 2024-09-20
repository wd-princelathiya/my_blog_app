from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel
from .forms import PostModelForm
# Create your views here.
def index(request):

    posts = PostModel.objects.all()

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

    else:
        form = PostModelForm()

    context = {
        'posts' : posts,
         'form':form,
         }


    return render(request , 'blog/index.html', context)

