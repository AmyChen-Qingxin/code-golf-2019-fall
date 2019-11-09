newdic={"AAAAA":"A","AAAAB":"B","AAABA":"C", 'AAABB': 'D', 'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J', 'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O', 'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T', 'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y', 'BBAAB': 'Z'}
cipher=str(input());msg='';cur='';count=0
for letter in cipher:
    for char in letter:
        if char.isupper():cur+='B'
        elif char.islower()or char==',':cur+='A'
        if len(cur)==5:msg+=newdic[cur];cur=''   
print(msg)