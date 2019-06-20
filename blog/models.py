from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length= 30)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.CharField('作者', max_length= 30)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.author


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category =  models.ForeignKey(Category, verbose_name='カテゴリ名', on_delete=models.PROTECT)
    likes = models.IntegerField(null=True, blank=True, default=0)
    images = models.ImageField(upload_to='')
    author = models.ForeignKey(Author, verbose_name='作者', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('お名前', max_length=50)
    text = models.TextField('コメント')
    post = models.ForeignKey(Post, verbose_name='紐づく記事', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]

