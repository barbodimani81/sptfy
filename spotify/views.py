from django.shortcuts import HttpResponse, render
from django.db import models
from django.db.models import Post

from spotify.models import Person
from django.db.models import Count, Avg, Sum, Min, Max, F, Q


def hello_view(request):
    return HttpResponse('salamaleykom')

def posts(request):
    posts = []
    min_id = request.GET.get("min_id")
    max_id = request.GET.get("max_id")
    for post in Post.objects.filter(id__gte=min_id, id__lte=max_id):
        posts.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "is_new": post.id > 10,
            }
        )

    return render(request, "posts.html", context={"posts": posts})

