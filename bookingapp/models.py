from django.db import models

# Create your models here.
class Booking(models.Model):

    DINING = [
        ("B", "Baan Tao"),
        ("C" , "Café 88"),
        ("T","The Terrace Bar"),
        ("W","The Waterfall Lounge"),
        ("R","In-Room Dining Services"),
    ]

    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    checkin = models.DateField()
    checkout = models.DateField()
    roomtype = models.CharField(max_length=1, choices = DINING)


    def __str__(self):
        return self.name
