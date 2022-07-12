from django.forms import ModelForm

from .models import Citizen


class CitizenForm(ModelForm):
    class Meta:
        model = Citizen
        fields = '__all__'
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относится пост',
        }
