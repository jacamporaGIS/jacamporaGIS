#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[8]:


pd.set_option('display.max_columns', None)
df = pd.read_csv(r'C:\Users\joeac\Documents\Course1\PropertyData_2021.txt', sep='|', encoding='ISO-8859-1', dtype='object')
df.head()


# In[9]:


Situs_Address = df['Situs_Address'].str.split(expand = True)

Directions = ['N','E','W','S', 'North', 'East', 'West', 'South', 'NE', 'NW', 'SE', 'SW', 'NORTH', 'EAST', 'WEST', 'SOUTH']

street_name = []
street_type = []
street_no = []
street_address = []
prefix = []
suffix = []

for row in Situs_Address.loc[:20].values.tolist():
    
    # 4 worded addresses
    if row[0] is not None and row[1] is not None and row[2] is not None and row[3] is not None and row[4] is None:
      
        street_name.append(row[2])
        street_type.append(row[3])
        street_no.append(row[0])
        street_address.append(row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3])
        prefix.append(row[1])
        suffix.append(None)
            
    # 3 worded addresses
    if row[0] is not None and row[1] is not None and row[2] is not None and row[3] is None:
    
        street_name.append(row[1])
        street_type.append(row[2])
        street_no.append(row[0])
        street_address.append(row[0] + ' ' + row[1] + ' ' + row[2])
        prefix.append(None)
        suffix.append(None)
        
    else:
        street_name.append(None)
        street_type.append(None)
        street_no.append(None)
        street_address.append(None)
        prefix.append(None)
        suffix.append(None)

    
        


# In[ ]:


try:

    env.overwriteOutput = True
    env.workspace = r'C:\Users\joeac\Documents\ArcGIS\Projects\MyProject3\MyProject3.gdb'
    fcname = 'PropertyData'
    fclass = os.path.join(arcpy.env.workspace,fcname)

    # fields from the PropertyData table

    fields = ['RP','Appraisal_Year','Account_Num','Record_Type','Sequence_No','PIDN',

              'Owner_Name','Owner_Address','Owner_CityState','Owner_Zip','Owner_Zip4',

              'Owner_CRRT','Situs_Address','Property_Class','TAD_Map','MAPSCO','Exemption_Code',

              'State_Use_Code','LegalDescription','Notice_Date','County','City','School',

              'Num_Special_Dist','Spec1','Spec2','Spec3','Spec4','Spec5','Deed_Date','Deed_Book',

              'Deed_Page','Land_Value','Improvement_Value','Total_Value','Garage_Capacity',

              'Num_Bedrooms','Num_Bathrooms','Year_Built','Living_Area','Swimming_Pool_Ind',

              'ARB_Indicator','Ag_Code','Land_Acres','Land_SqFt','Ag_Acres','Ag_Value',

              'Central_Heat_Ind','Central_Air_Ind','Structure_Count','From_Accts','Appraisal_Date',

              'Appraised_Value','GIS_Link','Instrument_No','Overlap_Flag','PropertyTax',

              'CityName', 'CountyName', 'Street_No', 'Street_Name', 'Street_Address', 'Street_Type', 'Street_Type', 'Prefix', 'Suffix']


    # fields from the pandas dataframe

    INPUTs = df.loc[:,['RP','Appraisal_Year','Account_Num','Record_Type','Sequence_No','PIDN',

              'Owner_Name','Owner_Address','Owner_CityState','Owner_Zip','Owner_Zip4',

              'Owner_CRRT','Situs_Address','Property_Class','TAD_Map','MAPSCO','Exemption_Code',

              'State_Use_Code','LegalDescription','Notice_Date','County','City','School',

              'Num_Special_Dist','Spec1','Spec2','Spec3','Spec4','Spec5','Deed_Date','Deed_Book',

              'Deed_Page','Land_Value','Improvement_Value','Total_Value','Garage_Capacity',

              'Num_Bedrooms','Num_Bathrooms','Year_Built','Living_Area','Swimming_Pool_Ind',

              'ARB_Indicator','Ag_Code','Land_Acres','Land_SqFt','Ag_Acres','Ag_Value',

              'Central_Heat_Ind','Central_Air_Ind','Structure_Count','From_Accts','Appraisal_Date',

              'Appraised_Value','GIS_Link','Instrument_No','Overlap_Flag','Property_Tax',

              'CityNames', 'Countyname', 'Street_No', 'Street_Name', 'Street_Address', 'Street_Type', 'Street_Type', 'Prefix', 'Suffix']].values.tolist()


    # create an InsertCursor object to insert rows

    InsertCursor = arcpy.da.InsertCursor(fclass,fields)

    for row in inputs:
        InsertCursor.insertRow(row)

    del InsertCursor

except Exception as ex:

    print(str(ex))

