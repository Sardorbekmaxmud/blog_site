from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm, EmailPostForm
from django.core.mail import send_mail


# Create your views here.
class PostListView(generic.ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


def post_detail(reqeust, year, month, day, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if reqeust.method == "POST":
        comment_form = CommentForm(data=reqeust.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(reqeust, template_name='blog/post/detail.html',
                  context={'post': post,
                           'comments': comments,
                           'new_comment': new_comment,
                           'comment_form': comment_form
                           })


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == "POST":
        form = EmailPostForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            title = f"{cd['name']} sizga '{post.title}' maqolasini o'qishni taklif etadi."
            message = f"{post.title} maqolasi manzili: {post_url}\n\n" \
                      f"{cd['name']}ning izohi: {cd['comment']}"

            send_mail(title, message, cd['email'], [cd['to']], fail_silently=False)
            sent = True
    else:
        form = EmailPostForm()

    return render(request, template_name='blog/post/share.html',
                  context={'post': post,
                           'form': form,
                           'sent': sent,
                           })
