from django.db import models


class Schedule(models.Model):
    class DayChoice(models.TextChoices):
        MONDAY = "Понеділок", "Понеділок"
        TUESDAY = "Вівторок", "Вівторок"
        WEDNESDAY = "Середа", "Середа"
        THURSDAY = "Четвер", "Четвер"
        FRIDAY = "П'ятниця", "П'ятниця"

    group = models.ForeignKey("Group", related_name="groups_schedule", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", related_name="subjects_schedule", on_delete=models.CASCADE)
    day = models.CharField(max_length=15, choices=DayChoice.choices)
    audience = models.CharField(max_length=10)
    time = models.TimeField()
    number_subject = models.IntegerField()
    

 
    def __str__(self):
        return f"{self.group.name} - {self.day}"


class Replacement(models.Model):
    old_subject = models.ForeignKey("Subject", related_name="old_subject", on_delete=models.CASCADE)
    new_subject = models.ForeignKey("Subject", related_name="new_subject", on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Replacement on {self.date}"