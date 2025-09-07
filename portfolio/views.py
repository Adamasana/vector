from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Projet, Message, Commentaire, Actualite, Index, Presente, Tech0, Tech1, TextMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Actualite, ProfilActualite, ImageProjet
# Create your views here.

def home(request):
    if request.method == "GET":
        # Récupérer les objets des modèles pour les afficher dans le template
        portfolios = Portfolio.objects.all()
        projets = Projet.objects.all()
        messages = Message.objects.all()
        index = Index.objects.first()
        presente = Presente.objects.first()
        techs0 = Tech0.objects.all()
        techs1 = Tech1.objects.all()
        textmessage = TextMessage.objects.first()
        commentaires = Commentaire.objects.all()
        

        context = {"portfolios": portfolios, 
                    "projets": projets, 
                    "messages": messages, 
                    "commentaires": commentaires,
                    "index": index,
                    "presente": presente,
                    "techs0": techs0,
                    "techs1": techs1,
                    "textmessage": textmessage}
        return render(request, "blog/index.html", context=context)

    if request.method == "POST":
        # Récupérer les données du formulaire
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        image = request.FILES.get("image")
        commentaire_texte = request.POST.get("commentaire")
        # Créer un nouvel objet Commentaire et l'enregistrer dans la base de données
        nouveau_commentaire = Commentaire(nom=nom, identifiant=telephone, image=image, commentaire=commentaire_texte)
        nouveau_commentaire.save()
        # Rediriger vers l'URL 'acceuil' après avoir enregistré le commentaire
        return redirect('acceuil')

def contact(request):
        if request.method == "GET":
            return render(request, 'blog/contact.html')

        if(request.method == "POST"):
                nom = request.POST.get('nom')
                identifiant = request.POST.get('identifiant')
                message = request.POST.get('message')

                message = Message(nom=nom, identifiant=identifiant, message=message)
                message.save()
                return redirect('acceuil')

def portfolio(request):
    if request.method == "GET":
        portfolios = Portfolio.objects.all()
        context = {"portfolios": portfolios}
        return render(request, 'blog/portfolio.html', context=context)

def actualite(request):
    if request.method == "GET":
        actualites = Actualite.objects.all()
        context = {"actualites": actualites}
        return render(request, 'blog/actualite.html', context=context)
    


def profilactualite(request, actualite_id):
    actualite = get_object_or_404(Actualite, id=actualite_id)
    profils_actualite = ProfilActualite.objects.filter(post=actualite)

    context = {
        'actualite': actualite,
        'profils_actualite': profils_actualite,
    }

    return render(request, 'blog/profilactualite.html', context)



def profilprojet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    images_projet = ImageProjet.objects.filter(projet=projet)

    context = {
        'projet': projet,
        'images_projet': images_projet,
    }

    return render(request, 'blog/profilprojet.html', context)
