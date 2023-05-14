from django.contrib import admin

from glasses.models import Frame, Lens, LensColor, Material, MaterialColor

admin.site.register(Frame)
admin.site.register(Lens)
admin.site.register(LensColor)
admin.site.register(Material)
admin.site.register(MaterialColor)
