from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def my_view(request):
    context = {
        'message': 'Hello, World!'
    }
    return render(request, 'index.html', context)