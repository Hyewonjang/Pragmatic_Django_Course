from django.db import models

# Create your models here.


class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) # null: text가 없어도 되는 것인지 표시(True면 없어도 된다는 의미)