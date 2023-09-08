from django.db import models
    
class City(models.Model):
    postcode = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.city} ({self.postcode})'
    
class Member(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=8)
    birthday = models.DateField()
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=8)
    postcode = models.ForeignKey(City, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Trainer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=8)
    birthday = models.DateField()
    strstreetaße = models.CharField(max_length=64)
    house_number = models.CharField(max_length=8)
    postcode = models.ForeignKey(City, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Sport(models.Model):
    name = models.CharField(max_length=64)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'

class Coaching(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.sport} with {self.trainer}'
