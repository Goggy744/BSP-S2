#Import pandas library using the alias pd
import pandas as pd


class Image:
    """
    Image class that represent a 28 by 28 pixels image
    """
    def __init__(self, img: list) -> None:
    
        """ Description
        Class constructor
    
        :type img: list
        :param img: a list of 784 pixels in which the first element is the label of the image
    
        :rtype: None
        """    
        self.__label = img[0]
        self.__pixels = self.pixel_slice(img)


    def get_label(self) -> int:
    
        """ Description
        Getter function for the label
        
        :rtype: int
        """    
        return self.__label
    
    
    def get_pixels(self) -> list:
    
        """ Description
        Getter function for the pixels
    
        :rtype: A list of 28 list
        """    
        return self.__pixels
    
    
    def pixel_slice(self, img: list) -> list:
    
        """ Description
        Function that take a list of 784 pixels and slice them into 28 lists of 28 pixels
    
        :type img:list:
        :param img:list:
        
        :rtype: list
        """    
        listPixels = []
        
        for i in range(1,29):
            listPixels.append(img[28*(i-1)+1:28*i+1])
        
        return listPixels
    
    def display(self) -> None:
    
        """ Description
        Function that display the image data : Label + Pixels
    
        :rtype: None
        """    
        print(f"Label: {self.__label}")
        print(f"Pixels: {self.__pixels}")
        
        
class Datasets:
    
    def __init__(self, data=[]) -> None:
    
        """ Description
        Class constructor
        
        :type data: list
        :param data: an empty list
    
    
        :rtype: None
        """    
        self.__data = data
        
        
    def get_data(self):
    
        """ Description
        Getter function for data
    
        :rtype: List of Image object
        """   
        return self.__data
    
    
    def add_data(self, Image : Image) -> None:
    
        """ Description
        Function that add an Image object to the dataset
        
        :type Image:Image
        :param Image: An Image object
    
        :rtype: None
        """    
        self.__data.append(Image)
    

#Read the data using pandas library
data = pd.read_csv("archive/sign_mnist_train.csv")
#Create a dataset instance
dataset = Datasets()

#Loop through the data values 
for img in data.values:
    #Add each Image to the dataset
    dataset.add_data(Image(img))



