import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import json
import seaborn as sns
import pandas as pd
import io

class EvolutionReport():
    def __init__(self, pt):
        self.pt = pt

    def get_evolution(self):
        df_array = [self.get_weights(), self.get_fat_mass(), self.get_lean_mass()]
        x_label_array = ["date", "date", "date"]
        y_label_array = ["weight", "fat_mass", "lean_mass"]
        return self.plot_images(df_array, x_label_array, y_label_array)

    def plot_sns(self, df_array, x_label_array, y_label_array):
        for df, x_label, y_label in zip(df_array, x_label_array, y_label_array):
            ax = sns.lineplot(
                data=df, 
                x=x_label, 
                y=y_label, 
                linewidth=2.5,
                label = y_label
                )
            for i, point in df.iterrows():
                ax.text(point[x_label], point[y_label], str(point[y_label]), fontsize=10)

            # plt.xlabel("Date")
            # plt.ylabel("Kg")
            # plt.legend()

    def plot_images(self, df_array, x_label_array, y_label_array):
        plt.switch_backend('Agg')
        plt.figure(figsize=(10, 15))
        plt.title("Evolução")
        plt.xticks(rotation=90)
        # sns.set_theme(style="darkgrid")
        sns.set_style("ticks")
        self.plot_sns(df_array, x_label_array, y_label_array)
        plt.xlabel("Date")
        plt.ylabel("Kg")
        plt.legend()
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

        

    def get_weights(self):

        weights = [(bio.DATE_TIMES, bio.WEIGHT) for bio in self.pt.bios]
        dict = {k:v for (k,v) in weights}
        df = self.get_df_from(dict)
        df.rename(columns={0: "weight"}, inplace=True)
        # print(df)
        # img = self.plot_image(df, "date_time", "weight", "Evolução")
        return df

    def get_fat_mass(self):

        fat_mass = [(bio.DATE_TIMES, bio.Fat) for bio in self.pt.bios]
        dict = {k:v for (k,v) in fat_mass}
        df = self.get_df_from(dict)
        df.rename(columns={0: "fat_mass"}, inplace=True)
        # print(df)
        # img = self.plot_image(df, "date_time", "fat_mass", "Evolução")
        return df

    def get_lean_mass(self):

        lean_mass = [(bio.DATE_TIMES, bio.SMM_Skeletal_Muscle_Mass_) for bio in self.pt.bios]
        dict = {k:v for (k,v) in lean_mass}
        df = self.get_df_from(dict)
        df.rename(columns={0: "lean_mass"}, inplace=True)
        # print(df)
        return df

    def get_df_from(self, dict):
        df = pd.DataFrame.from_dict(dict,orient = 'index')
        df["date_time"] = pd.to_datetime(df.index)
        df["date"] = df["date_time"].dt.strftime("%d/%m/%Y")
        df.set_index("date_time",inplace=True)
        df.sort_values("date_time", ascending=True, inplace=True)
        return df

    def get_images(self):
        df_array = [self.get_weights(), self.get_fat_mass(), self.get_lean_mass()]
        x_label_array = ["date", "date", "date"]
        y_label_array = ["Peso", "Gordura", "Musculo"]
        return self.plot_images(df_array, x_label_array, y_label_array)

    

    