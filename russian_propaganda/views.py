from django.shortcuts import render

# Create your views here.

def title_list(request):
    return render(request, 'propaganda/title_list.html', {})