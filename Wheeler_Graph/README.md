To construct and query wheeler graph, please follow the instructions below:

Generate DeBruijn Graph: python3 debruijn.py
Visualize DeBruijn Graph PNG (if Graphviz is downloaded): dot -Tpng [name of .dot file here] > [name of outputfile].png   
Create Wheeler Graph: 
Navigate to Wheelie Package Repository (Wheeler_Graph_Toolkit)
Move .dot file to ./bin (or adjust the command below)
% ./bin/recognizer  ./bin/[name of .dot file here] -w
Move the folder produced “out__[name of .dotfile]” to location of searchwheeler.py
Query Wheeler Graph: python3 searchwheeler.py
Change foldername to “out__[name of .dotfile]”
Change P 
