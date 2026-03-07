from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 1) # Show 3 posts per page
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    return render(
        request,
        'blog/post/list.html',
        {'posts':posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        #id =id,
        status = Post.Status.PUBLISHED,
        slug= post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post':post}
    )

def home(request):
    return render(
        request,
        'blog/blog.html'
    )