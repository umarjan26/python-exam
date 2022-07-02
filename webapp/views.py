from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.forms import GuestBookForm
from webapp.models import Guestbook, STATUS


def index(request):
    guest = Guestbook.objects.order_by("-created_at").filter(status="active")
    context = {"guest": guest}
    return render(request, "index.html", context)


def create_guest(request):
    if request.method == "GET":
        book = GuestBookForm()
        return render(request, "create.html", {'form': book})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get("author")
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            Guestbook.objects.create(author=author, email=email, text=text)
            return redirect("index")
        return render(request, "create.html", {"form": form})

