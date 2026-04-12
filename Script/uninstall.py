import os 

packages_to_save = ["certifi","charset-normalizer","docutils","idna","pip","Pygments","pypiwin32","pywin32","requests","setuptools","urllib3","winpython","wheel","Cython"] 

packages = open('packages.txt', 'r', encoding='utf-8', errors='ignore') 
for i in packages:    
    try:
        true_i = i[0:i.index("\n")]    
    except: 
        true_i = i            
    if true_i in packages_to_save:        
        pass    
    else:        
        try:
            os.system(r"C:\Users\Hp\WPy64-31241\python-3.12.4.amd64\python.exe -m pip uninstall -y {true_i}")        
        except:
            print("échec")