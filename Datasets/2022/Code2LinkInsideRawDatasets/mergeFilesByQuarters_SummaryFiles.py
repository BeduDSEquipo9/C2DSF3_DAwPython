import numpy as np
import pandas as pd

# First read to create DataFrame structure
airbnb_city = ['Boston','Chicago','Los-Angeles','NewYork','San-Francisco','Washington-DC']
#path='../Inside6Cities/' + airbnb_city +'/' + str(foldernumber) + '/listings/listings.csv'
#airbnb_foldernumber=4
df = pd.DataFrame()

for foldernumber in range (1,5) :
    print('Quarter: ',foldernumber)
    df_quarter=pd.DataFrame()
    for city in airbnb_city:
        print('City: ',city)
        
        path='../Inside6Cities/' + city +'/' + str(foldernumber) + '/listings.csv'
        print(path)
        try:
            temp_df = pd.read_csv(path)
        except Exception:
            #[error message]
            #print('Error: ',NameError)
            print('Folder: No existe, revisar: ',path)
        else:
            df_quarter = df_quarter.append(temp_df, ignore_index=True)
    #filename for city files
    #filename_city_raw=filename_city+'_raw.csv'
    #Create city files_raw
    #df_city.to_csv(filename_city_raw, index=False)

    #eliminate duplicates in city file
    filename_quarter='perQuarters2022/airbnb_2022_'+str(foldernumber)+'_quarter_SummaryFile.csv'
    df_quarter=df_quarter.drop_duplicates(subset=['id'], keep='last')
    df_quarter.to_csv(filename_quarter, index=False)
    #Append to main Dataframe
    df=df.append(df_quarter,ignore_index=True)
print('All column names:', len(list(df.columns)), '\n', list(df.columns))
#filename_all6cities_raw='airbnb_2022_6cities_raw.csv'
#df.to_csv(filename_all6cities_raw, index=False)

filename_all6cities_removeduplicates='airbnb_2022_Allcities_SummaryFile.csv'
df_removeduplicates=df.drop_duplicates(subset=['id'], keep='last')
df_removeduplicates.to_csv(filename_all6cities_removeduplicates, index=False)
