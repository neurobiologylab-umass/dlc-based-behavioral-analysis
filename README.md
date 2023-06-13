# DLC-based-behavioral-analysis

This repository contains code and documentation for using DeepLabCut (DLC) to analyze the behavior of animals. Specifically, the code in this repository provides a pipeline for using DLC to track the movement of animal paws and analyze their behavior.

## Requirements

- Python 3.x
- DeepLabCut
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Installation

### DeepLabCut Windows Installation Guide

This guide provides step-by-step instructions for installing DeepLabCut on a Windows machine. DeepLabCut is a popular open-source software package used for markerless pose estimation of animals in videos.

#### Prerequisites

Before proceeding with the installation, make sure you have the following prerequisites set up on your Windows machine:

- [Linux installation with WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

#### Installation Steps

Follow the steps below to install DeepLabCut on your Windows machine:

1. Open the Ubuntu subsystem installed with WSL 2.

2. Install the DeepLabCut helper package by running the following command in the Ubuntu subsystem:
   ```
   apt update && apt upgrade
   apt install python3-pip
   pip install deeplabcut-docker
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

## License

This code is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
