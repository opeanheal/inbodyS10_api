from classes.BaseReportBio import BaseReportBio
from classes.Utils import Utils
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class ReportBioStandard(BaseReportBio):
        
         
        def get_texts(self):
                options = {
                        'pt': [f'Circunferência da cintura estimada pela bioimpedância - {self.waist_cir} cm',
                        '-------',
                        f'Água Corporal Total - {self.TBW_Total_Body_Water} litros (esperado de {self.TBW_min} a {self.TBW_min} litros)',
                        'É o volume total de água no corpo. A soma da água intracelular e extracelular.',
                        f'Água Extracelular - É a quantidade de água fora das células',
                        f'Água Intracelular - É a quantidade de água dentro das células',
                        '-------',
                        f'Músculo Esquelético - A massa de músculo esquelético é computada baseada na massa de músculos dos membros, que é quase toda',
                        'composta de músculo esquelético e é cerca de 70% da quantidade de músculo do corpo inteiro.',
                        '-------',
                        f'Índice de edema - {self.ECW_TBW_Total}',
                        'A medida da quantidade de água intracelular e extracelular separadamente permite a avaliação do balanço dos níveis de água.',
                        'A taxa (água extracelular / água corporal total) pode ser avaliada não somente em cada parte do corpo, mas também no corpo inteiro.',
                        'Pessoas saudáveis se mantem em certo equilíbrio entre os compartimentos intra e extracelular com relação a quantidade de agua.',
                        'No entanto, se a quantidade de agua no compartimento extracelular se eleva, poderá ocorrer edema.',
                        'A taxa normal para ECW/TBW (índice de edema) é considerada 0.36 a 0.39.',
                        'Valores entre 0.39 e 0.40 significa edema leve e acima de 0.40 edema.',
                        'Índice de edema = água extracelular / água corporal total',
                        '-----',
                        'Parâmetros Nutricionais',
                        f'Taxa metabólica basal - {self.BMR} Kcal nas 24 horas',
                        f'Massa Celular Corporal - {self.Body_Cell_Mass} Kg (esperado de {self.BCM_min} a {self.BCM_max} Kg)',
                        f'Área de gordura viceral - {self.VFA} cm2',
                        'A gordura no corpo é dividida em categorias dependendo da localização da gordura: gordura viceral, gordura subcutânea e a gordura entre',
                        'os músculos. Um individuo com uma área de gordura viceral maior que 100cm2 é considerado ser abdominalmente obeso do compartimento',
                        'da gordura viceral.',
                        "-----",
                        'Dados colhidos na frequência de 50Khz:',
                        f'Reactância do corpo inteiro (X) -  {Utils.whole_body_reactance(self.raz,self.rtz,self.rlz):.2f} Ohm',
                        f'Resistência do corpo inteiro (R) -  {Utils.resistence(Utils.whole_body_impedance(self.rai,self.rti,self.rli),Utils.whole_body_reactance(self.raz,self.rtz,self.rlz)):.2f} Ohm',
                        f'Angulo de fase corporal total - {self.ang:.2f} graus',
                        "------",
                        f'BIVA'
                        f'Resistência(R) por metro(altura) - {self.x:.2f}',
                        f'Reactância(X) por metro(altura) - {self.y:.2f}']}

                return options[self.language]


        def show(self, size):
                
                positions = {
                        "rel_lines" : [0.037 ,0.0815, 0.1, 0.16, 0.18, 0.1975, 0.215, 0.2325, 0.297, 0.322, 0.347, 0.372, 0.397, 0.46, 0.482, 0.506, 0.529, 0.553],
                        "rel_lines_txt" : [0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94],
                        "rel_column_0" : [0.25],
                        "rel_column_1" : [0.1, 0.32, 0.5],
                        "rel_column_2" : [0.22, 0.3, 0.380, 0.61, 0.71, 0.8, 0.9],
                        "rel_column_bar" : [0.49],
                        "rel_column_txt" : [0.05]
                        }
  
  
                image_path = "assets/images/folha_result_inbody_s10.jpg"
                font_location = "assets/fonts/arial.ttf"

                # Open an Image
                img = Image.open(image_path)
                img = img.resize(size)
                x, y = img.size
                font_size = int(0.009 * y)
                font = ImageFont.truetype(font_location, font_size)
                font_name_size = int(0.012 * y)
                font_name = ImageFont.truetype(font_location, font_name_size)
                font_txt_size = int(0.007 * y)
                font_txt = ImageFont.truetype(font_location, font_txt_size)
                # Call draw Method to add 2D graphics in an image
                I1 = ImageDraw.Draw(img)
                # Add Text to an image
                # Lines
                rel_lines = positions['rel_lines']
                lines = [int(i*y) for i in rel_lines]
                rel_lines_txt = positions['rel_lines_txt']
                lines_txt = [int(i*y) for i in rel_lines_txt]
                # Columns
                rel_column_0 = positions['rel_column_0']
                column_0 = [int(i*x) for i in rel_column_0]
                rel_column_1 = positions['rel_column_1']
                column_1 = [int(i*x) for i in rel_column_1]
                rel_column_2 = positions['rel_column_2']
                column_2 = [int(i*x) for i in rel_column_2]
                rel_column_bar = positions['rel_column_bar']
                column_bar = [int(i*x) for i in rel_column_bar]
                rel_column_txt = positions['rel_column_txt']
                column_txt = [int(i*x) for i in rel_column_txt]
                # Text Lines
                texts = self.get_texts()
                # Name
                I1.text((column_0[0], lines[0]), self.name,
                        font=font_name,  fill=self.get_color('std'))
                # Ids
                I1.text((column_1[0], lines[1]), self.id,
                        font=font,  fill=self.get_color('std'))
                I1.text((column_1[1], lines[1]),
                        f'{self.heigth} cm', font=font, fill=self.get_color('std'))
                I1.text((column_1[2], lines[1]), self.date,
                        font=font, fill=self.get_color('std'))
                I1.text((column_1[0], lines[2]),
                        f'{self.age} anos', font=font, fill=self.get_color('std'))
                I1.text((column_1[1], lines[2]), self.sex,
                        font=font, fill=self.get_color('std'))
                # Corporal Composition Analisis
                I1.text((column_2[0], lines[3]), 'litros',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[3]), self.icw,
                        font=font, fill=self.get_color(self.cat_ICW))
                I1.text((column_2[2], lines[3]),
                        f'{self.icw_min} - {self.icw_max}', font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[4]), 'litros',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[4]), self.ecw,
                        font=font, fill=self.get_color(self.cat_ECW))
                I1.text((column_2[2], lines[4]),
                        f'{self.ecw_min} - {self.ecw_max}', font=font, fill=self.get_color('std'))
                I1.text((column_2[3], lines[4]), self.tbw,
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[5]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[5]), self.protein,
                        font=font, fill=self.get_color(self.cat_protein))
                I1.text((column_2[2], lines[5]),
                        f'{self.protein_min} - {self.protein_max}', font=font, fill=self.get_color('std'))
                I1.text((column_2[4], lines[5]), self.SLM_Soft_Lean_Mass,
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[6]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[6]), self.mineral,
                        font=font, fill=self.get_color(self.cat_mineral))
                I1.text((column_2[2], lines[6]),
                        f'{self.mineral_min} - {self.mineral_max}', font=font, fill=self.get_color('std'))
                I1.text((column_2[5], lines[6]), self.FFM_Fat_Free_Mass,
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[7]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[7]), self.fat,
                        font=font, fill=self.get_color(self.cat_fat))
                I1.text((column_2[2], lines[7]),
                        f'{self.fat_min} - {self.fat_max}', font=font, fill=self.get_color('std'))
                I1.text((column_2[6], lines[7]), self.weight,
                        font=font, fill=self.get_color('std'))
                # Fat-muscle analisis
                I1.text((column_2[0], lines[8]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[8]), self.weight,
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[2], lines[8]),
                        f'{self.weight_min} - {self.weight_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[8]), self.get_bars(
                        self.cat_weight), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[9]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[9]), self.SMM_Skeletal_Muscle_Mass,
                        font=font, fill=self.get_color(self.cat_SMM))
                I1.text((column_2[2], lines[9]),
                        f'{self.SMM_min} - {self.SMM_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[9]), self.get_bars(
                        self.cat_SMM), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[10]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[10]), self.fat,
                        font=font, fill=self.get_color(self.cat_fat))
                I1.text((column_2[2], lines[10]),
                        f'{self.fat_min} - {self.fat_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[10]), self.get_bars(
                        self.cat_fat), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[11]), '%',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[11]), self.PBF_Percent_Body_Fat,
                        font=font, fill=self.get_color(self.cat_PBF))
                I1.text((column_2[2], lines[11]),
                        f'{self.PBF_min} - {self.PBF_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[11]), self.get_bars(
                        self.cat_PBF), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[12]), 'Kg/m2',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[12]), self.BMI,
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[2], lines[12]),
                        f'{self.BMI_min} - {self.BMI_max}', font=font, fill=self.get_color('std'))
                #I1.text((column_bar[0],lines[12]), '', font = font, fill = self.get_color('std'))
                # Segmentar analisis
                I1.text((column_2[0], lines[13]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[13]), self.Segmental_Lean_LA,
                        font=font, fill=self.get_color(self.cat_Segmental_Lean_LA))
                I1.text((column_2[2], lines[13]),
                        f'{self.Segmental_Lean_LA_min} - {self.Segmental_Lean_LA_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[13]), self.get_bars(
                self.cat_Segmental_Lean_LA), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[14]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[14]), self.Segmental_Lean_LA,
                        font=font, fill=self.get_color(self.cat_Segmental_Lean_LA))
                I1.text((column_2[2], lines[14]),
                        f'{self.Segmental_Lean_LA_min} - {self.Segmental_Lean_LA_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[14]), self.get_bars(
                self.cat_Segmental_Lean_LA), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[15]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[15]), self.Segmental_Lean_TR,
                        font=font, fill=self.get_color(self.cat_Segmental_Lean_TR))
                I1.text((column_2[2], lines[15]),
                        f'{self.Segmental_Lean_TR_min} - {self.Segmental_Lean_TR_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[15]), self.get_bars(
                self.cat_Segmental_Lean_TR), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[16]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[16]), self.Segmental_Lean_RL,
                        font=font, fill=self.get_color(self.cat_Segmental_Lean_RL))
                I1.text((column_2[2], lines[16]),
                        f'{self.Segmental_Lean_RL_min} - {self.Segmental_Lean_RL_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[16]), self.get_bars(
                self.cat_Segmental_Lean_RL), font=font, fill=self.get_color('std'))
                I1.text((column_2[0], lines[17]), 'Kg',
                        font=font, fill=self.get_color('std'))
                I1.text((column_2[1], lines[17]), self.Segmental_Lean_LL,
                        font=font, fill=self.get_color(self.cat_Segmental_Lean_LL))
                I1.text((column_2[2], lines[17]),
                        f'{self.Segmental_Lean_LL_min} - {self.Segmental_Lean_LL_max}', font=font, fill=self.get_color('std'))
                I1.text((column_bar[0], lines[17]), self.get_bars(
                self.cat_Segmental_Lean_LL), font=font, fill=self.get_color('std'))
                # Text line by line
                I1.text((column_txt[0], lines_txt[0]),  texts[0],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[1]),  texts[1],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[2]),  texts[2],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[3]),  texts[3],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[4]),  texts[4],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[5]),  texts[5],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[6]),  texts[6],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[7]),  texts[7],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[8]),  texts[8],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[9]),  texts[9],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[10]), texts[10],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[11]), texts[11],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[12]), texts[12],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[13]), texts[13],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[14]), texts[14],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[15]), texts[15],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[16]), texts[16],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[17]), texts[17],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[18]), texts[18],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[19]), texts[19],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[20]), texts[20],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[21]), texts[21],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[22]), texts[22],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[23]), texts[23],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[24]), texts[24],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[25]), texts[25],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[26]), texts[26],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[27]), texts[27],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[28]), texts[28],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[29]), texts[29],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[30]), texts[30],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[31]), texts[31],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[32]), texts[32],
                        font=font_txt, fill=self.get_color('std'))
                I1.text((column_txt[0], lines_txt[33]), texts[33],
                        font=font_txt, fill=self.get_color('std'))
                # I1.text((column_txt[0],lines_txt[34]), texts[34] , font = font_txt, fill = self.get_color('std'))
                return img