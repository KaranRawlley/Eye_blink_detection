# Eye blink detection
   ## using openCV, Python, dlib

#### We'll use a metric called eye aspect ratio(EAR) for eye blink detection

### Steps to do so 

* Eye localization
* finding co-ordinates of eye
   ![](https://github.com/KaranRawlley/Eye_blink_detection/blob/master/blinkeye.jpg)
* calculation of EAR
* observing any rapid decrement in EAR (blink)


### Each eye is repesented by 6(x,y)-coordinates 

# EAR = (|p2-p6|+|p3-p5|)/2*|p1-p4|

### numerator computes distance between vertical eye co-ordinates
### denominator computes distance between horizontal eye co-ordinates


## EAR remains nearly constant while it is open , but falls rapidly towards zero when blinking or is nearly 0 when closed


