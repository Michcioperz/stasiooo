# encoding: utf-8
from django import forms
from tinymce import widgets
import datetime


class OwnEntryForm(forms.Form):
    title = forms.CharField(label="Tytuł", max_length=255)
    content = forms.CharField(label="Treść",
                              widget=widgets.TinyMCE(attrs={"cols": 80,
                                                            "rows": 30}))
    publication_date = forms.DateTimeField(label="Czas publikacji",
                                           initial=datetime.datetime.now())
