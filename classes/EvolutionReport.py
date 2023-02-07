import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import json
import seaborn as sns
import pandas as pd
import io



class EvolutionReport():
    def __init__(self, pt):
        self.pt = pt

    def get_weights(self):

        
        weights = [(bio.DATE_TIMES, bio.WEIGHT) for bio in self.pt.bios]
        dict = {k:v for (k,v) in weights}
        df = pd.DataFrame.from_dict(dict,orient = 'index')
        df["date_time"] = pd.to_datetime(df.index)
        #df["date"] = df["date_time"].dt.strftime("%d/%m/%Y")
        df.set_index("date_time",inplace=True)
        #df.sort_values("date")
       # df.drop(columns=["date_time"],inplace=True)
        df.rename(columns={0: "weight"}, inplace=True)
        
        #df.reset_index()
        print(df)

        #Plotar grafico
        plt.switch_backend('Agg')
        plt.figure(figsize=(10, 15))
        plt.title('Evolução')
        plt.xticks(rotation=90)
        sns.set_theme(style="darkgrid")
        sns.lineplot(data=df, x="date_time", y="weight", linewidth=2.5)
        plt.xlabel('Data')
        plt.ylabel('Peso')
        

        #Salvar imagem na memoria
        obj = io.BytesIO()
        plt.savefig(obj, format='png', dpi=100)
        obj.seek(0)

        img = Image.open(obj)
        if img.mode == 'RGBA':
                img = img.convert('RGB')
        # img.show()
        plt.close()
        return img