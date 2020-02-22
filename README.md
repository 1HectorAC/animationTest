# Animation Test using POV-Ray and Python

## Summary

This project will make a video clip using a 3D image making sofware called POV-ray and Python. The video is a short test that shows 3 balls spinning around a box and then expanding.

## Requirements

You will need to have Python installed. You will also need to install POV-Ray and have the "pvengine.exe" program in the top of the directory. You will also need to download the encoder to encode the images created into a video. It must be called "mencoder.exe" and also must be at the top of the directory.

## How to run

On a command line run:

``` command line
python animate2.py
```

The program will then run which will take a few minutes to complete. It will open and close a POV-ray window constatly until it finishes running. It will also generate a bunch of temporary image files that get deleted at the end (Note that if the program is interupted and ended early then these temporary files will remain in directory).
