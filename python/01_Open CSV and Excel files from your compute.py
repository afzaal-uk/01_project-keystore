#Files being checked
#------------------------------------------------------------------------

import pandas as pd # library for working with data
from pathlib import Path # finding path
data_folder = Path(r"C:\01_project_keystore\data\raw")
csv_files = list(data_folder.glob("*.csv")) # glob finding exact file name pattern
print("csv Files found: \n")

for file in csv_files:
    print(file.name)
    
print(f"\nTotal files: {len(csv_files)}")