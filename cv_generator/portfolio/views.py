from django.shortcuts import render
from portfolio.forms import ProfileForm

# Create your views here.


def detail_page(request):
    form = ProfileForm()

    if request.method == "POST":
        print(request.POST)
    context = {"form": form}
    return render(request, "templates/detail.html", context)
