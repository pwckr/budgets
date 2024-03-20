import os
from pickle import load, dump
from typing import Union, Dict, Set


class DataManager:
    """
    This class handles actual data management tasks such as:
    - the loading and creation of files
    - writing data to existing files
    """

    def load_create(self, file_specifications: dict) -> Union[dict, Dict, set, Set]:
        """This function loads a file if it exists, and creates one if not.
        
        Parameters:
        file_specifications (dict): dict that yields path, initialiser and name of file
        """
        if os.path.exists(file_specifications["path"]):
            with open(file_specifications["path"], "rb") as f:
                data = load(f)
                print(f"{file_specifications['name']} loaded.")
        else:
            print(f"Creating {file_specifications['name']}-file.")
            data = file_specifications["initialiser"]
        return data

    def write_data(self, file_specifications: dict, data: Union[set, dict]) -> None:
        """This function writes data to a given file.
        
        Parameters:
        file_specifications (dict): dict that yields path, initialiser and name of file
        data: this parameter is either a set or a dict
        """
        with open(file_specifications["path"], "wb") as f:
            dump(data, f)
        print(f"{file_specifications['name']} saved.")