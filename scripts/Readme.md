# Python Scripts Documentation

This documentation covers four Python scripts: `hash_filepath.py`, `rewrite_data.py`, `soaxLogs_to_image.py`, and `mann_whitney_u_test.py`. Each script serves a specific purpose in data processing, file management, and statistical analysis.

# Python Scripts Documentation

This documentation covers three Python scripts: `hash_filepath.py`, `rewrite_data.py`, and `soaxLogs_to_image.py`. Each script serves a specific purpose in data processing and file management.

## hash_filepath.py

### Overview
This script creates a hashtable (dictionary) of filenames based on file type, number, ridge, and stretch values from SOAX experiment logs.

### Functions

#### `create_filename_hashtable(directory)`

Creates a hashtable of filenames based on file type, number, ridge, and stretch values.

- **Parameters:**
  - `directory` (str): The directory path containing the SOAX experiment logs.
- **Returns:**
  - `dict`: A hashtable with keys as tuples of (file_type(number), (ridge, stretch)) and values as the corresponding filenames.

### Usage

```python
directory = "/path/to/soax/experiment/logs/"
filename_hashtable = create_filename_hashtable(directory)
print(filename_hashtable)
```

### Notes
- The script uses regular expressions to extract relevant information from filenames.
- There's commented-out code for saving the hashtable to a JSON file, which needs to be fixed.

## rewrite_data.py

### Overview
This script copies and renames files from a source directory to a destination directory.

### Functions

#### `rename_file(fname)`

Renames files by modifying their format.

- **Parameters:**
  - `fname` (str): The original filename.
- **Returns:**
  - `str`: The renamed filename.

#### `copy_data(src, dest)`

Copies files from the source directory to the destination directory, renaming them in the process.

- **Parameters:**
  - `src` (str): The source directory path.
  - `dest` (str): The destination directory path.

### Usage

```python
src = "/path/to/source/directory"
dest = "/path/to/destination/directory"
copy_data(src, dest)
```

### Notes
- The script creates the destination directory if it doesn't exist.
- It uses regular expressions to rename files from formats like "AB (1) g.tif" to "AB_1.tif".

## soaxLogs_to_image.py

### Overview
This script converts SOAX log files to images, representing actin filaments.

### Functions

#### `text_path_to_image(text_path)`

Converts a SOAX log file to an image representation.

- **Parameters:**
  - `text_path` (str): The path to the SOAX log file.
- **Returns:**
  - `numpy.ndarray`: A 2D numpy array representing the image.

### Usage

```python
text_path = "/path/to/soax/log/file.txt"
img = text_path_to_image(text_path)
```

### Notes
- The function processes SOAX log files, extracting actin filament data.
- It creates a 512x512 image where actin filaments are represented.
- The resulting image is rotated and flipped for proper orientation.
- Commented-out code for plotting and saving the image is included.

## General Notes

- These scripts are part of a larger project involving SOAX (Snake Optimization Analysis for X) data processing.
- They handle various aspects of file management, data extraction, and visualization for actin filament analysis.
- Some parts of the scripts (especially in `hash_filepath.py` and `soaxLogs_to_image.py`) have commented-out code that may need attention or implementation.


## mann_whitney.py

### Overview
This script performs a Mann-Whitney U test on two datasets and provides detailed statistical results and descriptive statistics.

### Functions

#### `mann_whitney_u_test(data1, data2, alpha=0.05, name_data1='Data 1', name_data2='Data 2')`

Performs a Mann-Whitney U test and prints the results.

- **Parameters:**
  - `data1` (array-like): First dataset
  - `data2` (array-like): Second dataset
  - `alpha` (float): Significance level (default: 0.05)
  - `name_data1` (str): Name of the first dataset (default: 'Data 1')
  - `name_data2` (str): Name of the second dataset (default: 'Data 2')
- **Returns:**
  - None (prints results to console)

### Usage

```python
import numpy as np
from mann_whitney_u_test import mann_whitney_u_test

# Generate example data
np.random.seed(42)
data1 = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=0.5, scale=1, size=100)

# Perform Mann-Whitney U test
mann_whitney_u_test(data1, data2, name_data1="Control Group", name_data2="Treatment Group")
```

### Notes
- The script uses SciPy for the Mann-Whitney U test and normal distribution functions.
- It calculates and displays:
  - p-value
  - Effect size (rank biserial correlation)
  - Confidence interval for the difference in medians
  - Statistical power
  - Descriptive statistics (median, mean, standard deviation, sample size) for both datasets
- Results are presented in a tabular format using the `tabulate` library for better readability.

## General Notes

- These scripts cover a range of functionalities from file management and data processing to statistical analysis.
- They are designed to work with SOAX (Snake Optimization Analysis for X) data and provide tools for analyzing actin filament data.
- The Mann-Whitney U test script can be used independently for statistical comparisons between two groups.
