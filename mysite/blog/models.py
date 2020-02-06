from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# [cmder] python manage.py migrate --update the models
# [cmder] python manage.py sqlmigrate blog 0001 --check out the db

# [cmder] python manage.py shell
# >>> from blog.models import Post
# >>> (line 3)

# >>> User.objects.all()
# >>> User.objects.get(id=?)
# >>> User.objects.filter(username=?)

# >>> post_1 = Post(title='Blog 1', .......)
# >>> post_1.save()
