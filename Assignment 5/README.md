Set Up
1. Open terminal/CMD line
2. Navigate to the folder containing files


How to build the docker image?
1. build the image with this command: docker build -t snake_game . 

How to Run the experiment
1. Use this command to get the estimated noise standard deviation (0.09861919952236592): docker run -ti snake_game 


How to get the Output of the experiment
1. You need to specify the directory of the folder where you want the output of the app to be sent, with the WORKDIR and the name of the docker image
Since I want the output to be saved in my current directory: docker run -v C:\Users\username\PycharmProjects\CYBR460game:/snake -it snake_game 


