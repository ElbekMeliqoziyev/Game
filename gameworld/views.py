from django.shortcuts import render
from .forms import GameForm
from django.views import View

from .models import Games, Category

# class HomeView(View):
#     def get(self, request):
#         return render(request, 'create.html')
    

class HomeView(View):
    def get(self, request):

        data = { 
            "games":Games.objects.all(),
            "most_played":"Games.objects.filter('')"
            }

        return render(request, 'index.html', context=data )

    def post(self, request):
        

        return render(request, 'index.html' )


class GameAddView(View):
    def get(self, request):
        data = {
            'form':GameForm(),
            'categories':Category.objects.all()
        }
        return render(request, 'create.html', context=data)
    
    def post(self, request):

        return render(request, 'create.html')