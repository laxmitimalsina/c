from django.db.models.base import Model
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.forms import fields, inlineformset_factory
from django.contrib.auth.models import User
from .models import (
    Profile,
    Project,
    Education,
    Skill,
    Experience,
    CustomSection,
)


# Create your views here.


def personal_detail_page(request):
    ProfileEditFormset = inlineformset_factory(
        User,
        Profile,
        fields=[
            "id",
            "photo",
            "name",
            "email",
            "phone_number",
            "website",
            "address1",
            "address2",
            "zip_code",
            "country",
            "city",
        ],
    )
    if request.method == "POST":
        formset = ProfileEditFormset(request.POST, request.FILES, instance=request.user)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            print(formset.errors)

    else:
        formset = ProfileEditFormset(instance=request.user)
    return render(request, "portfolio/personal_detail.html", {"formset": formset})


def project_form_page(request):
    ProjectEditFormset = inlineformset_factory(
        User,
        Project,
        fields=(
            "id",
            "title",
            "start_date",
            "end_date",
            "description",
            "image",
            "url",
        ),
    )

    if request.method == "POST":
        formset = ProjectEditFormset(request.POST, request.FILES, instance=request.user)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            print(formset.errors)

    else:
        formset = ProjectEditFormset(instance=request.user)

    return render(request, "portfolio/projects.html", {"formset": formset})


def education_form_page(request):
    EducationEditFormset = inlineformset_factory(
        User,
        Education,
        fields=("id", "title", "educational_institute", "city", "country"),
    )
    if request.method == "POST":
        formset = EducationEditFormset(request.POST, instance=request.user)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            print(formset.errors)

    else:
        formset = EducationEditFormset(instance=request.user)

    context = {"formset": formset}

    return render(request, "portfolio/education.html", context)


def experience_form_page(request):
    ExperienceEditFormset = inlineformset_factory(
        User,
        Experience,
        fields=("id", "title", "start_date", "end_date", "description"),
        extra=1,
    )
    if request.method == "POST":
        formset = ExperienceEditFormset(request.POST, instance=request.user)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            print(formset.errors)

    else:
        formset = ExperienceEditFormset(instance=request.user)

    return render(request, "portfolio/experience.html", {"formset": formset})


def skill_form_page(request):
    SkillEditFormset = inlineformset_factory(
        User, Skill, fields=("id", "title", "description", "add_skills")
    )
    if request.method == "POST":
        formset = SkillEditFormset(request.POST, instance=request.user)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            print(formset.errors)

    else:
        formset = SkillEditFormset(instance=request.user)
    return render(request, "portfolio/skills.html", {"formset": formset})


def add_section_page(request):
    CustomEditFormset = inlineformset_factory(
        User,
        CustomSection,
        fields=(
            "title",
            "image",
            "url",
            "start_date",
            "end_date",
            "description",
        ),
    )

    if request.method == "POST":
        formset = CustomEditFormset(request.POST, instance=request.user)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            print(formset.errors)

    else:
        formset = CustomEditFormset(instance=request.user)

    return render(request, "portfolio/add_section.html", {"formset": formset})
