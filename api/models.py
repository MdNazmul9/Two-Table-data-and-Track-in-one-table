from django.db import models

# Create your models here.
class Order(models.Model):
    sender_name = models.CharField(max_length=200)
    amt = models.IntegerField()
    receiver_name = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.sender_name

class Commission(models.Model):
    sender_name = models.CharField(max_length=200)
    amt = models.IntegerField()
    date = models.DateTimeField()
    receiver_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sender_name

class Reference(models.Model):
    sender_name = models.CharField(max_length=200)
    amt = models.IntegerField()
    date = models.DateTimeField()
    receiver_name = models.CharField(max_length=200)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE, related_name='odr')
    commission = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE, related_name='commit')

    def __str__(self):
        return self.receiver_name