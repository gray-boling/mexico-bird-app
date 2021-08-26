# mexico-bird-app
A model and simple app that takes images of birds (specfically trained for birds in Mexico w/ spanish names) and predicts the species with the possibility %.

Training data was parsed from publicly available images and labels on naturalista.mx. Naturalista.mx is an extension of the iNaturalist.org project began in 2008 at the University of California in Berkeley. The project is essentailly a crowd sourced database where users can upload images of birds and plants to be indentied or, if they're an expert, help identify the photos of others. The site has a very useful tool that allows you to filter the types of photos you want to see and download a .csv file containing all the information of those photos including the url to any specific image.

![mx_birds_naturalista_df](https://user-images.githubusercontent.com/85711261/130694757-212fda9e-7636-425a-887f-11ae9ba04d7e.png)

I constructed my data by first using this tool to filter for only photos of birds in Mexico within the previous year, to keep the size of the data directory manageable.
The machine learning aspects of this project were built with fastai, which has some great commands that make photographic dataset construction simple and quick.

Using the .csv provided by naturalista.mx, I first created folders in the root directory for each possible class, using os, by looping through the list of all unique "common_names" in the .csv file. Then within each class folder, this time using pandas, I created a class specific .csv listing all image urls for that class. This is where fastai simplifies the final step. Now with each directory constructed in that manner, it's as simple as using download_images() from fastai to read each .csv and download each image (I used the fastai default of 200 maximize images per class, again a data storage decision). Then verify_images() was used to delete any corrupted or non-image files for each class. 

![bird-batch-exp](https://user-images.githubusercontent.com/85711261/131007376-72debd3a-8b58-4628-8046-aa7ee045c8a5.png)

The images were then sorted and filtered in a way to maximize training efficiency while also allowing for the widest range of species to be learned by the model. For this project the limit was based fairly arbitrarily on a minimum number of photos cutoff that allowed for the widest representation of classes while also providing enough data for each class to generalize well (333 of 1073 species were used, 100 minimum photos per class).

The final dataset was stored in Google Drive as a .zip file. When training on Google Colab with large datasets, unzipping a .zip file into the environment from Drive is the most effecient approach.

The first training attempt I fit_one_cycle() for a few epochs to establish some parameters to work from. I used the fastai ImageClassifierCleaner() to remove unwanted or unidentifiable images and then retrained the network. After some 20 epochs the model achieved a 41% error rate. With 333 classes this would likely be suitable for deployment depending on the application. To compare results I then trained another network on the entire dataset, without cleaning it. The idea is that the goal of this model would be to deploy it to a site like naturalista.mx to assist in identifying birds, and therefore in theory pulling images from the site should be the best representation of the kinds of images the model will be seeing in inference.

With this approach the model reached a 33% error rate in fewer epochs (17). I deployed the model with the app-display.ipynb and this github repo using mybinder.org. Testing it where I currently live (a small southern Mexico town) the model was able to accurately identify several common birds species that I photographed around town with my phone.
