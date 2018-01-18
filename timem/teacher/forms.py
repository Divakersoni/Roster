from django import forms
from .models import Department, Teacher, Subject
from location.models import ClassRoom, Lab
from semclass.models import Sec, Sem
from django.core.validators import MinLengthValidator


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ()
        widgets = {
            'block': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
            'department_name': forms.TextInput(attrs={'placeholder': 'Computer Science','class': 'form-control'}),
            'department_initials': forms.TextInput(attrs={'placeholder': 'CSE','class': 'form-control'}),
        }
class SubjectForm(forms.ModelForm):
   class Meta:
        model = Subject
        exclude = ()
        widgets = {
            'type_subject': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
            'subject_name': forms.TextInput(attrs={'placeholder': 'Data Structure and algorithms','class': 'form-control'}),
            'subject_initials': forms.TextInput(attrs={'placeholder': 'DSA','class': 'form-control'}),
            'semester': forms.TextInput(attrs={'placeholder': '','class': 'form-control'}),
            'subject_code': forms.TextInput(attrs={'placeholder': '7CS','class': 'form-control'}),
            'department': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
            'teaching_hours_per_week': forms.TextInput(attrs={'placeholder': '','class': 'form-control'}),
            'teaching_hours_a_day': forms.TextInput(attrs={'placeholder': '','class': 'form-control'}),
        }
class SecForm(forms.ModelForm):
    class Meta:
        model = Sec
        exclude = ()
        widgets = {
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'Section': forms.TextInput(attrs={'placeholder': 'A','class': 'form-control'}),
            'sem': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
            'department': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
        }
class SemForm(forms.ModelForm):
    class Meta:
        model = Sem
        exclude = ()
        widgets = {
            'sem': forms.TextInput(attrs={'placeholder': '7','class': 'form-control'}),
            'department': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
        }
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ()
        widgets = {
            'teacher_name': forms.TextInput(attrs={'placeholder': '','class': 'form-control'}),
            'designation': forms.TextInput(attrs={'placeholder': '','class': 'form-control'}),
            'teacher_initials': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'years_of_experience': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'department': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'teaching_hours_per_week': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'total_teaching_hours_a_day': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'shift': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject1': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'teaching_hours_a_day_subject1': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject2': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'teaching_hours_a_day_subject2': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject3': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'teaching_hours_a_day_subject3': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject4': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'teaching_hours_a_day_subject4': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),

        }
class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        exclude = ()
        widgets = {
            'dept': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
            'block': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'sec1': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'sec2': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'room_no': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'alt_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }
class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        exclude = ()
        widgets = {
            'dept': forms.Select(attrs={'placeholder': '','class': 'form-control'}),
            'block': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject1': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject2': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject3': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'subject4': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'lab_no': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'alt_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }

