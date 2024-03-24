from django.contrib import admin
from django.utils.html import mark_safe
from courses.models import Category, Course, Lesson, User, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'name', 'created_date']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='200' height='140' src='/static/{instance.image.name}'/>")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


# Register your models here.
admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Lesson)
admin.site.register(User)
admin.site.register(Tag)


