# ROI Analysis Script

This script provides functionality for processing and visualizing Region of Interest (ROI) data from zip files.

## Features

- Read ROI data from zip files
- Process multiple ROI zip files in a directory
- Create xy coordinate pairs from ROI data
- Plot single or multiple ROIs on a black background
- Save and load ROI data in JSON format

## Usage

```python
# Example usage of the script
directory_path = "/content/roiData"
all_roi_data = process_roi_zip_files(directory_path)

# Save processed data to JSON file
with open("roi_data_full.json", "w") as json_file:
    json.dump(all_roi_data, json_file, indent=2)

# Read the processed ROI data
roi_data = read_roi_json("roi_data_full.json")

# Plot all files
plot_roi_data(roi_data)
```

## Functions

- `read_roi_files(file_path)`: Read ROI files from a zip archive
- `get_unique_n_values(rois)`: Get unique 'n' values from ROIs
- `create_xy_pairs(rois)`: Create lists of x,y pairs for each ROI
- `process_roi_zip_files(directory_path)`: Process all ROI zip files in a directory
- `read_roi_json(json_file_path)`: Read ROI data from a JSON file
- `plot_rois(xy_coords, roi_names, image_size, title)`: Plot one or multiple ROIs
- `plot_roi_data(roi_data, file_names, image_size)`: Plot ROI data for multiple files

## Requirements

- Python 3.x
- numpy
- matplotlib
- read_roi

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install numpy matplotlib read_roi
   ```

## License

This project is licensed under the MIT License.

---

# SOAX Tools Documentation

This section covers four Python scripts used for data processing, file management, and statistical analysis in the context of SOAX (Snake Optimization Analysis for X) experiments.

## Table of Contents

1. [hash_filepath.py](#hash_filepathpy)
2. [rewrite_data.py](#rewrite_datapy)
3. [soaxLogs_to_image.py](#soaxlogs_to_imagepy)
4. [mann_whitney.py](#mann_whitneypy)

## hash_filepath.py

### Overview

This script creates a hashtable (dictionary) of filenames based on file type, number, ridge, and stretch values from SOAX experiment logs.

### Functions

#### `create_filename_hashtable(directory)`

Creates a hashtable of filenames based on file type, number, ridge, and stretch values.

**Parameters:**
- `directory` (str): The directory path containing the SOAX experiment logs.

**Returns:**
- `dict`: A hashtable with keys as tuples of (file_type(number), (ridge, stretch)) and values as the corresponding filenames.

### Usage

```python
directory = "/path/to/soax/experiment/logs/"
filename_hashtable = create_filename_hashtable(directory)
print(filename_hashtable)
```

## rewrite_data.py

### Overview

This script copies and renames files from a source directory to a destination directory.

### Functions

#### `rename_file(fname)`

Renames files by modifying their format.

#### `copy_data(src, dest)`

Copies files from the source directory to the destination directory, renaming them in the process.

### Usage

```python
src = "/path/to/source/directory"
dest = "/path/to/destination/directory"
copy_data(src, dest)
```

## soaxLogs_to_image.py

### Overview

This script converts SOAX log files to images, representing actin filaments.

### Functions

#### `text_path_to_image(text_path)`

Converts a SOAX log file to an image representation.

### Usage

```python
text_path = "/path/to/soax/log/file.txt"
img = text_path_to_image(text_path)
```

## mann_whitney.py

### Overview

This script performs a Mann-Whitney U test on two datasets and provides detailed statistical results and descriptive statistics.

### Functions

#### `mann_whitney_u_test(data1, data2, alpha=0.05, name_data1='Data 1', name_data2='Data 2')`

Performs a Mann-Whitney U test and prints the results.

### Usage

```python
import numpy as np
from mann_whitney import mann_whitney_u_test

# Generate example data
np.random.seed(42)
data1 = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=0.5, scale=1, size=100)

# Perform Mann-Whitney U test
mann_whitney_u_test(data1, data2, name_data1="Control Group", name_data2="Treatment Group")
```

For more detailed information on each script, please refer to the individual script files and their docstrings.
