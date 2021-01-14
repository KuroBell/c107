import pandas as pd
import csv
import plotly.express as px

df=pd.read_csv("c107.csv")
print(df.groupby("level")["attempt"].mean())
m = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig = px.scatter(m,x="student_id",y="level",size="attempt",color="attempt")

fig.show()
