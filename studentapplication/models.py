from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.department}"
    


class StudentApplication(models.Model):
    first_name = models.CharField(max_length=50)
    secound_name = models.CharField(max_length=50)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    shirt_size = models.CharField(max_length=50, choices=SHIRT_SIZES, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.first_name} {self.secound_name}"

class CreateUserProfile(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField("Student Name", max_length=50)

    def __str__(self):
        return f"{self.full_name}"
