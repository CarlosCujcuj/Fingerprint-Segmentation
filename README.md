# Fingerprint Segmentation

The purpose of this project is to segment the image of a fingerprint using certain techniques of Computer Vision like:
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

---  
## How to run it?  
``` 
$ python fSegmentation.py inputImage.png outputImageName.png
```  
Where **inputImage** and **outputImageName** can be any image format  

---
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
 
