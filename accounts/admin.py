from django.contrib import admin

from .models import SECRETARY, SUPERVISOR,  User,Role

from company.models import Company, Job,Review

class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "date_joined",
        "last_login",
        # "is_information_confirmed",
    )
    list_filter = ("date_joined", "last_login", )


admin.site.register(User)

admin.site.register(SUPERVISOR)
admin.site.register(SECRETARY)
admin.site.register(Role)
admin.site.register(Company)
admin.site.register(Job)

