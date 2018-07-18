## Project Proposal
Scope:
For this project, our team examing whether or not school districts with higher budgets have higher standardized student test score averages (ACT/SAT). We will be using  national data on school districts budget funding and aggregate student performances by districts on standardized test scores for students in highschool (9-12). We will examine different regions to determine differences in budget allowance and test scores and examine other questions as our data allows. 

Sources of data:
SAT/ACT datasets
https://gosa.georgia.gov/downloadable-data
https://www.kaggle.com/noriuk/us-educational-finances

Data types:
county districts: string
US regions: list of strings
budget: integer 
SAT math: integer
SAT reading: integer
ACT math: integer
ACT science: integer
ACT english: integer
ACT reading: integer
state: geodata

Key questions:
1) Does the amount of federal budget allot to states have an impact on student's district's national test scores?
2) Is there a difference in federal budget by regions? (defined by the Census Bureau)
2a) Region 1: Northeast
        Connecticut
        Maine
        Massachusetts
        New Hampshire
        Rhode Island
        Vermont
        New Jersey
        New York
        Pennsylvania
    Region 2: Midwest 
        Illinois
        Indiana
        Michigan
        Ohio
        Wisconsin
        Iowa
        Kansas
        Minnesota
        Missouri
        Nebraska
        North Dakota
        South Dakota
    Region 3: South
        Delaware
        Florida
        Georgia
        Maryland
        North Carolina
        South Carolina
        Virginia
        District of Columbia
        West Virginia
        Alabama
        Kentucky
        Mississippi
        Tennessee
        Arkansas
        Louisiana
        Oklahoma
        Texas
    Region 4: West
        Arizona
        Colorado
        Idaho
        Montana
        Nevada
        New Mexico
        Utah
        Wyoming
        Alaska
        California
        Hawaii
        Oregon
        Washington
    We are excluding US state territories
3) Is there a difference in standardized test scores by region?
