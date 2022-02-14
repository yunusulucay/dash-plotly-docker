# Deploying a Dashboard by Dash Plot using Daily Climate Dataset

A dashboard created using Plotly's Dash library. There are 3 options in the dashboard. You can select plot types using radio buttons. In this dashboard I plotted histogram, line and scatter plots of dailyClimate dataframe. You can use another dataframe. But be careful on dataframe's index.

<img src="https://user-images.githubusercontent.com/42489236/153922414-3c8a3f46-7cb6-4c01-b4e2-f95e5605f114.png" data-canonical-src="https://user-images.githubusercontent.com/42489236/153922414-3c8a3f46-7cb6-4c01-b4e2-f95e5605f114.png" width="250" height="250" />
<img src="https://user-images.githubusercontent.com/42489236/153922464-9b305880-9940-4880-800b-391323c22e6a.png" data-canonical-src="https://user-images.githubusercontent.com/42489236/153922464-9b305880-9940-4880-800b-391323c22e6a.png" width="250" height="250" />
<img src="https://user-images.githubusercontent.com/42489236/153922499-0ca19c56-c3f0-40bf-af8a-980bfb4b891a.png" data-canonical-src="https://user-images.githubusercontent.com/42489236/153922499-0ca19c56-c3f0-40bf-af8a-980bfb4b891a.png" width="250" height="250" />

### Quick Usage

I assume docker is installed on your system. Go to Dockerfile directory and open terminal. Write ```docker build -t {image_name} .``` here with -t you can determine name of the image. After image creation process done you can see images writing ```docker images``` to terminal. Run container ```docker run -p 8050:8050 {image_name}```. And go to your browser and go to ```localhost:8050```. If you want docker to run background use detach mode. ```docker run -d -p 8050:8050 {image_name}```. Additionally image ID can be used instead of image name.

### DataFrame Overview

Dataframe that I used in this project.

![dataframe_head](https://user-images.githubusercontent.com/42489236/153916745-de049861-bc3c-4557-9043-7941e8f06941.png)

### Deploying Docker on AWS

![deploy_graph](https://user-images.githubusercontent.com/42489236/153919133-0050f53e-ce59-46b7-8110-eb3beb56bacc.jpg)

Create docker image using Dockerfile. Send the image to ECR. On ECS, using ECR image deploy the dockered container. [1]

**Sources**

https://faun.pub/quick-start-guide-to-docker-fa646e0f3f2d

[1] https://towardsdatascience.com/deploying-a-docker-container-with-ecs-and-fargate-7b0cbc9cd608
