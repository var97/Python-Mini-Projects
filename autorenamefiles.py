import os

os.chdir('E:/F.R.I.E.N.D.S/Season 3')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    #print(file_name)
    
    f_title, f_ep, f_epsname = file_name.split(' - ')
    new_name = '{}-{}{}'.format(f_ep, f_epsname, file_ext)

    os.rename(f, new_name)
