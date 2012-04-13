# Create your views here.

from django.shortcuts import render_to_response
from ktranslator.models import Login
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    if request.user.is_authenticated():
        greeting = "You're logged in now."

    else:
        greeting = "Not logged in. =("
    login = Login.objects.all()
    return render_to_response('ktranslator/index.html',{ 
        
        'login' :login, 
        'greeting':greeting,
    })
def detail(request, login_id):
       log = Login.objects.get(id=login_id)
       return render_to_response('ktranslator/detail.html',{ 
        
        'log' :log, 
    })
