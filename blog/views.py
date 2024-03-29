from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template import loader

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        print(post.__dict__)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    
@login_required
def newPost(request):

    c = {}

    # Get the template
    t = loader.get_template('./new_post.html')

    # Get the context
    return HttpResponse(t.render(c, request))

@login_required
def create_post(request):
    """
    Allow an admin user to create a Blop Post
    """
    if request.user:

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                messages.info(request, 'Blog added successfully!')
                return redirect('blog')
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog failed to add.')
        else:
            form = PostForm()
    else:
        messages.error(
            request, 'Sorry, you do not have permission to do that.')
        return redirect(reverse('home'))

    template = 'add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_blog(request, blog_post_id):
    """
    Allow all users to edit the blogs they created
    """
    if request.user:

        blog_post = get_object_or_404(Post, pk=blog_post_id)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=blog_post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Blog post updated successfully!')
                return redirect('blog')
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog post failed to update.')
        else:
            form = PostForm(instance=blog_post)
            messages.info(request, f'Editing {blog_post.title}')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'edit_blog.html'

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


def delete_blog(request, blog_post_id):
    """User can delet their own blog post"""
    if request.method == "POST":
        blog_post = get_object_or_404(Post, pk=blog_post_id)
        blog_post.delete()
    else:
        return render(request, 'delete_blog.html')
    messages.success(request, 'The blog has been deleted successfully!')

    return redirect('blog')
