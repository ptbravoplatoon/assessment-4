from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
