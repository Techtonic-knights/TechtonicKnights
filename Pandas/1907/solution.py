import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 20000, 50001, float('inf')]
    labels = ['Low Salary', 'Average Salary', 'High Salary']
    
    accounts['salary_category'] = pd.cut(accounts['income'], bins=bins, labels=labels, right=False)
    
    category_counts = accounts['salary_category'].value_counts().reset_index()
    
    category_counts.columns = ['category', 'accounts_count']
    
    return category_counts
