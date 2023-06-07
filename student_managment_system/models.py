from django.db import models
from django.contrib.auth.models import AbstractUser

class Uloga(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Korisnik(AbstractUser):
    STATUS = (('none', 'None'), ('izv', 'izvanredni student'), ('red', 'redovni student'))
    status = models.CharField(max_length=50, choices=STATUS)
    uloga = models.ForeignKey(Uloga, on_delete=models.SET_NULL, null=True, related_name = 'korisnici')

    def ___str___(self) -> str:
        return self.email

class Predmet(models.Model):
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    ects = models.PositiveSmallIntegerField()
    sem_izv = models.PositiveSmallIntegerField()
    sem_red = models.PositiveSmallIntegerField()
    IZBORNI = (('Da', 'Da'), ('Ne', 'Ne'))
    izborni = models.CharField(max_length=50, choices=IZBORNI)
    nositelj = models.ForeignKey(Korisnik, on_delete=models.SET_NULL, null=True, blank=True)

    def ___str___(self) -> str:
        return self.name

class Upis(models.Model):
    student = models.ForeignKey(Korisnik, on_delete=models.CASCADE, related_name = 'korisnici')
    predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE, related_name = 'predmeti')
    STATUS = (('upisan', 'Upisan'), ('neupisan', 'Neupisan'), ('izgubljen_potpis', 'Izgbuljen Potpis'), ('polozen', 'Polozen'))
    status = models.CharField(max_length=50, choices=STATUS)

    def ___str___(self) -> str:
        return self.student_id.username + " " + self.predmet_id.name