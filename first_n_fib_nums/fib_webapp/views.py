from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import FibonacciTable
from django.db.models import F

# Create your views here.

@require_http_methods(['GET'])
def fib_nums(request):
    num = int(request.GET.get('num'))
    # print(type(num))
    # return HttpResponse("hello world")
    #checking if there is an entry in the db already for num
    db = FibonacciTable.objects.filter(fib_no=num)
    # print(db)
    if db:
        # return directly
        all_rows = FibonacciTable.objects.filter(fib_no__lte=num)
        data = [
            {'fib_no': row.fib_no, 'value': row.value}
            for row in db
        ]

        json_data = json.dumps(data)

        return JsonResponse(json_data, safe=False)
    
    else:
        #calculate the remaining fibnums
        second_row = FibonacciTable.objects.order_by('-fib_no').first()
        first_row = FibonacciTable.objects.exclude(fib_no=second_row.fib_no).order_by('-fib_no').first()
        fib = second_row.fib_no
        second = second_row.value
        first = first_row.value

        while fib<num: 
            fib += 1
            temp = second+first
            new_fib_row = FibonacciTable(fib_no=fib, value=temp)
            new_fib_row.save()
            first, second = second, temp
        

        # now I have required fib nos in db retrieve them and return
        db = FibonacciTable.objects.filter(fib_no__lte=num)
        data = [
            {'fib_no': row.fib_no, 'value': row.value}
            for row in db
        ]

        json_data = json.dumps(data)

        return JsonResponse(json_data, safe=False)
