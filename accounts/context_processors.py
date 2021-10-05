from .models import User

from company.models import CompanyJobs


def users_count(request):

    context = {
        "users_count": CompanyJobs.objects.all()
    }
    return context
