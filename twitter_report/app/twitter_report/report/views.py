from django.shortcuts import render
from django.views.generic import ListView
from report.models import Twitter_user

# Create your views here.
class TwitterUserListView(ListView):
    model = Twitter_user