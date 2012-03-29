# Create your views here.

from django.shortcuts import render_to_response
from ktranslator.models import Login

def home(request):
    greeting = "This is the homepage."
    login = Login.objects.all()
    return render_to_response('ktranslator/index.html',{ 
        
        'login' :login, 
        'greeting':greeting,
    })
def detail(request, note_id):
       log = Login.objects.get(id=login_id)
       return render_to_response('ktranslator/detail.html',{ 
        
        'log' :log, 
    })
