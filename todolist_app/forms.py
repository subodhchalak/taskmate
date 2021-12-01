from django import forms

from todolist_app.models import TaskList

class TaskListForm(forms.ModelForm):
    class Meta:
        model=TaskList
        fields=['task', 'done']