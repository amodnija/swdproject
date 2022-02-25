from django.db import models


APPROVAL_CHOICES = (
    ('Y', 'Approved'),
    ('N', 'Not Approved'),
)


class Leave(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=60)
    leavestart = models.DateField('Start date of leave (mm/dd/yy)')
    leaveend = models.DateField('End date of leave (mm/dd/yy)')
    reason = models.TextField()
    availibilty = models.CharField(max_length=20)
    approval = models.CharField(max_length=40, choices=APPROVAL_CHOICES)
    submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
