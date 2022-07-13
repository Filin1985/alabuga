from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Citizen


def paginate_projects(request, citizens, results):
    page = request.GET.get('page')
    paginator = Paginator(citizens, results)

    try:
        citizens = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        citizens = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        citizens = paginator.page(page)

    left_index = (int(page) - 2)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, citizens

def search_citizen(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    citizens = Citizen.objects.distinct().filter(
        Q(first_name__icontains=search_query) |
        Q(last_name__icontains=search_query) |
        Q(age__icontains=search_query) |
        Q(status__icontains=search_query) |
        Q(income__icontains=search_query) |
        Q(master__last_name__icontains=search_query)
     )

    return citizens, search_query