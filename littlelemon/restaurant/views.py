# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)




def menu(request):
    # Retrieve all objects from the Menu model
    menu_data = Menu.objects.all()

    # Create a dictionary containing some main data
    main_data = {
        'menu': menu_data,

    }

    # Render a template with the menu_data and main_data variables
    # return render(request, '', {'menu_data': menu_data, 'main_data': main_data})
    return render(request, 'menu.html', main_data)


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    return render(request, 'menu_item.html', {"menu_item": menu_item})
