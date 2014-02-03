from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from models import Kullanici, Twit, Takip, DM

# Create your views here.
def index(request):
	if 'is_authenticated' in request.session:
		kullanici_id = request.session['kullanici_id']
		takip_edilen_sayi = Takip.objects.filter(edilen__id=kullanici_id).count()
		takip_eden_sayi = Takip.objects.filter(eden__id=kullanici_id).count()
		c = {'edilen_sayi':takip_edilen_sayi, 'eden_sayi':takip_eden_sayi}
		return render_to_response("index.html",c)
	else:
		c = {}
		c.update(csrf(request))
		return render_to_response("login.html",c)

def login(request):
	k = Kullanici.objects.filter(email=request.POST['username']) 
	if k.count() > 0:
		k = k[0]
		if k.password == request.POST['password']:
			request.session['is_authenticated'] = True
			request.session['kullanici_id'] = k.id
	return redirect('/twitter/index')

def logout(request):
	if 'is_authenticated' in request.session: 
		del request.session['is_authenticated']
	return redirect('/twitter/index')

def signup(request):
	if request.method != "POST":
		c = {}
		c.update(csrf(request))
		return render_to_response('signup.html',c)
	else:
		k = Kullanici(email=request.POST['username'],password=request.POST['password'],
					name=request.POST['name'])
		k.save()
		return redirect('/twitter/index')

