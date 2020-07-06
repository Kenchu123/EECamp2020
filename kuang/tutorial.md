## Face Detection

### Haar Cascades Classifier
#### Introduction
用監督式機器學習與"階層式分類器"做出的分類器

(machine learning, AdaBoost, Cascade Classification)

#### Haar-like features
這是一


#### Classifiers 分類器
這裡是一個二元分類器，就是給一個東西他會說Yes\No
人臉辨識就是給一張圖片中的一塊，給出是否是具有目標特徵

#### Cascade Classification 
「三個臭皮匠勝過一個諸葛亮」

要訓練一個很強的分類器很難，但是可以訓練很多個不強的分類器，每個分類器單獨無法盼人臉，但可能可以判是否有某個人臉的特徵，那很多個串起來後就可以分辨出人臉了

在2001年Paul Viola and Michael Jonesn所提出的論文"Rapid Object Detection using a Boosted Cascade of Simple Features"中，他們使用了超過6000個弱分類器做串連來得到一個很不錯的人臉辨識器。

但這樣的分類器乍看之下應該會很慢，但其實大多數的區塊都不含人臉，所以會在前幾個分類器就被判別不是人臉而不會繼續跑下去，所以大大提升了執行時間

### Open CV

#### Introduction


#### Classification in Open CV
用超過6000個弱分類器，以提升他的正確率
非人臉的圖片會在前幾階段就被刷掉，所以可以大大地加快判斷速度
用一個xml來表示一個classification
可以用 ``` 某 function() ``` 來引入這個分類氣

#### 內建的Classification
* haarcascade_frontalface_default.xml -> 人臉
* haarcascade_eye_tree_eyeglasses.xml -> 眼睛
* haarcascade_frontalface_alt_tree.xml
* haarcascade_frontalface_alt.xml
* haarcascade_frontalface_alt2.xml
* haarcascade_frontalface_default.xml
* haarcascade_fullbody.xml
* haarcascade_lefteye_2splits.xml
* haarcascade_lowerbody.xml
* haarcascade_mcs_eyepair_big.xml
* haarcascade_mcs_lefteye.xml
* haarcascade_mcs_mouth.xml
* haarcascade_mcs_nose.xml
* haarcascade_mcs_righteye.xml
* haarcascade_mcs_upperbody.xml
* haarcascade_profileface.xml
* haarcascade_righteye_2splits.xml
* haarcascade_upperbody.xml
* haarcascade_mcs_eyepair_small.xml



### Reference:
https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf
https://docs.opencv.org/3.4/d2/d99/tutorial_js_face_detection.html
https://chtseng.wordpress.com/2018/06/15/opencv-cascade-object-detection/
https://www.itread01.com/content/1542174802.html

