from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from .forms import CitizenForm
from .models import User, Citizen

def paginate_citizens(request, items):
    """Вспомогательная функция для создания объекта Paginator"""
    return Paginator(items, 10).get_page(request.GET.get('page'))

def index(request):
    return render(request, 'citizens/index.html', {})

def citizens(request):
    """Отображение всех последних 10 записей"""
    return render(
        request,
        'citizens/citizens_list.html',
        {'page_obj': paginate_citizens(request, Citizen.objects.all())}
    )

def citizen_detail(request, citizen_id):
    """Отображение информации конкретного жителя"""
    citizen = get_object_or_404(Citizen, id=citizen_id)
    context = {
        'citizen': citizen,
    }
    return render(request, 'citizens/citizen_detail.html', context)

@login_required
def citizen_create(request):
    """Создание нового жителя"""
    form = CitizenForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'citizens/create_citizen.html', {'form': form})
    citizen = form.save(commit=False)
    citizen.save()
    return redirect('citizens:citizens_list')

@login_required
def citizen_edit(request, citizen_id):
    """Изменение данных жителя"""
    is_edit = True
    citizen = get_object_or_404(Citizen, id=citizen_id)
    form = CitizenForm(request.POST or None, instance=citizen)
    if not form.is_valid():
        context = {
            'form': form,
            'is_edit': is_edit
        }
        return render(request, 'citizens/create_citizen.html', context)
    citizen = form.save()
    return redirect('citizens:citizen_detail', citizen_id)

class CitizenDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'citizens/citizen_delete.html'
    queryset = Citizen.objects.all()
    context_object_name = 'citizen'

    def get_success_url(self):
        return reverse('citizens:citizens_list')