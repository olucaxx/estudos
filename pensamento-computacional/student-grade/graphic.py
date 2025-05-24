import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notas_alunos.csv')
print(df)

df[['P1', 'P2', 'EXAME']].mean().plot(kind='bar', title='Média das Notas')
plt.show()

df['SITUAÇÃO'].value_counts().plot(kind='pie', title="Situação Alunos")
plt.ylabel('')
plt.show()