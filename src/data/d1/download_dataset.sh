#!/bin/bash
curl -L -o ../../../data/raw/d1/top-100-hubble-telescope-images.zip\
  https://www.kaggle.com/api/v1/datasets/download/redwankarimsony/top-100-hubble-telescope-images

unzip ../../../data/raw/d1/top-100-hubble-telescope-images.zip -d ../../../data/raw/d1/images/
