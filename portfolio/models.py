from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Portfolio(models.Model):
    nom = models.TextField()
    description = models.TextField()
    slug = models.SlugField()
    CATEGORIE_CHOICES = [
        ("ui", "Infographie"),
        ("web", "Design web"),
        ("app", "Developpement web")
        
    ]
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default="ui")
    image = models.ImageField(upload_to='media')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Projet(models.Model):
    nom = models.TextField()
    description = models.TextField()
    slug = models.SlugField()
    CATEGORIE_CHOICES = [
        ("web development", "web development"),
    ]
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default="web development")
    image = models.ImageField(upload_to='media')
    date = models.DateTimeField(auto_now=True)
    lien = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']


class Commentaire(models.Model):
    nom = models.TextField(default="Phantome")
    identifiant = models.TextField()
    commentaire = models.TextField(max_length=100)
    image = models.ImageField(upload_to='media', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Message(models.Model):
    nom = models.TextField(default="Phantome")
    identifiant = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Actualite(models.Model):
    titre = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date']

class ProfilActualite(models.Model):
    post = models.ForeignKey(Actualite, on_delete=models.CASCADE)
    titre = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField(max_length=415)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date']


class ImageProjet(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    titre = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date']


class Index(models.Model):
    salut = models.TextField()
    nom=models.TextField()
    intro=models.TextField()
    prof0=models.TextField()
    inter=models.TextField()
    prof1=models.TextField()
    image = models.ImageField(upload_to='static/images', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']


class Presente(models.Model):
    nom = models.TextField()
    prof0=models.TextField()
    prof1=models.TextField()
    prof2=models.TextField()
    rest=models.TextField()
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='static/images', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Tech0(models.Model):
    nom = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Tech1(models.Model):
    nom = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class TextMessage(models.Model):
    nom = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']