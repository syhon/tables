import numpy as np
array=[]
i=0
data=open("data.txt", "r")
for line in data:
    array.extend([None]);
    array[i]=str(line.replace(".", ","))
    i+=1
data.close()

data=open("data.txt", "w")
i=0
while i < len(array):
    data.write(array[i])
    i+=1
data.close()

data=np.genfromtxt("data.txt", unpack=True, dtype="U12")
#Länge der Spalten: len(data[i])
#Länge der Zeilen: len(data)
table=open("table.tex", "w")
table.write("\\begin{table}[H] \n   \centering \n   \caption{name} \n   \label{tab:name} \n   \\begin{tabular} ")
i=0
table.write("{ ")
while i<len(data):
    table.write("c ")
    i+=1
table.write("} \n \\toprule \n ")
i=0
while i < len(data):
    table.write("{$")
    table.write(data[i][0])
    table.write("\:/\: \mathrm{")
    table.write(data[i][1])
    table.write("}$}")
    if i+1 ==len(data):
        table.write(" \\\ \n")
    else:
        table.write(" & ")
    i+=1
table.write("    \midrule \n")
j=2
while j < len(data[0]):
    i=0
    table.write("    ")
    while i < len(data):
        table.write(data[i][j])
        if i+1 ==len(data):
            table.write(" \\\ \n")
        else:
            table.write(" & ")
        i+=1
    j+=1
table.write("    \\bottomrule \n  \end{tabular}\n\end{table}")
table.close()
