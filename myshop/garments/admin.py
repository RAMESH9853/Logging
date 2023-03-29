from django.contrib import admin

# Register your models here.
from garments.models import FormalShirt

# "do" for adimin shows

class FormalShirtAdmin(admin.ModelAdmin):
    list_display=('name','photo','desc','price','stock','available','created','updated')


# Register your models here.
admin.site.register(FormalShirt,FormalShirtAdmin)
