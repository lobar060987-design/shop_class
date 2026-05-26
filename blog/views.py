from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from blog.models import PostModel, CommentModel


# POSTLAR RO‘YXATI
def post_list_view(request):
    posts = PostModel.objects.all().order_by('-id')

    context = {
        'posts': posts
    }

    return render(request, 'post_list.html', context)


# POST DETAIL
def post_detail_view(request, slug):
    post = get_object_or_404(PostModel, slug=slug)

    # COMMENT QO‘SHISH
    if request.method == 'POST':

        # Login qilmagan user comment yoza olmaydi
        if not request.user.is_authenticated:
            return redirect('login')

        comment_text = request.POST.get('comment')


        if comment_text and comment_text.strip():

            CommentModel.objects.create(
                post=post,
                user=request.user,
                comment=comment_text.strip()
            )

            return redirect('blog:post-detail', slug=post.slug)

    # COMMENTLAR
    comments = post.comments.all().order_by('-id')

    # USER LIKE BOSGANMI
    is_liked = False

    if request.user.is_authenticated:
        is_liked = post.likes.filter(id=request.user.id).exists()

    context = {
        'post': post,
        'comments': comments,
        'is_liked': is_liked,
    }

    return render(request, 'post_detail.html', context)


# LIKE FUNKSIYASI
@login_required
def post_like_view(request, slug):

    post = get_object_or_404(PostModel, slug=slug)

    # LIKE / UNLIKE
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('blog:post-detail', slug=post.slug


# LIKE FUNKSIYASI
@login_required)
def post_like_view(request, slug):

    post = get_object_or_404(PostModel, slug=slug)

    # LIKE / UNLIKE
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('blog:post-detail', slug=post.slug)


# COMMENT LIKE
@login_required
def comment_like_view(request, id):

    comment = get_object_or_404(CommentModel, id=id)

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return redirect('blog:post-detail', slug=comment.post.slug)
# LIKE FUNKSIYASI
@login_required
def post_like_view(request, slug):

    post = get_object_or_404(PostModel, slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('blog:post-detail', slug=post.slug)


# COMMENT LIKE
@login_required
def comment_like_view(request, id):

    comment = get_object_or_404(CommentModel, id=id)

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return redirect('blog:post-detail', slug=comment.post.slug)


