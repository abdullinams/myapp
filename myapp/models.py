from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

class Doctor(models.Model):
    name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 11)
    work_experience = models.IntegerField()
    qualification = models.CharField(choices = (('Вторая', 'Вторая'),('Первая','Первая'),('Высшая','Высшая'),),max_length = 100)
    department = models.CharField(choices = (('Приемное','Приемное'), ('Терапевтическое', 'Терапевтическое')), max_length = 100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
