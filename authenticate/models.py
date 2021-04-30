# from django.db import models
# #from django.contrib.postgres.fields import ArrayField
#
# class Domain(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
#
# class Technology(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
#
#
# class DeveloperRepository(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
#     domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
#     project = models.CharField(max_length=200)
#     # project = ArrayField(models.CharField(max_length=200))
#     def __str__(self):
#         return self.name
