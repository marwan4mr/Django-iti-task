from django.db import models
import uuid

# Create your models here.
class Movie(models.Model):
    # django auto creates id field could have saved myself hours 😢 of reading
    # movie_id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=250, blank=False, null=False)
    discription = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True, default=0)
    cast = models.ForeignKey("Cast", related_name="movies", on_delete=models.DO_NOTHING, null=True, blank=True)
    poster = models.ImageField( upload_to='')
    def __str__(self):
        return self.name
    
    # 
class Category(models.Model):
    movies = models.ManyToManyField("Movie",related_name="category",null=True, blank=True)
    # categor_id = models.AutoField()
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.name



class Leader(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    def __str__(self):
        return self.name


class Cast(models.Model):
    number_of_people = models.IntegerField()
    leader = models.OneToOneField('Leader', on_delete=models.CASCADE, related_name="cast", null=True, blank=True)

    def __str__(self):
        return f'{self.leader.name}\'s Cast'
