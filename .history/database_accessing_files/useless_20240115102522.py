#ing
# tamil_text = "இந்த உலகம் அதிசயம். தமிழ் என்ற மொழி வளரும்."

# with io.open("pages/0032_pg.txt",'r',encoding='utf8') as f:
#     text = f.readlines()

# dict=[]
# for line in text:
#     line=line.strip()
#     dict.append(line)
# try:
#     for i in range(len(dict)):
#         dict[i]=dict[i].replace("\u200c","")
#         if dict[i] =='':
#             dict.pop(i)
#         if dict[i] ==".":
#             dict.pop(i)
#         if dict[i] =="\n":
#             dict.pop(i)
#         if dict[i] =="|":
#             dict.pop(i)
# except:
#     pass
# for i in range(len(dict)):
#     dict[i]=dict[i].replace("\u200c","")

# if(dict[1].isdigit()):
#     dict.pop(1)

# dict.pop()

# print("The title of the page is "+dict[0])
# final_string=""
# for i in dict:
#     final_string+=i
#     final_string+=" "

# with open("newfile.txt","w",encoding='utf8') as f:
#     f.write(final_string)

# print(final_string)



#tokenizing
# print(text)
# tokens = indic_tokenize.trivial_tokenize(text)


# try:
#     for i in range(len(tokens)):
#         if tokens[i] ==".":
#             tokens.pop(i)
#         if tokens[i] =="|":
#             tokens.pop(i)
# except:
#     pass
# with open("newfile.txt","w",encoding='utf8') as wf:
#     for k in tokens:
#         wf.write(k+" ")

# print(tokens)

tokens=['அங்கதேசம்\u200c', '-' , 'இது', ',', 'உரோமபதன்\u200c', 'அர', 'சாட்சியில்\u200c', 'மழையில்லாமலிருந்தது', '(',  'பின்ன     னால்\u200c','-', '௬சியசிங்க', 'முனிவர்வரவால்\u200c', 'மழைபெய்யப்\u200c',')' ,'பெற்றது', '.', 'இந்த', 'ராஜ       ஜ்யத்\u200c', 'அங்கதே\u200c', '-', 'இது', ',', 'உரோமபதன்\u200c', 'அர', 'சாட்சியில்\u200c','-']

dictio={"சுபம்":"சுபம்"}
temp=""
key=""
count=0
flag=False
for i in range(len(tokens)-1):
    if(tokens[i]==')'):
        temp+=')'
        flag=False
        continue
    if(tokens[i]=='('):
        temp+='('
        flag=True
        continue
    if(flag):
        temp+=tokens[i]
        continue
    if(tokens[i]=='-'):
        if(count==0):
            print("entered once")
            if(tokens[i-1]==":" or tokens[i-1]==" " or tokens[i-1]=="-" or tokens[i-1]=="" or tokens[i-1]=="\n"):
                key=tokens[i-2]
                
            else:
                key=tokens[i-1]
                # print(key+" is the keyyyyy")
            count=1
            continue
        elif count==1:
            dictio[key]=temp
            temp=""
            count=0
            key=""
            continue
    temp+=tokens[i]
dictio[key]=temp
# print(tokens)
print(dictio)