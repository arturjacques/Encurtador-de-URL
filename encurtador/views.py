from django.shortcuts import render


# Create your views here.
def criar_link_view(request):
    if request.method == "POST":
        print(request.user)
        print(request.POST.get('url'))
    context = {}
    return render(request, "entrada.html", context)
