# Depth Image Estimation Project

This project implements a method for estimating depth images from stereo image pairs using window-based matching and cosine similarity. The implementation is done using Python and OpenCV. This project includes a single file `depth_img_est.py` which performs the depth estimation.

## --------------------------------------------------------------

# Depth Image Estimation

## Table of Contents
- Installation
- Usage
- Project Structure
- Depth Estimation Process
- Results
- Acknowledgements

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Chow05/Depth-Image-Estimation-Project.git
    cd Depth_Image_Estimation
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your stereo image pairs in the `Depth_Image_Estimation/Aloe` directory. The images should be named `Aloe_left_1.png` and `Aloe_right_1.png`.

2. Run the `depth_img_est.py` script to estimate the depth image:
    ```bash
    python depth_img_est.py
    ```

## Project Structure

- `depth_img_est.py`: Main script for performing depth estimation.
- `Depth_Image_Estimation/Aloe/Aloe_left_1.png`: Left image of the stereo pair.
- `Depth_Image_Estimation/Aloe/Aloe_right_1.png`: Right image of the stereo pair.
- `Depth_Image_Estimation/win_cs_result.png`: Output depth image.
- `Depth_Image_Estimation/win_cs_color_result.png`: Color-mapped output depth image.

## Depth Estimation Process

The depth estimation process involves the following steps:

1. **Reading Images**: 
    - Load the left and right images from the specified paths.

2. **Sliding Window View**: 
    - Create sliding window views of the left and right images.

3. **Cosine Similarity Calculation**: 
    - Calculate the cosine similarity between the sliding windows of the left and right images.

4. **Cost Calculation**: 
    - Compute the cost for each disparity value.

5. **Depth Image Generation**: 
    - Generate the depth image based on the minimum cost indices.

## Results

The depth image and its color-mapped version are saved in the `Depth_Image_Estimation` directory as `win_cs_result.png` and `win_cs_color_result.png`, respectively.

## Acknowledgements

This project uses the following libraries:
- `cv2`
- `numpy`

Special thanks to the open-source community for providing these tools.
