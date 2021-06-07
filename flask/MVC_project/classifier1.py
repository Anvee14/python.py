import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps

X = np.load('C:/Users/anvee/my_git_projects/Python/flask/MVC_project/image.npz')['arr_0']
y = pd.read_csv("C:/Users/anvee/my_git_projects/Python/flask/MVC_project/labels.csv")["labels"]
#print(pd.Series(y).value_counts())
classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nclasses = len(classes)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=9, train_size=3500, test_size=500)

#scaling the features
X_train_scaled = X_train/255.0
X_test_scaled = X_test/255.0
 
clf = LogisticRegression(solver='saga', multi_class='multinomial').fit(
    X_train_scaled, y_train)
def get_pred(img):
    im_pil = Image.open(img)
    image_bw = im_pil.convert('L')
    image_bw_resized = image_bw.resize((28, 28), Image.ANTIALIAS)
    pixel_filter = 20
    min_pixel = np.percentile(image_bw_resized, pixel_filter)
    image_bw_resized_inverted_scaled = np.clip(
        image_bw_resized-min_pixel, 0, 255)
    max_pixel = np.max(image_bw_resized)
    image_bw_resized_inverted_scaled = np.asarray(
        image_bw_resized_inverted_scaled)/max_pixel
    test_sample = np.array(image_bw_resized_inverted_scaled).reshape(1, 660)
    test_pred = clf.predict(test_sample)
    return test_pred[0]


''' the percentile function get the minimum pixel and
and then using the clip function give
each image a number,And then get
the maximum pixel and make an
array of this'''
