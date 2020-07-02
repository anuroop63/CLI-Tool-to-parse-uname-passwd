#!/usr/bin/env python
# coding: utf-8
import json
import argparse

def parser(pwd_file,grp_file):                  #This function returns json object
    users=[]
    groups={}
    final={}

    with open(pwd_file,'r') as passwd:
       for line in passwd:
            if line[0]!='#':                    #Excluding the comment lines in file
                data=line.strip().split(':')
                temp=(data[0],data[2],data[4])  #Extracting uname, uid and uinfo field
                users.append(temp)              #Creating a list of tuples as (uname, uid, uinfo)

    with open(grp_file,'r') as group:
        for line in group:
            if line[0]!='#':
                data=line.strip().split(':')
                if data[3]!='':                     #Excluding groups with 0 members
                    ulist=list(data[3].split(','))  #Creating list of all users in each group
                    gname=data[0]                   #Extracting group name

                    for uname in ulist:
                        if uname not in groups:
                            groups[uname]=[gname]   #Creating a map of username as key and list of member groups
                        else:
                            groups[uname].append(gname) 

    #Parsing data extracted from both files and storing as per requirement in an object 
    for user in users:
        name=user[0]
        uid=user[1]
        full=user[2]
        
        final[name]={
            "uid":uid,
            "full_name":full,
            "groups": groups[name] if name in groups else []
        }
    return(json.dumps(final, indent=4))


def load_input():                       #Function to take command line arguments for custom file paths
    parser=argparse.ArgumentParser()
    parser.add_argument('-p',required=False, help='Enter "passwd" file path', dest='passwd', default='/etc/passwd')
    parser.add_argument('-g',required=False, help='Enter "group" file path', dest='group',default='/etc/group')
    inputs=parser.parse_args()
    return inputs.passwd, inputs.group


if __name__ == '__main__':
    try:    
        pwd_file,grp_file=load_input()
        output=parser(pwd_file,grp_file)
        print(output)
    
    except Exception as e:
        if str(e)=='list index out of range':
            print("Input file is corrupt, please check files are as per standard format!\n")

        else:
            print(e)