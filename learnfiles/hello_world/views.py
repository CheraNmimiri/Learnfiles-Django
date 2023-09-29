from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.template import loader
# from django.http import Http404
from .models import Info


def index(request):
    all_post = Info.objects.all()
    # output = " ,".join([i.username for i in all_post])
    # template = loader.get_template("index.html")
    context = {
        "all_post": all_post,
    }
    return render(request, 'index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, post_id):
    # First method
    # try:
    #     post = Info.objects.get(pk=post_id)
    # except Info.DoesNotExist:
    #     raise Http404("Post dosen't exist.")
    # second method
    post = get_object_or_404(Info, pk=post_id)
    # temp_reader = loader.get_template("detail.html")
    context = {
        "post": post,
    }
    # return HttpResponse(temp_reader.render(context, request))
    return render(request,  'detail.html', context)


def archive_posts(request, year):
    # show_archive_posts = Info.objects.filter(created__year=year)
    show_archive_posts = get_list_or_404(Info, publish__year=year)
    context = {
        "show_archive_posts": show_archive_posts
    }
    return render(request, 'archive.html', context)
