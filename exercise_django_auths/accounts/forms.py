from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    ALLOWED_DOMAINS = ['softuni.com', 'yahoo.com']

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.split('@')[1] not in self.ALLOWED_DOMAINS:
            raise ValidationError('Domain not allowed')
        return email
