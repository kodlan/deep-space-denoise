#!/bin/bash

curl -L -o ../../../data/raw/d2/astronomy-picture-of-the-day-data-collection.zip\
  https://www.kaggle.com/api/v1/datasets/download/harshitstark/astronomy-picture-of-the-day-data-collection

unzip ../../../data/raw/d2/astronomy-picture-of-the-day-data-collection.zip -d ../../../data/raw/d2/images/

mv ../../../data/raw/d2/images/apod_images/apod_images/* ../../../data/raw/d2/images/
rm -r ../../../data/raw/d2/images/apod_images/apod_images/
rm -r ../../../data/raw/d2/images/apod_images/
rm ../../../data/raw/d2/images/apod_data.csv