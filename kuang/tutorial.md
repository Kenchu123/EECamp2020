## Face Detection

### Haar Cascades Classifier
#### Introduction
用監督式機器學習與"階層式分類器"

(關鍵字：machine learning, AdaBoost, Haar Cascade Classification)

#### Haar-like features
這是一個對圖片一部份取特徵的ㄧ種取法，做法是把這些小匡疊在目標區塊，然後把白色區域對應的圖片的區域減掉黑色部分對應的圖片區域
![](https://docs.opencv.org/3.4/haar_features.jpg)

下圖舉例，有兩個不同的feature取法，中間的是取眼睛高度所在，右邊的是去眼睛確切的位置

1. 第一階段：中間的因為眼睛這條線通常比臉部其他地方深，所以可以找出眼睛的高度所在
2. 第二階段：人的眼睛通常會比中間(鼻梁)處還要深，所以用圖中右邊取特徵的框去取，就會得到比較大(小)的值，而可以是否有眼睛

![](https://docs.opencv.org/3.4/haar.png)


#### Classifiers 分類器
這裡是一個二元分類器，就是給一個目標問題他會說回答是或不是
人臉辨識就是給一張圖片中的一部分，給出是否是具有臉部特徵

#### Cascade Classification 
「三個臭皮匠勝過一個諸葛亮」

要訓練一個很強的分類器很難，但是可以訓練很多個針對不同特徵的分類器，每個分類器單獨無法盼人臉，但可能可以判是否有某個人臉的特徵，那很多個串起來後就可以分辨出人臉了

![](https://4.bp.blogspot.com/-r7xMgFjq1Ww/VfbezAxHYII/AAAAAAAAEdk/CvWdABRPu-Q/s1600/cascade_vis.png)

#### Conclusion
在2001年Paul Viola and Michael Jonesn所提出的論文"Rapid Object Detection using a Boosted Cascade of Simple Features"中，他們使用了超過6000個弱分類器做串連來得到一個很不錯的人臉辨識器。

這樣6000多個分類器乍看之下應該會很慢，但其實大多數的區塊都不含人臉，所以會在前幾個分類器就被判別不是人臉而不會繼續跑下去，所以大大提升了執行時間

OpenCV裡面所使用的人臉分配器就是用此理論時做的

### Open CV

#### Classification in Open CV
用一個xml來表示一個classification
可以用 ``` 某 function() ``` 來引入這個分類氣

#### 內建的Classification
* haarcascade_frontalface_default.xml -> 人臉
* haarcascade_eye_tree_eyeglasses.xml -> 眼睛
其他可以以下連結去找到：https://github.com/opencv/opencv/tree/master/data/haarcascades



### Reference:
https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf
https://docs.opencv.org/3.4/d2/d99/tutorial_js_face_detection.html
https://chtseng.wordpress.com/2018/06/15/opencv-cascade-object-detection/
https://www.itread01.com/content/1542174802.html
https://www.datacamp.com/community/tutorials/face-detection-python-opencv

