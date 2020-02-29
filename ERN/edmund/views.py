from django.shortcuts import render
from .models import Post
from .models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    latest_story = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-time_stamp')[0:3]
    latest_context = {
        'latest': latest,
        'latest_story': latest_story,
    }
    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save(
            
            
            
            
            
            
            
        )

    return render(request, "index.html", latest_context)


def blog(request):
    queryset = Post.objects.filter(featured=True)
    post_list = Post.objects.all()
    paginator = Paginator(post_list,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
        'page_request_var': page_request_var,
        'post_list': paginated_queryset,
    }
    return render(request, "blog.html", context)


def contact(request):
    return render(request, "contact.html")


def about_us(request):
    return render(request, "about-us.html")


def donations(request):
    return render(request, "elements.html")