import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    
    # Calculate number of rows and columns
    num_rows, num_columns = players.shape
    result = [num_rows, num_columns]
    return result