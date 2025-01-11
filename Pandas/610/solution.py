import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def can_form_triangle(row):
        x, y, z = row['x'], row['y'], row['z']
        return (x + y > z) and (x + z > y) and (y + z > x)

    triangle['Triangle'] = triangle.apply(can_form_triangle, axis=1).replace({True: 'Yes', False: 'No'})    
    return triangle
