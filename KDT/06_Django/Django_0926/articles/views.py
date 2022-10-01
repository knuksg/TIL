from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, "articles/index.html")


def create(request):
    context = {
        "content": request.GET.get("content"),
    }
    return render(request, "articles/create.html", context)
