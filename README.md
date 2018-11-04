# Phylo_2018
Project for Intro to Scientific Computing
1. Introduction
A brief description of the project?
I’m currently working as a research assistant on a project verifying USDA seed samples according to DNA testing. A time-consuming aspect of the project is manually running sequence data through several online applications to: translate, align, and finally build a phylogenetic tree. Another challenge is the lack of flexibility in choosing which sequences will be included in the final tree. 
The goal of the project?
The goal of this project is to replace each online application in the above process with python code.
2. Method
Python library or functions you might use?
The Biopython library should be useful in this project. The Seq Object can be operated on by functions such as: .complement, .reverse_complement, .transcribe, and .translate. Additionally, functions can be applied to Seq Objects in the same way they are applied to strings.
Biopython also works with three important tools needed to complete this project: the NCBI database, MUSCLE, and RAxML.
Biopython also contains a library of parsers for common sequence file formats, which will be important as fasta and phylip format will most likely be used throughout the project. 
3. Plan
Step 1: Receive a file with sequences in fasta format 
	*may need to adjust the format for biopython
Step 2: Translate each sequence to amino acid data using the .translate function
	*may need to account for differences in reading frame
Step 3: Align the sequences to each other using MUSCLE
Step 4: Build a maximum likelihood tree using RAxML
