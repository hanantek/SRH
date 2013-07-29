from django.views.generic import TemplateView
from cv.models import PersonalInfo

class HomeView(TemplateView):
	template_name = "reports/index.html"

class Profile(TemplateView):
	template_name = "reports/perfil.html"

	def get_context_data(self, **kwargs):
		context = super(Profile, self).get_context_data(**kwargs)
		user_id = self.kwargs.get('id', None)

		context['personal'] = PersonalInfo.objects.get(user=user_id)
		return context
