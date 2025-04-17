from django.contrib import admin
from .models import Details
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','qualification','gender','age','dob','address','mock_rating',]
    # list_display_links=['st_id']
admin.site.register(Details,StudentAdmin)


