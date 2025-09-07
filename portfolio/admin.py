from django.contrib import admin
from .models import Portfolio, Projet, Commentaire, Message, Actualite, ProfilActualite, Index, Presente, Tech0, Tech1, TextMessage, ImageProjet
# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug', 'categorie', 'image', 'date')

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug', 'categorie', 'image', 'date', 'lien')

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'commentaire', 'image', 'date')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'message', 'date')

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'description', 'date')

class IndexAdmin(admin.ModelAdmin):
    list_display = ('salut', 'nom', 'intro', 'prof0','inter', 'prof1', 'image', 'date')

class PresenteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prof0', 'prof1', 'prof2', 'rest', 'description', 'image', 'date')

class Tech0Admin(admin.ModelAdmin):
    list_display = ('nom', 'date')

class Tech1Admin(admin.ModelAdmin):
    list_display = ('nom', 'date')

class ProfilActualiteAdmin(admin.ModelAdmin):
    list_display = ('post', 'titre', 'image', 'description', 'date')

class ImageProjetAdmin(admin.ModelAdmin):
    list_display = ('projet', 'titre', 'image', 'date')

class TextMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'date')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(ProfilActualite, ProfilActualiteAdmin)
admin.site.register(ImageProjet, ImageProjetAdmin)
admin.site.register(Index, IndexAdmin)
admin.site.register(Presente, PresenteAdmin)
admin.site.register(Tech0, Tech0Admin)
admin.site.register(Tech1, Tech1Admin)
admin.site.register(TextMessage, TextMessageAdmin)