import pandas as pd
import sqlalchemy

col_names = ['Id','Birth','Educat','Maritial','Income','Kidhome','Teenhome','Dr',
             'Recency','Wines','Fruits','Meat', 'Fish', 'Sweet', 'Gold', 'Deals',
             'Web', 'Catalog', 'Store', 'WebVisits']

marketing = pd.read_csv('marketing_campaign.csv', sep='\t')
print(marketing.head())