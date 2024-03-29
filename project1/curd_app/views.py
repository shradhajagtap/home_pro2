from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import HostelForm
from .models import Hostel


@login_required(login_url="login_url")
def hostel_view(request):
    template_name = "curd_app/hostel_info.html"
    form = HostelForm()
    if request.method == "POST":
        form = HostelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_view(request):
    template_name = "curd_app/show.html"
    obj = Hostel.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Hostel.objects.get(id=pk)
    form = HostelForm(instance=obj)
    if request.method == "POST":
        form = HostelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, "curd_app/hostel_info.html", context)


def delete_view(request, pk):
    obj = Hostel.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, "curd_app/confirm.html")
