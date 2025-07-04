# Infarcted Ventricles Visualization with PyVista

This project provides a 3D interactive visualization of infarcted ventricular regions for multiple patients using PyVista. It displays the three main ventricular zones: **Core**, **Border Zone**, and **Healthy Tissue** (ventricle tagged mesh), allowing detailed exploration and analysis.

## Features

- **Three-panel layout:** Visualizes data from three different patients (Patient 2, Patient 5, Patient 36) side by side.
- **3D mesh rendering:** Loads and renders infarcted ventricular meshes (`Core Surface`, `Border Zone Surface`, and `ventricle_Tagged`) from `.vtk` files.
- **Interactive controls:**
  - Sliders to adjust the opacity of the ventricle tagged mesh per patient.
  - Sliders to set scalar threshold values dynamically without clearing the scene.
  - Checkbox buttons to toggle visibility of Core, Border Zone, and Ventricle meshes independently.
- **Custom scalar bar** for scalar values visualization on Patient 2 panel.
- **Intuitive UI** with labels and titles for each patient’s visualization.

## Requirements

- Python 3.x
- PyVista
- VTK (usually installed automatically with PyVista)
- NumPy (optional, depending on environment)

Install dependencies with:

```bash
pip install pyvista

/project_root
│
├── p2/
│   ├── Core Surface.vtk
│   ├── Border Zone Surface.vtk
│   └── ventricle_Tagged.vtk
│
├── p5/
│   ├── Core Surface.vtk
│   ├── Border Zone Surface.vtk
│   └── ventricle_Tagged.vtk
│
├── p36/
│   ├── Core Surface.vtk
│   ├── Border Zone Surface.vtk
│   └── ventricle_Tagged.vtk
│
└── your_script_name.py
```

## About the data
Core Surface.vtk: Mesh of the infarct core region.

Border Zone Surface.vtk: Mesh of the transitional infarct border zone.

ventricle_Tagged.vtk: Mesh of the entire ventricle tagged with scalar values (DistEndoToEpi), used for scalar visualization and threshold filtering.
