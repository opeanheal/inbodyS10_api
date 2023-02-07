# Importing the PIL library
from uuid import uuid4
from classes.Utils import Utils
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#from Utils import whole_body_impedance, whole_body_phase_angle, whole_body_reactance, resistence, get_references


class BaseReportBio:
         

        # pt is an object of class Patient and i is Index of Bio
        def __init__(self, pt, i, language='pt'):
                self.pt = pt
                self.name = str(pt.name)
                self.id = str(pt.bios[i].ID)
                self.heigth = str(pt.bios[i].HEIGHT)
                self.date = str(pt.bios[i].DATE_TIMES)
                self.age = str(int(pt.bios[i].AGE))
                self.sex = 'Masculino' if (pt.bios[i].SEX) == 1 else 'Feminino'
                self.gender = 'M' if (pt.bios[i].SEX) == 1 else 'F'
                self.icw = str(pt.bios[i].ICW)
                self.icw_min = str(pt.bios[i].ICW_MIN)
                self.icw_max = str(pt.bios[i].ICW_MAX)
                self.ecw = str(pt.bios[i].ECW)
                self.ecw_min = str(pt.bios[i].ECW_MIN)
                self.ecw_max = str(pt.bios[i].ECW_MAX)
                self.tbw = str(pt.bios[i].TBW_Total_Body_Water_)
                self.protein = str(pt.bios[i].Protein)
                self.protein_min = str(pt.bios[i].Protein_MIN)
                self.protein_max = str(pt.bios[i].Protein_MAX)
                self.SLM_Soft_Lean_Mass = str(pt.bios[i].SLM_Soft_Lean_Mass_)
                self.mineral = str(pt.bios[i].Mineral)
                self.mineral_min = str(pt.bios[i].Mineral_MIN)
                self.mineral_max = str(pt.bios[i].Mineral_MAX)
                self.FFM_Fat_Free_Mass = str(pt.bios[i].FFM_Fat_Free_Mass_)
                self.fat = str(pt.bios[i].Fat)
                self.fat_min = str(pt.bios[i].Fat_MIN)
                self.fat_max = str(pt.bios[i].Fat_MAX)
                self.weight = str(pt.bios[i].WEIGHT)
                self.weight_min = str(pt.bios[i].WEIGHT_MIN)
                self.weight_max = str(pt.bios[i].WEIGHT_MAX)
                self.SMM_Skeletal_Muscle_Mass = str(
                    pt.bios[i].SMM_Skeletal_Muscle_Mass_)
                self.SMM_min = str(pt.bios[i].SMM_MIN)
                self.SMM_max = str(pt.bios[i].SMM_MAX)
                self.FFM_Fat_Free_Mass = str(pt.bios[i].FFM_Fat_Free_Mass_)
                self.FFM_min = str(pt.bios[i].FFM_MIN)
                self.FFM_max = str(pt.bios[i].FFM_MAX)
                self.PBF_Percent_Body_Fat = str(pt.bios[i].PBF_Percent_Body_Fat_)
                self.PBF_min = str(pt.bios[i].PBF_MIN)
                self.PBF_max = str(pt.bios[i].PBF_MAX)
                self.BMI = str(pt.bios[i].BMI)
                self.BMI_min = str(pt.bios[i].BMI_MIN)
                self.BMI_max = str(pt.bios[i].BMI_MAX)

                self.Segmental_Lean_RA = str(pt.bios[i].Segmental_Lean_RA_)
                self.Segmental_Lean_RA_min = str(pt.bios[i].Segmental_Lean_RA__MIN)
                self.Segmental_Lean_RA_max = str(pt.bios[i].Segmental_Lean_RA__MAX)

                self.Segmental_Lean_LA = str(pt.bios[i].Segmental_Lean_LA_)
                self.Segmental_Lean_LA_min = str(pt.bios[i].Segmental_Lean_LA_)
                self.Segmental_Lean_LA_max = str(pt.bios[i].Segmental_Lean_LA_)

                self.Segmental_Lean_TR = str(pt.bios[i].Segmental_Lean_TR_)
                self.Segmental_Lean_TR_min = str(pt.bios[i].Segmental_Lean_TR__MIN)
                self.Segmental_Lean_TR_max = str(pt.bios[i].Segmental_Lean_TR__MAX)

                self.Segmental_Lean_RL = str(pt.bios[i].Segmental_Lean_RL_)
                self.Segmental_Lean_RL_min = str(pt.bios[i].Segmental_Lean_TR__MAX)
                self.Segmental_Lean_RL_max = str(pt.bios[i].Segmental_Lean_TR__MAX)

                self.Segmental_Lean_LL = str(pt.bios[i].Segmental_Lean_LL_)
                self.Segmental_Lean_LL_min = str(pt.bios[i].Segmental_Lean_LL__MIN)
                self.Segmental_Lean_LL_max = str(pt.bios[i].Segmental_Lean_LL__MAX)

                self.waist_cir = str(pt.bios[i].Waist_Cir)

                self.TBW_Total_Body_Water = str(pt.bios[i].TBW_Total_Body_Water_)
                self.TBW_min = str(pt.bios[i].TBW_MIN)
                self.TBW_max = str(pt.bios[i].TBW_MAX)
                self.ECW_TBW_Total = str(pt.bios[i].ECW_TBW_Total_)

                self.BMR = str(pt.bios[i].BMR)

                self.Body_Cell_Mass = str(pt.bios[i].Body_Cell_Mass)
                self.BCM_min = str(pt.bios[i].BCM_MIN)
                self.BCM_max = str(pt.bios[i].BCM_MAX)

                self.VFA = str(pt.bios[i].VFA)

                self._50khz_RA_Impedance = str(pt.bios[i]._50khz_RA_Impedance)
                self._50khz_TR_Impedance = str(pt.bios[i]._50khz_TR_Impedance)
                self._50khz_RL_Impedance = str(pt.bios[i]._50khz_RL_Impedance)

                self._50khz_RA_Reactance = str(pt.bios[i]._50khz_RA_Reactance)
                self._50khz_TR_Reactance = str(pt.bios[i]._50khz_TR_Reactance)
                self._50khz_RL_Reactance = str(pt.bios[i]._50khz_RL_Reactance)

                self.language = language

                # Categorical feferences (unde_bad - normal - over_bad - over_good)

                self.cat_ICW = 'under_bad' if float(self.icw) < float(
                    self.icw_min) else 'over_bad' if float(self.icw) > float(self.icw_max) else 'normal'
                self.cat_ECW = 'under_bad' if float(self.ecw) < float(
                    self.ecw_min) else 'over_bad' if float(self.ecw) > float(self.ecw_max) else 'normal'
                self.cat_protein = 'under_bad' if float(self.protein) < float(
                    self.protein_min) else 'over_good' if float(self.protein) > float(self.protein_max) else 'normal'
                self.cat_mineral = 'under_bad' if float(self.mineral) < float(
                    self.mineral_min) else 'over_good' if float(self.mineral) > float(self.mineral_max) else 'normal'
                self.cat_weight = 'under_bad' if float(self.weight) < float(
                    self.weight_min) else 'over_bad' if float(self.weight) > float(self.weight_max) else 'normal'
                self.cat_SMM = 'under_bad' if float(self.SMM_Skeletal_Muscle_Mass) < float(
                    self.SMM_min) else 'over_good' if float(self.SMM_Skeletal_Muscle_Mass) > float(self.SMM_max) else 'normal'
                self.cat_FFM = 'under_bad' if float(self.FFM_Fat_Free_Mass) < float(
                    self.FFM_min) else 'over_good' if float(self.FFM_Fat_Free_Mass) > float(self.FFM_max) else 'normal'
                self.cat_PBF = 'under_bad' if float(self.PBF_Percent_Body_Fat) < float(
                    self.PBF_min) else 'over_bad' if float(self.PBF_Percent_Body_Fat) > float(self.PBF_max) else 'normal'
                self.cat_fat = 'under_bad' if float(self.fat) < float(
                    self.fat_min) else 'over_bad' if float(self.fat) > float(self.fat_max) else 'normal'
                self.cat_BMI = 'under_bad' if float(self.BMI) < float(
                    self.BMI_min) else 'over_bad' if float(self.BMI) > float(self.BMI_max) else 'normal'
                self.cat_Segmental_Lean_RA = 'under_bad' if float(self.Segmental_Lean_RA) < float(
                    self.Segmental_Lean_RA_min) else 'over_good' if float(self.Segmental_Lean_RA) > float(self.Segmental_Lean_RA_max) else 'normal'
                self.cat_Segmental_Lean_LA = 'under_bad' if float(self.Segmental_Lean_LA) < float(
                    self.Segmental_Lean_LA_min) else 'over_good' if float(self.Segmental_Lean_LA) > float(self.Segmental_Lean_LA_max) else 'normal'
                self.cat_Segmental_Lean_TR = 'under_bad' if float(self.Segmental_Lean_TR) < float(
                    self.Segmental_Lean_TR_min) else 'over_good' if float(self.Segmental_Lean_TR) > float(self.Segmental_Lean_TR_max) else 'normal'
                self.cat_Segmental_Lean_RL = 'under_bad' if float(self.Segmental_Lean_RL) < float(
                    self.Segmental_Lean_RL_min) else 'over_good' if float(self.Segmental_Lean_RL) > float(self.Segmental_Lean_RL_max) else 'normal'
                self.cat_Segmental_Lean_LL = 'under_bad' if float(self.Segmental_Lean_LL) < float(
                    self.Segmental_Lean_LL_min) else 'over_good' if float(self.Segmental_Lean_LL) > float(self.Segmental_Lean_LL_max) else 'normal'

                # Maths

                self.rai = float(self._50khz_RA_Impedance)
                self.rti = float(self._50khz_TR_Impedance)
                self.rli = float(self._50khz_RL_Impedance)
                # print(self.rai,self.rti,self.rli)

                self.raz = float(self._50khz_RA_Reactance)
                self.rtz = float(self._50khz_TR_Reactance)
                self.rlz = float(self._50khz_RL_Reactance)

                self.reactance = float(Utils.whole_body_reactance(
                    self.raz, self.rtz, self.rlz))
                self.impedance = float(Utils.whole_body_impedance(
                    self.rai, self.rti, self.rli))
                self.res = float(Utils.resistence(self.impedance, self.reactance))

                self.ang = float(Utils.whole_body_phase_angle(
                    self.impedance, self.reactance))
                # print(self.ang)

                self.y = float(self.reactance/(float(self.heigth)/100))
                self.x = float(self.res/(float(self.heigth)/100))

                self.n, self.mean_r, self.std_r, self.mean_x, self.std_x, self.r = Utils.get_references(
                    self.gender, 'american', float(self.BMI), float(self.age), '')
                print(self.language)

        def get_color(self, str):
                rgb = {
                'red': (196, 21, 28),
                'blue': (18, 10, 143),
                'green': (0, 100, 0),
                'black': (0, 0, 0)}

                options = {
                'std': rgb['black'],
                'normal': rgb['green'],
                'under_bad': rgb['red'],
                'under_good': rgb['blue'],
                'over_bad': rgb['red'],
                'over_good': rgb['blue']}
        
                return options[str]  # If error is because there is no option

        def get_bars(self, string):

                bars = {'under': '|-----|',
                        'normal': '|-------------------------|',
                        'over': '|-------------------------------------------|'}

                options = {'std': '',
                         'normal': bars['normal'],
                        'under_bad': bars['under'],
                        'over_bad': bars['over'],
                         'under_good': bars['under'],
                        'over_good': bars['over']}

                return options[string]  # If error is because there is no option


        def save(self, size):
                filename = f'results/{uuid4()}.png'
                img = self.show(size)
                img.save(filename)
                return filename

        
