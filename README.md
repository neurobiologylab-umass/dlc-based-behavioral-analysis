# DLC-based-behavioral-analysis

This repository contains code and documentation for using DeepLabCut (DLC) to analyze the behavior of animals. Specifically, the code in this repository provides a pipeline for using DLC to track the movement of animal paws and analyze their behavior.

## DeepLabCut Windows Installation Guide

This section guides you through a step-by-step process to install DeepLabCut on a Windows machine. DeepLabCut is an open-source package primarily used for markerless pose estimation of animals in videos.

### Installation Steps

#### 1. Download Anaconda:

Anaconda is a free and open-source distribution of Python and R, primarily used for scientific computing. It simplifies package management and deployment. You can download and install Anaconda from [here](https://www.anaconda.com).

   <img src="./imgs/anaconda_download.jpg" alt="download anaconda" width="500" style="border: 1px solid black;">

#### 2. Download the Conda Environment File:

Download the Conda environment file [`DLC-CPU.yaml`](https://github.com/neurobiologylab/dlc-based-behavioral-analysis/blob/main/env/DLC-CPU.yaml).

#### 3. Create a New Folder:

Create a new folder named "DeepLabCut" in your preferred workspace directory.

#### 4. Launch Anaconda Navigator:

Start the Anaconda Navigator application.

#### 5. Launch CMD.exe Prompt:

In the Anaconda Navigator, launch the "CMD.exe Prompt" which will open a new command prompt window.

   <img src="./imgs/anaconda_navigator.jpg" alt="anaconda navigator" width="500" style="border: 1px solid black;">

#### 6. Navigate to the Workspace:

In the command prompt window, navigate to your "DeepLabCut" directory. For example, if your "DeepLabCut" folder is in the root of the C drive, you would type:

   ```
   cd C:\your_workspace_directory\DeepLabCut
   ```

#### 7. Create the Conda Environment:

In the "DeepLabCut" directory, use the downloaded `.yaml` file to create a new Conda environment:

   ```
   conda env create -f DLC-CPU.yaml
   ```

   <img src="./imgs/create_environment.jpg" alt="create environment" width="500" style="border: 1px solid black;">

#### 8. Activate the New Environment:

Activate the new Conda environment with:

   ```
   conda activate DEEPLABCUT
   ```

#### 9. Launch a DeepLabCut Session:

Initiate a DeepLabCut session using the command prompt:

   ```
   python -m deeplabcut
   ```

For more installation tips, visit the [official DeepLabCut documentation](https://deeplabcut.github.io/DeepLabCut/docs/recipes/installTips.html).


## DeepLabCut Usage Guide

This guide provides detailed instructions on how to use DeepLabCut (DLC) for your video analysis tasks.

### Steps

1. **Start DeepLabCut**: 

    Launch the "CMD.exe Prompt" from Anaconda Navigator, and enter the following commands:

    ```
    conda activate DEEPLABCUT
    python -m deeplabcut
    ```
    This will open the DeepLabCut welcome window.

   <img src="./imgs/dlc_welcome.jpg" width="500" style="border: 1px solid black;">

2. **Create a new project**: 

    Click on `Create New Project` on the welcome page. 

    - Fill out the project name and experimenter name, then check the `Copy videos to project folder` checkbox.
    - Do not use the `Browse videos` button which does work(bug). Use **drag & drop** to add your videos. Note: DLC may not recognize MPEG files correctly, so it's recommended to use MP4 files. Ensure that you don't change the video file location after this step.
    - Once all fields are filled, click `Create`.

3. **Edit Configuration File**: 

    - Locate the `Config.yaml` file in your project directory and open it.
    - Replace the `bodyparts` list with the labels you want to use for your project. 
    - The `numframes2pick` parameter specifies the number of frames to extract for labeling. For accurate analysis, it is recommended to pick a couple hundred frames.
    - The `skeleton` parameter represents the connections between each label. These connections will be displayed in the final video.
    - Save your changes (Ctrl+S) and verify them by clicking the `Edit Config.yaml` button in DeepLabCut.

4. **Extract Frames**: 

    Navigate to the `Extract Frames` tab in DeepLabCut. 

    - You can keep the default settings.
    - For better analysis, it's recommended to crop the frame. Draw a rectangle around the area of interest in the GUI, then click `Crop`.
    - Once you're done, click `Extract Frames`.

5. **Label Frames**: 

    Navigate to the `Label Frames` tab. 

    - Click the `Label Frames` button to open the frame labeling interface.
    - Load the frames you extracted in the previous step.
    - Use the tools in the interface to label the body parts in each frame. Remember to save your changes (Ctrl+S).
    - Check if the `CollectedData_YourName.csv` and `CollectedData_YourName.h5` files have been created in the `labeled-data/video_name` directory in your project folder.

6. **Create a Training Dataset**: 

    Navigate to the `Create Training Dataset` tab. 

    - You can keep the default settings.
    - Click `Create Training Dataset`.

7. **Train the Network**: 

    Navigate to the `Train Network` tab. 

    - Set `displayiters` to 20000, `saveiters` to 50000, and `maxiters` to 1000000.
    - Click `Start Training`. The training process will take some time and you can monitor its progress in the Anaconda Prompt.

8. **Evaluate the Network**: 

    Navigate to the `Evaluate Network` tab. 

    - Check both `plotting` and `comparisonbodyparts` options.
    - Click `Start Evaluation`.

9. **Analyze Videos**: 

    Navigate to the `Analyze Videos` tab. 

    - Click `Select videos` and add the videos you want to analyze.
    - Ensure `save_as_csv` is checked.
    - Click `Analyze Videos`. 

10. **Create Labeled Videos**: 

    Navigate to the `Create Labeled Videos` tab. 

    - Add the videos you analyzed in the previous step.
    - Check both `plot_tracklets` and `save_frames` options.
    - Click `Create Videos`.

11. **Extract Outliers (optional)**: 

    If the analysis results are not satisfactory, navigate to the `Extract Outlier Frames` tab. 

    - Add the videos you want to refine.
    - Specify the extraction algorithm. If you choose `manual`, a new interface will open, allowing you to go through each frame of the video and mark frames that need to be relabeled.
    - Click `Extract Outlier Frames`.

12. **Refine Labels (optional)**: 

    If you have outlier frames, navigate to the `Refine Labels` tab. 

    - Load the frames, move the mislabeled points to their correct positions, then save your changes.
    - You can verify your changes by checking the `CollectedData_YourName.csv` file in the `labeled-data/video_name` directory in your project folder.
    - Once you're done, click `Merge datasets`.

Congratulations! You have successfully used DeepLabCut to analyze your videos. For further analysis, you can import the CSV files created during the analysis into your preferred data analysis software.














## Usage

To use this code, you must first create a DLC project for your animal behavior data. Once you have created a project and labeled your data, you can use the scripts in this repository to analyze the data and generate visualizations.

The main script for analyzing the data is `analyze_behavior.ipynb`, which takes a DLC project file as input and outputs data on paw movement and behavior. The script generates various visualizations to help you understand the data, including time series plots of paw movement and behavioral analysis plots.

## Contributing

Contributions to this project are welcome. If you find a bug or have a suggestion for how to improve the code, please open an issue or submit a pull request.

