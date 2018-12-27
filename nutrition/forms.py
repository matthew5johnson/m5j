from django import forms
from nutrition.models import Recipe, Item, CoreData


class ScrapeForm(forms.Form):
	name = forms.CharField()
	state = forms.CharField()
	data_source = forms.CharField()
	notes = forms.CharField()
	servingsize = forms.FloatField()
	servingsizeunits = forms.CharField()

class ManualForm(forms.ModelForm):

	class Meta:
		model = CoreData
		fields = '__all__'

class AddForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = 'name', 'recipe', 'grams', 'units', 'conversion', 'cost_per_100_cal', 'cost_per_gram', 'monday_1', 'monday_2', 'monday_3', 'tuesday_1', 'tuesday_2', 'tuesday_3', 'wednesday_1', 'wednesday_2', 'wednesday_3', 'thursday_1', 'thursday_2', 'thursday_3', 'friday_1', 'friday_2', 'friday_3', 'saturday_1', 'saturday_2', 'saturday_3', 'sunday_1', 'sunday_2', 'sunday_3'

class RecipeForm(forms.ModelForm):

	class Meta:
		model = Recipe 
		fields = '__all__'
