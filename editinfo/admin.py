from django.contrib import admin
# admin.site.register(DeveloperRepository)
# Register your models here.
from editinfo.models import Developer,Technology, Domain, Q_A, Blog, Project
admin.site.register(Developer)
# Register your models here.
admin.site.register(Technology)
admin.site.register(Domain)
# Register your models here.
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Q_A)