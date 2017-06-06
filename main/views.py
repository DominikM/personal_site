from django.shortcuts import render
from .models import Page

# Create your views here.


def index(request):
    pages = Page.objects.order_by('order').values('url')
    return render(request, 'main/home.html', {'pages': pages})


def page(request, page_url):
    try:
        page = Page.objects.get(url=page_url)
    except Page.DoesNotExist:
        return render(request, 'main/404.html')

    pages = Page.objects.order_by('order').values('url')

    if page.blog:
        posts = page.post_set.filter(visible=True).order_by('-posted_time') \
            .values('title', 'body', 'posted_time', 'modified_time')[:5]
    else:
        posts = page.post_set.filter(visible=True).order_by('order') \
            .values('title', 'body')[:5]

    print(posts)

    return render(request, 'main/page.html', {
                      'pages': pages,
                      'page': {
                          'title': page.title,
                          'description': page.description
                      },
                      'posts': posts,
                      'blog': page.blog
                  })


