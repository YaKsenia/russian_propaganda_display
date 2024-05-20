from django.shortcuts import render
from django.utils import timezone
from .models import Title

def title_list(request):
    titles = Title.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'propaganda/title_list.html', {'titles': titles})