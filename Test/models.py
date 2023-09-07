from django.db import models
    
class Stadt(models.Model):
    plz = models.CharField(max_length=5, primary_key=True)
    ort = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.ort} ({self.plz})'
    
class Adresse(models.Model):
    straße = models.CharField(max_length=64)
    hausnummer = models.CharField(max_length=8)
    plz = models.ForeignKey(Stadt, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.straße} {self.hausnummer} {self.plz}'
    
class Mitglied(models.Model):
    vorname = models.CharField(max_length=64)
    nachname = models.CharField(max_length=8)
    geburtsdatum = models.DateField()
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.vorname} {self.nachname}'
    
class Trainer(models.Model):
    vorname = models.CharField(max_length=64)
    nachname = models.CharField(max_length=8)
    geburtsdatum = models.DateField()
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.vorname} {self.nachname}'
    
class Sportart(models.Model):
    name = models.CharField(max_length=64)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'

class Trainiert(models.Model):
    sportart = models.ForeignKey(Sportart, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.trainer} -> {self.sportart}'
