from django.db import models
from django.conf import settings


class Room(models.Model):
    number = models.CharField(max_length = 63)
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Room - №{self.number}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = "bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "bookings")

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Booked - {self.room} - by {self.user}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-end_time", "room"]
