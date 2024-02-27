from django.contrib import admin
from .models import Hobbies
from .models import Portfolio
from .models import Contacts

# Register your models here.


admin.site.register(Hobbies)
admin.site.register(Portfolio)
admin.site.register(Contacts)
