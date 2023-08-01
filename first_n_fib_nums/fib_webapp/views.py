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
    
    #checking if there is an entry in the db already for num
    db = FibonacciTable.objects.filter(fib_no=num)
    # print(db)
    if db:
        # return directly
        all_rows = FibonacciTable.objects.filter(fib_no__lte=num)
        data = [
            {'fib_no': row.fib_no, 'value': row.value}
            for row in all_rows
        ]

        # json_data = json.dumps(data)

        return JsonResponse(data, safe=False)
    
    else:
        '''
            first check if db table is empty
            if yes enter the first 2 entries
        '''
        if FibonacciTable.objects.all().count()==0:
            first_entry = FibonacciTable(fib_no=1, value='0')
            first_entry.save()
            second_entry = FibonacciTable(fib_no=2, value='1')
            second_entry.save()

        #calculate the remaining fibnums
        second_row = FibonacciTable.objects.order_by('-fib_no').first()
        first_row = FibonacciTable.objects.exclude(fib_no=second_row.fib_no).order_by('-fib_no').first()
        fib = second_row.fib_no
        # second = second_row.value
        # first = first_row.value
        second = int(second_row.value)
        first = int(first_row.value)

        while fib<num: 
            fib += 1
            temp = second+first
            new_fib_row = FibonacciTable(fib_no=fib, value=str(temp))
            new_fib_row.save()
            first, second = second, temp
        

        # now I have required fib nos in db retrieve them and return
        db = FibonacciTable.objects.filter(fib_no__lte=num)
        data = [
            {'fib_no': row.fib_no, 'value': row.value}
            for row in db
        ]

        # json_data = json.dumps(data)

        return JsonResponse(data, safe=False)
