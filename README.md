# usf-engy680-urban-energy-fall2026
Shared code for Urban Energy and Climate course materials.

## Setup

We will work through these steps together in class, so just use this README as a reference.

### Install conda from command-line (recommended for Macs) or graphical Anaconda distribution:

- `brew install miniconda`
- _or_ Download Miniconda or full Anaconda distribution from https://www.anaconda.com/download and run installer.

### Sync environment:

Navigate to repo home directory (i.e. `[YOUR_LOCAL_PATH]/usf-engy680-urban-energy-fall2026/`) and run in terminal:

`conda env create -f environment.yml -n [MY_ENVIRONMENT_NAME]`

replacing [MY_ENVIRONMENT_NAME] with a name for your local environment like engy680.

#### On a PC you can run a terminal inside the Anaconda application, or you can create the environment entirely using the application **[Needs testing]**:
1.  Open the Anaconda Navigator application.
2.  Click the Environments tab on the left.
3.  At the bottom of the environments list, click the Import button (if you don't see it, look for a + or gear icon and select Import).
4.  Enter a Name for the new environment.
5.  Under Specification File, browse to your edited .yml file.
6.  Click Import / Create and wait for the solver to finish. This can take several minutes.

## Edit notebooks in Jupyter Lab

From the command-line, first activate your new environment and then open jupyter-lab:

`conda activate [MY_ENVIRONMENT_NAME]`

`jupyter-lab`

This should launch a new browser window in Jupyter Lab.

Alternatively, you can activate your new environment and launch Jupyter Lab directly from the Anaconda Navigator.

Follow the navigation buttons in Jupyter Lab to open the desired notebook file (files ending in '.ipynb') or create a new one. It autosaves as you edit or run cells.

When you're done you can shut down Jupyter Lab, and you can check in your code to your personal private course repo using GitHub Desktop.