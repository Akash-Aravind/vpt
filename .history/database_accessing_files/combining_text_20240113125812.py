import io

#specify the page numbers as the parameters of range
for i in range(12,999):
    if(i>99):
        filename=f"0{i}_pg.txt"
    elif(i<10):
        filename=f"000{i}_pg.txt"
    elif(i>=10):
        filename=f"00{i}_pg.txt"
    with io.open(f"database_accessing_files/pages/{filename}","r",encoding='utf8') as f:
        textlines=f.readlines()

    textlines.pop()

    for i in range(6):
        line=textlines[i].split(" ")
        if(len(line)<=1):
            textlines.remove(textlines[i])


    with io.open("database_accessing_files/test.txt","a",encoding='utf8') as append_file:
        append_file.writelines(textlines)
