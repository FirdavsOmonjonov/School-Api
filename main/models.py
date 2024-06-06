from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name + " " + self.l_name

class Teacher(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    price = models.IntegerField()
    class_name = models.ManyToManyField(Class)

    def __str__(self):
        return self.f_name + " " + self.l_name

