from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

from nutrition.modules.checks import confirm_table_is_correct, sanity_check



class Scrape:

  def table(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # This site tries to prevent scraping by checking UAs
    page_content = urlopen(req).read()

    # page = urlopen(url)
    # page_content = page.read()
    soup = BeautifulSoup(page_content, 'lxml')

    tables = soup.findChildren('table')
    nutrition_table = tables[len(tables)-1]
    rows = nutrition_table.find_all(['th', 'tr'])
    website_scrape = []
    for row in rows:
      cells = row.findChildren('td')
      for cell in cells:
        website_scrape.append(cell.text)

    test_1 = confirm_table_is_correct(website_scrape)

    header = ['Protein', 'Carbohydrates', 'Fat - total', 'Dietary Fiber', 'Calories', 'Starch', 'Total Sugars', 'Monosaccharides',\
            'Fructose', 'Glucose', 'Galactose', 'Disaccharides', 'Lactose', 'Maltose', 'Sucrose', 'Soluble Fiber',\
            'Insoluble Fiber', 'Other Carbohydrates', 'Monounsaturated Fat', 'Polyunsaturated Fat',\
            'Saturated Fat', 'Trans Fat', 'Cholesterol', 'Water', 'Vitamin B1', 'Vitamin B2',\
            'Vitamin B3', 'Vitamin B3 (Niacin Equivalents)', 'Vitamin B6', 'Vitamin B12', 'Biotin',\
            'Choline', 'Folate', 'Folate (DFE)', 'Folate (food)', 'Pantothenic Acid', 'Vitamin C',\
            'Vitamin A International Units (IU)', 'Vitamin A mcg Retinol Activity Equivalents (RAE)',\
            'Vitamin A mcg Retinol Equivalents (RE)', 'Retinol mcg Retinol Equivalents (RE)', 'Carotenoid mcg Retinol Equivalents (RE)',\
            'Alpha-Carotene', 'Beta-Carotene', 'Beta-Carotene Equivalents', 'Cryptoxanthin',\
            'Lutein and Zeaxanthin', 'Lycopene', 'Vitamin D International Units (IU)', 'Vitamin D mcg',\
            'Vitamin E mg Alpha-Tocopherol Equivalents (ATE)', 'Vitamin E International Units (IU)', 'Vitamin E mg',\
            'Vitamin K', 'Boron', 'Calcium', 'Chloride', 'Chromium', 'Copper', 'Fluoride',\
            'Iodine', 'Iron', 'Magnesium', 'Manganese', 'Molybdenum', 'Phosphorus', 'Potassium', 'Selenium',\
            'Sodium', 'Zinc', 'Omega-3 Fatty Acids', 'Omega-6 Fatty Acids', '14:1 Myristoleic',\
            '15:1 Pentadecenoic', '16:1 Palmitol', '17:1 Heptadecenoic', '18:1 Oleic', '20:1 Eicosenoic', '22:1 Erucic',\
            '24:1 Nervonic', '18:2 Linoleic', '18:2 Conjugated Linoleic (CLA)', '18:3 Linolenic', '18:4 Stearidonic',\
            '20:3 Eicosatrienoic', '20:4 Arachidonic', '20:5 Eicosapentaenoic (EPA)', '22:5 Docosapentaenoic (DPA)',\
            '22:6 Docosahexaenoic (DHA)', '4:0 Butyric', '6:0 Caproic', '8:0 Caprylic', '10:0 Capric', '12:0 Lauric',\
            '14:0 Myristic', '15:0 Pentadecanoic', '16:0 Palmitic', '17:0 Margaric', '18:0 Stearic', '20:0 Arachidic',\
            '22:0 Behenate', '24:0 Lignoceric', 'Alanine', 'Arginine', 'Aspartic Acid', 'Cysteine', 'Glutamic Acid',\
            'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline',\
            'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine', 'Ash', 'Organic Acids (Total)', 'Acetic Acid',\
            'Citric Acid', 'Lactic Acid', 'Malic Acid', 'Taurine', 'Sugar Alcohols (Total)', 'Glycerol', 'Inositol',\
            'Mannitol', 'Sorbitol', 'Xylitol', 'Artificial Sweeteners (Total)', 'Aspartame', 'Saccharin', 'Alcohol',\
            'Caffeine']

    raw_values = []
    for i in header:
        for m in website_scrape:
            if i == m:
                index_of_interest = website_scrape.index(m) + 1
                raw_values.append(website_scrape[index_of_interest])


    test_2 = sanity_check(header, raw_values)    

    units = []
    for i in range(0, len(raw_values)):
        item_unit = ''.join(re.findall(r'(?<=\s)[a-zA-Z()\s]*', raw_values[i]))
        units.append(item_unit)
        
    values = []
    for i in range(0, len(raw_values)):
        item_value = ''.join(re.findall(r'[0-9.-]*', raw_values[i]))
        values.append(item_value)
    for i in values:
        if i == '--':
            index = values.index(i)
            values[index] = 0
    
    test_3 = sanity_check(units, values)


    print(test_1, test_2, test_3)

    return(values, units, test_1, test_2, test_3)