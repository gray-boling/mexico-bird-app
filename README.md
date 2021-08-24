# mexico-bird-app
A model and simple app that takes images of birds (specfically trained for birds in Mexico w/ spanish names) and predicts the species with the possibility %.

Training data was parsed from publicly available images and labels on naturalista.mx. Naturalista.mx is an extension of the iNaturalist.org project began in 2008 ay the University of California in Berkeley. The project is essentailly a crowd sourced database where users can upload images of birds and plants to be indentied or, if they're an expert, help identify the photos of others. The site has a very useful tool that allows you to filter the types of photos you want to see and download a .csv file containing all the information of that photo including the url to that specific image.

![mx_birds_naturalista_df](https://user-images.githubusercontent.com/85711261/130694757-212fda9e-7636-425a-887f-11ae9ba04d7e.png)


I constructed my data by first using this tool to filter for only photos of birds in Mexico within the previous year, to keep the size of the data directory manageable.
The machine learning aspects of this project were built with fastai, which has some great commands that make photographic data construction simple and quick.

Using the .csv provided by naturalista.mx, I first created folders in the root directory for each possible class, using os, by looping through all unique "common_names" in the .csv. Then within each class folder, this time with pandas, I created a class specific .csv listing all image urls for that class. This is where fastai simplifies the final step. Now with each directory constructed in that manner, it's as simple as using download_images() from fastai to read each .csv and download each image (I used the fastai default of 200 maximize images per class, again a data storage decision). Then verify_images() was used to delete any corrupted or non-image files per class. 

The images were then sorted and filtered in a way to maximize training efficiency while also allowing for the widest range of species to be learned by the model. For this project the limit was based simply on a minimum photos cutoff that allowed for the widest representation of species while also providing enough data to generalize well (333 of X species were used).

The final dataset was stored in Google Drive as a .zip file. When training on Google Colab with large datasets, unzipping a .zip file into the environment is the most effecient approach.
