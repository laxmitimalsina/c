from django.db.models.base import Model
from django.forms.models import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
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
    # EducationEditFormset = modelformset_factory(
    #     Education, form=EducationForm, extra=2
    # )
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
            print("frm is invalid")
            print(formset.errors)
    else:
        formset = EducationEditFormset(instance=request.user)

    context = {"formset": formset}

    # if formset.is_valid():
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         instance.user = request.user
    #         instance.save()
    # context = {
    #     "formset": formset,
    # }

    return render(request, "portfolio/education.html", context)

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
    ExperienceFormset = modelformset_factory(
        Profile, form=ExperienceForm, extra=2
    )
    experience = Experience.objects.filter(user=request.user)
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


def profile_update(request):

    ProfileEditFormset = modelformset_factory(
        Profile, form=ProfileForm, extra=2
    )

    formset = ProfileEditFormset(request.POST)
    if formset.is_valid():
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
    context = {
        "formset": formset,
    }

    return render(request, "profile_info_edit.html", context)


# class CvEditView(SingleObjectMixin, FormView):
#     model = Profile
#     template_name = "profile_info_edit.html"

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Profile.objects.all())
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Profile.objects.all())
#         return super().post(request, *args, **kwargs)

#     def get_form(self, form_class=None):
#         return ProfileInfoFormset(**self.get_form_kwargs(), instance=object)

#     def from_valid(self, form):
#         form.save()
#         messages.add_message(
#             self.request, messages.SUCCESS, "Changes were saved."
#         )

#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse("user_details")


# def profile_update(request):

#     ProfileEditFormset = modelformset_factory(
#         Profile, form=ProfileForm, extra=1
#     )
#     formset = ProfileEditFormset(request.POST or None)
#     if formset.is_valid():
#         instances = formset.save(commit=False)
#         for instance in instances:
#             instance.user = request.user
#             instance.save()
#     context = {
#         "formset": formset,
#     }

#     return render(request, "profile_info_edit.html", context)
