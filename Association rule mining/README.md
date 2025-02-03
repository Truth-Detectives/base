This is a simple code for association rule mining that just includes getting the number of total "associated" transactions in a grocery csv dataset as well as all the unique products available. It then uses apriori to find associations on these sales.
In this instance the date was used to tell when items were bought at the same time for the total "associated" transactions.

To use the association rule mining example notebook
First install apyori by doing "!pip install apyori"
Apriori is the algorithm used for association rule mining to get relationships in a dataset. This is done by counting item occurences, generating any frequent itemsets and then it extracts rules with high confidence and lift.
Then you could run each cell and get an output from the data set given or any similar dataset with 4% confidence. 

numpy would be used for handling a large 2d array for ease of use while pandas would be used to read data from the excel sheet.

The one-hot encoding would encode the dataset into a binary format for apriori to use it easier.
The total products show the number of unique products in the dataset while the total transactions show the amount of sales in the dataset. Transactions will then filter out any 0 from the one-hot encoding to get only the filtered values for associations.