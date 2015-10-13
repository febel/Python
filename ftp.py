#!/usr/local/bin/python3
#--*--coding:utf8--*-- 

from ftplib import FTP 
import os,sys 

class DirEntry: 
        def __init__(self, line): 
                self.parts=line.split(None,8) 

        def isvalid(self): 
                return len(self.parts) >= 6 

        def gettype(self): 
                return self.parts[0][0] 

        def getfilename(self): 
                if self.gettype() != 'l': 
                        return self.parts[-1] 
                else: 
                        return self.parts[-1].split(' -> ',1)[0] 

        def getlinkdest(self): 
                if self.gettype()=='l': 
                        return self.parts[-1].split(' -> ',1)[1] 
                else: 
                        raise RuntimeError("erreur d'appel de getlinkdest() ") 

class DirScanner(dict): 
        def addline(self,line): 
                obj=DirEntry(line) 
                if obj.isvalid(): 
                        self[obj.getfilename()]=obj 
def downloadfile(ftpobj,filename): 
        ftpobj.voidcmd("TYPE I") 
        datasock, estsize=ftpobj.ntransfercmd("RETR %s"%filename) 
        transbytes = 0 
        fd=open(filename,'wb') 
        while 1: 
                buf=datasock.recv(2048) 
                if not len(buf): 
                        break 
                fd.write(buf) 
                transbytes += len(buf) 
                sys.stdout.write("%s: reception de %d "%(filename,transbytes)) 
                if estsize: 
                        sys.stdout.write("sur %d octets (%.1f%%)\r"%(estsize,100.0 * float(transbytes)/float(estsize))) 
                else: 
                        sys.stdout.write("octets\r") 
        fd.close() 
        datasock.close() 
        ftpobj.voidresp() 
        sys.stdout.write("\n") 
def downloaddir(ftpobj,localpath,remotepath): 
        print("**** repertoire en cours %s"%remotepath) 
        localpath=os.path.abspath(localpath) 
        oldlocaldir=os.getcwd() 
        if not os.path.isdir(localpath): 
                os.mkdir(localpath) 
        olddir=ftpobj.pwd() 
        try: 
                os.chdir(localpath) 
                ftpobj.cwd(remotepath) 
                d=DirScanner() 
                f.dir(d.addline) 
                for filename, entryobj in d.items(): 
                        if entryobj.gettype() == '-': 
                                downloadfile(ftpobj,filename) 
                        elif entryobj.gettype() == 'd': 
                                downloaddir(ftpobj, localpath + '/'+filename,remotepath+ '/' +filename) 
                                print("**** repertoire en cours %s "%remotepath) 
        finally: 
                os.chdir(oldlocaldir) 
                ftpobj.cwd(olddir) 

f=FTP('ftp.kernel.org') 
f.login() 
downloaddir(f,'old-versions','/pub/linux/kernel/Historic/old-versions') 
f.quit()
