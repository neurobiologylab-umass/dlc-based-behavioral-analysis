# DLC-based-behavioral-analysis

This repository contains code and documentation for using DeepLabCut (DLC) to analyze the behavior of animals. Specifically, the code in this repository provides a pipeline for using DLC to track the movement of animal paws and analyze their behavior.

## Requirements

- Python 3.x
- DeepLabCut
- NumPy
- Pandas
- Matplotlib
- Seaborn

## DeepLabCut Windows Installation Guide

This guide provides step-by-step instructions for installing DeepLabCut on a Windows machine. DeepLabCut is a popular open-source software package used for markerless pose estimation of animals in videos.

### Installation Steps

Follow the steps below to install DeepLabCut on your Windows machine:

#### Conda Install:
##### Prerequisites
Anaconda: A free and open-source distribution of Python and R for scientific computing. It simplifies package management and deployment.

1. Download and install [Anaconda](https://www.anaconda.com/distribution/): A free and open-source distribution of Python and R for scientific computing. It simplifies package management and deployment.
   
2. Visit the [DeepLabCut's homepage](http://www.mackenziemathislab.org/deeplabcut) and download the Conda environment file (`.yaml`). The download button can be found at the bottom of the page.

3. Create a new folder named "DeepLabCut" in your "Documents" directory.

4. Launch the Anaconda Navigator (Anaconda3).

5. In the Anaconda Navigator, launch the "CMD.exe Prompt". This will open a new command prompt window.

6. Navigate to the "DeepLabCut" directory in the command prompt:
   
   ```
   cd C:\Users\YourUserName\Documents\DeepLabCut
   ```

7. In the "DeepLabCut" directory, create the new Conda environment with the downloaded `.yaml` file:

   ```
   conda env create -f DEEPLABCUT.yaml
   ```

8. If prompted, enter your administrator password to allow the installation of "python.exe".

9. Once the installation is complete, activate the new Conda environment:

   ```
   conda activate DEEPLABCUT
   ```

10. Close the command prompt.

11. Back in the Anaconda Navigator, select "DeepLabCut" from the "Applications on" dropdown menu.

12. Find "CMD.exe Prompt" and click on "Install". Provide administrator credentials if prompted.

13. After installation, click on "Launch" to open a new command prompt.

14. In the new command prompt, launch a DeepLabCut session:

    ```
    ipython
    import deeplabcut
    deeplabcut.launch_dlc()
    ```

Your command prompt should look like this:

    ```
    (DEEPLABCUT) C:\Users\YourUserName>ipython
    Python 3.8.10 | packaged by conda-forge | (default, May 11 2021, 06:25:23) [MSC v.1916 64 bit (AMD64)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.25.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: import deeplabcut

    In [2]: deeplabcut.launch_dlc()
    ```

15. If everything has been installed correctly, the DeepLabCut GUI should now appear.


#### Docker Install:

##### Prerequisites

Before proceeding with the installation, make sure you have the following prerequisites set up on your Windows machine:

- [Linux installation with WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

1. Open the Ubuntu(22.04) subsystem installed with WSL 2.

2. Install the DeepLabCut helper package by running the following command in the Ubuntu subsystem:
   ```
   sudo apt update
   sudo apt upgrade
   sudo apt install python3-pip
   sudo pip install deeplabcut-docker
   ```

3. Verify the Docker installation by running the following command:
   ```
   docker version
   ```

4. To launch the DeepLabCut graphical user interface (GUI) directly, run the following command:
   ```
   deeplabcut-docker gui
   ```

Congratulations! You have successfully installed DeepLabCut on your Windows machine. You can now use DeepLabCut for markerless pose estimation in your research projects.

For more information on how to use DeepLabCut, refer to the official DeepLabCut documentation and tutorials available on the [DeepLabCut GitHub repository](https://github.com/DeepLabCut/DeepLabCut).

To use this code, you must first install DeepLabCut and its dependencies. Once you have installed DeepLabCut, you can install the additional required packages using pip:

```
pip install numpy pandas matplotlib seaborn
```

## Usage

To use this code, you must first create a DLC project for your animal behavior data. Once you have created a project and labeled your data, you can use the scripts in this repository to analyze the data and generate visualizations.

The main script for analyzing the data is `analyze_behavior.ipynb`, which takes a DLC project file as input and outputs data on paw movement and behavior. The script generates various visualizations to help you understand the data, including time series plots of paw movement and behavioral analysis plots.

## Contributing

Contributions to this project are welcome. If you find a bug or have a suggestion for how to improve the code, please open an issue or submit a pull request.

