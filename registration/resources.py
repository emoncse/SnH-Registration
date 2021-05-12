from import_export import resources
from .models import Recruitment


class RecruitmentResources(resources.ModelResource):
    class Meta:
        model = Recruitment

