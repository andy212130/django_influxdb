from django.contrib import admin
from .models import Post,upload_file
#import .models
# Register your models here.

#class Postadmin(admin.ModelAdmin):
#	list_display=('title','body','pub_date')

admin.site.register(Post)
admin.site.register(upload_file)
