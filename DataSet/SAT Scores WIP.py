
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


# Create a reference the CSV file desired
csv_path = "SAT.csv"

# Read the CSV into a Pandas DataFrame
SAT_df = pd.read_csv(csv_path)

# Print the first five rows of data to the screen
SAT_df.tail()


# In[9]:


SAT_df = SAT_df.drop(['SCHOOL_DISTRCT_CD', 'SUBGRP_DESC',
                      'INSTN_NUMBER', 'INSTN_AVG_SCORE_VAL', 
                      'INSTN_NUM_TESTED_CNT','INSTN_NAME'], axis=1 )
SAT_df.head()


# In[10]:


SAT_df = SAT_df.rename(columns={"LONG_SCHOOL_YEAR":"Year", "SCHOOL_DSTRCT_NM": "Schl Dist Name", "TEST_CMPNT_TYP_CD":
                                "Category of SAT Scores","NATIONAL_NUM_TESTED_CNT": "Nat Num Stdnt Tested", "STATE_NUM_TESTED_CNT": 
                                "St Num Stdnt Tested", "DSTRCT_NUM_TESTED_CNT": "Dist Num Stdnt Tested",
                               "STATE_AVG_SCORE_VAL": "St Avg SAT Score", "DSTRCT_AVG_SCORE_VAL": "Dist Avg SAT Score"})

SAT_df


# In[140]:


Combined_SAT_df = SAT_df[ SAT_df["Category of SAT Scores"] == "Combined" ] 
Combined_SAT_df2 = SAT_df[ SAT_df["Category of SAT Scores"] == "Combined Test Score" ] 

Combined_SAT_df3 = Combined_SAT_df.append(Combined_SAT_df2)
len(Combined_SAT_df3)
Combined_SAT_df3.tail()


# In[141]:


Combined_SAT_df["School Year"] = Combined_SAT_df["Year"].map(lambda x:5)
Combined_SAT_df["School Year"]


# In[131]:


for x in Combined_SAT_df:
    print(x)
    if x == ("2010-11"):
        list.append(2010)
    elif x == ("2011-12"):
        list.append(2011)
    elif x == ("2012-13"):
        list.append(2012)
    elif x == ("2013-14"):
        list.append(2013)
    elif x == ("2014-15"):
        list.append(2014)
Combined_SAT_df.head()   

