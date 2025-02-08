from pymol import cmd
import os

def analyze_secondary_structures(pdb_ids, output_file="ss_analysis.txt"):
    try:
        cmd.delete("all")
        for pdb_id in pdb_ids:
            cmd.fetch(pdb_id)
            cmd.show_as("cartoon")
            
            ss = [i.ss for i in cmd.get_model ("n. CA").atom]
            
            if len(ss) == 0:
                return "No residues found in structure"
                
            helix_content = 100.0 * ss.count("H") / len(ss)
            sheet_content = 100.0 * ss.count("S") / len(ss)
            loop_content = 100.0 * ss.count("") / len(ss)
            
            output_text = (
                f"Secondary Structure Analysis for {pdb_id}\n"
                f"Helix content: {helix_content:5.2f}%\n"
                f"Sheet content: {sheet_content:5.2f}%\n"
                f"Loop content: {loop_content:5.2f}%\n"
            )
            
            print(output_text)
            
            output_file = "analysis of " + pdb_id + ".txt"
            
            with open(output_file, 'w') as f:
                f.write(output_text)            

            cmd.delete("all")
        
    except cmd.CmdException as e:
        return f"Error fetching structure: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
