from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo  # bring in our model
from .models import Contact

# Register your models here.
admin.site.register(Todo)
admin.site.register(Contact)
