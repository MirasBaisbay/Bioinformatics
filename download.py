import requests
import os

pdb_ids = ['5OW9', '5OWD', '5E7V', '6FOB', '6FO7']

output_dir = "PDB_Structures"
os.makedirs(output_dir, exist_ok=True)

for pdb_id in pdb_ids:
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = os.path.join(output_dir, f"{pdb_id}.pdb")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {pdb_id}.pdb")
    else:
        print(f"Failed to download: {pdb_id}")

print("Download complete!")
