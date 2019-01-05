	## footers_holder is a list of the values (model representation) of the headers display list
	# footers_holder = []
	# for headers in headers_display:
	# 	footers_holder.append(display_to_weekmodel[headers])

	# calculated_footer = {
	# 	'recipe': 'Recipe',
	# 	'name': 'Item',
	# 	'weekly_grams': 'Grams',
	# 	'weekly_cost': 'sum',
	# 	'cost_per_100_cal': 'averageper100',
	# 	'cost_per_g_protein': 'averageperprotein',
	# 	'cost_per_g_fiber': 'averageperfiber',
	# 	'week_Calories': 'sum',
	# 	'week_Protein': 'sum',
	# 	'week_Fattotal': 'sum',
	# 	'week_Carbohydrates': 'sum',
	# 	'week_DietaryFiber': 'sum',
	# 	'week_Starch': 'sum',
	# 	'week_TotalSugars': 'sum',
	# 	'week_Monosaccharides': 'sum',
	# 	'week_Fructose': 'sum',
	# 	'week_Glucose': 'sum',
	# 	'week_Galactose': 'sum',
	# 	'week_Disaccharides': 'sum',
	# 	'week_Lactose': 'sum',
	# 	'week_Maltose': 'sum',
	# 	'week_Sucrose': 'sum',
	# 	'week_SolubleFiber': 'sum',
	# 	'week_InsolubleFiber': 'sum',
	# 	'week_OtherCarbohydrates': 'sum',
	# 	'week_MonounsaturatedFat': 'sum',
	# 	'week_PolyunsaturatedFat': 'sum',
	# 	'week_SaturatedFat': 'sum',
	# 	'week_TransFat': 'sum',
	# 	'week_Cholesterol': 'sum',
	# 	'week_Water': 'sum',
	# 	'week_VitaminB1': 'sum',
	# 	'week_VitaminB2': 'sum',
	# 	'week_VitaminB3': 'sum',
	# 	'week_VitaminB3NiacinEquivalents': 'sum',
	# 	'week_VitaminB6': 'sum',
	# 	'week_VitaminB12': 'sum',
	# 	'week_Biotin': 'sum',
	# 	'week_Choline': 'sum',
	# 	'week_Folate': 'sum',
	# 	'week_FolateDFE': 'sum',
	# 	'week_Folatefood': 'sum',
	# 	'week_PantothenicAcid': 'sum',
	# 	'week_VitaminC': 'sum',
	# 	'week_VitaminAInternationalUnitsIU': 'sum',
	# 	'week_VitaminAmcgRetinolActivityEquivalentsRAE': 'sum',
	# 	'week_VitaminAmcgRetinolEquivalentsRE': 'sum',
	# 	'week_RetinolmcgRetinolEquivalentsRE': 'sum',
	# 	'week_CarotenoidmcgRetinolEquivalentsRE': 'sum',
	# 	'week_AlphaCarotene': 'sum',
	# 	'week_BetaCarotene': 'sum',
	# 	'week_BetaCaroteneEquivalents': 'sum',
	# 	'week_Cryptoxanthin': 'sum',
	# 	'week_LuteinandZeaxanthin': 'sum',
	# 	'week_Lycopene': 'sum',
	# 	'week_VitaminDInternationalUnitsIU': 'sum',
	# 	'week_VitaminDmcg': 'sum',
	# 	'week_VitaminEmgAlphaTocopherolEquivalentsATE': 'sum',
	# 	'week_VitaminEInternationalUnitsIU': 'sum',
	# 	'week_VitaminEmg': 'sum',
	# 	'week_VitaminK': 'sum',
	# 	'week_Boron': 'sum',
	# 	'week_Calcium': 'sum',
	# 	'week_Chloride': 'sum',
	# 	'week_Chromium': 'sum',
	# 	'week_Copper': 'sum',
	# 	'week_Fluoride': 'sum',
	# 	'week_Iodine': 'sum',
	# 	'week_Iron': 'sum',
	# 	'week_Magnesium': 'sum',
	# 	'week_Manganese': 'sum',
	# 	'week_Molybdenum': 'sum',
	# 	'week_Phosphorus': 'sum',
	# 	'week_Potassium': 'sum',
	# 	'week_Selenium': 'sum',
	# 	'week_Sodium': 'sum',
	# 	'week_Zinc': 'sum',
	# 	'week_Omega3FattyAcids': 'sum',
	# 	'week_Omega6FattyAcids': 'sum',
	# 	'week_a141Myristoleic': 'sum',
	# 	'week_a151Pentadecenoic': 'sum',
	# 	'week_a161Palmitol': 'sum',
	# 	'week_a171Heptadecenoic': 'sum',
	# 	'week_a181Oleic': 'sum',
	# 	'week_a201Eicosenoic': 'sum',
	# 	'week_a221Erucic': 'sum',
	# 	'week_a241Nervonic': 'sum',
	# 	'week_a182Linoleic': 'sum',
	# 	'week_a182ConjugatedLinoleicCLA': 'sum',
	# 	'week_a183Linolenic': 'sum',
	# 	'week_a184Stearidonic': 'sum',
	# 	'week_a203Eicosatrienoic': 'sum',
	# 	'week_a204Arachidonic': 'sum',
	# 	'week_a205EicosapentaenoicEPA': 'sum',
	# 	'week_a225DocosapentaenoicDPA': 'sum',
	# 	'week_a226DocosahexaenoicDHA': 'sum',
	# 	'week_a40Butyric': 'sum',
	# 	'week_a60Caproic': 'sum',
	# 	'week_a80Caprylic': 'sum',
	# 	'week_a100Capric': 'sum',
	# 	'week_a120Lauric': 'sum',
	# 	'week_a140Myristic': 'sum',
	# 	'week_a150Pentadecanoic': 'sum',
	# 	'week_a160Palmitic': 'sum',
	# 	'week_a170Margaric': 'sum',
	# 	'week_a180Stearic': 'sum',
	# 	'week_a200Arachidic': 'sum',
	# 	'week_a220Behenate': 'sum',
	# 	'week_a240Lignoceric': 'sum',
	# 	'week_Alanine': 'sum',
	# 	'week_Arginine': 'sum',
	# 	'week_AsparticAcid': 'sum',
	# 	'week_Cysteine': 'sum',
	# 	'week_GlutamicAcid': 'sum',
	# 	'week_Glycine': 'sum',
	# 	'week_Histidine': 'sum',
	# 	'week_Isoleucine': 'sum',
	# 	'week_Leucine': 'sum',
	# 	'week_Lysine': 'sum',
	# 	'week_Methionine': 'sum',
	# 	'week_Phenylalanine': 'sum',
	# 	'week_Proline': 'sum',
	# 	'week_Serine': 'sum',
	# 	'week_Threonine': 'sum',
	# 	'week_Tryptophan': 'sum',
	# 	'week_Tyrosine': 'sum',
	# 	'week_Valine': 'sum',
	# 	'week_Ash': 'sum',
	# 	'week_OrganicAcidsTotal': 'sum',
	# 	'week_AceticAcid': 'sum',
	# 	'week_CitricAcid': 'sum',
	# 	'week_LacticAcid': 'sum',
	# 	'week_MalicAcid': 'sum',
	# 	'week_Taurine': 'sum',
	# 	'week_SugarAlcoholsTotal': 'sum',
	# 	'week_Glycerol': 'sum',
	# 	'week_Inositol': 'sum',
	# 	'week_Mannitol': 'sum',
	# 	'week_Sorbitol': 'sum',
	# 	'week_Xylitol': 'sum',
	# 	'week_ArtificialSweetenersTotal': 'sum',
	# 	'week_Aspartame': 'sum',
	# 	'week_Saccharin': 'sum',
	# 	'week_Alcohol': 'sum',
	# 	'week_Caffeine': 'sum'
	# }

	# WRI = {
	# 	'week_VitaminAmcgRetinolActivityEquivalentsRAE': 6300,
	# 	'week_VitaminC': 630,
	# 	'week_Calcium': 9100,
	# 	'week_Iron': 126,
	# 	'week_VitaminDmcg': 140,
	# 	'week_VitaminEmg': 105,
	# 	'week_VitaminK': 840,
	# 	'week_VitaminB1': 8.4,
	# 	'week_VitaminB2': 9.1,
	# 	'week_VitaminB3': 112,
	# 	'week_VitaminB6': 11.9,
	# 	'week_Folate': 2800,
	# 	'week_VitaminB12': 16.8,
	# 	'week_Biotin': 210,
	# 	'week_PantothenicAcid': 35,
	# 	'week_Phosphorus': 8750,
	# 	'week_Iodine': 1050,
	# 	'week_Magnesium': 2940,
	# 	'week_Zinc': 77,
	# 	'week_Selenium': 385,
	# 	'week_Copper': 6.3,
	# 	'week_Manganese': 16.1,
	# 	'week_Chromium': 245,
	# 	'week_Molybdenum': 315,
	# 	'week_Chloride': 16100,
	# 	'week_Potassium': 32900,
	# 	'week_Choline': 3850,
	# }


	# # # # make a dictionary of the values from the double for loop. 
	# # # # then do another for loop through the list of footers to get the value of each spot in the dict
	
	# for keys in calculated_footer:
	# 	if calculated_footer[keys] == 'sum':
	# 		answer_sum = 0
	# 		for m in range(0,len(full_item_list)):
	# 			answer_sum = answer_sum + full_item_list.values()[m][keys]
	# 		if keys in WRI:
	# 			calculated_footer[keys] = '%s (WRI %s)' % (round(answer_sum, 1), WRI[keys])				
	# 		else:
	# 			calculated_footer[keys] = round(answer_sum, 1)
	# 	# elif calculated_footer[keys] == 'average':
	# 	# 	grams_sum = 0
	# 	# 	weighted_numerator = 0
	# 	# 	for m in range(0,len(full_item_list)):
	# 	# 		weighted_numerator = weighted_numerator + (full_item_list.values()[m]['weekly_grams'] * full_item_list.values()[m][keys])
	# 	# 		grams_sum = grams_sum + full_item_list.values()[m]['weekly_grams']
	# 	# 	answer_weighted_average =  weighted_numerator / grams_sum	
	# 	# 	calculated_footer[keys] = round(answer_weighted_average, 2)
		
	# 	elif calculated_footer[keys] == 'averageper100':
	# 		cost_sum = 0
	# 		calories_sum = 0
	# 		for m in range(0, len(full_item_list)):
	# 			cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
	# 			calories_sum = calories_sum + full_item_list.values()[m]['week_Calories']
	# 		answer_weighted_average = (cost_sum/calories_sum) * 100
	# 		calculated_footer[keys] = round(answer_weighted_average, 2)
	# 	elif calculated_footer[keys] == 'averageperprotein':
	# 		cost_sum = 0
	# 		protein_sum = 0
	# 		for m in range(0, len(full_item_list)):
	# 			cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
	# 			protein_sum = protein_sum + full_item_list.values()[m]['week_Protein']
	# 		answer_weighted_average = cost_sum/protein_sum
	# 		calculated_footer[keys] = round(answer_weighted_average, 2)
	# 	elif calculated_footer[keys] == 'averageperfiber':
	# 		cost_sum = 0
	# 		fiber_sum = 0
	# 		for m in range(0, len(full_item_list)):
	# 			cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
	# 			fiber_sum = fiber_sum + full_item_list.values()[m]['week_DietaryFiber']
	# 		answer_weighted_average = cost_sum/fiber_sum
	# 		calculated_footer[keys] = round(answer_weighted_average, 2)
	# 	else:
	# 		print('none')

	# # ### A list of footers as they appear as keys in the calculated_footers dict
	# footers = ['recipe', 'name', 'weekly_grams', 'weekly_cost', 'cost_per_100_cal', 'cost_per_g_protein', 'cost_per_g_fiber', 'week_Calories', 'week_Protein', 'week_Fattotal', 'week_Carbohydrates', 'week_DietaryFiber', 'week_Starch', 'week_TotalSugars', 'week_Monosaccharides', 'week_Fructose', 'week_Glucose', 'week_Galactose', 'week_Disaccharides', 'week_Lactose', 'week_Maltose', 'week_Sucrose', 'week_SolubleFiber', 'week_InsolubleFiber', 'week_OtherCarbohydrates', 'week_MonounsaturatedFat', 'week_PolyunsaturatedFat', 'week_SaturatedFat', 'week_TransFat', 'week_Cholesterol', 'week_Water', 'week_VitaminB1', 'week_VitaminB2', 'week_VitaminB3', 'week_VitaminB3NiacinEquivalents', 'week_VitaminB6', 'week_VitaminB12', 'week_Biotin', 'week_Choline', 'week_Folate', 'week_FolateDFE', 'week_Folatefood', 'week_PantothenicAcid', 'week_VitaminC', 'week_VitaminAInternationalUnitsIU', 'week_VitaminAmcgRetinolActivityEquivalentsRAE', 'week_VitaminAmcgRetinolEquivalentsRE', 'week_RetinolmcgRetinolEquivalentsRE', 'week_CarotenoidmcgRetinolEquivalentsRE', 'week_AlphaCarotene', 'week_BetaCarotene', 'week_BetaCaroteneEquivalents', 'week_Cryptoxanthin', 'week_LuteinandZeaxanthin', 'week_Lycopene', 'week_VitaminDInternationalUnitsIU', 'week_VitaminDmcg', 'week_VitaminEmgAlphaTocopherolEquivalentsATE', 'week_VitaminEInternationalUnitsIU', 'week_VitaminEmg', 'week_VitaminK', 'week_Boron', 'week_Calcium', 'week_Chloride', 'week_Chromium', 'week_Copper', 'week_Fluoride', 'week_Iodine', 'week_Iron', 'week_Magnesium', 'week_Manganese', 'week_Molybdenum', 'week_Phosphorus', 'week_Potassium', 'week_Selenium', 'week_Sodium', 'week_Zinc', 'week_Omega3FattyAcids', 'week_Omega6FattyAcids', 'week_a141Myristoleic', 'week_a151Pentadecenoic', 'week_a161Palmitol', 'week_a171Heptadecenoic', 'week_a181Oleic', 'week_a201Eicosenoic', 'week_a221Erucic', 'week_a241Nervonic', 'week_a182Linoleic', 'week_a182ConjugatedLinoleicCLA', 'week_a183Linolenic', 'week_a184Stearidonic', 'week_a203Eicosatrienoic', 'week_a204Arachidonic', 'week_a205EicosapentaenoicEPA', 'week_a225DocosapentaenoicDPA', 'week_a226DocosahexaenoicDHA', 'week_a40Butyric', 'week_a60Caproic', 'week_a80Caprylic', 'week_a100Capric', 'week_a120Lauric', 'week_a140Myristic', 'week_a150Pentadecanoic', 'week_a160Palmitic', 'week_a170Margaric', 'week_a180Stearic', 'week_a200Arachidic', 'week_a220Behenate', 'week_a240Lignoceric', 'week_Alanine', 'week_Arginine', 'week_AsparticAcid', 'week_Cysteine', 'week_GlutamicAcid', 'week_Glycine', 'week_Histidine', 'week_Isoleucine', 'week_Leucine', 'week_Lysine', 'week_Methionine', 'week_Phenylalanine', 'week_Proline', 'week_Serine', 'week_Threonine', 'week_Tryptophan', 'week_Tyrosine', 'week_Valine', 'week_Ash', 'week_OrganicAcidsTotal', 'week_AceticAcid', 'week_CitricAcid', 'week_LacticAcid', 'week_MalicAcid', 'week_Taurine', 'week_SugarAlcoholsTotal', 'week_Glycerol', 'week_Inositol', 'week_Mannitol', 'week_Sorbitol', 'week_Xylitol', 'week_ArtificialSweetenersTotal', 'week_Aspartame', 'week_Saccharin', 'week_Alcohol', 'week_Caffeine'] 
	# final_footers = []
	# for title in footers:
	# 	for keys in calculated_footer:
	# 		if keys == title:
	# 			final_footers.append(calculated_footer[keys])

