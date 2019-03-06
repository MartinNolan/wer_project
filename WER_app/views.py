from django.shortcuts import render
from django.http import HttpResponse
from WER_app.models import Review

def index(request):
    return render(request, 'WER_app/index.html')


def search(request):
    return render(request, 'WER_app/search.html')
    
    
def review_sample(request):
    review_list = Review.objects.order_by('reviewID')[:4] 
    context_dict = {'reviews': review_list}

    return render(request, 'WER_app/review_sample.html', context_dict)




