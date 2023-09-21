def format_name (first_name:str,last_name:str) -> str :
    return last_name+", "+first_name

def to_listing (first_name:str,last_name:str,phone_number:int) -> str:
    return format_name(first_name,last_name,) + ": "+ phone_number


print (to_listing("Mafu","Shixyuu","123"))
