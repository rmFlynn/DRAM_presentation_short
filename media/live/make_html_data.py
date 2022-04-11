import pandas as pd
from pretty_html_table import build_table

df = pd.read_csv("annotations.tsv", sep='\t', index_col=0)
df = df.head(200)
html_table_blue_light = build_table(df, 'blue_light')
print(html_table_blue_light)
with open('annotations.html', 'w') as f:
    f.write(html_table_blue_light)

df = pd.read_csv("./genome_stats.tsv", sep='\t', index_col=0)
df = df.head(200)
html_table_blue_light = build_table(df, 'blue_light')
print(html_table_blue_light)
with open('genome_stats.html', 'w') as f:
    f.write(html_table_blue_light)

