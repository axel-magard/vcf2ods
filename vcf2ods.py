import vobject
import os
from pyexcel_ods3 import save_data
from collections import OrderedDict
from optparse import OptionParser

parser = OptionParser()

usage = """
python vcf2ods.py VCF_FILE [ODS_FILE]
"""

(options, args) = parser.parse_args()
if len(args) < 1:
    print(usage)
    os,exit()

inFile = args[0]
tmpFile = inFile.replace(".","_.")
vcfFile = os.path.basename(inFile).split(".")[0]+".ods"


# Fix split lines
lines = []
with open(inFile) as inf:
    for line in inf:
        if line.startswith("="):
            lines[-1] = lines[-1][:-1] + line[1:]
        else:    
            lines.append(line)

f = open(tmpFile, "w")
f.writelines(lines)
f.close()        

data = OrderedDict()
rows = []
header = ["Name","Address","Phone 1","Phone # 1","Phone 2","Phone # 2","EMail 1","EMail # 1","EMail 2","EMail # 2","Note"]
rows.append(header)

with open(tmpFile) as inf:
    indata = inf.read()
    vc = vobject.readComponents(indata, ignoreUnreadable=True)
    for v in vc:
        rows.append([])
        # print(v)
        rows[-1].append(str(v.n.value).strip())
        try:
            rows[-1].append(str(v.adr.value).strip())
        except:
            rows[-1].append("")    
        tel_list = v.tel_list[:2]   # Support max 2 telephone numbers
        for t in tel_list:
            rows[-1].append(t.singletonparams[0])
            rows[-1].append(t.value.replace("-",""))
        if len(tel_list) < 2:   
            rows[-1].append("")
            rows[-1].append("") 
        try:
            email_list = v.email_list[:2]   # Support max 2 emails
        except AttributeError:
            rows[-1].append("")
            rows[-1].append("")
            rows[-1].append("")
            rows[-1].append("")
        else:                    
            for t in email_list:
                rows[-1].append(t.singletonparams[0])
                rows[-1].append(t.value.replace("",""))
            if len(email_list) < 2:   
                rows[-1].append("")
                rows[-1].append("") 

        try:
            rows[-1].append(str(v.note.value).strip())
        except AttributeError:
            rows[-1].append("")        

os.remove(tmpFile)            
data.update({"Sheet 1": rows})
save_data(vcfFile, data)
try:
    os.system(vcfFile)
except: pass    