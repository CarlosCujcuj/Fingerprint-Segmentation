# Image Segmentation

The purpose of this project is to segment different images using certain techniques of Computer Vision like:
* Blur
* Kernels
* Image Binarization
* Morphological Operators

And also other very important techniques like:
* [Connected Components Labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)
* [Disjoint-set Data Structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

**Example:**
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/inputImage.png" height="300" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/fprint3_ccl.png" height="300" />
</p>


## How to run it?  
``` 
$ python fSegmentation.py inputImage.png outputImageName.png
```  
Where **inputImage** and **outputImageName** can be any image format  


## Brief Step by Step How it Works

1. Binarization  

We begin by adding a binarization to our image. This is for making our processing more easy by only having two values to work with: **0** (black)  and **255** (white). So we need to choose a middle **value**, if the pixel value is below this number the pixel gets a value of 0, otherwise a value of 255. This **value** is called **Threshold**, for this project we chose **127**.  

*Here's an example how it works:*
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/binarization.jpg" height="200" />
</p>


2. Padding  

Later we add a padding of 1px to our image, this is because we need to apply a kernel in the future.  
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/download.png" height="150" />
</p>
 
 3. Connected Component Labelling
 
 One common problem encountered in image analysis is to figure out which parts of an object are "connected", physically. That is, irrespective of the colour. Here's an example:
 
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/labelling-example.jpg" height="250" /> 
</p>

In the above image, the red and green circles are distinct. But the goal is not to detect circles (you can do that using the Circle Hough Transform). The goal is to identify the two "blobs". Each blob consisting of two circles, one red and one green.

So, the desired output is something like this:
 
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/labelling-labelled.jpg" height="250" /> 
</p>

With this type of output, you can easily figure out how many components the image has, and which pixels are connected. The blue pixels are all connected and form one component. Similarly, the green one. 

This will help us to detect every segment *(represented by a color)* of the fingerprint image.

Reference : [connected-component-labelling](http://aishack.in/tutorials/connected-component-labelling/)

Here's another example how should work:

<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/label-example-binary.jpg" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/label-binary-final.jpg" height="200" />
</p>

For a more deep explanation you can read this article which helped me to understand very well how the algorithm works:  
* [Connected Component Labelling by Utkarsh Sinha](http://aishack.in/tutorials/labelling-connected-components-example)

---  

With all these concepts and algorithms together we completed our project, which helps us to detect the different segments of our fingerprint image.   
However, we can apply this script to more images, and the results are quite pretty by changing the color pallete:

a. 
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilsotsu.jpg" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilOtsuOutput.png" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilOtsuOutput2.png" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilOtsuOutput3.png" height="200" />
</p>

b. 
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilsphan.jpg" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilSphanOutput.png" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilSphanOutput2.png" height="200" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/pupilSphanOutput3.png" height="200" />
</p>

c.  
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/thresholdinggood.jpg" height="350" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/thresholdinggoodOutput.png" height="350" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/thresholdinggoodOutput2.png" height="350" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/thresholdinggoodOutput3.png" height="350" />
</p>

d.  
<p align="center">
<img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/airplane.png" height="370" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/airplaneOutput.png" height="370" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/airplaneOutput2.png" height="370" /> <img src="https://github.com/CarlosCujcuj/Fingerprint-Segmentation/blob/master/imgs/airplaneOutput3.png" height="370" />
</p>
