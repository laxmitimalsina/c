from django.shortcuts import redirect, render
from django.contrib import messages
from .models import (
    Profile,
    Project,
    Education,
    Skill,
    Experience,
    CustomSection,
)


from .forms import (
    CustomSectionForm,
    ExperienceForm,
    ProfileForm,
    ProjectForm,
    EducationForm,
    SkillForm,
)


# Create your views here.


def personal_detail_page(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = ProfileForm(instance=profile)

    return render(request, "portfolio/personal_detail.html", {"form": form})


def project_form_page(request):
    project = Project.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = ProjectForm(instance=project)

    return render(request, "portfolio/projects.html", {"form": form})


def education_form_page(request):
    education = Education.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = EducationForm(instance=education)

    return render(request, "portfolio/education.html", {"form": form})


def experience_form_page(request):
    experience = Experience.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = ExperienceForm(instance=experience)

    return render(request, "portfolio/experience.html", {"form": form})


def skill_form_page(request):
    skill = Skill.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = SkillForm(instance=skill)
    return render(request, "portfolio/skills.html", {"form": form})


def add_section_page(request):
    custom_section = CustomSection.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = CustomSectionForm(request.POST, instance=custom_section)
        post = form.save(commit=False)
        post.user = request.user
        post.save()
    else:
        form = CustomSection(instance=custom_section)

    return render(request, "portfolio/add_section.html")
