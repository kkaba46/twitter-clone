from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def static_file(request):
	return render_to_response("new_static_template.html")
