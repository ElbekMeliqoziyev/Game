from django.shortcuts import render

from django.views import View

from .models import Games, Category

class HomeView(View):
    def get(self, request):

        data = { 
            "games":Games.objects.all(),
            "most_played":"Games.objects.filter('')"
            }

        return render(request, 'index.html', context=data )

    def post(self, request):
        

        return render(request, 'index.html' )

