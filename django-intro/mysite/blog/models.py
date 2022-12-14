from django.db import models

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Tarefas(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    done = models.CharField(
        max_length=1,
        choices=STATUS,
    )
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']


def __str__(self):
    return self.title
