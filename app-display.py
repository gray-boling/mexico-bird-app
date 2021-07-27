#import fastai.vision.all and vision.widgets to create widgets
from fastai.vision.all import *
from fastai.vision.wi
#Make the two text comments below a markdown in your notebook
#MX Bird Classifier
#Will identify a pictured bird as one of 333 trained species
#declare path and load our export.pkl file
path = Path()
learn_inf = load_learner(Path(path), 'birds_37per_333_classes.pkl', cpu=True)
#declare a button,output,label widget
btn_upload = widgets.FileUpload()
out_pl = widgets.Output()
lbl_pred = widgets.Label()
#define an on_data_change function which execute when an image is #uploaded.It gets the image uploaded,display the image,make a #prediction of the image and output prediction, probability of #predictions
def on_data_change(change):
    lbl_pred.value = ''
    img = PILImage.create(btn_upload.data[-1])
    out_pl.clear_output()
    with out_pl: display(img.to_thumb(128,128))
    pred,pred_idx,probs = learn_inf.predict(img)
    lbl_pred.value = f'Prediction: {pred}; Probability:{probs[pred_idx]:.04f}'
#button to click to upload image
btn_upload.observe(on_data_change, names=['data'])
#display label,btn_upload,out_pl,lbl_pred vertically
display(VBox([widgets.Label('Select an Image of Malaria Parasite!'), btn_upload, out_pl, lbl_pred]))