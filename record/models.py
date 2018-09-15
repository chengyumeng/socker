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
    height = models.IntegerField()
    weight = models.IntegerField()
    message = models.CharField(max_length=1024)


class Goal(models.Model):
    socker_name = models.CharField(max_length=1024)
    socker_id = models.IntegerField()
    competition = models.CharField(max_length=512)
    number = models.IntegerField()


class Assist(models.Model):
    socker_name = models.CharField(max_length=1024)
    socker_id = models.IntegerField()
    competition = models.CharField(max_length=512)
    number = models.IntegerField()


class Competition(models.Model):
    competition = models.CharField(max_length=512)
    start_time = models.TimeField()
    home_club_name = models.CharField(max_length=1024)
    home_club_id = models.IntegerField()
    home_club_score = models.IntegerField()
    guest_club_name = models.CharField(max_length=1024)
    guest_club_id = models.IntegerField()
    guest_club_score = models.IntegerField()



