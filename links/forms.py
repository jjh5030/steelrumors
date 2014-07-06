from .models import Link, Vote
from django import forms

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		exclude = ("submitter", "rank_score",)


class VoteForm(forms.ModelForm):
	class Meta:
		model = Vote