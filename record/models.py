from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=1024)
    birth = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    home_filed = models.CharField(max_length=512)
    address = models.CharField(max_length=1024)


class Record(models.Model):
    competition = models.CharField(max_length=512)
    season = models.CharField(max_length=255)
    club_id = models.IntegerField()
    club_name = models.CharField(max_length=1024)
    win = models.IntegerField()
    draw = models.IntegerField()
    lose = models.IntegerField()
    goal = models.IntegerField()
    lose = models.IntegerField()
    score = models.IntegerField()

class Socker(models.Model):
    name = models.CharField(max_length=1024)
    club_id = models.IntegerField()
    club = models.CharField(max_length=1024)
    country = models.CharField(max_length=255)
    birthday = models.TimeField()
    tall = models.IntegerField()
    weight = models.IntegerField()
    message = models.CharField(max_length=1024)

class TopGoal(models.Model):
    pass
