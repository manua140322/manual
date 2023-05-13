from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput, CheckboxInput
from .models import Category, Teststask, Question, Decision
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title',]
        widgets = {
            'title': TextInput(attrs={"size":"50"}),            
        }        

class TeststaskForm(forms.ModelForm):
    class Meta:
        model = Teststask
        fields = ['category', 'title', 'details', 'minutes', 'limit']
        widgets = {
            'category': forms.Select(attrs={'class': 'chosen'}),
            'title': TextInput(attrs={"size":"50"}),
            'details': Textarea(attrs={'cols': 50, 'rows': 5}),            
            'minutes': NumberInput(attrs={"size":"10", "min":1}),
            'limit': NumberInput(attrs={"size":"10", "min":10, "max":100}),            
        }
        labels = {
            'category': _('category'),            
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'photo', 'reply1', 'ok1', 'reply2', 'ok2', 'reply3', 'ok3', 'reply4', 'ok4', 'reply5', 'ok5']
        widgets = {
            'question': Textarea(attrs={'cols': 60, 'rows': 6}),
            'reply1': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok1' : CheckboxInput(),
            'reply2': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok2' : CheckboxInput(),
            'reply3': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok3' : CheckboxInput(),
            'reply4': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok4' : CheckboxInput(),
            'reply5': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok5' : CheckboxInput(),
        }
        labels = {
            'teststask': _('teststask'),            
        }

class DecisionForm(forms.ModelForm):
    class Meta:
        model = Decision
        fields = ['user', 'title', 'solution', 'rating']
        widgets = {
            'user': forms.Select(attrs={'class': 'chosen', "disabled": "true"}),
            'title': TextInput(attrs={"size":"100", "readonly": "readonly"}),
            'solution': Textarea(attrs={'cols': 60, 'rows': 6, "readonly": "readonly"}),
            'rating': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        
# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
