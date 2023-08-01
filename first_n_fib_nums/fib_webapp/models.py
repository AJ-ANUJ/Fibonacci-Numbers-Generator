from django.db import models

# Create your models here.

class FibonacciTable(models.Model):

    fib_no = models.BigIntegerField(db_index=True);
    value = models.BigIntegerField();

    @classmethod
    def add_default_rows(cls):
        rows = [
            FibonacciTable(fib_no=1, value=0),
            FibonacciTable(fib_no=2, value=1)
        ]

        FibonacciTable.objects.bulk_create(rows)

    def __str__(self):
        return f'{self.fib_no} fibonacci number is {self.value}.'
