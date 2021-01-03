# Create a function that converts a date
# formatted as MM/DD/YYYY to YYYYDDMM.

def format_date(date):

    date = date.split("/")
    return date[2] + date[1] +date[0]
print(format_date("11/12/2019"))
