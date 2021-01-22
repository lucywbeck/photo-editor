import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image as Kivy_Image
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from PIL import Image as PIL_Image
from image import *


class Interface(BoxLayout):
    """
    This class is a controller for the photo application.
    """
    def __init__(self,**kwargs):
        """
        Initializes the application.
        """
        super(Interface, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self._button_dict = {}
        self._image = Image('birds.png')
        # Create top button row
        button_layout = BoxLayout(orientation = 'horizontal', size_hint=(1, 0.1))
        button_layout.cols = 5
        top_buttons = ['Image...','Brightness', 'Contrast', 'Warmth', 'Saturation']
        for button in top_buttons:
            self._button_dict[button] = Button(text=button, background_normal='', background_down='', background_color=[.5, .5, .5, 1])
            self._button_dict[button].bind(on_release=self._released)
            button_layout.add_widget(self._button_dict[button])
        self.add_widget(button_layout)
        self._create_dropdown()
        # Create slider row
        slider_layout = BoxLayout(orientation = 'horizontal', size_hint=(1, 0.1))
        slider_layout.cols = 1
        self._slider = Slider(min=-100, max=100, value=0)
        slider_layout.add_widget(self._slider)
        self.add_widget(slider_layout)
        # Create photo row
        photo_layout = BoxLayout(orientation = 'horizontal', size_hint=(1, 0.7))
        self._original = Kivy_Image(source=self._image.source)
        photo_layout.add_widget(self._original)
        self._edited = Kivy_Image(source=self._image.source)
        photo_layout.add_widget(self._edited)
        self.add_widget(photo_layout)
        # Create bottom button row
        button_layout = BoxLayout(orientation = 'horizontal', size_hint=(1, 0.1))
        button_layout.cols = 5
        bottom_buttons = ['Vignette', 'B&W', 'Invert', 'Solarise', 'Pixelize']
        for button in bottom_buttons:
            self._button_dict[button] = Button(text=button, background_normal='', background_down='', background_color=[.5, .5, .5, 1])
            self._button_dict[button].bind(on_release=self._released)
            button_layout.add_widget(self._button_dict[button])
        self.add_widget(button_layout)
        # Declare rest of variables
        self._file_chooser = None
        self._label = None
        self._popup = None
        self._text_input = None

    def _create_dropdown(self):
        """
        Creates a dropdown menu for the image button.
        """
        # Create dropdown for image button
        dropdown = DropDown()
        # Create load button
        self._button_dict['Load'] = Button(text='Load', background_normal='', background_down='',\
            background_color=[.5, .5, .5, 1], size_hint_y=None, height=45)
        self._button_dict['Load'].bind(on_release=self._released)
        self._button_dict['Load'].bind(on_release=self._load)
        dropdown.add_widget(self._button_dict['Load'])
        # Create Save button
        self._button_dict['Save'] = Button(text='Save', background_normal='', background_down='',\
            background_color=[.5, .5, .5, 1], size_hint_y=None, height=45)
        self._button_dict['Save'].bind(on_release=self._released)
        self._button_dict['Save'].bind(on_release=self._save)
        dropdown.add_widget(self._button_dict['Save'])
        # Bind Image button to dropdown
        self._button_dict['Image...'].bind(on_release=dropdown.open)

    def _released(self, instance):
        """
        Carries out the user's request when a button is released

        Parameter instance: The position where the button was pressed
        Precondition: instance is a valid position
        """
        for key in self._button_dict:
            if self._button_dict[key] == instance:
                self._slider.value = 0
                self._reset_buttons()
                if key == 'Image...':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Load':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Save':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Brightness':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Contrast':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Warmth':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Saturation':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Vignette':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'B&W':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Invert':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Solarise':
                    self._button_dict[key].background_color = [0,.64,1,1]
                elif key == 'Pixelize':
                    self._button_dict[key].background_color = [0,.64,1,1]

    def _reset_buttons(self):
        """
        Resets all of the buttons.
        """
        for key in self._button_dict:
            self._button_dict[key].background_color = [.5, .5, .5, 1]

    def _update(self,dt):
        """
        Updates the photo app.

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        for key in self._button_dict:
            if self._button_dict[key].background_color == [0,.64,1,1]:
                if key == 'Brightness':
                    self._brightness()
                elif key == 'Contrast':
                    self._contrast()
                elif key == 'Warmth':
                    self._warmth()
                elif key == 'Saturation':
                    self._saturation()
                elif key == 'Vignette':
                    self._vignette()
                elif key == 'B&W':
                    self._bw()
                elif key == 'Invert':
                    self._invert()
                elif key == 'Solarise':
                    self._solarise()
                elif key == 'Pixelize':
                    self._pixelize()
        try:
            self._label.text = self._file_chooser.selection[0]
        except:
            pass

    def _load(self,instance):
        """
        Creates a popup to allow the user to load an image file directly from his
        or her device.

        Parameter instance: The position where the button was pressed
        Precondition: instance is a valid position
        """
        content = BoxLayout(orientation='vertical')
        # Create file chooser
        self._file_chooser = FileChooserIconView(path='.', filters=['*.png'])
        content.add_widget(self._file_chooser)
        # Create label
        self._label = Label(size_hint_y=None, height=30, font_size=14, text='')
        content.add_widget(self._label)
        # Create buttons
        options = BoxLayout(size_hint_y=None, height=30)
        cancel_choice = Button(text='Cancel',on_release=self._dismiss_popup)
        options.add_widget(cancel_choice)
        load_choice = Button(text='Load', on_release=self._load_file)
        options.add_widget(load_choice)
        content.add_widget(options)
        # Create popup
        self._popup = Popup(title='Load image', content=content, size_hint=(0.8,0.8), pos_hint={'center_x':0.5, 'center_y':0.5})
        self._popup.open()

    def _dismiss_popup(self,instance):
        """
        Dismisses the popup.

        Parameter instance: The position where the button was pressed
        Precondition: instance is a valid position
        """
        self._popup.dismiss()

    def _load_file(self,instance):
        """
        Loads an image file directly from the user's device to the photo app.

        Parameter instance: The position where the button was pressed
        Precondition: instance is a valid position
        """
        try:
            file = self._file_chooser.selection[0]
            self._image = Image(file)
            self._original.source = self._image.source
            self._original.reload()
            self._edited.source = self._image.source
            self._edited.reload()
            self._popup.dismiss()
        except:
            pass

    def _save(self,instance):
        """
        Creates a popup to allow the user to save an image file directly to his
        or her device.

        Parameter instance: The position where the button was pressed
        Precondition: instance is a valid position
        """
        content = BoxLayout(orientation='vertical')
        # Create file chooser
        self._file_chooser = FileChooserIconView(rootpath='.', filters=['*.png'])
        content.add_widget(self._file_chooser)
        # Create text box
        self._text_input = TextInput(size_hint_y=None, height=30, font_size=14, multiline=False)
        content.add_widget(self._text_input)
        # Create buttons
        options = BoxLayout(size_hint_y=None, height=30)
        cancel_choice = Button(text='Cancel',on_release=self._dismiss_popup)
        options.add_widget(cancel_choice)
        load_choice = Button(text='Save', on_release=self._save_file)
        options.add_widget(load_choice)
        content.add_widget(options)
        # Create popup
        self._popup = Popup(title='Save image', content=content, size_hint=(0.8,0.8), pos_hint={'center_x':0.5, 'center_y':0.5})
        self._popup.open()

    def _save_file(self,instance):
        """
        Saves an image file directly from the photo app to the user's device.

        Parameter instance: The position where the button was pressed
        Precondition: instance is a valid position
        """
        try:
            # Create a new image with the original image size
            new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
            new_pix = new_image.load()
            # Copy the current image's pixels to the new image's pixels
            for y in range(self._image.height):
                for x in range(self._image.width):
                    pixel = self._image.pix[x,y]
                    r = pixel[0]
                    g = pixel[1]
                    b = pixel[2]
                    new_pix[x,y] = (r,g,b)
            # Save and reload the new image
            name = self._text_input.text
            new_image.save(name + '.png')
            self._popup.dismiss()
        except:
            pass

    def _brightness(self):
        """
        Changes the image's brightness.
        """
        value = self._slider.value
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                r = round(pixel[0] * (1 + value/100))
                g = round(pixel[1] * (1 + value/100))
                b = round(pixel[2] * (1 + value/100))
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _contrast(self):
        """
        Changes the image's contrast.

        Formula from https://www.dfstudios.co.uk/articles/programming/image-programming-algorithms/
        image-processing-algorithms-part-5-contrast-adjustment/
        """
        value = self._slider.value
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        contrast = (259 * (value + 255)) / (255 * (259 - value))
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                r = round(contrast * (pixel[0] - 128) + 128)
                g = round(contrast * (pixel[1] - 128) + 128)
                b = round(contrast * (pixel[2] - 128) + 128)
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _warmth(self):
        """
        Changes the image's warmth.
        """
        value = self._slider.value
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                r = round(pixel[0] + value)
                if r > 255:
                    r = 255
                if r < 0:
                    r = 0
                g = pixel[1]
                b = pixel[2]
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _saturation(self):
        """
        Changes the image's saturation.
        """
        value = self._slider.value
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                hsv = self._rgb_to_hsv(pixel)
                hsv[1] = hsv[1] * (1 + value/100)
                if hsv[1] > 1:
                    hsv[1] = 1
                if hsv[1] < 0:
                    hsv[1] = 0
                rgb = self._hsv_to_rgb(hsv)
                r = round(rgb[0])
                g = round(rgb[1])
                b = round(rgb[2])
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _vignette(self):
        """
        Adds the vignette filter to the image.
        """
        value = self._slider.value
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                centerw = self._image.width/2
                centerh = self._image.height/2
                term1 = (centerw - x)**2
                term2 = (centerh - y)**2
                # d1 is the distance from the pixel to the center of the image
                d1 = (term1 + term2)
                # d2 is the distance from the center of the image to any of the corners
                d2 = (centerw**2 + centerh**2)
                vignette = 1-(d1/d2)
                pixel = self._image.pix[x,y]
                r = round(pixel[0] * vignette)
                g = round(pixel[1] * vignette)
                b = round(pixel[2] * vignette)
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _bw(self):
        """
        Adds the black and white filter to the image.
        """
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                average = (pixel[0] + pixel[1] + pixel[2])/3
                if average > 100:
                    r = 255
                    g = 255
                    b = 255
                else:
                    r = 0
                    g = 0
                    b = 0
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _invert(self):
        """
        Adds the invert filter to the image.
        """
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                r = 255 - pixel[0]
                g = 255 - pixel[1]
                b = 255 - pixel[2]
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _solarise(self):
        """
        Adds the solarise filter to the image.
        """
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        new_pix = new_image.load()
        # Change the new image's pixels
        for y in range(self._image.height):
            for x in range(self._image.width):
                pixel = self._image.pix[x,y]
                if pixel[0] < 100:
                    r = 255 - pixel[0]
                else:
                    r = pixel[0]
                if pixel[1] < 100:
                    g = 255 - pixel[1]
                else:
                    g = pixel[1]
                if pixel[2] < 100:
                    b = 255 - pixel[2]
                else:
                    b = pixel[2]
                new_pix[x,y] = (r,g,b)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _pixelize(self):
        """
        Adds the pixelize filter to the image.
        """
        # Create a new image with the original image size
        new_image = PIL_Image.new('RGB', (self._image.width,self._image.height), 'white')
        # Change the new image's pixels
        STEP = 5
        total = 0
        col_range = self._image.width//STEP
        if self._image.width % STEP != 0:
            col_range += 1
        row_range = self._image.height//STEP
        if self._image.height % STEP != 0:
            row_range += 1
        for row in range(row_range):
            for col in range(col_range):
                self._pixelize_helper(self._image, new_image, STEP,STEP*row,STEP*col)
        # Save and reload the new image
        new_image.save('new.png')
        self._edited.source = 'new.png'
        self._edited.reload()

    def _pixelize_helper(self, image, new_image, STEP, ypos, xpos):
        """
        Serves as a helper function to _pixelize()
        """
        total_red = 0
        total_green = 0
        total_blue = 0

        step_width = STEP
        step_height = STEP

        if xpos + STEP > image.width:
            step_width = image.width - xpos
        if ypos + STEP > image.height:
            step_height = image.height - ypos

        num_pixels = step_width * step_height

        for y in range(ypos, ypos + step_height):
            for x in range(xpos, xpos + step_width):
                pixel = image.pix[x,y]
                total_red += pixel[0]
                total_green += pixel[1]
                total_blue += pixel[2]

        average_red = round(total_red / num_pixels)
        average_green = round(total_green / num_pixels)
        average_blue= round(total_blue / num_pixels)

        new_pix = new_image.load()
        for y in range(ypos, ypos + step_height):
            for x in range(xpos, xpos + step_width):
                r = average_red
                g = average_green
                b = average_blue
                new_pix[x,y] = (r,g,b)


    def _rgb_to_hsv(self,rgb):
        """
        Return a list of HSV values

        Formula from https://en.wikipedia.org/wiki/HSL_and_HSV

        Parameter rgb: the color to convert to a HSV object
        Precondition: rgb is a list of RGB values
        """
        # The RGB numbers are in the range 0..255.
        # Change them to range 0..1 by dividing them by 255.0.
        r = rgb[0] / 255.0
        g = rgb[1] / 255.0
        b = rgb[2] / 255.0
        maximum = max(r,g,b)
        minimum = min(r,g,b)
        if maximum == minimum:
            h = 0
        elif maximum == r and g>=b:
            h = 60.0 * (g-b)/(maximum-minimum)
        elif maximum == r and g<b:
            h = 60.0 * (g-b)/(maximum-minimum) + 360.0
        elif maximum == g:
            h = 60.0 * (b-r)/(maximum-minimum) + 120.0
        elif maximum == b:
            h = 60.0 * (r-g)/(maximum-minimum) + 240.0
        if maximum == 0:
            s = 0
        else:
            s = 1 - minimum / maximum
        v = maximum
        return [h,s,v]

    def _hsv_to_rgb(self,hsv):
        """
        Returns a list of RGB values

        Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

        Parameter hsv: the color to convert to a RGB object
        Precondition: hsv is a list of HSV values
        """
        h = hsv[0]
        s = hsv[1]
        v = hsv[2]
        hi = int(h/60)
        f = h/60 - hi
        p = v*(1-s)
        q = v*(1-f*s)
        t = v*(1-(1-f)*s)

        if hi == 0 or hi == 5:
            r = v
        elif hi == 1:
            r = q
        elif hi == 2 or hi == 3:
            r = p
        elif hi == 4:
            r = t

        if hi == 0:
            g = t
        elif hi == 1 or hi == 2:
            g = v
        elif hi == 3:
            g = q
        elif hi ==4 or hi == 5:
            g = p

        if hi == 0 or hi == 1:
            b = p
        elif hi == 2:
            b = t
        elif hi == 3 or hi == 4:
            b = v
        elif hi == 5:
            b = q

        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        return [r,g,b]

class PhotoApp(App):
    """
    The controller class for the photo application.
    """
    def build(self):
        """
        Initializes the graphics window.
        """
        interface = Interface()
        Clock.schedule_interval(interface._update, 1.0 / 60.0)
        return interface


if __name__ == '__main__':
    PhotoApp().run()
