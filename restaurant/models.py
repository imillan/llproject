from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self) -> str:
        return f"Reservation for:{self.name},{self.number_of_guests} guests on {self.booking_date}"


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return f'Menu item name:{self.title}, price: {str(self.price)}'
