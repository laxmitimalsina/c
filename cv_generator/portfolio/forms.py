from .models import (
    Profile,
    Project,
    Skill,
    Education,
    CustomSection,
    Experience,
)
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["user"]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ["user"]


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["user"]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ["user"]


class CustomSectionForm(forms.ModelForm):
    class Meta:
        model = CustomSection
        exclude = ["user"]
