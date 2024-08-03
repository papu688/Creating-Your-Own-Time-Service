from django.db import models

class Time(models.Model):
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S")