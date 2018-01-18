from django.db import models

from teacher.models import Department


class Sem(models.Model):
    sem = models.SmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sem) + ',' + str(self.department.department_initials)


class Sec(models.Model):
    shift_1 = 0
    shift_2 = 1
    Type_shift = (
        (shift_1, "I"),
        (shift_2, "II")
    )
    sem = models.ForeignKey(Sem, on_delete=models.CASCADE)
    Section = models.CharField(max_length=10)
    shift = models.SmallIntegerField(choices=Type_shift, default=shift_1)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sem.sem) + ',' + str(self.sem.department.department_initials) + ',' + str(self.Section)
