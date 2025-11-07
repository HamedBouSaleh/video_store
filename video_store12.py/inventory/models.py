from django.db import models

class Video(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=100)
    Actor1Name = models.CharField(max_length=100)
    Actor2Name = models.CharField(max_length=100)
    DirectorName = models.CharField(max_length=100)
    MovieGenre = models.CharField(max_length=50)
    ReleaseYear = models.IntegerField()

    def __str__(self):
        return self.MovieTitle
