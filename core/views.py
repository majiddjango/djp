from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from django.http import HttpResponse

@login_required
def home(request):
    context = {}
    context['title'] = 'حانه'
    user = request.user
    if request.POST:
        form = ItemForm(request.POST)
        passed = request.POST.get('passed',0)
        if passed == 'on':
            passed = True
        else:
            passed = False
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = user
            item.passed = passed
            form.save(commit=True)
            form = ItemForm()
            items = Item.objects.filter(owner=user)
            context['items'] = items
            context['form'] = form
            return render(request,'core/home.html',context)
        else:
            items = Item.objects.filter(owner=user)
            context['items'] = items
            context['form'] = form
            return render(request,'core/home.html',context)
    form = ItemForm()
    items = Item.objects.filter(owner=user)
    context['items'] = items
    context['form'] = form
    return render(request,'core/home.html',context)

def base_layout(request):
    context = {}
    template='base1.html'
    form = ItemForm()
    context['form'] = form

    return render(request,template,context)

@login_required
def remove(request,id):
    user = request.user
    item = get_object_or_404(Item,id=id)
    if item.owner != user:
        return redirect('home')
    else:
        item.delete()
        return redirect('home')


@login_required
def edit(request,id):
    context = {}
    context['title'] = 'ویرایش'
    user = request.user
    item = get_object_or_404(Item,id=id)
    if item.owner != user:
        return redirect('home')
    else:
        form = ItemForm(request.POST or None, instance=item)
        if request.POST and form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form'] = form
            return render(request,'core/edit.html',context)

@login_required
def getdata(request):
    user = request.user
    results=Item.objects.filter(owner=user)
    jsondata = serializers.serialize('json',results)
    return HttpResponse(jsondata)

