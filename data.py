#Import pandas library using the alias pd
import pandas as pd


class Image:
    def __init__(self, img: list) -> None:
        self.__label = img[0]
        self.__pixels = self.pixel_slice(img)

    def get_label(self) -> int:
        return self.__label
    
    def get_pixels(self) -> list:
        return self.__pixels
    
    def pixel_slice(self, img: list) -> list:
        listPixels = []
        
        for i in range(1,29):
            listPixels.append(img[28*(i-1)+1:28*i+1])
        
        return listPixels
    
    def display(self) -> None:
        print(f"Label: {self.__label}")
        print(f"Pixels: {self.__pixels}")
        
        
class Datasets:
    
    def __init__(self, data=[]) -> None:
        self.__data = data
        
    def get_data(self):
        return self.__data
    
    def add_data(self, Image : Image) -> None:
        self.__data.append(Image)
    

data = pd.read_csv("archive/sign_mnist_train.csv")
dataset = Datasets()

for img in data.values:
    dataset.add_data(Image(img))



