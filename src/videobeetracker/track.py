#!/usr/bin/env python

import cv
import argparse

DEBUG_VISUAL = True

class Target:

    def __init__(self, source = None):
        #
        if source:
            self.capture = cv.CaptureFromFile(source)
        else:
            self.capture = cv.CaptureFromCAM(0)
        cv.NamedWindow("Target", 1)

    def run(self, args):
        # Capture first frame to get size
        frame = cv.QueryFrame(self.capture)
        #frame_size = cv.GetSize(frame)
        color_image = cv.CreateImage(cv.GetSize(frame), 8, 3)
        grey_image = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
        moving_average = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_32F, 3)

        first = True
        #closest_to_left = cv.GetSize(frame)[0]
        #closest_to_right = cv.GetSize(frame)[1]
        while True:


            color_image = cv.QueryFrame(self.capture)
            if not color_image:
                print "END OF FILE"
                break
        
            # Smooth to get rid of false positives
            cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)

            if first:
                difference = cv.CloneImage(color_image)
                temp = cv.CloneImage(color_image)
                cv.ConvertScale(color_image, moving_average, 1.0, 0.0)
                first = False
            else:
                cv.RunningAvg(color_image, moving_average, args.motiondelay, None)

            # Convert the scale of the moving average.
            cv.ConvertScale(moving_average, temp, 1.0, 0.0)

            # Minus the current frame from the moving average.
            cv.AbsDiff(color_image, temp, difference)

        
            # Convert the image to grayscale.
            cv.CvtColor(difference, grey_image, cv.CV_RGB2GRAY)
            if DEBUG_VISUAL:
                cv.ShowImage("Grey_image: Difference", grey_image)
            # Convert the image to black and white.
            cv.Threshold(grey_image, grey_image, args.threshold, 255, cv.CV_THRESH_BINARY)
            if DEBUG_VISUAL:
                cv.ShowImage("Grey_image: Black n White", grey_image)
#
            # Dilate and erode to get people blobs
            cv.Dilate(grey_image, grey_image, None, args.dilate)
            if DEBUG_VISUAL:
                cv.ShowImage("Dilate", grey_image)
            cv.Erode(grey_image, grey_image, None, args.erode)
            if DEBUG_VISUAL:
                cv.ShowImage("Erode", grey_image)

            storage = cv.CreateMemStorage(0)
            contour = cv.FindContours(grey_image, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
            
            counter = 0
            while contour:
                counter += 1
                bound_rect = cv.BoundingRect(list(contour))
                contour = contour.h_next()

                pt1 = (bound_rect[0], bound_rect[1])
                pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
                cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 1)
            print counter
            
            cv.ShowImage("Target", color_image)

            # Listen for ESC key
            c = cv.WaitKey(7) % 0x100
            if c == 27:
                break

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Videotracking of bees')
    parser.add_argument('--source', help='the sourcefile')
    parser.add_argument('--dilate', help='cv: dilate', default=18, type=int)
    parser.add_argument('--erode', help='cv: erode', default=10, type=int)
    parser.add_argument('--threshold', help='cv: threshold', default=40, type=int)
    parser.add_argument('--motiondelay', help='cv: motiondelay', default=0.5, type=float)
    
    args = parser.parse_args()


    t = Target(source=args.source)
    t.run(args)
