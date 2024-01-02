import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    
    # Displaying the first 3 rows of the DataFrame
    first_three_rows = employees.head(3)
    return first_three_rows