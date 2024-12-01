import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').agg(student_count=('student', 'count')).reset_index()
    return df[df['student_count'] >= 5][['class']]
