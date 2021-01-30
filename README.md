# Photo-Editor
Photo Editor allows the user to upload any PNG file and adjust brightness, contrast, warmth, saturation, and apply a variety of photo filters such as Vignette, Black and White, Invert, Solarise, and Pixelize. 

I developed a graphical user interface (GUI) that displays the original and edited image side by side as the user applies his or her edits. I designed the filters by using mathematical algorithms to manipulate pixel data in the form of RGB and HSV values. I also implemented an edit history that tracks up to 50 modifications, allowing the user to undo and reset edits to an image. All code was written in Python. After the user is satisfied with the edited photo, he or she may save the photo directly to his or her device.

# Prerequisites
Follow these instructions to download Kivy: https://kivy.org/doc/stable/gettingstarted/installation.html

IMPORTANT: Make sure to follow the instructions for "Installing Kivy’s dependencies" to support video and audio.

For Windows users, open up a command shell and run the following commands in order one at a time:
```
python -m pip install kivy[base] kivy_examples

python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew; 

python -m pip install kivy.deps.gstreamer
```
# Launching Photo-Editor
Download the code as a ZIP file and extract the file. 
Change the directory in your command shell so that you are inside of the extracted Photo-Editor folder.
Type ```python editor.py``` on your command line and press enter. 
# Videos
Click here to view a video on youtube previewing Photo Editor's features: [Photo Editor by Lucy Beck](https://www.youtube.com/watch?v=ZFpjhEbxg-8&list=PL4oFuWmD_bSUw76gEzB1mhwHcuxlfvlTJ)

