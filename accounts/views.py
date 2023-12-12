from django.urls import reverse_lazy
from django.views import generic
from .forms import StyledUserCreationForm  # Import your custom form

class SignUpView(generic.CreateView):
    form_class = StyledUserCreationForm  # Use the custom form
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
