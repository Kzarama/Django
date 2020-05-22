from django.http import HttpResponse
import json

def sort_ints(request):
    """recive a list of numbers for the url and cast to int and sort, then show a json of the sorted numbers"""
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')