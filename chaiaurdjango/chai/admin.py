from django.contrib import admin

from .models import ChaiVarity,ChaiReveiw,Stores,Certificate
# Register your models here.
class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReveiw
    extra = 2;
    
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ChaiReviewInLine]
    
class StoresAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_variteies',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')
    
admin.site.register(ChaiVarity,ChaiVarityAdmin)
admin.site.register(Stores,StoresAdmin)
admin.site.register(Certificate,ChaiCertificateAdmin)