from django.contrib import admin
from .models import Profile, Education, ChildInfo
from .forms import ProfileForm


class ChildInfoInline(admin.StackedInline):
    model = ChildInfo
    extra = 1

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ('user', 'image', 'displayname', 'info')
    search_fields = ('displayname',)
    list_filter = ('user', 'displayname')
    inlines = [ChildInfoInline, EducationInline]

admin.site.register(Education)
admin.site.register(ChildInfo)