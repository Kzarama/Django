from django.http import HttpResponse
from datetime import datetime
import json

def hello(request):
    now = datetime.now().strftime('%dth %b %Y - %H:%M hrs')
    return HttpResponse('Hello World!!! the time is {now}'.format(now=now))

def sortNumbers(request):
    try:
        numbers = [int(i) for i in request.GET['numbers'].split(',')]
        sorted_numbers = sorted(numbers)
        data = {
            'status' : 'ok',
            'numbers' : sorted_numbers,
            'message' : 'integers sorted successfully'
        }
        return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    except:
        return HttpResponse('error: no hay numeros en request')

def sayHi(request, name, age):
    if age < 12:
        message = 'sorry {}, you are not allow'.format(name)
    else:
        message = 'hi, welcome {} to platzigram!'.format(name)
    return HttpResponse (message)