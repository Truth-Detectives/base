Youtube api:
For the youtube api once there is an approriate youtube api key (from google cloud) you can run the code given on a similar dataset to get the likes comments and views on a youtube video. If the url does not exist it will output 0. These have been removed from the combined dataset.

SingFake dataset
This code uses Fpmax for association rule mining as opposed to apriori algorithm.
This was used on the singfake dataset where likes,comments and views were compared.
Once the mlxtend is installed then running everything on the notebook should output the stats of all the metadata collected and then the different associations found from the dataset.

The end snippet of code puts the output in a text file just for a full/complete output.