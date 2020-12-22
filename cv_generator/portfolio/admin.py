from django.contrib import admin
from django.db import models
from .models import (
    Education,
    Language,
    Project,
    Profile,
    Skill,
)
from ckeditor.widgets import CKEditorWidget


class EducationAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "institute",
    ]
    search_fields = ["title"]
    list_per_page = 30
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.register(Education, EducationAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "user",
    ]
    search_fields = ["name"]
    list_per_page = 30
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.register(Skill, SkillAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "user",
    ]
    search_fields = ["title"]
    list_per_page = 30
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.register(Project, ProjectAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "user",
    ]
    search_fields = ["user"]
    list_per_page = 30
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.register(Language, LanguageAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "user",
    ]
    search_fields = ["name"]
    list_per_page = 30
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.register(Profile, ProfileAdmin)
