from . models import Task,category
from django import forms


class addTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs= {}, format='%d-%m-%Y'),
            # 'time': forms.TimeField(attrs={'type':'time'})
        }
        
        def __init__(self, *args, **kwargs):
            super(addTask, self).__init__(*args, **kwargs)
            default_category = category.objects.get(name='work')  # Replace 'Default' with the actual category name
            default_category_id = default_category.id

        # Set the default category for the form
            self.fields['category'].initial = default_category_id

class addCategory(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name']



