# Three-Coupled-Oscillators-Interactive-Sim

## Overview
The "Interactive System of Three Coupled Oscillators" is a specialized educational tool aimed at providing an interactive and visual understanding of the dynamics in a system of three coupled oscillators. This tool integrates Python's powerful VPython library for 3D visualization and Tkinter for an intuitive user interface, offering a unique and engaging educational experience.

## Features
- Real-time 3D visualization of a system of three coupled oscillators using VPython.
- Interactive GUI built with Tkinter, allowing users to modify initial conditions and physical parameters like mass and spring constants.
- Functionalities to pause, resume, and terminate the simulation on demand.
- Detailed help section to guide users on interacting with the simulation effectively.

## Installation
Ensure Python is installed on your system to run this simulation. It is recommended to use a virtual environment for running this project to avoid conflicts with other packages. 
You can set up the project by following these steps:

- **Using venv** (Recommended for users without Conda)
1. Clone the repository:
```bash
git clone https://github.com/1Basile/Three-Coupled-Oscillators-Interactive-Sim.git
```
2. Change into the project directory:
```bash
cd Three-Coupled-Oscillators-Interactive-Sim
```
3. Create a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
  - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
  - On Unix or MacOS:
    ```bash
    source venv/bin/activate
    ```
    
5. Install the required dependencies:
```bash
pip install -r requirements.txt
```
- **Using Conda**
1. Clone the repository:
```bash
git clone https://github.com/1Basile/Three-Coupled-Oscillators-Interactive-Sim.git
```
2. Change into the project directory:
```bash
cd Three-Coupled-Oscillators-Interactive-Sim
```
3. Create a Conda environment:
```bash
conda create --name myenv python=3.x
```
4. Activate the Conda environment:
```bash
conda activate myenv
```
6. Install the required dependencies. If available in Conda, prefer Conda packages for better compatibility:
```bash
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```

## Usage
Execute the simulation with the following command:
```bash
python CoupledOscillatorsSimulator.py
```

Use the sliders in the Tkinter window to adjust parameters and initial conditions. The VPython canvas will display the simulation in real-time. Control the simulation using the 'spacebar' to pause/resume and the 'q' key or 'Esc' to terminate or exit.

## Contributing
Your contributions to enhance or expand this project are highly appreciated. Feel free to fork the repository and submit pull requests with your improvements.

