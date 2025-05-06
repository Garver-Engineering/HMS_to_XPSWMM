# %%
# Import Excel File which was a DSS export, and look at wanted output format for XPSWMM External data
input_data = r"L:\2024\T27-2400870 - Owasso 96th Mingo to Garnett\Design\Calculations\Hydraulics\Existing Conditions\Inflow Hydrographs\100yr_TR_Inflow_Hydrographs.xlsx"
output_ex = r"L:\2024\T27-2400870 - Owasso 96th Mingo to Garnett\Design\Q\100yr.txt"
output = r"100yr.txt"

# Open the input file and read the data
import pandas as pd
import os

# %%
df = pd.read_excel(input_data)
# lets look at only the first 10 rows and first 7 columns.
df.iloc[:10, :7]

# %%
# lets look at the example output file to see what we are trying to achieve
with open(output_ex, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
# %%
# from the example output file we can see that there a no headers or index columns, and the rows are each a value and the station ID. 
# there is also no comma at the end of a row.

# In the dataframe, the stations start on column 6 from the left to the end of the dataframe's columns, [6:].
# The station ID are in the header row, and the values start on the 7th row below the header row. [7:]
# lets get an example of the station ID's and the values for the first 2 stations.
df_station_data = df.iloc[6:, 4:]
# reindex the dataframe to start at 0, and reset the index
df_station_data = df_station_data.reset_index(drop=True)
df_station_data

# %%
# get max value in the dataframe
df_station_data.max()

# %%
# now lets write the data to a text file in the format we want.
# we will write the data to a text file with no headers or index columns, and each row will be a value and the station ID.
# there will be no comma at the end of a row.
for i in range(len(df_station_data.columns)):
    # get the station ID from the header row
    station_id = df_station_data.columns[i]
    # get the values for the station
    values = df_station_data.iloc[:, i].values
    # open the output file in append mode
    with open(output, 'a') as f:
        # write the values to the file, one per line, with the station ID at the end of each line
        for value in values:
            f.write(f"{round(value,3)}, {station_id}\n")
# %%
