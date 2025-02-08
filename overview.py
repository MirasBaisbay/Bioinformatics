def main():
    """
    1. PDB IDS:
        Mannually extract pdb ids from the pdb database.
        OR 
        Use the script to find the pdb ids (using RCSB API).
    """
    
    # 1. our pdb ids:
    pdb_ids = []
    
    # 2. download pdb files, already have a script for this
    download_pdb_files(pdb_ids)
    
    # 3. Analyze ss, have a script for this
    analyze_secondary_structure(pdb_ids)
    # or the same with torsion angles
    # for pdb_id in pdb_ids:
    #    analyze_secondary_structures(pdb_id)
    
    # 4. Calculate torsion angles, need to write a script for this
    for pdb_id in pdb_ids:
        calculate_torsion_angles(pdb_id)
    
    # 5. Calculate helix-helix angles
    for pdb_id in pdb_ids:
        calculate_helix_helix_angles(pdb_id)
        
    # 6. Superimpose structures
    superimpose_structures(pdb_ids)
    
    # 7. Clustering and so on (later)
    
    
    
if __name__ == "main":
    main()