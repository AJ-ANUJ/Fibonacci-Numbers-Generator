from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import FibonacciTable

# Create your views here.

@require_http_methods(['GET'])
def fib_nums(request):
    num = request.GET.get('num')

    #checking if there is an entry in the db already for num
    db = FibonacciTable.objects.filter(fib_no__lte=num)

    if db:
        # return directly
        return 0
    
    else:
        #calculate the remaining fibnums
        pass