from nutrition.models import CoreData, Item, Recipe 

# class load_footer:

def totals():
	active_rows = Item.objects.filter(active=True)

	footer_guide = {
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

	# # # make a dictionary of the values from the double for loop. 
	# # # then do another for loop through the list of footers to get the value of each spot in the dict

	for keys in footer_guide:
		if footer_guide[keys] == 'sum':
			answer_sum = 0
			# for m in range(0,len(active_rows)):
			# 	answer_sum = answer_sum + active_rows.values()[m][keys]
			c = Item.objects.filter(pk=1000)[0]
			# c.keys = answer_sum
			print(c.keys)

		# if keys in WRI:
		# 	calculated_footer[keys] = '%s (WRI %s)' % (round(answer_sum, 1), WRI[keys])				
		# else:
		# 	calculated_footer[keys] = round(answer_sum, 1)
	# elif calculated_footer[keys] == 'average':
	# 	grams_sum = 0
	# 	weighted_numerator = 0
	# 	for m in range(0,len(full_item_list)):
	# 		weighted_numerator = weighted_numerator + (full_item_list.values()[m]['weekly_grams'] * full_item_list.values()[m][keys])
	# 		grams_sum = grams_sum + full_item_list.values()[m]['weekly_grams']
	# 	answer_weighted_average =  weighted_numerator / grams_sum	
	# 	calculated_footer[keys] = round(answer_weighted_average, 2)

	# elif calculated_footer[keys] == 'averageper100':
	# 	cost_sum = 0
	# 	calories_sum = 0
	# 	for m in range(0, len(full_item_list)):
	# 		cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
	# 		calories_sum = calories_sum + full_item_list.values()[m]['week_Calories']
	# 	answer_weighted_average = (cost_sum/calories_sum) * 100
	# 	calculated_footer[keys] = round(answer_weighted_average, 2)
	# elif calculated_footer[keys] == 'averageperprotein':
	# 	cost_sum = 0
	# 	protein_sum = 0
	# 	for m in range(0, len(full_item_list)):
	# 		cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
	# 		protein_sum = protein_sum + full_item_list.values()[m]['week_Protein']
	# 	answer_weighted_average = cost_sum/protein_sum
	# 	calculated_footer[keys] = round(answer_weighted_average, 2)
	# elif calculated_footer[keys] == 'averageperfiber':
	# 	cost_sum = 0
	# 	fiber_sum = 0
	# 	for m in range(0, len(full_item_list)):
	# 		cost_sum = cost_sum + full_item_list.values()[m]['weekly_cost']
	# 		fiber_sum = fiber_sum + full_item_list.values()[m]['week_DietaryFiber']
	# 	answer_weighted_average = cost_sum/fiber_sum
	# 	calculated_footer[keys] = round(answer_weighted_average, 2)
	# else:
	# 	print('none')

