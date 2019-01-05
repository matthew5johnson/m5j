from .forms import ScrapeForm, AddForm, RecipeForm, ManualForm
from django.shortcuts import render, get_object_or_404, redirect
from nutrition.modules.scraping import Scrape
from nutrition.modules.load_scraping import Upload
from nutrition.modules.item_logic import Complete
from nutrition.models import CoreData, Item, Recipe

# Create your views here.
def nutrition_homepage(request):
	return render(request, 'nutrition/nutrition_homepage.html')

def day(request):
	## All dictionary keys are as they appear in the model
	DRI = {
		'VitaminAmcgRetinolActivityEquivalentsRAE': 900,
		'VitaminC': 90,
		'Calcium': 1300,
		'Iron': 18,
		'VitaminDmcg': 20,
		'VitaminEmg': 15,
		'VitaminK': 120,
		'VitaminB1': 1.2,
		'VitaminB2': 1.3,
		'VitaminB3': 16,
		'VitaminB6': 1.7,
		'Folate': 400,
		'VitaminB12': 2.4,
		'Biotin': 30,
		'PantothenicAcid': 5,
		'Phosphorus': 1250,
		'Iodine': 150,
		'Magnesium': 420,
		'Zinc': 11,
		'Selenium': 55,
		'Copper': 0.9,
		'Manganese': 2.3,
		'Chromium': 35,
		'Molybdenum': 45,
		'Chloride': 2300,
		'Potassium': 4700,
		'Choline': 550,
	}

	breakfast = Item.objects.filter(monday_1=True)
	supper = Item.objects.filter(monday_3=True)

	# use querysets to sum and average columns.
	# new DRI model, and make the footer the total/DRI to get % of needed
	# breakfast_footer_options = ['Calories', 'Protein']
	calculated_footer = {
		'Item': '',
		'Grams': '',
		'Cost': 'Cost',
		'cost_per_100_cal': 'average',
		'Calories': 'sum',
		'Protein': 'sum',
		'F': 'F',
		'Potassium': 'sum',
	}

	# # make a dictionary of the values from the double for loop. 
	# # then do another for loop through the list of footers to get the value of each spot in the dict
	
	for keys in calculated_footer:
		if calculated_footer[keys] == 'sum':
			answer_sum = 0
			for m in range(0,len(breakfast)):
				answer_sum = answer_sum + breakfast.values()[m][keys]
			if keys in DRI:
				calculated_footer[keys] = '%s (%s)' % (round(answer_sum, 1), DRI[keys])				
			else:
				calculated_footer[keys] = round(answer_sum, 1)
		elif calculated_footer[keys] == 'average':
			grams_sum = 0
			weighted_numerator = 0
			for m in range(0,len(breakfast)):
				weighted_numerator = weighted_numerator + (breakfast.values()[m]['grams'] * breakfast.values()[m][keys])
				grams_sum = grams_sum + breakfast.values()[m]['grams']
			answer_weighted_average =  weighted_numerator / grams_sum	
			calculated_footer[keys] = round(answer_weighted_average, 2)
		else:
			print('none')

	### A list of footers as they appear as keys in the calculated_footers dict
	footers = ['Item', 'Grams', 'Cost', 'cost_per_100_cal', 'Calories', 'Protein', 'F', 'Potassium']
	final_footers = []
	for title in footers:
		for keys in calculated_footer:
			if keys == title:
				final_footers.append(calculated_footer[keys])
	
	return render(request, 'nutrition/day.html', {'breakfast': breakfast, 'supper': supper, 'final_footers': final_footers})

