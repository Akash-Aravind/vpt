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

tokens=['அங்கதேசம்\u200c', '-' , 'இது', ',', 'உரோமபதன்\u200c', 'அர', 'சாட்சியில்\u200c', 'மழையில்லாமலிருந்தது', '.', '', 'பின்ன     னால்\u200c', '௬சியசிங்க', 'முனிவர்வரவால்\u200c', 'மழைபெய்யப்\u200c', 'பெற்றது', '.', 'இந்த', 'ராஜ       ஜ்யத்\u200c', 'தைத்துரியோதனனால்\u200c', 'கர்னன்\u200c', 'பெற்று', 'அரசாண்டான்\u200c106', 'பொ', 'எ        எ', 'ஊஷவிறம', '.', '', '', '(', 'மாரதம்\u200c', '-', 'ஆதிபர்வம்\u200c', ')', '.', '', 'அங்கநாடு',   '-', 'விசயவரன்\u200c', 'என்னும்\u200c', 'அரச', 'னுடைய', 'நாடு', '.', "'", 'இதன்\u200c', 'தலைநகர   ர்\u200c', 'சண்பை', '.', '(', 'பெருங்கதை', '.', '', 'அங்கமோகினி', '-', 'திவோதானன்\u200c', 'தேவி',    '.', '', 'அங்கம்\u200c', '-', '1', '.', '(', '2', ')', 'யானை', ';', 'ப', 'பரி', ',', '', 'காலாள ள்\u200c', '.', '', '', 'க', '.', '(', '10', ')', 'மலை', ',', 'ஆறு', ',', 'டட', 'ஊர்\u200c', ',',  '', 'மாலை', ',', 'பரி', ',', 'கரி', ',', 'முரசு', ',', 'கொடி', ',', 'செங்\u200c', 'கோல்\u200c' ,'3', '.', '(', '5', ')', 'திதி', ',', 'வாரம்\u200c', ',', 'நக்ஷத்திரம்\u200c', ','   , '', 'யோகம்\u200c', ',', 'கரணம்\u200c', '.', '', '', '']
for i in tokens:
    print(tokens)