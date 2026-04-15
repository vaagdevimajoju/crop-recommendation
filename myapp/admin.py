from django.contrib import admin
from .models import ContactMessage
# Register your models here.
from .models import Crop

admin.site.register(Crop)


admin.site.register(ContactMessage)