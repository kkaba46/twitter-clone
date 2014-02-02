from django.db import models

# Create your models here.

class Kullanici(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	photo = models.FileField(upload_to="/Users/emrahayanoglu/projects/twitterClone/upload",null=True)

class Twit(models.Model):
	kullanici = models.ForeignKey(Kullanici)
	ebeveyn = models.ForeignKey('self', null=True)
	mesaj = models.CharField(max_length=140)
	created_at = models.DateTimeField(auto_now_add=True)
	is_deleted = models.BooleanField()

class DM(models.Model):
	mesaj = models.CharField(max_length=250)
	kime = models.ForeignKey(Kullanici, related_name="kime")
	kimden = models.ForeignKey(Kullanici, related_name="kimden")

class Takip(models.Model):
	eden = models.ManyToManyField(Kullanici, related_name="eden")
	edilen = models.ManyToManyField(Kullanici, related_name="edilen")
