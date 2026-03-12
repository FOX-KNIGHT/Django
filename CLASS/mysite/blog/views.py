from django.shortcuts import render,get_object_or_404
from .form import EmailPostForm
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.mail import send_mail

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1  # Show 1 posts per page
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

#def post_share(request, post_id):
    post = get_object_or_404(Post,
                            id=post_id,
                            status=Post.Status.PUBLISHED
                            )
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(
        request,
        'blog/post/share.html',
        {
        'post': post,
        'form': form
        }
        )

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation

            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you read {post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        }
    )

def home(request):
    return render(
        request,
        'blog/blog.html'
    )