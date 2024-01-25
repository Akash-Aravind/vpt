import io
from indicnlp.tokenize import indic_tokenize
import sys 
import psycopg2

#reading of the test.txt file
with io.open("database_accessing_files/test2.txt",'r',encoding='utf8') as f:
    text = f.read()

#tokenizing the text
tokens1 = indic_tokenize.trivial_tokenize(text)
tokens = []

for line in tokens1:
    split_strings = line.split('\n')
    tokens.extend(split_strings)
print(tokens)
#removing the page number and title of the page
# try:
#     tokens.pop(0)
#     tokens.pop(0)
# except:
#     pass

#initializing dictionary
dictio={"சுபம்":"சுபம்"}
temp=""
key=""
count=0
flag=False
#looping through tokens and when - is found the text before it becomes key and the text after it becomes the value till next - is found
for i in range(len(tokens)-1):
    # if(tokens[i]=="("):
    #     flag=True
    #     temp+=tokens[i]+" ";
    #     continue
    # if(flag):
    #     temp+=tokens[i]+" ";
    #     continue
    # if(tokens[i]==")"):
    #     flag=False
    #     temp+=tokens[i]+" ";
    #     continue
    if(tokens[i]=="-" and count==0):

        if(tokens[i-1]==":" or tokens[i-1]==" " or tokens[i-1]=="-" or tokens[i-1]=="" or tokens[i-1]=="\n"):
            key=tokens[i-2]
        else:
            key=tokens[i-1]
        count+=1
        continue
    elif(tokens[i+1]=="-"and count==1):
        count=0
        
        if(len(temp.strip())<3999):
            if(len(temp.strip())==0):
                key=""
                temp=""
                continue
            if(temp.strip()[-1]=='('):
                dictio[key]=temp[:len(temp)-2]
            else:
                dictio[key]=temp
        
        key=""
        temp=""
        continue
    
    temp+=tokens[i]+" ";




for i in dictio.keys():
    print(i)

print(dictio)







#pushing to postgres database

#details


# hostname='localhost'
# databasename='vpt(WORD_MEANING)'
# username='postgres'
# pwd='akash'
# port_id=5432

# conn=None
# cur=None

# try:
#     #connecting to database
#     conn=psycopg2.connect(
#         host=hostname,
#         dbname=databasename,
#         user=username,
#         password=pwd,
#         port=port_id
#     )

#     cur=conn.cursor()


#     cur.execute('DROP TABLE IF EXISTS dictionary')
#     db_creationscript='''CREATE TABLE IF NOT EXISTS root_dict(
#                     key     varchar(200) NOT NULL,
#                     values   varchar(6000) NOT NULL
#     )'''
#     cur.execute(db_creationscript)

#     db_inssertionscript='''INSERT INTO root_dict (key,values) VALUES (%s,%s)'''


#     insertvalues=dictio

#     #the key value pairs of the dictionary are inserted into separate columns named as key and values
#     for i,j in insertvalues.items():
#         cur.execute(db_inssertionscript,(i,j)) 
#     conn.commit()

# except Exception as connection_missing:
#     print(connection_missing)
# finally:
#     if conn !=None:
#         conn.close()
#     if cur!=None:
#         cur.close()
