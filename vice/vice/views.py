from django.shortcuts import render

def main(request):
    return render(request, 'main_temp.html', {'greeting': 'Welcome'})