def week(request):
	display_to_weekmodel = {
		'Recipe': 'recipe',
		'Item': 'name',
		'Grams': 'weekly_grams',
		'Cost': 'weekly_cost',
		'$/100cal': 'cost_per_100_cal',
		'$/gP': 'cost_per_g_protein',
		'$/gFi': 'cost_per_g_fiber',
		'Protein': 'week_Protein',
		'Carbohydrates': 'week_Carbohydrates',
		'Fat': 'week_Fattotal',
		'Fiber': 'week_DietaryFiber',
		'Calories': 'week_Calories',
		'Starch': 'week_Starch',
		'Total Sugars': 'week_TotalSugars',
		'Monosaccharides': 'week_Monosaccharides',
		'Fructose': 'week_Fructose',
		'Glucose': 'week_Glucose',
		'Galactose': 'week_Galactose',
		'Disaccharides': 'week_Disaccharides',
		'Lactose': 'week_Lactose',
		'Maltose': 'week_Maltose',
		'Sucrose': 'week_Sucrose',
		'Soluble Fiber': 'week_SolubleFiber',
		'Insoluble Fiber': 'week_InsolubleFiber',
		'Other Carbohydrates': 'week_OtherCarbohydrates',
		'Monounsaturated Fat': 'week_MonounsaturatedFat',
		'Polyunsaturated Fat': 'week_PolyunsaturatedFat',
		'Saturated Fat': 'week_SaturatedFat',
		'Trans Fat': 'week_TransFat',
		'Cholesterol': 'week_Cholesterol',
		'Water': 'week_Water',
		'Vitamin B1': 'week_VitaminB1',
		'Vitamin B2': 'week_VitaminB2',
		'Vitamin B3': 'week_VitaminB3',
		'Vitamin B3 (Niacin Equivalents)': 'week_VitaminB3NiacinEquivalents',
		'Vitamin B6': 'week_VitaminB6',
		'Vitamin B12': 'week_VitaminB12',
		'Biotin': 'week_Biotin',
		'Choline': 'week_Choline',
		'Folate': 'week_Folate',
		'Folate (DFE)': 'week_FolateDFE',
		'Folate (food)': 'week_Folatefood',
		'Pantothenic Acid': 'week_PantothenicAcid',
		'Vitamin C': 'week_VitaminC',
		'Vitamin A International Units (IU)': 'week_VitaminAInternationalUnitsIU',
		'Vitamin A mcg Retinol Activity Equivalents (RAE)': 'week_VitaminAmcgRetinolActivityEquivalentsRAE',
		'Vitamin A mcg Retinol Equivalents (RE)': 'week_VitaminAmcgRetinolEquivalentsRE',
		'Retinol mcg Retinol Equivalents (RE)': 'week_RetinolmcgRetinolEquivalentsRE',
		'Carotenoid mcg Retinol Equivalents (RE)': 'week_CarotenoidmcgRetinolEquivalentsRE',
		'Alpha-Carotene': 'week_AlphaCarotene',
		'Beta-Carotene': 'week_BetaCarotene',
		'Beta-Carotene Equivalents': 'week_BetaCaroteneEquivalents',
		'Cryptoxanthin': 'week_Cryptoxanthin',
		'Lutein and Zeaxanthin': 'week_LuteinandZeaxanthin',
		'Lycopene': 'week_Lycopene',
		'Vitamin D International Units (IU)': 'week_VitaminDInternationalUnitsIU',
		'Vitamin D mcg': 'week_VitaminDmcg',
		'Vitamin E mg Alpha-Tocopherol Equivalents (ATE)': 'week_VitaminEmgAlphaTocopherolEquivalentsATE',
		'Vitamin E International Units (IU)': 'week_VitaminEInternationalUnitsIU',
		'Vitamin E mg': 'week_VitaminEmg',
		'Vitamin K': 'week_VitaminK',
		'Boron': 'week_Boron',
		'Calcium': 'week_Calcium',
		'Chloride': 'week_Chloride',
		'Chromium': 'week_Chromium',
		'Copper': 'week_Copper',
		'Fluoride': 'week_Fluoride',
		'Iodine': 'week_Iodine',
		'Iron': 'week_Iron',
		'Magnesium': 'week_Magnesium',
		'Manganese': 'week_Manganese',
		'Molybdenum': 'week_Molybdenum',
		'Phosphorus': 'week_Phosphorus',
		'Potassium': 'week_Potassium',
		'Selenium': 'week_Selenium',
		'Sodium': 'week_Sodium',
		'Zinc': 'week_Zinc',
		'Omega-3': 'week_Omega3FattyAcids',
		'Omega-6': 'week_Omega6FattyAcids',
		'14:1 Myristoleic': 'week_a141Myristoleic',
		'15:1 Pentadecenoic': 'week_a151Pentadecenoic',
		'16:1 Palmitol': 'week_a161Palmitol',
		'17:1 Heptadecenoic': 'week_a171Heptadecenoic',
		'18:1 Oleic': 'week_a181Oleic',
		'20:1 Eicosenoic': 'week_a201Eicosenoic',
		'22:1 Erucic': 'week_a221Erucic',
		'24:1 Nervonic': 'week_a241Nervonic',
		'18:2 Linoleic': 'week_a182Linoleic',
		'18:2 Conjugated Linoleic (CLA)': 'week_a182ConjugatedLinoleicCLA',
		'18:3 Linolenic': 'week_a183Linolenic',
		'18:4 Stearidonic': 'week_a184Stearidonic',
		'20:3 Eicosatrienoic': 'week_a203Eicosatrienoic',
		'20:4 Arachidonic': 'week_a204Arachidonic',
		'20:5 Eicosapentaenoic (EPA)': 'week_a205EicosapentaenoicEPA',
		'22:5 Docosapentaenoic (DPA)': 'week_a225DocosapentaenoicDPA',
		'22:6 Docosahexaenoic (DHA)': 'week_a226DocosahexaenoicDHA',
		'4:0 Butyric': 'week_a40Butyric',
		'6:0 Caproic': 'week_a60Caproic',
		'8:0 Caprylic': 'week_a80Caprylic',
		'10:0 Capric': 'week_a100Capric',
		'12:0 Lauric': 'week_a120Lauric',
		'14:0 Myristic': 'week_a140Myristic',
		'15:0 Pentadecanoic': 'week_a150Pentadecanoic',
		'16:0 Palmitic': 'week_a160Palmitic',
		'17:0 Margaric': 'week_a170Margaric',
		'18:0 Stearic': 'week_a180Stearic',
		'20:0 Arachidic': 'week_a200Arachidic',
		'22:0 Behenate': 'week_a220Behenate',
		'24:0 Lignoceric': 'week_a240Lignoceric',
		'Alanine': 'week_Alanine',
		'Arginine': 'week_Arginine',
		'Aspartic Acid': 'week_AsparticAcid',
		'Cysteine': 'week_Cysteine',
		'Glutamic Acid': 'week_GlutamicAcid',
		'Glycine': 'week_Glycine',
		'Histidine': 'week_Histidine',
		'Isoleucine': 'week_Isoleucine',
		'Leucine': 'week_Leucine',
		'Lysine': 'week_Lysine',
		'Methionine': 'week_Methionine',
		'Phenylalanine': 'week_Phenylalanine',
		'Proline': 'week_Proline',
		'Serine': 'week_Serine',
		'Threonine': 'week_Threonine',
		'Tryptophan': 'week_Tryptophan',
		'Tyrosine': 'week_Tyrosine',
		'Valine': 'week_Valine',
		'Ash': 'week_Ash',
		'Organic Acids (Total)': 'week_OrganicAcidsTotal',
		'Acetic Acid': 'week_AceticAcid',
		'Citric Acid': 'week_CitricAcid',
		'Lactic Acid': 'week_LacticAcid',
		'Malic Acid': 'week_MalicAcid',
		'Taurine': 'week_Taurine',
		'Sugar Alcohols (Total)': 'week_SugarAlcoholsTotal',
		'Glycerol': 'week_Glycerol',
		'Inositol': 'week_Inositol',
		'Mannitol': 'week_Mannitol',
		'Sorbitol': 'week_Sorbitol',
		'Xylitol': 'week_Xylitol',
		'Artificial Sweeteners (Total)': 'week_ArtificialSweetenersTotal',
		'Aspartame': 'week_Aspartame',
		'Saccharin': 'week_Saccharin',
		'Alcohol': 'week_Alcohol',
		'Caffeine': 'week_Caffeine',
	}
	headers_display = ['Recipe', 'Item', 'Grams', 'Cost', '$/100cal', '$/gP', '$/gFi', 'Calories', 'Protein', 'Fat', 'Carbohydrates', 'Fiber', 'Starch', 'Total Sugars', 'Monosaccharides', 'Fructose', 'Glucose', 'Galactose', 'Disaccharides', 'Lactose', 'Maltose', 'Sucrose', 'Soluble Fiber', 'Insoluble Fiber', 'Other Carbohydrates', 'Monounsaturated Fat', 'Polyunsaturated Fat', 'Saturated Fat', 'Trans Fat', 'Cholesterol', 'Water', 'Vitamin B1', 'Vitamin B2', 'Vitamin B3', 'Vitamin B3 (Niacin Equivalents)', 'Vitamin B6', 'Vitamin B12', 'Biotin', 'Choline', 'Folate', 'Folate (DFE)', 'Folate (food)', 'Pantothenic Acid', 'Vitamin C', 'Vitamin A International Units (IU)', 'Vitamin A mcg Retinol Activity Equivalents (RAE)', 'Vitamin A mcg Retinol Equivalents (RE)', 'Retinol mcg Retinol Equivalents (RE)', 'Carotenoid mcg Retinol Equivalents (RE)', 'Alpha-Carotene', 'Beta-Carotene', 'Beta-Carotene Equivalents', 'Cryptoxanthin', 'Lutein and Zeaxanthin', 'Lycopene', 'Vitamin D International Units (IU)', 'Vitamin D mcg', 'Vitamin E mg Alpha-Tocopherol Equivalents (ATE)', 'Vitamin E International Units (IU)', 'Vitamin E mg', 'Vitamin K', 'Boron', 'Calcium', 'Chloride', 'Chromium', 'Copper', 'Fluoride', 'Iodine', 'Iron', 'Magnesium', 'Manganese', 'Molybdenum', 'Phosphorus', 'Potassium', 'Selenium', 'Sodium', 'Zinc', 'Omega-3', 'Omega-6', '14:1 Myristoleic', '15:1 Pentadecenoic', '16:1 Palmitol', '17:1 Heptadecenoic', '18:1 Oleic', '20:1 Eicosenoic', '22:1 Erucic', '24:1 Nervonic', '18:2 Linoleic', '18:2 Conjugated Linoleic (CLA)', '18:3 Linolenic', '18:4 Stearidonic', '20:3 Eicosatrienoic', '20:4 Arachidonic', '20:5 Eicosapentaenoic (EPA)', '22:5 Docosapentaenoic (DPA)', '22:6 Docosahexaenoic (DHA)', '4:0 Butyric', '6:0 Caproic', '8:0 Caprylic', '10:0 Capric', '12:0 Lauric', '14:0 Myristic', '15:0 Pentadecanoic', '16:0 Palmitic', '17:0 Margaric', '18:0 Stearic', '20:0 Arachidic', '22:0 Behenate', '24:0 Lignoceric', 'Alanine', 'Arginine', 'Aspartic Acid', 'Cysteine', 'Glutamic Acid', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine', 'Ash', 'Organic Acids (Total)', 'Acetic Acid', 'Citric Acid', 'Lactic Acid', 'Malic Acid', 'Taurine', 'Sugar Alcohols (Total)', 'Glycerol', 'Inositol', 'Mannitol', 'Sorbitol', 'Xylitol', 'Artificial Sweeteners (Total)', 'Aspartame', 'Saccharin', 'Alcohol', 'Caffeine']

	# full_item_list = Item.objects.all()
	full_item_list = Item.objects.filter(active=True)
	# loop through headers_display and match their keys w dict keys to find values
	# the values will be used to go to serverside: values need to be model names

	## footers_holder is a list of the values (model representation) of the headers display list
	footers_holder = []
	for headers in headers_display:
		footers_holder.append(display_to_weekmodel[headers])

	calculated_footer = {
		'recipe': 'Recipe',
		'name': 'Item',
		'weekly_grams': 'Grams',
		'weekly_cost': 'sum',
		'cost_per_100_cal': 'averageper100',
		'cost_per_g_protein': 'averageperprotein',
		'cost_per_g_fiber': 'averageperfiber',
		'week_Calories': 'sum',
		'week_Protein': 'sum',
		'week_Fattotal': 'sum',
		'week_Carbohydrates': 'sum',
		'week_DietaryFiber': 'sum',
		'week_Starch': 'sum',
		'week_TotalSugars': 'sum',
		'week_Monosaccharides': 'sum',
		'week_Fructose': 'sum',
		'week_Glucose': 'sum',
		'week_Galactose': 'sum',
		'week_Disaccharides': 'sum',
		'week_Lactose': 'sum',
		'week_Maltose': 'sum',
		'week_Sucrose': 'sum',
		'week_SolubleFiber': 'sum',
		'week_InsolubleFiber': 'sum',
		'week_OtherCarbohydrates': 'sum',
		'week_MonounsaturatedFat': 'sum',
		'week_PolyunsaturatedFat': 'sum',
		'week_SaturatedFat': 'sum',
		'week_TransFat': 'sum',
		'week_Cholesterol': 'sum',
		'week_Water': 'sum',
		'week_VitaminB1': 'sum',
		'week_VitaminB2': 'sum',
		'week_VitaminB3': 'sum',
		'week_VitaminB3NiacinEquivalents': 'sum',
		'week_VitaminB6': 'sum',
		'week_VitaminB12': 'sum',
		'week_Biotin': 'sum',
		'week_Choline': 'sum',
		'week_Folate': 'sum',
		'week_FolateDFE': 'sum',
		'week_Folatefood': 'sum',
		'week_PantothenicAcid': 'sum',
		'week_VitaminC': 'sum',
		'week_VitaminAInternationalUnitsIU': 'sum',
		'week_VitaminAmcgRetinolActivityEquivalentsRAE': 'sum',
		'week_VitaminAmcgRetinolEquivalentsRE': 'sum',
		'week_RetinolmcgRetinolEquivalentsRE': 'sum',
		'week_CarotenoidmcgRetinolEquivalentsRE': 'sum',
		'week_AlphaCarotene': 'sum',
		'week_BetaCarotene': 'sum',
		'week_BetaCaroteneEquivalents': 'sum',
		'week_Cryptoxanthin': 'sum',
		'week_LuteinandZeaxanthin': 'sum',
		'week_Lycopene': 'sum',
		'week_VitaminDInternationalUnitsIU': 'sum',
		'week_VitaminDmcg': 'sum',
		'week_VitaminEmgAlphaTocopherolEquivalentsATE': 'sum',
		'week_VitaminEInternationalUnitsIU': 'sum',
		'week_VitaminEmg': 'sum',
		'week_VitaminK': 'sum',
		'week_Boron': 'sum',
		'week_Calcium': 'sum',
		'week_Chloride': 'sum',
		'week_Chromium': 'sum',
		'week_Copper': 'sum',
		'week_Fluoride': 'sum',
		'week_Iodine': 'sum',
		'week_Iron': 'sum',
		'week_Magnesium': 'sum',
		'week_Manganese': 'sum',
		'week_Molybdenum': 'sum',
		'week_Phosphorus': 'sum',
		'week_Potassium': 'sum',
		'week_Selenium': 'sum',
		'week_Sodium': 'sum',
		'week_Zinc': 'sum',
		'week_Omega3FattyAcids': 'sum',
		'week_Omega6FattyAcids': 'sum',
		'week_a141Myristoleic': 'sum',
		'week_a151Pentadecenoic': 'sum',
		'week_a161Palmitol': 'sum',
		'week_a171Heptadecenoic': 'sum',
		'week_a181Oleic': 'sum',
		'week_a201Eicosenoic': 'sum',
		'week_a221Erucic': 'sum',
		'week_a241Nervonic': 'sum',
		'week_a182Linoleic': 'sum',
		'week_a182ConjugatedLinoleicCLA': 'sum',
		'week_a183Linolenic': 'sum',
		'week_a184Stearidonic': 'sum',
		'week_a203Eicosatrienoic': 'sum',
		'week_a204Arachidonic': 'sum',
		'week_a205EicosapentaenoicEPA': 'sum',
		'week_a225DocosapentaenoicDPA': 'sum',
		'week_a226DocosahexaenoicDHA': 'sum',
		'week_a40Butyric': 'sum',
		'week_a60Caproic': 'sum',
		'week_a80Caprylic': 'sum',
		'week_a100Capric': 'sum',
		'week_a120Lauric': 'sum',
		'week_a140Myristic': 'sum',
		'week_a150Pentadecanoic': 'sum',
		'week_a160Palmitic': 'sum',
		'week_a170Margaric': 'sum',
		'week_a180Stearic': 'sum',
		'week_a200Arachidic': 'sum',
		'week_a220Behenate': 'sum',
		'week_a240Lignoceric': 'sum',
		'week_Alanine': 'sum',
		'week_Arginine': 'sum',
		'week_AsparticAcid': 'sum',
		'week_Cysteine': 'sum',
		'week_GlutamicAcid': 'sum',
		'week_Glycine': 'sum',
		'week_Histidine': 'sum',
		'week_Isoleucine': 'sum',
		'week_Leucine': 'sum',
		'week_Lysine': 'sum',
		'week_Methionine': 'sum',
		'week_Phenylalanine': 'sum',
		'week_Proline': 'sum',
		'week_Serine': 'sum',
		'week_Threonine': 'sum',
		'week_Tryptophan': 'sum',
		'week_Tyrosine': 'sum',
		'week_Valine': 'sum',
		'week_Ash': 'sum',
		'week_OrganicAcidsTotal': 'sum',
		'week_AceticAcid': 'sum',
		'week_CitricAcid': 'sum',
		'week_LacticAcid': 'sum',
		'week_MalicAcid': 'sum',
		'week_Taurine': 'sum',
		'week_SugarAlcoholsTotal': 'sum',
		'week_Glycerol': 'sum',
		'week_Inositol': 'sum',
		'week_Mannitol': 'sum',
		'week_Sorbitol': 'sum',
		'week_Xylitol': 'sum',
		'week_ArtificialSweetenersTotal': 'sum',
		'week_Aspartame': 'sum',
		'week_Saccharin': 'sum',
		'week_Alcohol': 'sum',
		'week_Caffeine': 'sum'
	}

	WRI = {
		'week_VitaminAmcgRetinolActivityEquivalentsRAE': 6300,
		'week_VitaminC': 630,
		'week_Calcium': 9100,
		'week_Iron': 126,
		'week_VitaminDmcg': 140,
		'week_VitaminEmg': 105,
		'week_VitaminK': 840,
		'week_VitaminB1': 8.4,
		'week_VitaminB2': 9.1,
		'week_VitaminB3': 112,
		'week_VitaminB6': 11.9,
		'week_Folate': 2800,
		'week_VitaminB12': 16.8,
		'week_Biotin': 210,
		'week_PantothenicAcid': 35,
		'week_Phosphorus': 8750,
		'week_Iodine': 1050,
		'week_Magnesium': 2940,
		'week_Zinc': 77,
		'week_Selenium': 385,
		'week_Copper': 6.3,
		'week_Manganese': 16.1,
		'week_Chromium': 245,
		'week_Molybdenum': 315,
		'week_Chloride': 16100,
		'week_Potassium': 32900,
		'week_Choline': 3850,
	}


	# # # make a dictionary of the values from the double for loop. 
	# # # then do another for loop through the list of footers to get the value of each spot in the dict
	
	for keys in calculated_footer:
		if calculated_footer[keys] == 'sum':
			answer_sum = 0
			for m in range(0,len(full_item_list)):
				answer_sum = answer_sum + full_item_list.values()[m][keys]
			if keys in WRI:
				calculated_footer[keys] = '%s (WRI %s)' % (round(answer_sum, 1), WRI[keys])				
			else:
				calculated_footer[keys] = round(answer_sum, 1)
		# elif calculated_footer[keys] == 'average':
		# 	grams_sum = 0
		# 	weighted_numerator = 0
		# 	for m in range(0,len(full_item_list)):
		# 		weighted_numerator = weighted_numerator + (full_item_list.values()[m]['weekly_grams'] * full_item_list.values()[m][keys])
		# 		grams_sum = grams_sum + full_item_list.values()[m]['weekly_grams']
		# 	answer_weighted_average =  weighted_numerator / grams_sum	
		# 	calculated_footer[keys] = round(answer_weighted_average, 2)
		
		elif calculated_footer[keys] == 'averageper100':
			cost_sum = 0
			calories_sum = 0
			for m in range(0, len(full_item_list)):
				cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
				calories_sum = calories_sum + full_item_list.values()[m]['week_Calories']
			answer_weighted_average = (cost_sum/calories_sum) * 100
			calculated_footer[keys] = round(answer_weighted_average, 2)
		elif calculated_footer[keys] == 'averageperprotein':
			cost_sum = 0
			protein_sum = 0
			for m in range(0, len(full_item_list)):
				cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
				protein_sum = protein_sum + full_item_list.values()[m]['week_Protein']
			answer_weighted_average = cost_sum/protein_sum
			calculated_footer[keys] = round(answer_weighted_average, 2)
		elif calculated_footer[keys] == 'averageperfiber':
			cost_sum = 0
			fiber_sum = 0
			for m in range(0, len(full_item_list)):
				cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
				fiber_sum = fiber_sum + full_item_list.values()[m]['week_DietaryFiber']
			answer_weighted_average = cost_sum/fiber_sum
			calculated_footer[keys] = round(answer_weighted_average, 2)
		else:
			print('none')

	# ### A list of footers as they appear as keys in the calculated_footers dict
	footers = ['recipe', 'name', 'weekly_grams', 'weekly_cost', 'cost_per_100_cal', 'cost_per_g_protein', 'cost_per_g_fiber', 'week_Calories', 'week_Protein', 'week_Fattotal', 'week_Carbohydrates', 'week_DietaryFiber', 'week_Starch', 'week_TotalSugars', 'week_Monosaccharides', 'week_Fructose', 'week_Glucose', 'week_Galactose', 'week_Disaccharides', 'week_Lactose', 'week_Maltose', 'week_Sucrose', 'week_SolubleFiber', 'week_InsolubleFiber', 'week_OtherCarbohydrates', 'week_MonounsaturatedFat', 'week_PolyunsaturatedFat', 'week_SaturatedFat', 'week_TransFat', 'week_Cholesterol', 'week_Water', 'week_VitaminB1', 'week_VitaminB2', 'week_VitaminB3', 'week_VitaminB3NiacinEquivalents', 'week_VitaminB6', 'week_VitaminB12', 'week_Biotin', 'week_Choline', 'week_Folate', 'week_FolateDFE', 'week_Folatefood', 'week_PantothenicAcid', 'week_VitaminC', 'week_VitaminAInternationalUnitsIU', 'week_VitaminAmcgRetinolActivityEquivalentsRAE', 'week_VitaminAmcgRetinolEquivalentsRE', 'week_RetinolmcgRetinolEquivalentsRE', 'week_CarotenoidmcgRetinolEquivalentsRE', 'week_AlphaCarotene', 'week_BetaCarotene', 'week_BetaCaroteneEquivalents', 'week_Cryptoxanthin', 'week_LuteinandZeaxanthin', 'week_Lycopene', 'week_VitaminDInternationalUnitsIU', 'week_VitaminDmcg', 'week_VitaminEmgAlphaTocopherolEquivalentsATE', 'week_VitaminEInternationalUnitsIU', 'week_VitaminEmg', 'week_VitaminK', 'week_Boron', 'week_Calcium', 'week_Chloride', 'week_Chromium', 'week_Copper', 'week_Fluoride', 'week_Iodine', 'week_Iron', 'week_Magnesium', 'week_Manganese', 'week_Molybdenum', 'week_Phosphorus', 'week_Potassium', 'week_Selenium', 'week_Sodium', 'week_Zinc', 'week_Omega3FattyAcids', 'week_Omega6FattyAcids', 'week_a141Myristoleic', 'week_a151Pentadecenoic', 'week_a161Palmitol', 'week_a171Heptadecenoic', 'week_a181Oleic', 'week_a201Eicosenoic', 'week_a221Erucic', 'week_a241Nervonic', 'week_a182Linoleic', 'week_a182ConjugatedLinoleicCLA', 'week_a183Linolenic', 'week_a184Stearidonic', 'week_a203Eicosatrienoic', 'week_a204Arachidonic', 'week_a205EicosapentaenoicEPA', 'week_a225DocosapentaenoicDPA', 'week_a226DocosahexaenoicDHA', 'week_a40Butyric', 'week_a60Caproic', 'week_a80Caprylic', 'week_a100Capric', 'week_a120Lauric', 'week_a140Myristic', 'week_a150Pentadecanoic', 'week_a160Palmitic', 'week_a170Margaric', 'week_a180Stearic', 'week_a200Arachidic', 'week_a220Behenate', 'week_a240Lignoceric', 'week_Alanine', 'week_Arginine', 'week_AsparticAcid', 'week_Cysteine', 'week_GlutamicAcid', 'week_Glycine', 'week_Histidine', 'week_Isoleucine', 'week_Leucine', 'week_Lysine', 'week_Methionine', 'week_Phenylalanine', 'week_Proline', 'week_Serine', 'week_Threonine', 'week_Tryptophan', 'week_Tyrosine', 'week_Valine', 'week_Ash', 'week_OrganicAcidsTotal', 'week_AceticAcid', 'week_CitricAcid', 'week_LacticAcid', 'week_MalicAcid', 'week_Taurine', 'week_SugarAlcoholsTotal', 'week_Glycerol', 'week_Inositol', 'week_Mannitol', 'week_Sorbitol', 'week_Xylitol', 'week_ArtificialSweetenersTotal', 'week_Aspartame', 'week_Saccharin', 'week_Alcohol', 'week_Caffeine'] 
	final_footers = []
	for title in footers:
		for keys in calculated_footer:
			if keys == title:
				final_footers.append(calculated_footer[keys])



	return render(request, 'nutrition/week.html', {'headers': headers_display, 'full_item_list': full_item_list, 'final_footers': final_footers})

def scrape(request):
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = ScrapeForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			state = form.cleaned_data['state']
			data_source = form.cleaned_data['data_source']
			notes = form.cleaned_data['notes']
			servingsize = form.cleaned_data['servingsize']
			servingsizeunits = form.cleaned_data['servingsizeunits']	
			
			data, units, test_1, test_2, test_3 = Scrape.table(data_source)
			if 'ERROR' in test_1 or 'ERROR' in test_2 or 'ERROR' in test_3:
				return redirect('error')

			user_inputs = [name, state, data_source, notes, servingsize, servingsizeunits]

			Upload.data(user_inputs, data, units)
			return redirect('menu')
	else:
		form = ScrapeForm()

	return render(request, 'nutrition/scrape.html', {'form': form})

def manual(request):
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = ManualForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('menu')
	else:
		form = ManualForm()

	return render(request, 'nutrition/manual.html', {'form': form})

def core_edit(request, pk):
	populate = get_object_or_404(CoreData, pk=pk)
	if request.method =='POST':
		form = ManualForm(request.POST, instance=populate)
		if form.is_valid():
			form.save()
			return redirect('menu')
	else:
		form = ManualForm(instance=populate)
	return render(request, 'nutrition/editcore.html', {'form': form})



def add_item(request):
	### This whole block worked perfectly ###
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = AddForm(request.POST)
		if form.is_valid():
			# add = form.save(commit=False)
			### Get pk here, then do all of the logic to calculate every value
			## needed into a 3rd table layered on top. Do also in edit view below
			## just do it into the same 2nd table. with for loop over .values() dict
			# headers = ['Protein', 'Carbohydrates', 'Fattotal', 'DietaryFiber', 'Calories', 'Starch', 'TotalSugars', 'Monosaccharides', 'Fructose', 'Glucose', 'Galactose', 'Disaccharides', 'Lactose', 'Maltose', 'Sucrose', 'SolubleFiber', 'InsolubleFiber', 'OtherCarbohydrates', 'MonounsaturatedFat', 'PolyunsaturatedFat', 'SaturatedFat', 'TransFat', 'Cholesterol', 'Water', 'VitaminB1', 'VitaminB2', 'VitaminB3', 'VitaminB3NiacinEquivalents', 'VitaminB6', 'VitaminB12', 'Biotin', 'Choline', 'Folate', 'FolateDFE', 'Folatefood', 'PantothenicAcid', 'VitaminC', 'VitaminAInternationalUnitsIU', 'VitaminAmcgRetinolActivityEquivalentsRAE', 'VitaminAmcgRetinolEquivalentsRE', 'RetinolmcgRetinolEquivalentsRE', 'CarotenoidmcgRetinolEquivalentsRE', 'AlphaCarotene', 'BetaCarotene', 'BetaCaroteneEquivalents', 'Cryptoxanthin', 'LuteinandZeaxanthin', 'Lycopene', 'VitaminDInternationalUnitsIU', 'VitaminDmcg', 'VitaminEmgAlphaTocopherolEquivalentsATE', 'VitaminEInternationalUnitsIU', 'VitaminEmg', 'VitaminK', 'Boron', 'Calcium', 'Chloride', 'Chromium', 'Copper', 'Fluoride', 'Iodine', 'Iron', 'Magnesium', 'Manganese', 'Molybdenum', 'Phosphorus', 'Potassium', 'Selenium', 'Sodium', 'Zinc', 'Omega3FattyAcids', 'Omega6FattyAcids', 'a141Myristoleic', 'a151Pentadecenoic', 'a161Palmitol', 'a171Heptadecenoic', 'a181Oleic', 'a201Eicosenoic', 'a221Erucic', 'a241Nervonic', 'a182Linoleic', 'a182ConjugatedLinoleicCLA', 'a183Linolenic', 'a184Stearidonic', 'a203Eicosatrienoic', 'a204Arachidonic', 'a205EicosapentaenoicEPA', 'a225DocosapentaenoicDPA', 'a226DocosahexaenoicDHA', 'a40Butyric', 'a60Caproic', 'a80Caprylic', 'a100Capric', 'a120Lauric', 'a140Myristic', 'a150Pentadecanoic', 'a160Palmitic', 'a170Margaric', 'a180Stearic', 'a200Arachidic', 'a220Behenate', 'a240Lignoceric', 'Alanine', 'Arginine', 'AsparticAcid', 'Cysteine', 'GlutamicAcid', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine', 'Ash', 'OrganicAcidsTotal', 'AceticAcid', 'CitricAcid', 'LacticAcid', 'MalicAcid', 'Taurine', 'SugarAlcoholsTotal', 'Glycerol', 'Inositol', 'Mannitol', 'Sorbitol', 'Xylitol', 'ArtificialSweetenersTotal', 'Aspartame', 'Saccharin', 'Alcohol', 'Caffeine']
			# name = cleaned_data['name']
			# c = CoreData.objects.filter(name=name).values()[0]
			# insert_values = []
			# for i in headers:
			# 	insert_values.append(c[i])

			name = form.cleaned_data['name']
			recipe = form.cleaned_data['recipe']
			grams = form.cleaned_data['grams']
			units = form.cleaned_data['units']
			conversion = form.cleaned_data['conversion']
			cost_per_100_cal = form.cleaned_data['cost_per_100_cal']
			cost_per_gram = form.cleaned_data['cost_per_gram']
			monday_1 = form.cleaned_data['monday_1']
			monday_2 = form.cleaned_data['monday_2']
			monday_3 = form.cleaned_data['monday_3']
			tuesday_1 = form.cleaned_data['tuesday_1']
			tuesday_2 = form.cleaned_data['tuesday_2']
			tuesday_3 = form.cleaned_data['tuesday_3']
			wednesday_1 = form.cleaned_data['wednesday_1']
			wednesday_2 = form.cleaned_data['wednesday_2']
			wednesday_3 = form.cleaned_data['wednesday_3']
			thursday_1 = form.cleaned_data['thursday_1']
			thursday_2 = form.cleaned_data['thursday_2']
			thursday_3 = form.cleaned_data['thursday_3']
			friday_1 = form.cleaned_data['friday_1']
			friday_2 = form.cleaned_data['friday_2']
			friday_3 = form.cleaned_data['friday_3']
			saturday_1 = form.cleaned_data['saturday_1']
			saturday_2 = form.cleaned_data['saturday_2']
			saturday_3 = form.cleaned_data['saturday_3']
			sunday_1 = form.cleaned_data['sunday_1']
			sunday_2 = form.cleaned_data['sunday_2']
			sunday_3 = form.cleaned_data['sunday_3']

			form_data = [name, recipe, grams, units, conversion, cost_per_100_cal, cost_per_gram, monday_1, monday_2, monday_3, tuesday_1, tuesday_2, tuesday_3, wednesday_1, wednesday_2, wednesday_3, thursday_1, thursday_2, thursday_3, friday_1, friday_2, friday_3, saturday_1, saturday_2, saturday_3, sunday_1, sunday_2, sunday_3]
			outputs = Complete.logic(form_data, 'new')
			print(outputs)
			return redirect('nutrition_homepage')
	else:
		form = AddForm()
	return render(request, 'nutrition/additem.html', {'form': form})


def edit_item(request, pk):
	populate = get_object_or_404(Item, pk=pk)
	if request.method =='POST':
		form = AddForm(request.POST, instance=populate)
		if form.is_valid():
			name = form.cleaned_data['name']
			recipe = form.cleaned_data['recipe']
			grams = form.cleaned_data['grams']
			units = form.cleaned_data['units']
			conversion = form.cleaned_data['conversion']
			cost_per_100_cal = form.cleaned_data['cost_per_100_cal']
			cost_per_gram = form.cleaned_data['cost_per_gram']
			monday_1 = form.cleaned_data['monday_1']
			monday_2 = form.cleaned_data['monday_2']
			monday_3 = form.cleaned_data['monday_3']
			tuesday_1 = form.cleaned_data['tuesday_1']
			tuesday_2 = form.cleaned_data['tuesday_2']
			tuesday_3 = form.cleaned_data['tuesday_3']
			wednesday_1 = form.cleaned_data['wednesday_1']
			wednesday_2 = form.cleaned_data['wednesday_2']
			wednesday_3 = form.cleaned_data['wednesday_3']
			thursday_1 = form.cleaned_data['thursday_1']
			thursday_2 = form.cleaned_data['thursday_2']
			thursday_3 = form.cleaned_data['thursday_3']
			friday_1 = form.cleaned_data['friday_1']
			friday_2 = form.cleaned_data['friday_2']
			friday_3 = form.cleaned_data['friday_3']
			saturday_1 = form.cleaned_data['saturday_1']
			saturday_2 = form.cleaned_data['saturday_2']
			saturday_3 = form.cleaned_data['saturday_3']
			sunday_1 = form.cleaned_data['sunday_1']
			sunday_2 = form.cleaned_data['sunday_2']
			sunday_3 = form.cleaned_data['sunday_3']

			form_data = [name, recipe, grams, units, conversion, cost_per_100_cal, cost_per_gram, monday_1, monday_2, monday_3, tuesday_1, tuesday_2, tuesday_3, wednesday_1, wednesday_2, wednesday_3, thursday_1, thursday_2, thursday_3, friday_1, friday_2, friday_3, saturday_1, saturday_2, saturday_3, sunday_1, sunday_2, sunday_3]
			outputs = Complete.logic(form_data, pk)
			print(outputs)
			return redirect('nutrition_homepage')
	else:
		form = AddForm(instance=populate)
	return render(request, 'nutrition/edititem.html', {'form': form})
	

def add_recipe(request):
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = RecipeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('nutrition_homepage')
	else:
		form = RecipeForm()
	return render(request, 'nutrition/addrecipe.html', {'form': form})


def edit_recipe(request, pk):
	populate = get_object_or_404(Recipe, pk=pk)
	if request.method =='POST':
		form = RecipeForm(request.POST, instance=populate)
		if form.is_valid():
			form.save()
			return redirect('nutrition_homepage')
	else:
		form = RecipeForm(instance=populate)
	return render(request, 'nutrition/editrecipe.html', {'form': form})


def menu(request):
	menu = CoreData.objects.all()
	return render(request, 'nutrition/menu.html', {'menu': menu})

def error(request):
	return render(request, 'nutrition/error.html')