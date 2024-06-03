from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("User", limit_choices_to={"role": "Teacher"}, on_delete=models.CASCADE)

    def __str__(self):
        return self.name