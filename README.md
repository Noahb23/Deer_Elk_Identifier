# Deer and Elk Recognizer

 This AI can inform the user for which is which, when the user sees a deer or elk in the wild. This is very useful, as it can help people who are not very informed on these animals to learn more about them and help define these animals. This can be used by anyoone, from those who don't know much about these animals, to researchers, who are studying the animals for research purposes. There are also fun facts of the animal recognized that appear in the terminal as well.

![add image descrition here](direct image link here)

## The Algorithm

The algorithm of this project works by first inputting the dataset in the repository, which was composed on many animals, however, was shortened down to only contain deer and elk. Then, the model sorts them from one another and puts them into two catagories, one is deer, and the other being elk. The resnet-18 was retrained to work with both deer and elk through image recognition. This dataset was put through the model 35 times, also known as epochs, which helps maintain accuracy in determining the animal. Next, it displays whether the photo shows a elk or a deer, and it tells the percentage of certainty it has to the photo showing that image. There are fun facts that appear of the animal recognized, which is done by having a set of fun facts for each animal, which was found by researching the animals and finding interesting and unique things about both of them. These facts are stored using the lists and using the random library, each of these facts are randomized and a fact of the recognized animal is shown. 

## Running this project

1. Download the repository and Jetson-Inference
2. Cd into the my_project directory
3. In the terminal, type `python3 my-recognition.py (location of image to test)` and press enter
4. Wait and see the results in the terminal
[View a video explanation here](video link)


## Resources

[The dataset used in this projec](https://www.kaggle.com/datasets/virtualdvid/oregon-wildlife)
[Jetson-inference](https://github.com/dusty-nv/jetson-inference/tree/master)
