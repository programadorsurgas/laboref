from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404
from .forms import EditAnimalForm
from .models import Animal


def index(request):
    animal_list = Animal.objects.all()
    template = loader.get_template('animal/index.html')
    context = {
        'animal_list': animal_list,
    }
    return HttpResponse(template.render(context, request))


def detail_animal_view(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, "animal/detail.html", {'animal': animal})


def edit_animal_view(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    if request.method == "GET":
        form = EditAnimalForm(initial={
            'animal_name': animal.animal_name
        })
        ctx = {'form': form, 'animal': animal}
    return render(request, "animal/edit.html", {'animal': animal})
