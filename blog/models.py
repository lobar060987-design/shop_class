from django.db import models
from django.utils.text import slugify
from django.conf import settings


# BANNER
class BannerModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"

    def __str__(self):
        return self.title


# POST
class PostModel(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(upload_to='posts/')

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    # LIKE
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='liked_posts'
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


# COMMENT
class CommentModel(models.Model):

    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Commentlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.post.title}"

    class CommentModel(models.Model):
        post = models.ForeignKey(
            PostModel,
            on_delete=models.CASCADE,
            related_name='comments'
        )

        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )

        comment = models.TextField()

        created_at = models.DateTimeField(auto_now_add=True)

        # COMMENT LIKE
        likes = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            blank=True,
            related_name='liked_comments'
        )

        class Meta:
            verbose_name = "Comment"
            verbose_name_plural = "Commentlar"
            ordering = ['-created_at']

        def total_likes(self):
            return self.likes.count()

        def __str__(self):
            return f"{self.user} - {self.post.title}"