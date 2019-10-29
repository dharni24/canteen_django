from django.db import models

# Create your models here.

class Student(models.Model):
	roll = models.CharField(max_length = 15)
	psw = models.CharField(max_length = 20)
	wallet = models.IntegerField()

	class Meta:
		db_table = "student"

class Orders(models.Model):
	order_id = models.IntegerField()
	roll = models.CharField(max_length = 15)
	desc = models.CharField(max_length = 100)
	total = models.IntegerField()

	class Meta:
		db_table = "orders"