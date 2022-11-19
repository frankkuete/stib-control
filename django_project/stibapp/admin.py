# Register your models here.
from django.contrib import admin

# Register your models here.
from stibapp.models import User, Admin, Station, Line, StationOrder, Control


class UserAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'isadmin')


admin.site.register(User, UserAdmin, )


class AdminAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'code')


admin.site.register(Admin, AdminAdmin)


class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'locality')


admin.site.register(Station, StationAdmin)


class LineAdmin(admin.ModelAdmin):
    list_display = ('direction', 'number', 'category')


admin.site.register(Line, LineAdmin)


class LineOrderAdmin(admin.ModelAdmin):
    list_display = ('line', 'station', 'order')


admin.site.register(StationOrder, LineOrderAdmin)


class ControlAdmin(admin.ModelAdmin):
    list_display = ('line', 'station')


admin.site.register(Control, ControlAdmin)
