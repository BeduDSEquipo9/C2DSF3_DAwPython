#Created using IntelliJ Pycharm.sh IDE
import numpy as np
import pandas as pd

# First read to create DataFrame structure
airbnb_city = ['Boston','Chicago','Los-Angeles','NewYork','San-Francisco','Washington-DC']
#path='../Inside6Cities/' + airbnb_city +'/' + str(foldernumber) + '/listings/listings.csv'
airbnb_foldernumber=4
df = pd.DataFrame()

for city in airbnb_city:
    print('City: ',city)
    df_city=pd.DataFrame()
    for foldernumber in range (1,5) :
        path='../InsideCitiesRawDatasets/' + city +'/' + str(foldernumber) + '/listings/listings.csv'
        print(path)
        try:
            temp_df = pd.read_csv(path)
        except Exception:
            #[error message]
            #print('Error: ',NameError)
            print('Folder: No existe, revisar: ',path)
        else:
            df_city = df_city.append(temp_df, ignore_index=True)
    #filename for city files
    #filename_city_raw=filename_city+'_raw.csv'
    #Create city files_raw
    #df_city.to_csv(filename_city_raw, index=False)

    #eliminate duplicates in city file
    filename_city='../perCity/airbnb_2022_'+ city+'.csv'
    df_city_removeduplicates=df_city.drop_duplicates(subset=['id'], keep='last')
    df_city_removeduplicates.to_csv(filename_city, index=False)
    #Append to main Dataframe
    df=df.append(df_city,ignore_index=True)
print('All column names:', len(list(df.columns)), '\n', list(df.columns))
#filename_all6cities_raw='airbnb_2022_6cities_raw.csv'
#df.to_csv(filename_all6cities_raw, index=False)

filename_all6cities_removeduplicates='../airbnb_2022_6cities.csv'
df_removeduplicates=df.drop_duplicates(subset=['id'], keep='last')
df_removeduplicates.to_csv(filename_all6cities_removeduplicates, index=False)
