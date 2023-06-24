from sklearn.preprocessing import LabelEncoder

def Encoder(ab):
          columnsToEncode = list(ab.select_dtypes(include=['category','object']))
          le = LabelEncoder()
          for feature in columnsToEncode:
              try:
                  ab[feature] = le.fit_transform(ab[feature])
              except:
                  print('Error encoding '+feature)
          return ab

