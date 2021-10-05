import csv

import itertools
import os
from .models import Company, CompanyJobs
from django.conf import  settings




def get_jobs_filename(country):
    return os.path.join(settings.JOBS_DATA_LOCATION,country.lower(),"fake_job_postings.csv")


def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_jobs_from_file(filename):
    JoBs=load_file(filename)
  
    # print(occupations)

    for JoB in JoBs:
        CompanyJobs.objects.create(
            job_id=JoB.get("job_id"),
            title=JoB.get("title"),
            location=JoB.get("location"),
            department=JoB.get("department"),
            salary_range=JoB.get("salary_range"),
            company_profile=JoB.get("company_profile"),
            description=JoB.get("description"),
            requirements=JoB.get("requirements"),
            benefits=JoB.get("benefits"),
            telecommuting=JoB.get("telecommuting"),
            has_company_logo=JoB.get("has_company_logo"),
            has_questions=JoB.get("has_questions"),
            employment_type=JoB.get("employment_type"),
            required_experience=JoB.get("required_experience"),
            required_education=JoB.get("required_education"),
            industry=JoB.get("industry"),
            functions=JoB.get("functions"),
            fraudulent=JoB.get("fraudulent"),
            
            

        )



