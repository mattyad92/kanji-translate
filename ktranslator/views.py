# Create your views here.

from django.shortcuts import render_to_response
from ktranslator.models import Login

def home(request):
    greeting = "This is the homepage."
    login = Login.objects.all()
    return render_to_response('ktranslator/index.html',{ 
        

         'greeting':greeting,
    })

