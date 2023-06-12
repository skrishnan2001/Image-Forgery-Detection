# Image-Forgery-Detection-and-Localization
This project utilizes two deep learning based approaches for detecting and localizing Splicing and Copy-Move forgeries in images.

## Project Abstract
Digital picture usage has increased at a never-before-seen rate in our day and age, due to the proliferation of gadgets like smartphones and tablets. Furthermore, the development of user-friendly image manipulation software that is available at reasonable prices has made manipulating such content more effortless than ever. Some of these images are tampered with so that it is impossible for the human eye to detect. Moreover, social media platforms have made their distribution to the general public a simple task. It is hence very important to develop automated methods that can detect such forgeries. In this project, we detect and localize splicing and copy-move image forgeries in images by using two different deep-learning techniques - Convolutional Neural Networks (CNN) and Unsupervised Self-Consistency Learning.

For the CNN based method, the network returns a feature representation which is passed on to an Support Vector Machine (SVM) classifier that predicts if an image is forged or authentic. If forgery is detected, the area of tampering is detected and returned. The Unsupervised Self Consistency Learning scheme uses the Exchangeable Image File Format (EXIF) metadata attributes of an image in order to detect and localize forgeries. An image that is identified as forged then undergoes segmentation to localize the spliced region.

## High Level Architecture
![Screenshot](https://github.com/skrishnan2001/Image-Forgery-Detection/blob/master/Architecture%20Diagrams/High%20Level%20Architecture-FYP.drawio.png)

## CNN Approach Architecture Diagram
![Screenshot](https://github.com/skrishnan2001/Image-Forgery-Detection/blob/master/Architecture%20Diagrams/CNN%20Approach%20Architecture%20Diagram.drawio.png)

## Self-Consistency Network Training
![Screenshot](https://github.com/skrishnan2001/Image-Forgery-Detection/blob/master/Architecture%20Diagrams/Self-Consistency%20Model%20Training%20Architecture.drawio.png)

## Self-Consistency Forgery Localization Architecture
![Screenshot](https://github.com/skrishnan2001/Image-Forgery-Detection/blob/master/Architecture%20Diagrams/Self-Consistency%20Localization.drawio.png)




