from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, View, TemplateView
from .models import Comment, Like, Blog
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from .forms import commentForm


# Create your views here.
class blog_list(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog_list.html'
    queryset = Blog.objects.order_by('-publish_date')


class myBlog(LoginRequiredMixin, TemplateView):
    template_name = 'app_blog/my_blog.html'


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'app_blog/create_blog.html'

    def form_valid(request, self, form):
       # form = MyForm(request.POST, request.FILES)
        blog_obj = form.save()
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))





@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = commentForm()
    already_liked = Like.objects.filter(blog=blog, user=request.user)

    if already_liked:
        liked = True
    else:
        liked = False

    if request.method == 'POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'slug': slug}))

    diction = {'blog': blog, 'comment_form': comment_form, 'liked': liked}
    return render(request, 'app_blog/blog_details.html', context=diction)


@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if not already_liked:
        like_post = Like(blog=blog, user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'slug': blog.slug}))


@login_required
def unlike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'slug': blog.slug}))


class UpdateBlog(LoginRequiredMixin, UpdateView):
    # queryset = Blog.objects.all()
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'app_blog/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('app_blog:blog_details', kwargs={'slug': self.object.slug})


