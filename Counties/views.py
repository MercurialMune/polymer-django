from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import JsonResponse
from Counties.models import Counties


def search_results(request):
    if request.method == 'GET':
        data = {
            'is_available':False
        }
        county = request.GET.get('query')
        try:
            countymodel = Counties.objects.get(county__icontains=county)
            data['is_available'] = True
            data['is_singular'] = True
            data["county"] = countymodel.county
            data["places"] = countymodel.places

        except MultipleObjectsReturned:
            data['is_available'] = True
            data['is_multiple'] = True
            countymodels = Counties.objects.filter(county__icontains=county)
            data['counties'] = {c.county:[p for p in c.places] for c in countymodels}
        except ObjectDoesNotExist:
            pass

        return JsonResponse(data)


