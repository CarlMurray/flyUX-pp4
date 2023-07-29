from datetime import datetime, timedelta

def create_alt_date_range(leg_date):
    """
    Function used to create new list of dates for alternate date selector on flight search results page when HTMX request made

    Args:
        leg_date (datetime): The departure date of the outbound/return flight

    Returns:
        list: A list of specified length containing new dates to show in alternate date selector in DOM
    """
    slider_date_list = [] 
    # DEFINES AMOUNT OF DATES TO GENERATE
    slider_date_range = range(-2, 3)
    for x in slider_date_range:
        # CREATES DATETIME AND ADDS/SUBTRACTS 1 DAY
        date = datetime.strptime(leg_date, '%Y-%m-%d') + timedelta(days=x)
        slider_date_list.append(date)
    return slider_date_list