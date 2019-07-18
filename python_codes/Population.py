import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    #location where file is downloaded
    filename = "~/Downloads/population.xlsx"

    #create data_frame from xlsx sheet.
    df = pd.read_excel(filename, header=[2], index_col=None)

    #Numerical Question_2#

    # Aggregating population for each year on Geography. 
    grouped = df[df['Sex'] == 'All'].groupby(['Geography code', 'Geography'])['2013','2014', '2015', '2016'].agg('sum').reset_index()

    # To get Geography which has least population over all year -[2013, 2014, 2015, 2016] apply filter.
    record_with_least_population = grouped[(grouped['2013'] == grouped['2013'].agg('min')) & (grouped['2014'] == grouped['2014'].agg('min')) & (grouped['2015'] == grouped['2015'].agg('min')) & (grouped['2016'] == grouped['2016'].agg('min'))]

   #Printing answer to Q2

   #Ans: Isles of Scilly
   print list(record_with_least_population['Geography'])



   # Numerical Question_3

   #Logic is explained as below:
   #1- Get all the record for females <- female
   #2- Get all the record for males   <- male
   #3- Merge both female and male dataframe <- merged
   #4- Enrich merged dataframe with ratio column
   #5- Enrich merged dataframe with change_in_ratio column


   female = df[df['Sex'] == 'Female'].groupby(['Geography code', 'Geography', 'Sex'])['2013','2014', '2015', '2016'].agg('sum').reset_index().sort_values(by = 'Geography code')


   male = df[df['Sex'] == 'Male'].groupby(['Geography code', 'Geography', 'Sex'])['2013','2014', '2015', '2016'].agg('sum').reset_index().sort_values(by = 'Geography code')


   merged = pd.merge(female, male, on = ['Geography code', 'Geography'])
   joined['ratio_2013'] = joined['2013_x']/ joined['2013_y']  #Enrich merged df
   joined['ratio_2016'] = joined['2016_x']/ joined['2016_y']  #Enrich merged df
   joined['ratio_change'] = abs(joined['ratio_2016'] - joined['ratio_2013']) / 100 #Enrich merged df
   max_ratio_value = joined.ix[joined['ratio_2013'].idxmax()]['ratio_2013']     #Ans: 1.103591279555338
   max_ratio_geography = joined.ix[joined['ratio_2013'].idxmax()]['Geography']  #Ans: Knowsley
   max_ratio_change = joined.ix[joined['ratio_change'].idxmax()]['Geography']  #Ans: Moray




   #Numerical Question_4
   #Logic is explained as below:
   #1- Group dataframe over Age/Sex after filtering out All sex and aggegate over population in 2016
   #2- Plot the aggregated graph
   
   grouped_dataset = df[df['Sex'] != 'All'].groupby(['Age', 'Sex'])['2016'].agg('sum').unstack().plot(kind='bar',stacked=True)
   grouped_dataset.get_figure().savefig('/Users/ramsinha/Downloads/population_distribution.pdf')

   #Graph is attached in email




