# Datasets

This document describes all datasets used in the project, including:

- Source & license
- Download instructions
- Preprocessing steps
- How they are used (train/val/test, synthetic vs real, etc.)

## Dataset D0 – Mikulski Archive for Space Telescopes (MAST)
- **ID**: D0  
- **Name**: Mikulski Archive for Space Telescopes (MAST)
- **Source**: https://archive.stsci.edu/home, https://archive.stsci.edu/search-interfaces/hla?utm_source=chatgpt.com
- **License**:   
- **Data format**:
- **Notes**: MAST hosts all calibrated data from Hubble, JWST, TESS, Kepler, etc., including science-grade FITS images (often many thousands of pixels across). Requires scripts to access the images.

## Dataset D1 – Top 100 Hubble Telescope Images
- **ID**: D1  
- **Name**: Top 100 Hubble Telescope Images
- **Source**: https://www.kaggle.com/datasets/redwankarimsony/top-100-hubble-telescope-images/data
- **License**: ?  
- **Data format**: FITS
- **Download**:
  - Script: `src/data/d1/download_dataset.sh`
  - Output path: `data/raw/d1/`
<!--
- **Preprocessing**:
  - Convert to linear RGB (if necessary)
  - Resize / crop into 512×512 patches
  - Save to `data/processed/D1/`
-->

## Dataset D2 – Astronomy Picture of the Day Data Collection

- **ID**: D2  
- **Name**: Astronomy Picture of the Day Data Collection 
- **Source**: https://www.kaggle.com/datasets/harshitstark/astronomy-picture-of-the-day-data-collection  
- **License**: MIT
- **Data format**: JPG

## Dataset D3 – James Webb Telescope Images (Original size)

- **ID**: D3  
- **Name**: James Webb Telescope Images (Original size)  
- **Source**: https://www.kaggle.com/datasets/goelyash/james-webb-telescope-images-original-size  
- **License**: CC0: Public Domain  
- **Data format**: TIF, PNG
- **Size**: 15 images, 798MB

## Dataset D4 – Hubble snapshots

- **ID**: D4  
- **Name**: Hubble snapshots 
- **Source**: https://www.kaggle.com/datasets/quiexx/hubble-snapshots  
- **License**: Unknown  
- **Data format**: 1024x1024 JPG
- **Size**: 261 images, 34MB

## Dataset D5 – Astrophysical_Objects_Image_Dataset_Maxia_E

- **ID**: D5  
- **Name**: Astrophysical_Objects_Image_Dataset_Maxia_E
- **Source**: https://www.kaggle.com/datasets/quiexx/hubble-snapshots  
- **License**: MIT  
- **Data format**: PNG, JPG
- **Size**: ???
- **Notes**: A lot of images a CGI and not real astrophotography images


