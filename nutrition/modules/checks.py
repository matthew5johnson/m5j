def confirm_table_is_correct(list1):
    # The table with all of the nutrition is usually found as the last table on the webpage. 
    # So we're using the nutrition_table variable (above) to find it
    # but we want to make sure the table it finds is actually the one that we want, which should have 332 items
    if len(list1) == 332:
        return("Success: The correct table has been found and scraped from the website")
    else:
        return("ERROR: The wrong table has been scraped from the website")

def sanity_check(list1, list2):
    if len(list1) == len(list2):
        return("Success: The two lists are the same length")
    else:
        return("ERROR: The two lists are different lengths")