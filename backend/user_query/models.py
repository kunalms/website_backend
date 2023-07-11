from django.db import models


class UserQuery(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    is_fresher = models.BooleanField(default=True)
    years_of_experience = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

