def is_year_leap(year):
    if year % 4 == 0:
       return True 
    else:
        return False
    
result = is_year_leap(2022)
print("год 2022:", result)