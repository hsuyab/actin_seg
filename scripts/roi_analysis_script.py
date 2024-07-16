import os
import glob
import json
import numpy as np
import matplotlib.pyplot as plt
from read_roi import read_roi_zip

def read_roi_files(file_path):
    """
    Read ROI files from a zip archive and return the ROI data.

    Args:
    file_path (str): Path to the ROI zip file.

    Returns:
    dict: Dictionary containing ROI data.
    """
    return read_roi_zip(file_path)

def get_unique_n_values(rois):
    """
    Get all unique 'n' values from the ROIs.

    Args:
    rois (dict): Dictionary containing ROI data.

    Returns:
    set: A set of unique 'n' values.
    """
    return set(roi['n'] for roi in rois.values() if 'n' in roi)

def create_xy_pairs(rois):
    """
    Create lists of x,y pairs corresponding to each ROI name.

    Args:
    rois (dict): Dictionary containing ROI data.

    Returns:
    dict: A dictionary with ROI names as keys and lists of (x,y) tuples as values.
    """
    xy_pairs = {}
    for name, roi in rois.items():
        if 'x' in roi and 'y' in roi:
            x_coords = [roi['x']] if isinstance(roi['x'], (int, float)) else roi['x']
            y_coords = [roi['y']] if isinstance(roi['y'], (int, float)) else roi['y']

            if len(x_coords) != len(y_coords):
                print(f"Warning: ROI '{name}' has mismatched number of x and y coordinates.")
                continue

            xy_pairs[name] = list(zip(x_coords, y_coords))
        else:
            print(f"Warning: ROI '{name}' is missing 'x' or 'y' coordinates.")

    return xy_pairs

def process_roi_zip_files(directory_path):
    """
    Process all ROI zip files in the given directory and store the xy coordinates in a JSON format.

    Args:
    directory_path (str): Path to the directory containing ROI zip files.

    Returns:
    dict: A dictionary containing ROI data for each file, suitable for JSON serialization.
    """
    roi_data = {}
    zip_files = glob.glob(os.path.join(directory_path, "*.zip"))

    for zip_file in zip_files:
        file_key = os.path.splitext(os.path.basename(zip_file))[0]
        rois = read_roi_zip(zip_file)
        file_roi_data = {}
        for roi_name, roi_info in rois.items():
            if 'x' in roi_info and 'y' in roi_info:
                x_coords = roi_info['x'] if isinstance(roi_info['x'], list) else [roi_info['x']]
                y_coords = roi_info['y'] if isinstance(roi_info['y'], list) else [roi_info['y']]
                xy_coords = list(zip(x_coords, y_coords))
                file_roi_data[roi_name] = xy_coords
        roi_data[file_key] = file_roi_data

    return roi_data

def read_roi_json(json_file_path):
    """
    Read ROI data from a JSON file.

    Args:
    json_file_path (str): Path to the JSON file containing ROI data.

    Returns:
    dict: The ROI data as a dictionary.
    """
    with open(json_file_path, 'r') as f:
        roi_data = json.load(f)
    return roi_data

def plot_rois(xy_coords, roi_names=None, image_size=(512, 512), title="ROI Plot"):
    """
    Plot one or multiple ROIs on a black image.

    Args:
    xy_coords (dict or list): Either a dictionary of ROI coordinates or a list of (x, y) pairs for a single ROI.
    roi_names (str or list, optional): Name(s) of the ROI(s) to plot. If None, plot all ROIs in xy_coords.
    image_size (tuple, optional): Size of the image (height, width). Default is (512, 512).
    title (str, optional): Title for the plot. Default is "ROI Plot".

    Returns:
    None: Displays the plot.
    """
    img = np.zeros(image_size)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(img, cmap='gray')

    colors = plt.cm.rainbow(np.linspace(0, 1, 10))

    if isinstance(xy_coords, list):
        x, y = zip(*xy_coords)
        ax.plot(x, y, '-o', color=colors[0], linewidth=0.5, markersize=2)
        ax.set_title(f"ROI: {roi_names if roi_names else 'Unnamed'}")
    else:
        if roi_names is None:
            roi_names = list(xy_coords.keys())
        elif isinstance(roi_names, str):
            roi_names = [roi_names]

        for i, roi_name in enumerate(roi_names):
            if roi_name in xy_coords:
                x, y = zip(*xy_coords[roi_name])
                ax.plot(x, y, '-o', color=colors[i % len(colors)], linewidth=0.5, markersize=2, label=roi_name)
            else:
                print(f"Warning: ROI '{roi_name}' not found in the provided coordinates.")

        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_title(title)

    ax.set_xlim(0, image_size[1])
    ax.set_ylim(image_size[0], 0)
    plt.tight_layout()
    plt.show()

def plot_roi_data(roi_data, file_names=None, image_size=(512, 512)):
    """
    Plot ROI data for specified file names.

    Args:
    roi_data (dict): Dictionary containing ROI data.
    file_names (str or list, optional): Name(s) of the file(s) to plot. If None, plot all files.
    image_size (tuple, optional): Size of the image (height, width). Default is (512, 512).

    Returns:
    None: Displays the plot(s).
    """
    if file_names is None:
        file_names = list(roi_data.keys())
    elif isinstance(file_names, str):
        file_names = [file_names]

    file_names = [f for f in file_names if f in roi_data]

    if not file_names:
        print("No valid file names provided.")
        return

    n_files = len(file_names)
    n_cols = min(3, n_files)
    n_rows = (n_files - 1) // n_cols + 1

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6*n_cols, 5*n_rows), squeeze=False)
    fig.suptitle("ROI Plots", fontsize=16)

    colors = plt.cm.rainbow(np.linspace(0, 1, 10))

    for i, file_name in enumerate(file_names):
        row = i // n_cols
        col = i % n_cols
        ax = axes[row, col]

        img = np.zeros(image_size)
        ax.imshow(img, cmap='gray')

        file_data = roi_data[file_name]
        for j, (roi_name, coordinates) in enumerate(file_data.items()):
            x, y = zip(*coordinates)
            ax.plot(x, y, '-o', color=colors[j % len(colors)], linewidth=0.5, markersize=2, label=roi_name)

        ax.set_xlim(0, image_size[1])
        ax.set_ylim(image_size[0], 0)
        ax.set_title(file_name)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='x-small')

    for i in range(n_files, n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        fig.delaxes(axes[row, col])

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Process ROI zip files
    directory_path = "/content/roiData"
    all_roi_data = process_roi_zip_files(directory_path)

    # Save processed data to JSON file
    with open("roi_data_full.json", "w") as json_file:
        json.dump(all_roi_data, json_file, indent=2)

    print("ROI data has been processed and saved to roi_data_full.json")

    # Read the processed ROI data
    roi_data = read_roi_json("roi_data_full.json")

    # Plot all files
    plot_roi_data(roi_data)

    # Plot a single file (uncomment to use)
    # plot_roi_data(roi_data, "AB 5")

    # Plot multiple specific files (uncomment to use)
    # plot_roi_data(roi_data, ["AB 5", "BB 10"])

    # Get and print the keys (file names) in the ROI data
    print("Files in the ROI data:", roi_data.keys())

    # Example of using other functions (uncomment to use)
    # single_roi_file = read_roi_files("/path/to/single/roi/file.zip")
    # unique_n_values = get_unique_n_values(single_roi_file)
    # xy_pairs = create_xy_pairs(single_roi_file)
    # plot_rois(xy_pairs, title="Single ROI File Plot")
