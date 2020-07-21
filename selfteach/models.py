from django.db import models

# Create your models here.

# CREATE TABLE "book" (
# 	"name"	TEXT NOT NULL UNIQUE,
# 	"author"	TEXT NOT NULL,
# 	"edition"	TEXT NOT NULL
# );
class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    edition = models.CharField(max_length=120)
    image = models.ImageField(upload_to='selfteach/uploads/')

