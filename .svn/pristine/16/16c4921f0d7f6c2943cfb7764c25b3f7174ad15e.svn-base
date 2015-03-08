from django.db import models
from django.contrib.auth.models import User

class Month(models.Model):
	user = models.ForeignKey(User)
	day1 = models.IntegerField(default=-1)
	day2 = models.IntegerField(default=-2)
	day3 = models.IntegerField(default=-3)
	day4 = models.IntegerField(default=-4)
	day5 = models.IntegerField(default=-5)
	day6 = models.IntegerField(default=-6)
	day7 = models.IntegerField(default=-7)
	day8 = models.IntegerField(default=-8)
	day9 = models.IntegerField(default=-9)
	day10 = models.IntegerField(default=-10)
	day11 = models.IntegerField(default=-11)
	day12 = models.IntegerField(default=-12)
	day13 = models.IntegerField(default=-13)
	day14 = models.IntegerField(default=-14)
	day15 = models.IntegerField(default=-15)
	day16 = models.IntegerField(default=-16)
	day17 = models.IntegerField(default=-17)
	day18 = models.IntegerField(default=-18)
	day19 = models.IntegerField(default=-19)
	day20 = models.IntegerField(default=-20)
	day21 = models.IntegerField(default=-21)
	day22 = models.IntegerField(default=-22)
	day23 = models.IntegerField(default=-23)
	day24 = models.IntegerField(default=-24)
	day25 = models.IntegerField(default=-25)
	day26 = models.IntegerField(default=-26)
	day27 = models.IntegerField(default=-27)
	day28 = models.IntegerField(default=-28)
	day29 = models.IntegerField(default=-29)
	day30 = models.IntegerField(default=-30)
	day31 = models.IntegerField(default=-31)
	def __str__(self):
		return 'march'

class Day(models.Model):
	date = models.DateField('day')
	user = models.ForeignKey(User)
	def __str__(self):
		return str(self.date)

class Event(models.Model):
	start = models.TimeField('start time')
	end = models.TimeField('end time')
	name = models.CharField(max_length=60)
	day = models.ForeignKey(Day)
	def __str__(self):
		return self.name
