from PIL import Image 
import os
path1="img\\teams\\msi" 
getfiles=os.listdir(path1)
new=[]
for x in getfiles:
    os.rename(os.path.join(path1,x),os.path.join(path1,'temp_'+x))
    new.append(os.path.join(path1,'temp_'+x))
for x in range(0,len(new)):
    im=Image.open(new[x])
    re=im.resize((400,400))
    re=re.convert('RGB')
    re.save(os.path.join(path1,getfiles[x][:-4]+'.jpg'))
    im.close()
    os.remove(new[x])
