from django.db import models

from semclass.models import Sec
from teacher.models import Subject,Department


class ClassRoom(models.Model):
    Block_A = 0
    Block_B = 1
    Block_C = 2
    Block_D = 3
    Type_Block = (
        (Block_A, 'A'),
        (Block_B, 'B'),
        (Block_C, 'C'),
        (Block_D, 'D')
    )
    block = models.SmallIntegerField(choices=Type_Block, default=Block_A)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    room_no = models.CharField(max_length=10)
    sec1 = models.ForeignKey(Sec, on_delete=models.CASCADE, related_name='sec1', blank=True, null=True)
    sec2 = models.ForeignKey(Sec, on_delete=models.CASCADE, related_name='sec2', blank=True, null=True)
    alt_name = models.CharField(max_length=10, default='LH1', null=True)

    def __str__(self):
        return self.room_no + ',' + str(self.get_block_display()) + ','


class Lab(models.Model):
    Block_A = 0
    Block_B = 1
    Block_C = 2
    Block_D = 3
    Type_Block = (
        (Block_A, 'A'),
        (Block_B, 'B'),
        (Block_C, 'C'),
        (Block_D, 'D')
    )
    block = models.SmallIntegerField(choices=Type_Block, default=Block_A)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept')
    lab_no = models.CharField(max_length=10)
    alt_name = models.CharField(max_length=10, default='cp1', null=True)
    subject1 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub1')
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub2', blank=True, null=True)
    subject3 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub3', blank=True, null=True)
    subject4 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub4', blank=True, null=True)

    def __str__(self):
        return self.lab_no + '(' + str(self.get_block_display()) + ')'
