import math

class Utils:

  def get_references(gender,ethinic,bmi,age,diseases):
      #gender = Male = M / Female = F
      #age = int
      #bmi = int (25 = 0-25)
      #ethinic = american, italian, american mexican, brasilian

      #-----------------------------------------------------------------------------------
      #População branca
      #Homens

      if gender == 'M' and 0<=bmi<=25 and 20<=age<=29 and ethinic == 'white_american':
          n,mean_r,std_r,mean_x,std_x,r = 193 ,286.5, 29.5, 42.7, 5.5, 0.58
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 0<=bmi<=25 and 30<=age<=39 and ethinic == 'white_american':
          n,mean_r,std_r,mean_x,std_x,r = 151, 290.8, 35.5, 41.1 , 6.0, 0.75
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 0<=bmi<=25 and 40<=age<=49 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 115, 291.1, 32.4, 39.9, 5.8, 0.69
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 0<=bmi<=25 and 50<=age<=59 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 97, 296.4, 37.4, 37.9, 6.3, 0.67
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 0<=bmi<=25 and age>=60 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 97, 304.5, 33.8, 37.2, 6.0, 0.60
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 20<=age<=29 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 128, 263.9, 27.0, 40.1, 5.6, 0.62
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 30<=age<=39 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 193, 265.3, 27.6, 38.8, 5.1, 0.74
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 40<=age<=49 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 188, 263.3, 27.9, 37.4, 5.3, 0.61
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 50<=age<=59 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 180, 267.2, 28.6, 35.4, 4.8, 0.66
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and age<=60 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 230, 270.4, 32.5, 33.1, 5.3, 0.64
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and 20<=age<=29 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 36, 237.8, 23.4, 35.8, 4.9, 0.72
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and 30<=age<=39 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 62, 239.7, 27.5, 34.7, 4.4, 0.68
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and 40<=age<=49 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 71, 238.7, 25.6, 33.9, 5.3, 0.66
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and 50<=age<=59 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 89, 241.6, 22.4, 32.3, 4.7, 0.41
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and age>=60 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 111, 248.3, 26.8, 31.5, 5.1, 0.60
          #print(n, mean_r,std_r,mean_x,std_x,r)

      #-----------------------------------------------------------------------------------
      #População negra
      #Mulheres

      elif gender == 'F' and 0<=bmi<=25 and 20<=age<=29 and ethinic == 'white_american':
          n,mean_r,std_r,mean_x,std_x,r = 280, 378.4, 44.0, 50.2, 7.3, 0.69
          #print(n, mean_r,std_r,mean_x,std_x,r'

      elif gender == 'F' and 0<=bmi<=25 and 30<=age<=39 and ethinic == 'white_american':
          n,mean_r,std_r,mean_x,std_x,r = 261, 370.7, 38.5, 47.7, 6.4, 0.69
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 0<=bmi<=25 and 40<=age<=49 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 182, 386.6, 44.0, 48.9, 7.2, 0.73

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 0<=bmi<=25 and 50<=age<=59 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 146, 393.0, 43.6, 46.9, 6.9, 0.64

          #print(n, mean_r,std_r,mean_x,std_x,r)
      elif gender == 'F' and 0<=bmi<=25 and age>=60 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 140, 406.1, 49.3, 45.0, 6.6, 0.57
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 25.1<=bmi<=30 and 20<=age<=29 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 70, 353.2, 36.7, 46.6, 7.0, 0.65

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 25.1<=bmi<=30 and 30<=age<=39 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 119, 351.0, 32.0, 46.6, 6.7, 0.68
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 25.1<=bmi<=30 and 40<=age<=49 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 134, 353.1, 35.8, 45.7, 6.3, 0.69
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 25.1<=bmi<=30 and 50<=age<=59 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 134, 353.1, 36.8, 43.8, 5.6, 0.51

          #print(n, mean_r,std_r,mean_x,std_x,r)
      elif gender == 'F' and 25.1<=bmi<=30 and age>=60 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 159, 362.1, 38.1, 42.9, 6.9, 0.64

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 20<=age<=29 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 29, 333.8, 43.4, 44.7, 5.4, 0.63

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 30<=age<=39 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 73, 318.5, 30.6, 43.1, 5.4, 0.57

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 40<=age<=49 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 77, 326.8, 33.7, 43.6, 7.3, 0.70

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 50<=age<=59 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 84, 330.1, 31.4, 40.7, 6.3, 0.68
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and age>=60 and ethinic == 'white_american': 
          n,mean_r,std_r,mean_x,std_x,r = 87, 337.3, 44.6, 39.6, 6.5, 0.57

          #print(n, mean_r,std_r,mean_x,std_x,r)
      #-----------------------------------------------------------------------------------
      #População negra
      #Homens

      elif gender == 'M' and 0<=bmi<=25 and 20<=age<=29 and ethinic == 'black_american':
          n,mean_r,std_r,mean_x,std_x,r = 217, 294.1, 33.4, 45.4, 6.8, 0.66

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 0<=bmi<=25 and 30<=age<=39 and ethinic == 'black_american':
          n,mean_r,std_r,mean_x,std_x,r = 182, 290.9, 35.2, 43.5, 6.4, 0.66
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'M' and 0<=bmi<=25 and 40<=age<=49 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 115, 298.6, 35.9, 42.0, 6.3, 0.70
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'M' and 0<=bmi<=25 and 50<=age<=59 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 55, 309.8, 43.2, 41.4, 7.7, 0.74
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'M' and 0<=bmi<=25 and age>=60 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 74, 312.7, 43.3, 38.0, 7.5, 0.68

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 20<=age<=29 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r =141, 264.2, 29.7, 41.5, 6.1, 0.74

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 30<=age<=39 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 153, 264.7, 31.1, 40.8, 6.0, 0.72

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 40<=age<=49 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 139 ,268.6, 27.3, 40.6, 6.5, 0.67

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and 50<=age<=59 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r =78, 267.5, 32.2, 37.3, 5.7, 0.72

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 25.1<=bmi<=30 and age>=60 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r =100, 275.0, 34.5, 36.4, 7.1, 0.73

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and 20<=age<=29 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 66, 246.4, 32.8, 39.6, 5.8, 0.65
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'M' and 30.1<=bmi<=35 and 30<=age<=39 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r =77, 243.1, 30.4, 38.1, 5.7, 0.80
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'M' and 30.1<=bmi<=35 and 40<=age<=49 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 57, 252.3, 27.9, 38.1, 5.7, 0.80
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'M' and 30.1<=bmi<=35 and 50<=age<=59 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 37, 244.3, 21.3, 32.9, 4.8, 0.69
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'M' and 30.1<=bmi<=35 and age>=60 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 56, 246.2, 32.3, 32.0, 6.0, 0.72
          #print(n, mean_r,std_r,mean_x,std_x,r)

      #-----------------------------------------------------------------------------------
      #População negra
      #Mulheres

      elif gender == 'F' and 0<=bmi<=25 and 20<=age<=29 and ethinic == 'black_american':
          n,mean_r,std_r,mean_x,std_x,r =207, 388.9, 48.6, 53.9, 8.7, 0.76

          #print(n, mean_r,std_r,mean_x,std_x,r'

      elif gender == 'F' and 0<=bmi<=25 and 30<=age<=39 and ethinic == 'black_american':
          n,mean_r,std_r,mean_x,std_x,r = 167, 387.1, 37.4, 52.6, 7.6, 0.62

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 0<=bmi<=25 and 40<=age<=49 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 75, 396.3, 44.9, 54.2, 8.4, 0.70
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'F' and 0<=bmi<=25 and 50<=age<=59 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 35, 398.2, 46.2, 48.8, 8.9, 0.85
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 0<=bmi<=25 and age>=60 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r =44, 412.2, 50.7, 49.8, 9.4, 0.51

          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'F' and 25.1<=bmi<=30 and 20<=age<=29 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 146, 349.8, 37.5, 49.3, 7.5, 0.75

          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'F' and 25.1<=bmi<=30 and 30<=age<=39 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 155, 355.5, 36.6, 50.4, 7.0, 0.73
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'F' and 25.1<=bmi<=30 and 40<=age<=49 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 125, 349.3, 36.3, 47.6, 6.7, 0.68
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'F' and 25.1<=bmi<=30 and 50<=age<=59 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 61, 358.9, 40.0, 47.1, 7.2, 0.75
          #print(n, mean_r,std_r,mean_x,std_x,r)


      elif gender == 'F' and 25.1<=bmi<=30 and age>=60 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 84, 365.9, 42.9, 45.9, 7.6, 0.65
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 20<=age<=29 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 75, 334.3, 32.0, 48.8, 5.7, 0.49
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 30<=age<=39 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 103, 328.6, 42.3, 47.1, 8.0, 0.68
          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 40<=age<=49 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 93, 320.8, 37.7, 45.0, 7.0, 0.65

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and 50<=age<=59 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r = 68, 327.4, 40.9, 42.9, 8.0, 0.54

          #print(n, mean_r,std_r,mean_x,std_x,r)

      elif gender == 'F' and 30.1<=bmi<=35 and age>=60 and ethinic == 'black_american': 
          n,mean_r,std_r,mean_x,std_x,r =72, 333.8, 38.2, 41.9, 6.7, 0.66
          #print(n, mean_r,std_r,mean_x,std_x,r)

      else:
          print('Paciente sem referência na literatura')
          n,mean_r,std_r,mean_x,std_x,r = 72, 333.8, 38.2, 41.9, 6.7, 0.66

      return (n, mean_r, std_r, mean_x, std_x, r)

  def whole_body_impedance(z_of_right_arm, z_of_trunk,z_of_right_leg):
    return z_of_trunk + z_of_right_arm + z_of_right_leg

  def whole_body_reactance(x_of_right_arm, x_of_trunk, x_of_right_leg):
    return x_of_right_arm + x_of_trunk + x_of_right_leg

  def resistence(impedance,reactance):
    return ((impedance**2)-(reactance**2))**0.5

  def whole_body_phase_angle(whole_body_impedance, whole_body_reactance):
    ratio = whole_body_reactance/whole_body_impedance
    return math.degrees(math.asin(ratio))