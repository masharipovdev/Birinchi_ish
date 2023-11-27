from django.db import models

# Create your models here.


class CreateJobs(models.Model):
    user_id = models.IntegerField()
    create_date = models.DateTimeField()
    deadline_start = models.DateTimeField()
    deadline_end = models.DateTimeField()
    title = models.CharField(max_length=255)
    descreption = models.TextField()
    status = models.IntegerField()
    update_date = models.DateTimeField()
    comment = models.TextField()

    def __str__(self):
        return self.title
