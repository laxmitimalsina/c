from django.urls import path

from .views import (
    personal_detail_page,
    project_form_page,
    education_form_page,
    experience_form_page,
    skill_form_page,
)


urlpatterns = [
    path("basic-info", personal_detail_page, name="basic"),
    path("project-info", project_form_page, name="project"),
    path("education-info", education_form_page, name="education"),
    path("experience-info", experience_form_page, name="experience"),
    path("skill-info", skill_form_page, name="skill"),
]
