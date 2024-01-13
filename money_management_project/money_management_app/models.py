from django.db import models

class Transaction(models.Model):
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])

    def __str__(self):
        return f"{self.amount} - {self.category} ({self.type})"
