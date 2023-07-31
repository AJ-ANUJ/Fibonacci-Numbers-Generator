from django.db import models

# Create your models here.

class FibonacciTable(models.Model):

    fib_no = models.BigIntegerField();
    value = models.BigIntegerField();

    def __str__(self):
        return f'{fib_no} fibonaccti number is {value}.'
