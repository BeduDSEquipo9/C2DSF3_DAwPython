import numpy as np
import pandas as pd

# First read to create DataFrame structure
city ='MexicoCity'
#path='../Inside6Cities/' + airbnb_city +'/' + str(foldernumber) + '/listings/listings.csv'

#df = pd.DataFrame()
print('City: ',city)
df_city=pd.DataFrame()
for foldernumber in range (1,5) :
    path='../InsideCitiesRawDatasets/' + city +'/' + str(foldernumber) + '/listings.csv'
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
    filename_city='../perCity/airbnb_2022_'+ city+'_SummaryFile.csv'
    df_city_removeduplicates=df_city.drop_duplicates(subset=['id'], keep='last')
    df_city_removeduplicates.to_csv(filename_city, index=False)
    #Append to main Dataframe
    #df=df.append(df_city,ignore_index=True)
print('All column names:', len(list(df_city.columns)), '\n', list(df_city.columns))
#filename_all6cities_raw='airbnb_2022_6cities_raw.csv'
#df.to_csv(filename_all6cities_raw, index=False)

#filename_all6cities_removeduplicates='airbnb_2022_6cities.csv'
#df_removeduplicates=df.drop_duplicates(subset=['id'], keep='last')
#df_removeduplicates.to_csv(filename_all6cities_removeduplicates, index=False)
