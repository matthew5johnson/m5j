from nutrition.models import CoreData, Item, Recipe

class Complete:

	def logic(form_data, pk):
		# form_data = [name, recipe, grams, units, conversion, cost_per_100_cal, cost_per_gram, monday_1, monday_2, monday_3, tuesday_1, tuesday_2, tuesday_3, wednesday_1, wednesday_2, wednesday_3, thursday_1, thursday_2, thursday_3, friday_1, friday_2, friday_3, saturday_1, saturday_2, saturday_3, sunday_1, sunday_2, sunday_3]
		
		## Get core data
		name = form_data[0]
		c = CoreData.objects.filter(name=name).values()[0]
		get_core_values = []
		core_value_headers = ['servingsize', 'Protein', 'Carbohydrates', 'Fattotal', 'DietaryFiber', 'Calories', 'Starch', 'TotalSugars', 'Monosaccharides', 'Fructose', 'Glucose', 'Galactose', 'Disaccharides', 'Lactose', 'Maltose', 'Sucrose', 'SolubleFiber', 'InsolubleFiber', 'OtherCarbohydrates', 'MonounsaturatedFat', 'PolyunsaturatedFat', 'SaturatedFat', 'TransFat', 'Cholesterol', 'Water', 'VitaminB1', 'VitaminB2', 'VitaminB3', 'VitaminB3NiacinEquivalents', 'VitaminB6', 'VitaminB12', 'Biotin', 'Choline', 'Folate', 'FolateDFE', 'Folatefood', 'PantothenicAcid', 'VitaminC', 'VitaminAInternationalUnitsIU', 'VitaminAmcgRetinolActivityEquivalentsRAE', 'VitaminAmcgRetinolEquivalentsRE', 'RetinolmcgRetinolEquivalentsRE', 'CarotenoidmcgRetinolEquivalentsRE', 'AlphaCarotene', 'BetaCarotene', 'BetaCaroteneEquivalents', 'Cryptoxanthin', 'LuteinandZeaxanthin', 'Lycopene', 'VitaminDInternationalUnitsIU', 'VitaminDmcg', 'VitaminEmgAlphaTocopherolEquivalentsATE', 'VitaminEInternationalUnitsIU', 'VitaminEmg', 'VitaminK', 'Boron', 'Calcium', 'Chloride', 'Chromium', 'Copper', 'Fluoride', 'Iodine', 'Iron', 'Magnesium', 'Manganese', 'Molybdenum', 'Phosphorus', 'Potassium', 'Selenium', 'Sodium', 'Zinc', 'Omega3FattyAcids', 'Omega6FattyAcids', 'a141Myristoleic', 'a151Pentadecenoic', 'a161Palmitol', 'a171Heptadecenoic', 'a181Oleic', 'a201Eicosenoic', 'a221Erucic', 'a241Nervonic', 'a182Linoleic', 'a182ConjugatedLinoleicCLA', 'a183Linolenic', 'a184Stearidonic', 'a203Eicosatrienoic', 'a204Arachidonic', 'a205EicosapentaenoicEPA', 'a225DocosapentaenoicDPA', 'a226DocosahexaenoicDHA', 'a40Butyric', 'a60Caproic', 'a80Caprylic', 'a100Capric', 'a120Lauric', 'a140Myristic', 'a150Pentadecanoic', 'a160Palmitic', 'a170Margaric', 'a180Stearic', 'a200Arachidic', 'a220Behenate', 'a240Lignoceric', 'Alanine', 'Arginine', 'AsparticAcid', 'Cysteine', 'GlutamicAcid', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine', 'Ash', 'OrganicAcidsTotal', 'AceticAcid', 'CitricAcid', 'LacticAcid', 'MalicAcid', 'Taurine', 'SugarAlcoholsTotal', 'Glycerol', 'Inositol', 'Mannitol', 'Sorbitol', 'Xylitol', 'ArtificialSweetenersTotal', 'Aspartame', 'Saccharin', 'Alcohol', 'Caffeine']
		for i in core_value_headers:
			get_core_values.append(c[i])
		get_core_units = []
		core_unit_headers = ['uProtein', 'uCarbohydrates', 'uFattotal', 'uDietaryFiber', 'uCalories', 'uStarch', 'uTotalSugars', 'uMonosaccharides', 'uFructose', 'uGlucose', 'uGalactose', 'uDisaccharides', 'uLactose', 'uMaltose', 'uSucrose', 'uSolubleFiber', 'uInsolubleFiber', 'uOtherCarbohydrates', 'uMonounsaturatedFat', 'uPolyunsaturatedFat', 'uSaturatedFat', 'uTransFat', 'uCholesterol', 'uWater', 'uVitaminB1', 'uVitaminB2', 'uVitaminB3', 'uVitaminB3NiacinEquivalents', 'uVitaminB6', 'uVitaminB12', 'uBiotin', 'uCholine', 'uFolate', 'uFolateDFE', 'uFolatefood', 'uPantothenicAcid', 'uVitaminC', 'uVitaminAInternationalUnitsIU', 'uVitaminAmcgRetinolActivityEquivalentsRAE', 'uVitaminAmcgRetinolEquivalentsRE', 'uRetinolmcgRetinolEquivalentsRE', 'uCarotenoidmcgRetinolEquivalentsRE', 'uAlphaCarotene', 'uBetaCarotene', 'uBetaCaroteneEquivalents', 'uCryptoxanthin', 'uLuteinandZeaxanthin', 'uLycopene', 'uVitaminDInternationalUnitsIU', 'uVitaminDmcg', 'uVitaminEmgAlphaTocopherolEquivalentsATE', 'uVitaminEInternationalUnitsIU', 'uVitaminEmg', 'uVitaminK', 'uBoron', 'uCalcium', 'uChloride', 'uChromium', 'uCopper', 'uFluoride', 'uIodine', 'uIron', 'uMagnesium', 'uManganese', 'uMolybdenum', 'uPhosphorus', 'uPotassium', 'uSelenium', 'uSodium', 'uZinc', 'uOmega3FattyAcids', 'uOmega6FattyAcids', 'ua141Myristoleic', 'ua151Pentadecenoic', 'ua161Palmitol', 'ua171Heptadecenoic', 'ua181Oleic', 'ua201Eicosenoic', 'ua221Erucic', 'ua241Nervonic', 'ua182Linoleic', 'ua182ConjugatedLinoleicCLA', 'ua183Linolenic', 'ua184Stearidonic', 'ua203Eicosatrienoic', 'ua204Arachidonic', 'ua205EicosapentaenoicEPA', 'ua225DocosapentaenoicDPA', 'ua226DocosahexaenoicDHA', 'ua40Butyric', 'ua60Caproic', 'ua80Caprylic', 'ua100Capric', 'ua120Lauric', 'ua140Myristic', 'ua150Pentadecanoic', 'ua160Palmitic', 'ua170Margaric', 'ua180Stearic', 'ua200Arachidic', 'ua220Behenate', 'ua240Lignoceric', 'uAlanine', 'uArginine', 'uAsparticAcid', 'uCysteine', 'uGlutamicAcid', 'uGlycine', 'uHistidine', 'uIsoleucine', 'uLeucine', 'uLysine', 'uMethionine', 'uPhenylalanine', 'uProline', 'uSerine', 'uThreonine', 'uTryptophan', 'uTyrosine', 'uValine', 'uAsh', 'uOrganicAcidsTotal', 'uAceticAcid', 'uCitricAcid', 'uLacticAcid', 'uMalicAcid', 'uTaurine', 'uSugarAlcoholsTotal', 'uGlycerol', 'uInositol', 'uMannitol', 'uSorbitol', 'uXylitol', 'uArtificialSweetenersTotal', 'uAspartame', 'uSaccharin', 'uAlcohol', 'uCaffeine']
		for n in core_unit_headers:
			get_core_units.append(c[n])


		##############
		###  For daily
		##############

		## Calculate the multiplier that will scale core values based on my items grams and conversion factor
		## Conversion factor: if coredata is in a different state than my final state. i.e. cooked vs raw
		my_grams = form_data[2]
		conversion = form_data[4]
		core_grams = get_core_values[0]
		values_multiplier = (my_grams/core_grams) * conversion

		## Apply the multiplier to convert the core values into my adjusted values
		calculated_daily_values = []
		for i in get_core_values[1:]:
			a = i * values_multiplier
			calculated_daily_values.append(round(a,3))

		## Calc daily cost
		cost_per_gram = form_data[6]
		cost_based_on_grams = my_grams * cost_per_gram
		cost_per_100_cal = form_data[5]
		cost_based_on_cal = calculated_daily_values[4] * cost_per_100_cal / 100

		if calculated_daily_values[0] == 0:
			cost_per_g_protein = 0
		else:
			cost_per_g_protein = cost_based_on_grams / calculated_daily_values[0]

		if calculated_daily_values[3] == 0:
			cost_per_g_fiber = 0
		else:
			cost_per_g_fiber = cost_based_on_grams / calculated_daily_values[3]

		################
		###  For weekly 
		################

		## Get the number of days/servings of the item per week
		days = 0
		for time_slot in form_data[7:]:
			if time_slot == True:
				days += 1

		## Convert every daily value to a weekly basis
		calculated_weekly_values = []
		for value in calculated_daily_values:
			weekly = value * days 
			calculated_weekly_values.append(weekly)

		## Calc weekly cost
		weekly_cost = cost_based_on_grams * days

		## Calc weekly grams
		weekly_grams = my_grams * days


		########################################
		### Insert data into Item database table
		########################################
		if pk == 'new':	
			new = Item.objects.create(cost_based_on_grams=cost_based_on_grams, cost_based_on_cal=cost_based_on_cal, weekly_cost=weekly_cost, cost_per_g_protein=cost_per_g_protein, cost_per_g_fiber=cost_per_g_fiber, name=form_data[0], recipe=form_data[1], grams=form_data[2], weekly_grams=weekly_grams, units=form_data[3], conversion=form_data[4], cost_per_100_cal=form_data[5], cost_per_gram=form_data[6], monday_1=form_data[7], monday_2=form_data[8], monday_3=form_data[9], tuesday_1=form_data[10], tuesday_2=form_data[11], tuesday_3=form_data[12], wednesday_1=form_data[13], wednesday_2=form_data[14], wednesday_3=form_data[15], thursday_1=form_data[16], thursday_2=form_data[17], thursday_3=form_data[18], friday_1=form_data[19], friday_2=form_data[20], friday_3=form_data[21], saturday_1=form_data[22], saturday_2=form_data[23], saturday_3=form_data[24], sunday_1=form_data[25], sunday_2=form_data[26], sunday_3=form_data[27], Protein=calculated_daily_values[0], Carbohydrates=calculated_daily_values[1], Fattotal=calculated_daily_values[2], DietaryFiber=calculated_daily_values[3], Calories=calculated_daily_values[4], Starch=calculated_daily_values[5], TotalSugars=calculated_daily_values[6], Monosaccharides=calculated_daily_values[7], Fructose=calculated_daily_values[8], Glucose=calculated_daily_values[9], Galactose=calculated_daily_values[10], Disaccharides=calculated_daily_values[11], Lactose=calculated_daily_values[12], Maltose=calculated_daily_values[13], Sucrose=calculated_daily_values[14], SolubleFiber=calculated_daily_values[15], InsolubleFiber=calculated_daily_values[16], OtherCarbohydrates=calculated_daily_values[17], MonounsaturatedFat=calculated_daily_values[18], PolyunsaturatedFat=calculated_daily_values[19], SaturatedFat=calculated_daily_values[20], TransFat=calculated_daily_values[21], Cholesterol=calculated_daily_values[22], Water=calculated_daily_values[23], VitaminB1=calculated_daily_values[24], VitaminB2=calculated_daily_values[25], VitaminB3=calculated_daily_values[26], VitaminB3NiacinEquivalents=calculated_daily_values[27], VitaminB6=calculated_daily_values[28], VitaminB12=calculated_daily_values[29], Biotin=calculated_daily_values[30], Choline=calculated_daily_values[31], Folate=calculated_daily_values[32], FolateDFE=calculated_daily_values[33], Folatefood=calculated_daily_values[34], PantothenicAcid=calculated_daily_values[35], VitaminC=calculated_daily_values[36], VitaminAInternationalUnitsIU=calculated_daily_values[37], VitaminAmcgRetinolActivityEquivalentsRAE=calculated_daily_values[38], VitaminAmcgRetinolEquivalentsRE=calculated_daily_values[39], RetinolmcgRetinolEquivalentsRE=calculated_daily_values[40], CarotenoidmcgRetinolEquivalentsRE=calculated_daily_values[41], AlphaCarotene=calculated_daily_values[42], BetaCarotene=calculated_daily_values[43], BetaCaroteneEquivalents=calculated_daily_values[44], Cryptoxanthin=calculated_daily_values[45], LuteinandZeaxanthin=calculated_daily_values[46], Lycopene=calculated_daily_values[47], VitaminDInternationalUnitsIU=calculated_daily_values[48], VitaminDmcg=calculated_daily_values[49], VitaminEmgAlphaTocopherolEquivalentsATE=calculated_daily_values[50], VitaminEInternationalUnitsIU=calculated_daily_values[51], VitaminEmg=calculated_daily_values[52], VitaminK=calculated_daily_values[53], Boron=calculated_daily_values[54], Calcium=calculated_daily_values[55], Chloride=calculated_daily_values[56], Chromium=calculated_daily_values[57], Copper=calculated_daily_values[58], Fluoride=calculated_daily_values[59], Iodine=calculated_daily_values[60], Iron=calculated_daily_values[61], Magnesium=calculated_daily_values[62], Manganese=calculated_daily_values[63], Molybdenum=calculated_daily_values[64], Phosphorus=calculated_daily_values[65], Potassium=calculated_daily_values[66], Selenium=calculated_daily_values[67], Sodium=calculated_daily_values[68], Zinc=calculated_daily_values[69], Omega3FattyAcids=calculated_daily_values[70], Omega6FattyAcids=calculated_daily_values[71], a141Myristoleic=calculated_daily_values[72], a151Pentadecenoic=calculated_daily_values[73], a161Palmitol=calculated_daily_values[74], a171Heptadecenoic=calculated_daily_values[75], a181Oleic=calculated_daily_values[76], a201Eicosenoic=calculated_daily_values[77], a221Erucic=calculated_daily_values[78], a241Nervonic=calculated_daily_values[79], a182Linoleic=calculated_daily_values[80], a182ConjugatedLinoleicCLA=calculated_daily_values[81], a183Linolenic=calculated_daily_values[82], a184Stearidonic=calculated_daily_values[83], a203Eicosatrienoic=calculated_daily_values[84], a204Arachidonic=calculated_daily_values[85], a205EicosapentaenoicEPA=calculated_daily_values[86], a225DocosapentaenoicDPA=calculated_daily_values[87], a226DocosahexaenoicDHA=calculated_daily_values[88], a40Butyric=calculated_daily_values[89], a60Caproic=calculated_daily_values[90], a80Caprylic=calculated_daily_values[91], a100Capric=calculated_daily_values[92], a120Lauric=calculated_daily_values[93], a140Myristic=calculated_daily_values[94], a150Pentadecanoic=calculated_daily_values[95], a160Palmitic=calculated_daily_values[96], a170Margaric=calculated_daily_values[97], a180Stearic=calculated_daily_values[98], a200Arachidic=calculated_daily_values[99], a220Behenate=calculated_daily_values[100], a240Lignoceric=calculated_daily_values[101], Alanine=calculated_daily_values[102], Arginine=calculated_daily_values[103], AsparticAcid=calculated_daily_values[104], Cysteine=calculated_daily_values[105], GlutamicAcid=calculated_daily_values[106], Glycine=calculated_daily_values[107], Histidine=calculated_daily_values[108], Isoleucine=calculated_daily_values[109], Leucine=calculated_daily_values[110], Lysine=calculated_daily_values[111], Methionine=calculated_daily_values[112], Phenylalanine=calculated_daily_values[113], Proline=calculated_daily_values[114], Serine=calculated_daily_values[115], Threonine=calculated_daily_values[116], Tryptophan=calculated_daily_values[117], Tyrosine=calculated_daily_values[118], Valine=calculated_daily_values[119], Ash=calculated_daily_values[120], OrganicAcidsTotal=calculated_daily_values[121], AceticAcid=calculated_daily_values[122], CitricAcid=calculated_daily_values[123], LacticAcid=calculated_daily_values[124], MalicAcid=calculated_daily_values[125], Taurine=calculated_daily_values[126], SugarAlcoholsTotal=calculated_daily_values[127], Glycerol=calculated_daily_values[128], Inositol=calculated_daily_values[129], Mannitol=calculated_daily_values[130], Sorbitol=calculated_daily_values[131], Xylitol=calculated_daily_values[132], ArtificialSweetenersTotal=calculated_daily_values[133], Aspartame=calculated_daily_values[134], Saccharin=calculated_daily_values[135], Alcohol=calculated_daily_values[136], Caffeine=calculated_daily_values[137])
			primary = new.pk
			update = Item.objects.filter(pk=primary)[0]

			update.week_Protein = calculated_weekly_values[0]
			update.week_Carbohydrates = calculated_weekly_values[1]
			update.week_Fattotal = calculated_weekly_values[2]
			update.week_DietaryFiber = calculated_weekly_values[3]
			update.week_Calories = calculated_weekly_values[4]
			update.week_Starch = calculated_weekly_values[5]
			update.week_TotalSugars = calculated_weekly_values[6]
			update.week_Monosaccharides = calculated_weekly_values[7]
			update.week_Fructose = calculated_weekly_values[8]
			update.week_Glucose = calculated_weekly_values[9]
			update.week_Galactose = calculated_weekly_values[10]
			update.week_Disaccharides = calculated_weekly_values[11]
			update.week_Lactose = calculated_weekly_values[12]
			update.week_Maltose = calculated_weekly_values[13]
			update.week_Sucrose = calculated_weekly_values[14]
			update.week_SolubleFiber = calculated_weekly_values[15]
			update.week_InsolubleFiber = calculated_weekly_values[16]
			update.week_OtherCarbohydrates = calculated_weekly_values[17]
			update.week_MonounsaturatedFat = calculated_weekly_values[18]
			update.week_PolyunsaturatedFat = calculated_weekly_values[19]
			update.week_SaturatedFat = calculated_weekly_values[20]
			update.week_TransFat = calculated_weekly_values[21]
			update.week_Cholesterol = calculated_weekly_values[22]
			update.week_Water = calculated_weekly_values[23]
			update.week_VitaminB1 = calculated_weekly_values[24]
			update.week_VitaminB2 = calculated_weekly_values[25]
			update.week_VitaminB3 = calculated_weekly_values[26]
			update.week_VitaminB3NiacinEquivalents = calculated_weekly_values[27]
			update.week_VitaminB6 = calculated_weekly_values[28]
			update.week_VitaminB12 = calculated_weekly_values[29]
			update.week_Biotin = calculated_weekly_values[30]
			update.week_Choline = calculated_weekly_values[31]
			update.week_Folate = calculated_weekly_values[32]
			update.week_FolateDFE = calculated_weekly_values[33]
			update.week_Folatefood = calculated_weekly_values[34]
			update.week_PantothenicAcid = calculated_weekly_values[35]
			update.week_VitaminC = calculated_weekly_values[36]
			update.week_VitaminAInternationalUnitsIU = calculated_weekly_values[37]
			update.week_VitaminAmcgRetinolActivityEquivalentsRAE = calculated_weekly_values[38]
			update.week_VitaminAmcgRetinolEquivalentsRE = calculated_weekly_values[39]
			update.week_RetinolmcgRetinolEquivalentsRE = calculated_weekly_values[40]
			update.week_CarotenoidmcgRetinolEquivalentsRE = calculated_weekly_values[41]
			update.week_AlphaCarotene = calculated_weekly_values[42]
			update.week_BetaCarotene = calculated_weekly_values[43]
			update.week_BetaCaroteneEquivalents = calculated_weekly_values[44]
			update.week_Cryptoxanthin = calculated_weekly_values[45]
			update.week_LuteinandZeaxanthin = calculated_weekly_values[46]
			update.week_Lycopene = calculated_weekly_values[47]
			update.week_VitaminDInternationalUnitsIU = calculated_weekly_values[48]
			update.week_VitaminDmcg = calculated_weekly_values[49]
			update.week_VitaminEmgAlphaTocopherolEquivalentsATE = calculated_weekly_values[50]
			update.week_VitaminEInternationalUnitsIU = calculated_weekly_values[51]
			update.week_VitaminEmg = calculated_weekly_values[52]
			update.week_VitaminK = calculated_weekly_values[53]
			update.week_Boron = calculated_weekly_values[54]
			update.week_Calcium = calculated_weekly_values[55]
			update.week_Chloride = calculated_weekly_values[56]
			update.week_Chromium = calculated_weekly_values[57]
			update.week_Copper = calculated_weekly_values[58]
			update.week_Fluoride = calculated_weekly_values[59]
			update.week_Iodine = calculated_weekly_values[60]
			update.week_Iron = calculated_weekly_values[61]
			update.week_Magnesium = calculated_weekly_values[62]
			update.week_Manganese = calculated_weekly_values[63]
			update.week_Molybdenum = calculated_weekly_values[64]
			update.week_Phosphorus = calculated_weekly_values[65]
			update.week_Potassium = calculated_weekly_values[66]
			update.week_Selenium = calculated_weekly_values[67]
			update.week_Sodium = calculated_weekly_values[68]
			update.week_Zinc = calculated_weekly_values[69]
			update.week_Omega3FattyAcids = calculated_weekly_values[70]
			update.week_Omega6FattyAcids = calculated_weekly_values[71]
			update.week_a141Myristoleic = calculated_weekly_values[72]
			update.week_a151Pentadecenoic = calculated_weekly_values[73]
			update.week_a161Palmitol = calculated_weekly_values[74]
			update.week_a171Heptadecenoic = calculated_weekly_values[75]
			update.week_a181Oleic = calculated_weekly_values[76]
			update.week_a201Eicosenoic = calculated_weekly_values[77]
			update.week_a221Erucic = calculated_weekly_values[78]
			update.week_a241Nervonic = calculated_weekly_values[79]
			update.week_a182Linoleic = calculated_weekly_values[80]
			update.week_a182ConjugatedLinoleicCLA = calculated_weekly_values[81]
			update.week_a183Linolenic = calculated_weekly_values[82]
			update.week_a184Stearidonic = calculated_weekly_values[83]
			update.week_a203Eicosatrienoic = calculated_weekly_values[84]
			update.week_a204Arachidonic = calculated_weekly_values[85]
			update.week_a205EicosapentaenoicEPA = calculated_weekly_values[86]
			update.week_a225DocosapentaenoicDPA = calculated_weekly_values[87]
			update.week_a226DocosahexaenoicDHA = calculated_weekly_values[88]
			update.week_a40Butyric = calculated_weekly_values[89]
			update.week_a60Caproic = calculated_weekly_values[90]
			update.week_a80Caprylic = calculated_weekly_values[91]
			update.week_a100Capric = calculated_weekly_values[92]
			update.week_a120Lauric = calculated_weekly_values[93]
			update.week_a140Myristic = calculated_weekly_values[94]
			update.week_a150Pentadecanoic = calculated_weekly_values[95]
			update.week_a160Palmitic = calculated_weekly_values[96]
			update.week_a170Margaric = calculated_weekly_values[97]
			update.week_a180Stearic = calculated_weekly_values[98]
			update.week_a200Arachidic = calculated_weekly_values[99]
			update.week_a220Behenate = calculated_weekly_values[100]
			update.week_a240Lignoceric = calculated_weekly_values[101]
			update.week_Alanine = calculated_weekly_values[102]
			update.week_Arginine = calculated_weekly_values[103]
			update.week_AsparticAcid = calculated_weekly_values[104]
			update.week_Cysteine = calculated_weekly_values[105]
			update.week_GlutamicAcid = calculated_weekly_values[106]
			update.week_Glycine = calculated_weekly_values[107]
			update.week_Histidine = calculated_weekly_values[108]
			update.week_Isoleucine = calculated_weekly_values[109]
			update.week_Leucine = calculated_weekly_values[110]
			update.week_Lysine = calculated_weekly_values[111]
			update.week_Methionine = calculated_weekly_values[112]
			update.week_Phenylalanine = calculated_weekly_values[113]
			update.week_Proline = calculated_weekly_values[114]
			update.week_Serine = calculated_weekly_values[115]
			update.week_Threonine = calculated_weekly_values[116]
			update.week_Tryptophan = calculated_weekly_values[117]
			update.week_Tyrosine = calculated_weekly_values[118]
			update.week_Valine = calculated_weekly_values[119]
			update.week_Ash = calculated_weekly_values[120]
			update.week_OrganicAcidsTotal = calculated_weekly_values[121]
			update.week_AceticAcid = calculated_weekly_values[122]
			update.week_CitricAcid = calculated_weekly_values[123]
			update.week_LacticAcid = calculated_weekly_values[124]
			update.week_MalicAcid = calculated_weekly_values[125]
			update.week_Taurine = calculated_weekly_values[126]
			update.week_SugarAlcoholsTotal = calculated_weekly_values[127]
			update.week_Glycerol = calculated_weekly_values[128]
			update.week_Inositol = calculated_weekly_values[129]
			update.week_Mannitol = calculated_weekly_values[130]
			update.week_Sorbitol = calculated_weekly_values[131]
			update.week_Xylitol = calculated_weekly_values[132]
			update.week_ArtificialSweetenersTotal = calculated_weekly_values[133]
			update.week_Aspartame = calculated_weekly_values[134]
			update.week_Saccharin = calculated_weekly_values[135]
			update.week_Alcohol = calculated_weekly_values[136]
			update.week_Caffeine = calculated_weekly_values[137]

			update.save()


			# then update the weekly fields with pk just like in the load scraping module	
		else:
			# filter for that pk, then update the values like in load module	
			update = Item.objects.filter(pk=pk)[0]
			
			update.cost_based_on_grams = cost_based_on_grams
			update.cost_based_on_cal = cost_based_on_cal
			update.weekly_cost = weekly_cost
			update.cost_per_g_protein = cost_per_g_protein
			update.cost_per_g_fiber = cost_per_g_fiber

			update.name = form_data[0]
			update.recipe = form_data[1]
			update.grams = form_data[2]
			update.weekly_grams = weekly_grams
			update.units = form_data[3]
			update.conversion = form_data[4]
			update.cost_per_100_cal = form_data[5]
			update.cost_per_gram = form_data[6]
			update.monday_1 = form_data[7]
			update.monday_2 = form_data[8]
			update.monday_3 = form_data[9]
			update.tuesday_1 = form_data[10]
			update.tuesday_2 = form_data[11]
			update.tuesday_3 = form_data[12]
			update.wednesday_1 = form_data[13]
			update.wednesday_2 = form_data[14]
			update.wednesday_3 = form_data[15]
			update.thursday_1 = form_data[16]
			update.thursday_2 = form_data[17]
			update.thursday_3 = form_data[18]
			update.friday_1 = form_data[19]
			update.friday_2 = form_data[20]
			update.friday_3 = form_data[21]
			update.saturday_1 = form_data[22]
			update.saturday_2 = form_data[23]
			update.saturday_3 = form_data[24]
			update.sunday_1 = form_data[25]
			update.sunday_2 = form_data[26]
			update.sunday_3 = form_data[27]

			update.Protein = calculated_daily_values[0]
			update.Carbohydrates = calculated_daily_values[1]
			update.Fattotal = calculated_daily_values[2]
			update.DietaryFiber = calculated_daily_values[3]
			update.Calories = calculated_daily_values[4]
			update.Starch = calculated_daily_values[5]
			update.TotalSugars = calculated_daily_values[6]
			update.Monosaccharides = calculated_daily_values[7]
			update.Fructose = calculated_daily_values[8]
			update.Glucose = calculated_daily_values[9]
			update.Galactose = calculated_daily_values[10]
			update.Disaccharides = calculated_daily_values[11]
			update.Lactose = calculated_daily_values[12]
			update.Maltose = calculated_daily_values[13]
			update.Sucrose = calculated_daily_values[14]
			update.SolubleFiber = calculated_daily_values[15]
			update.InsolubleFiber = calculated_daily_values[16]
			update.OtherCarbohydrates = calculated_daily_values[17]
			update.MonounsaturatedFat = calculated_daily_values[18]
			update.PolyunsaturatedFat = calculated_daily_values[19]
			update.SaturatedFat = calculated_daily_values[20]
			update.TransFat = calculated_daily_values[21]
			update.Cholesterol = calculated_daily_values[22]
			update.Water = calculated_daily_values[23]
			update.VitaminB1 = calculated_daily_values[24]
			update.VitaminB2 = calculated_daily_values[25]
			update.VitaminB3 = calculated_daily_values[26]
			update.VitaminB3NiacinEquivalents = calculated_daily_values[27]
			update.VitaminB6 = calculated_daily_values[28]
			update.VitaminB12 = calculated_daily_values[29]
			update.Biotin = calculated_daily_values[30]
			update.Choline = calculated_daily_values[31]
			update.Folate = calculated_daily_values[32]
			update.FolateDFE = calculated_daily_values[33]
			update.Folatefood = calculated_daily_values[34]
			update.PantothenicAcid = calculated_daily_values[35]
			update.VitaminC = calculated_daily_values[36]
			update.VitaminAInternationalUnitsIU = calculated_daily_values[37]
			update.VitaminAmcgRetinolActivityEquivalentsRAE = calculated_daily_values[38]
			update.VitaminAmcgRetinolEquivalentsRE = calculated_daily_values[39]
			update.RetinolmcgRetinolEquivalentsRE = calculated_daily_values[40]
			update.CarotenoidmcgRetinolEquivalentsRE = calculated_daily_values[41]
			update.AlphaCarotene = calculated_daily_values[42]
			update.BetaCarotene = calculated_daily_values[43]
			update.BetaCaroteneEquivalents = calculated_daily_values[44]
			update.Cryptoxanthin = calculated_daily_values[45]
			update.LuteinandZeaxanthin = calculated_daily_values[46]
			update.Lycopene = calculated_daily_values[47]
			update.VitaminDInternationalUnitsIU = calculated_daily_values[48]
			update.VitaminDmcg = calculated_daily_values[49]
			update.VitaminEmgAlphaTocopherolEquivalentsATE = calculated_daily_values[50]
			update.VitaminEInternationalUnitsIU = calculated_daily_values[51]
			update.VitaminEmg = calculated_daily_values[52]
			update.VitaminK = calculated_daily_values[53]
			update.Boron = calculated_daily_values[54]
			update.Calcium = calculated_daily_values[55]
			update.Chloride = calculated_daily_values[56]
			update.Chromium = calculated_daily_values[57]
			update.Copper = calculated_daily_values[58]
			update.Fluoride = calculated_daily_values[59]
			update.Iodine = calculated_daily_values[60]
			update.Iron = calculated_daily_values[61]
			update.Magnesium = calculated_daily_values[62]
			update.Manganese = calculated_daily_values[63]
			update.Molybdenum = calculated_daily_values[64]
			update.Phosphorus = calculated_daily_values[65]
			update.Potassium = calculated_daily_values[66]
			update.Selenium = calculated_daily_values[67]
			update.Sodium = calculated_daily_values[68]
			update.Zinc = calculated_daily_values[69]
			update.Omega3FattyAcids = calculated_daily_values[70]
			update.Omega6FattyAcids = calculated_daily_values[71]
			update.a141Myristoleic = calculated_daily_values[72]
			update.a151Pentadecenoic = calculated_daily_values[73]
			update.a161Palmitol = calculated_daily_values[74]
			update.a171Heptadecenoic = calculated_daily_values[75]
			update.a181Oleic = calculated_daily_values[76]
			update.a201Eicosenoic = calculated_daily_values[77]
			update.a221Erucic = calculated_daily_values[78]
			update.a241Nervonic = calculated_daily_values[79]
			update.a182Linoleic = calculated_daily_values[80]
			update.a182ConjugatedLinoleicCLA = calculated_daily_values[81]
			update.a183Linolenic = calculated_daily_values[82]
			update.a184Stearidonic = calculated_daily_values[83]
			update.a203Eicosatrienoic = calculated_daily_values[84]
			update.a204Arachidonic = calculated_daily_values[85]
			update.a205EicosapentaenoicEPA = calculated_daily_values[86]
			update.a225DocosapentaenoicDPA = calculated_daily_values[87]
			update.a226DocosahexaenoicDHA = calculated_daily_values[88]
			update.a40Butyric = calculated_daily_values[89]
			update.a60Caproic = calculated_daily_values[90]
			update.a80Caprylic = calculated_daily_values[91]
			update.a100Capric = calculated_daily_values[92]
			update.a120Lauric = calculated_daily_values[93]
			update.a140Myristic = calculated_daily_values[94]
			update.a150Pentadecanoic = calculated_daily_values[95]
			update.a160Palmitic = calculated_daily_values[96]
			update.a170Margaric = calculated_daily_values[97]
			update.a180Stearic = calculated_daily_values[98]
			update.a200Arachidic = calculated_daily_values[99]
			update.a220Behenate = calculated_daily_values[100]
			update.a240Lignoceric = calculated_daily_values[101]
			update.Alanine = calculated_daily_values[102]
			update.Arginine = calculated_daily_values[103]
			update.AsparticAcid = calculated_daily_values[104]
			update.Cysteine = calculated_daily_values[105]
			update.GlutamicAcid = calculated_daily_values[106]
			update.Glycine = calculated_daily_values[107]
			update.Histidine = calculated_daily_values[108]
			update.Isoleucine = calculated_daily_values[109]
			update.Leucine = calculated_daily_values[110]
			update.Lysine = calculated_daily_values[111]
			update.Methionine = calculated_daily_values[112]
			update.Phenylalanine = calculated_daily_values[113]
			update.Proline = calculated_daily_values[114]
			update.Serine = calculated_daily_values[115]
			update.Threonine = calculated_daily_values[116]
			update.Tryptophan = calculated_daily_values[117]
			update.Tyrosine = calculated_daily_values[118]
			update.Valine = calculated_daily_values[119]
			update.Ash = calculated_daily_values[120]
			update.OrganicAcidsTotal = calculated_daily_values[121]
			update.AceticAcid = calculated_daily_values[122]
			update.CitricAcid = calculated_daily_values[123]
			update.LacticAcid = calculated_daily_values[124]
			update.MalicAcid = calculated_daily_values[125]
			update.Taurine = calculated_daily_values[126]
			update.SugarAlcoholsTotal = calculated_daily_values[127]
			update.Glycerol = calculated_daily_values[128]
			update.Inositol = calculated_daily_values[129]
			update.Mannitol = calculated_daily_values[130]
			update.Sorbitol = calculated_daily_values[131]
			update.Xylitol = calculated_daily_values[132]
			update.ArtificialSweetenersTotal = calculated_daily_values[133]
			update.Aspartame = calculated_daily_values[134]
			update.Saccharin = calculated_daily_values[135]
			update.Alcohol = calculated_daily_values[136]
			update.Caffeine = calculated_daily_values[137]


			update.week_Protein = calculated_weekly_values[0]
			update.week_Carbohydrates = calculated_weekly_values[1]
			update.week_Fattotal = calculated_weekly_values[2]
			update.week_DietaryFiber = calculated_weekly_values[3]
			update.week_Calories = calculated_weekly_values[4]
			update.week_Starch = calculated_weekly_values[5]
			update.week_TotalSugars = calculated_weekly_values[6]
			update.week_Monosaccharides = calculated_weekly_values[7]
			update.week_Fructose = calculated_weekly_values[8]
			update.week_Glucose = calculated_weekly_values[9]
			update.week_Galactose = calculated_weekly_values[10]
			update.week_Disaccharides = calculated_weekly_values[11]
			update.week_Lactose = calculated_weekly_values[12]
			update.week_Maltose = calculated_weekly_values[13]
			update.week_Sucrose = calculated_weekly_values[14]
			update.week_SolubleFiber = calculated_weekly_values[15]
			update.week_InsolubleFiber = calculated_weekly_values[16]
			update.week_OtherCarbohydrates = calculated_weekly_values[17]
			update.week_MonounsaturatedFat = calculated_weekly_values[18]
			update.week_PolyunsaturatedFat = calculated_weekly_values[19]
			update.week_SaturatedFat = calculated_weekly_values[20]
			update.week_TransFat = calculated_weekly_values[21]
			update.week_Cholesterol = calculated_weekly_values[22]
			update.week_Water = calculated_weekly_values[23]
			update.week_VitaminB1 = calculated_weekly_values[24]
			update.week_VitaminB2 = calculated_weekly_values[25]
			update.week_VitaminB3 = calculated_weekly_values[26]
			update.week_VitaminB3NiacinEquivalents = calculated_weekly_values[27]
			update.week_VitaminB6 = calculated_weekly_values[28]
			update.week_VitaminB12 = calculated_weekly_values[29]
			update.week_Biotin = calculated_weekly_values[30]
			update.week_Choline = calculated_weekly_values[31]
			update.week_Folate = calculated_weekly_values[32]
			update.week_FolateDFE = calculated_weekly_values[33]
			update.week_Folatefood = calculated_weekly_values[34]
			update.week_PantothenicAcid = calculated_weekly_values[35]
			update.week_VitaminC = calculated_weekly_values[36]
			update.week_VitaminAInternationalUnitsIU = calculated_weekly_values[37]
			update.week_VitaminAmcgRetinolActivityEquivalentsRAE = calculated_weekly_values[38]
			update.week_VitaminAmcgRetinolEquivalentsRE = calculated_weekly_values[39]
			update.week_RetinolmcgRetinolEquivalentsRE = calculated_weekly_values[40]
			update.week_CarotenoidmcgRetinolEquivalentsRE = calculated_weekly_values[41]
			update.week_AlphaCarotene = calculated_weekly_values[42]
			update.week_BetaCarotene = calculated_weekly_values[43]
			update.week_BetaCaroteneEquivalents = calculated_weekly_values[44]
			update.week_Cryptoxanthin = calculated_weekly_values[45]
			update.week_LuteinandZeaxanthin = calculated_weekly_values[46]
			update.week_Lycopene = calculated_weekly_values[47]
			update.week_VitaminDInternationalUnitsIU = calculated_weekly_values[48]
			update.week_VitaminDmcg = calculated_weekly_values[49]
			update.week_VitaminEmgAlphaTocopherolEquivalentsATE = calculated_weekly_values[50]
			update.week_VitaminEInternationalUnitsIU = calculated_weekly_values[51]
			update.week_VitaminEmg = calculated_weekly_values[52]
			update.week_VitaminK = calculated_weekly_values[53]
			update.week_Boron = calculated_weekly_values[54]
			update.week_Calcium = calculated_weekly_values[55]
			update.week_Chloride = calculated_weekly_values[56]
			update.week_Chromium = calculated_weekly_values[57]
			update.week_Copper = calculated_weekly_values[58]
			update.week_Fluoride = calculated_weekly_values[59]
			update.week_Iodine = calculated_weekly_values[60]
			update.week_Iron = calculated_weekly_values[61]
			update.week_Magnesium = calculated_weekly_values[62]
			update.week_Manganese = calculated_weekly_values[63]
			update.week_Molybdenum = calculated_weekly_values[64]
			update.week_Phosphorus = calculated_weekly_values[65]
			update.week_Potassium = calculated_weekly_values[66]
			update.week_Selenium = calculated_weekly_values[67]
			update.week_Sodium = calculated_weekly_values[68]
			update.week_Zinc = calculated_weekly_values[69]
			update.week_Omega3FattyAcids = calculated_weekly_values[70]
			update.week_Omega6FattyAcids = calculated_weekly_values[71]
			update.week_a141Myristoleic = calculated_weekly_values[72]
			update.week_a151Pentadecenoic = calculated_weekly_values[73]
			update.week_a161Palmitol = calculated_weekly_values[74]
			update.week_a171Heptadecenoic = calculated_weekly_values[75]
			update.week_a181Oleic = calculated_weekly_values[76]
			update.week_a201Eicosenoic = calculated_weekly_values[77]
			update.week_a221Erucic = calculated_weekly_values[78]
			update.week_a241Nervonic = calculated_weekly_values[79]
			update.week_a182Linoleic = calculated_weekly_values[80]
			update.week_a182ConjugatedLinoleicCLA = calculated_weekly_values[81]
			update.week_a183Linolenic = calculated_weekly_values[82]
			update.week_a184Stearidonic = calculated_weekly_values[83]
			update.week_a203Eicosatrienoic = calculated_weekly_values[84]
			update.week_a204Arachidonic = calculated_weekly_values[85]
			update.week_a205EicosapentaenoicEPA = calculated_weekly_values[86]
			update.week_a225DocosapentaenoicDPA = calculated_weekly_values[87]
			update.week_a226DocosahexaenoicDHA = calculated_weekly_values[88]
			update.week_a40Butyric = calculated_weekly_values[89]
			update.week_a60Caproic = calculated_weekly_values[90]
			update.week_a80Caprylic = calculated_weekly_values[91]
			update.week_a100Capric = calculated_weekly_values[92]
			update.week_a120Lauric = calculated_weekly_values[93]
			update.week_a140Myristic = calculated_weekly_values[94]
			update.week_a150Pentadecanoic = calculated_weekly_values[95]
			update.week_a160Palmitic = calculated_weekly_values[96]
			update.week_a170Margaric = calculated_weekly_values[97]
			update.week_a180Stearic = calculated_weekly_values[98]
			update.week_a200Arachidic = calculated_weekly_values[99]
			update.week_a220Behenate = calculated_weekly_values[100]
			update.week_a240Lignoceric = calculated_weekly_values[101]
			update.week_Alanine = calculated_weekly_values[102]
			update.week_Arginine = calculated_weekly_values[103]
			update.week_AsparticAcid = calculated_weekly_values[104]
			update.week_Cysteine = calculated_weekly_values[105]
			update.week_GlutamicAcid = calculated_weekly_values[106]
			update.week_Glycine = calculated_weekly_values[107]
			update.week_Histidine = calculated_weekly_values[108]
			update.week_Isoleucine = calculated_weekly_values[109]
			update.week_Leucine = calculated_weekly_values[110]
			update.week_Lysine = calculated_weekly_values[111]
			update.week_Methionine = calculated_weekly_values[112]
			update.week_Phenylalanine = calculated_weekly_values[113]
			update.week_Proline = calculated_weekly_values[114]
			update.week_Serine = calculated_weekly_values[115]
			update.week_Threonine = calculated_weekly_values[116]
			update.week_Tryptophan = calculated_weekly_values[117]
			update.week_Tyrosine = calculated_weekly_values[118]
			update.week_Valine = calculated_weekly_values[119]
			update.week_Ash = calculated_weekly_values[120]
			update.week_OrganicAcidsTotal = calculated_weekly_values[121]
			update.week_AceticAcid = calculated_weekly_values[122]
			update.week_CitricAcid = calculated_weekly_values[123]
			update.week_LacticAcid = calculated_weekly_values[124]
			update.week_MalicAcid = calculated_weekly_values[125]
			update.week_Taurine = calculated_weekly_values[126]
			update.week_SugarAlcoholsTotal = calculated_weekly_values[127]
			update.week_Glycerol = calculated_weekly_values[128]
			update.week_Inositol = calculated_weekly_values[129]
			update.week_Mannitol = calculated_weekly_values[130]
			update.week_Sorbitol = calculated_weekly_values[131]
			update.week_Xylitol = calculated_weekly_values[132]
			update.week_ArtificialSweetenersTotal = calculated_weekly_values[133]
			update.week_Aspartame = calculated_weekly_values[134]
			update.week_Saccharin = calculated_weekly_values[135]
			update.week_Alcohol = calculated_weekly_values[136]
			update.week_Caffeine = calculated_weekly_values[137]

			update.save()





		return('ok')