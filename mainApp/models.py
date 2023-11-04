from django.db import models


class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=200)
    qisqa_matn = models.CharField(max_length=350)
    batafsil = models.TextField()
    rasm = models.ImageField(upload_to="yangilik/")
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha


class Xodim(models.Model):
    ism = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    soha = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='xodim/')

    def __str__(self):
        return f"{self.ism} {self.fam}"


class Xizmat(models.Model):
    nom = models.CharField(max_length=255)
    batafsil = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Ichimlik(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='ichimlik/')

    def __str__(self):
        return self.nom


class Mijoz(models.Model):
    FIO = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    fikr = models.TextField(null=True, blank=True)
    xizmat = models.ManyToManyField(Xizmat, blank=True)
    ichimlik = models.ForeignKey(Ichimlik, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.FIO