from django.shortcuts import render

# Create your views here.
from webapp.models import Guestbook


def index(request):
    guest = Guestbook.objects.order_by("-created_at").filter(status="active")
    context = {"guest": guest}
    return render(request, "index.html", context)


def create_guest(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CHOICES})
    else:
        task = request.POST.get("task")
        status = request.POST.get("status")
        created_at = request.POST.get("created_at")
        new_task = Task.objects.create(task=task, status=status, created_at=created_at)
        context = {"task": new_task}
        return redirect("index_view", pk=new_task.pk)