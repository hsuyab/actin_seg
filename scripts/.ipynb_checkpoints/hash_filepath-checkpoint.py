from glob import glob
import re
import json


def create_filename_hashtable(directory):
    """
    Create a hashtable of filenames based on file type, number, ridge, and stretch values.
    
    Args:
        directory (str): The directory path containing the SOAX experiment logs.
    
    Returns:
        dict: A hashtable (dictionary) with keys as tuples of (file_type(number), (ridge, stretch))
              and values as the corresponding filenames.
    """
    # Retrieve text files using glob
    text_files = glob(directory + "/*//*.txt")
    
    # Extract folder names from file paths
    folder_names = [file.split('/')[-2] for file in text_files]
    
    # Keep unique folder names and sort them
    unique_folder_names = list(set(folder_names))
    unique_folder_names = [i.strip() for i in unique_folder_names]
    unique_folder_names.sort()
    
    # Create a dictionary to store the filename hash
    filename_hash = {}
    
    # Iterate over each folder in the unique folder names
    for folder in unique_folder_names:
        # Retrieve SOAX experiment logs for the current folder
        logs = glob(directory + "/" + folder + "//*.txt")
        
        # Process each log file
        for filename in logs:
            # Use regex to extract file type, number, ridge, and stretch values from the filename
            match = re.search(r'(AB|BB)\((\d+)\).*--ridge(\d+\.\d+)--stretch(\d+\.\d+)', filename)
            
            if match:
                file_type = match.group(1)
                number = match.group(2)
                ridge = match.group(3)
                stretch = match.group(4)
                
                # Create a key using the file type, number, ridge, and stretch values
                key = (file_type + '(' + number + ')', (float(ridge), float(stretch)))
                
                # Store the filename in the filename_hash dictionary using the key
                filename_hash[key] = filename
    
    return filename_hash

if __name__ == "__main__":
    # Example usage
    directory = (
        "/Users/hsuyab/Documents/Spring 2024/"
        "RA Staiger/SOAX project/Atharva/"
        "SOAX analysis/soax_raw_output_all_files_gray 121923/"
    )

    filename_hashtable = create_filename_hashtable(directory)
    print(filename_hashtable)

    #WORK ON FIXING THE SAVING PART
    # Save the filename_hashtable to a JSON file
    # path2data = "/Users/hsuyab/Documents/GitHub/actin_seg/data"
    # output_file = f"{path2data}/filename_hashtable.json"
    # with open(output_file, "w") as file:
    #     json.dump(filename_hashtable, file, indent=4)
