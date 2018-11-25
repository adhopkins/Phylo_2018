
#Muscle Alignment
from Bio.Align.Applications import MuscleCommandline
#Path relative to project
in_file=input('file_name= ')
out_file="align.fasta"
muscle_exe="muscle"
#using default fasta output
cline = MuscleCommandline(muscle_exe, input=in_file, out=out_file)
#creating best tree file
from Bio.Phylo.Applications import RaxmlCommandline
raxml_cline = RaxmlCommandline(sequences=out_file,model="PROTCATWAG", name="tree")
raxml_cline(out_file)
