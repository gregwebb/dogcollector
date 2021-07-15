from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Treat
from .forms import WalkingForm

class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

def home(request):
  return render(request, 'home.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  treats_dog_doesnt_have = Treat.objects.exclude(id__in = dog.treats.all().values_list('id'))
  walking_form = WalkingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog, 'walking_form': walking_form,
    'treats': treats_dog_doesnt_have
  })

def add_walking(request, dog_id):
  form = WalkingForm(request.POST)
  if form.is_valid():
    new_walking = form.save(commit=False)
    new_walking.dog_id = dog_id
    new_walking.save()
  return redirect('detail', dog_id=dog_id)

def assoc_treat(request, dog_id, treat_id):
  Dog.objects.get(id=dog_id).treats.add(treat_id)
  return redirect('detail', dog_id=dog_id)

def unassoc_treat(request, dog_id, treat_id):
  Dog.objects.get(id=dog_id).treats.remove(treat_id)
  return redirect('detail', dog_id=dog_id)

class TreatList(ListView):
  model = Treat

class TreatDetail(DetailView):
  model = Treat

class TreatCreate(CreateView):
  model = Treat
  fields = '__all__'

class TreatUpdate(UpdateView):
  model = Treat
  fields = ['name', 'flavor']

class TreatDelete(DeleteView):
  model = Treat
  success_url = '/treats/'