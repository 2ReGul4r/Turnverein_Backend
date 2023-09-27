from django.db import models
from django.contrib.auth.models import AbstractUser
    
class City(models.Model):
    postcode = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.city} ({self.postcode})'
    
class Member(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField()
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=8)
    postcode = models.ForeignKey(City, related_name='m_city', on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Trainer(AbstractUser):
    birthday = models.DateField()
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=8)
    postcode = models.ForeignKey(City, related_name='t_city', on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Sport(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.name}'
    
class Coursedate(models.Model):
    course_length = models.IntegerField()
    days = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    
    def __str__(self):
        formatter = {
            'Saturday': 32,
            'Friday': 16,
            'Thursday': 8,
            'Wednesday': 4,
            'Tuesday': 2,
            'Monday': 1
        }
        day_code = int(self.days)
        day_list = []
        for day, value in formatter.items():
            if day_code >= value:
                day_list.append(day)
                day_code -= value
        return f'{", ".join(day_list[::-1])} at {self.hour}:{str(self.minute).zfill(2)}'

class Course(models.Model):
    sport = models.ForeignKey(Sport, related_name='sport', on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, related_name='trainer', on_delete=models.CASCADE)
    date = models.ForeignKey(Coursedate, related_name='date', on_delete=models.CASCADE)
    hall = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.sport} with {self.trainer}'
    
class Participant(models.Model):
    id_course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    id_member = models.ForeignKey(Member, related_name='member', on_delete=models.CASCADE)
