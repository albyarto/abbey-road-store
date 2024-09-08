from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Abbey Road T-Shirt',
        'price': 'Rp 300.000',
        'description': 'The Beatles T-Shirt',
        'class': 'PBP D',
        'my_name': 'Muhammad Albyarto Ghazali',
    }

    return render(request, "main.html", context)