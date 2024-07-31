from django.db import models


class ClassModel(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'


class StudentModel(models.Model):
    photo = models.ImageField(upload_to='profile_photos')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    class_number = models.ForeignKey(
        ClassModel,
        on_delete=models.PROTECT,
        related_name='students'
    )
    brilliant_coin = models.PositiveIntegerField(default=0)
    ruby_coin = models.PositiveIntegerField(default=0)
    gold_coin = models.PositiveIntegerField(default=0)
    silver_coin = models.PositiveIntegerField(default=0)
    bronze_coin = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.surname} {self.class_number.number}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
