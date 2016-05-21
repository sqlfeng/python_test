#coding:utf-8
import requests
import re
import sys
'''
coremail邮件系统企业通讯录导出脚本
'''
def login(domain,username,password):
    data={'startReferer':'','uid':username,'password':password}
    httptou={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
    s=requests.session()
    httppost=s.post("http://"+domain+"/coremail/login.jsp",data=data,headers=httptou)
    getemail=re.findall('\(this\);"\r\n                                                href="(.*?)" hidefocus>',httppost.text,re.S)
    tongxunlu= getemail[0]
    mailpage="http://"+domain+"/coremail/XJS/"+tongxunlu
    httpgetmailpage=s.get(mailpage)
    bumens=re.findall(' href="\.\.(.*?)" hidefocus=',httpgetmailpage.text,re.S)
    for bumen in bumens:
        paa=bumen[51:]
        file = open(paa[3:].replace('/','')+'.txt','a+')
        getmail=s.get("http://"+domain+"/coremail/XJS"+bumen)
        pages=re.findall(' selected>(.*?)</option>',getmail.text,re.S)
        allpage=pages[0]
        yeshu= allpage[2:]
        for i in range(1,int(yeshu)+1):
            url="http://"+domain+"/coremail/XJS"+bumen+"&page_no="+str(i)
            fanye=s.get(url)
            zhengze='&'+paa+'&uid=(.*?)">'
            maildizhis=re.findall(zhengze,fanye.text,re.S)
            ids=list(set(maildizhis))
            for res in ids:
                print res
                file.write(res+'\n')
        file.close()
if __name__ == '__main__':
    commands=sys.argv[1:2]
    commandss=sys.argv[2:3]
    commandsss=sys.argv[3:]
    args="".join(commands)
    argss="".join(commandss)
    argsss="".join(commandsss)
    if len(args) < 1:
        print "*"*80
        print "                 E.g:python coremail_export.py mail.baidu.com  user pass (不带@域名)"
        print "                                                       by sqlfeng"
        print "*"*80
    else:
        login(args,argss,argsss)
