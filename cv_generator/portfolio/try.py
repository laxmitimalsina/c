from docxtpl import DocxTemplate
import jinja2
import os

document = DocxTemplate("Resume_simple.docx")
context = {
    "name": "Laxmi Timalsina",
    "haus_nr": 2,
    "street": "George ST",
    "city": "Mortdale",
    "postcode": 12345,
    "skill_description": """This is short description for skill.\n this is a short paragraph for skill description. Ich habe hunger""",
    "experiences": [
        {
            "experience_month": "June",
            "experience_year": 2012,
            "working_status": "June 2013",
            "company_name": "Starbucks",
            "location_name": "Bondi Junction",
            "job_title": "Supervisor",
            "experience_description": "Ich bin Laxmi.Ich liebe Tanzen.Ich hobby ist arbiten",
        },
        {
            "experience_month": "January",
            "experience_year": 2014,
            "working_status": "Present",
            "company_name": "Microsoft",
            "location_name": "Bondi",
            "job_title": "Software Developer",
        },
    ],
}
document.render(context)
document.save("new_file.docx")
