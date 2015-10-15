#!/usr/bin/env python
#--*-- coding:UTF-8 --*--

import sys, DNS
query=sys.argv[1]
DNS.DiscoverNameServers()
reqobj=DNS.Request()
answerobj=reqobj.req(name=query, qtype=DNS.Type.ANY)

if not len(answerobj.answers):
        print "pas trouvé"
        
for item in answerobj.answers:
    print "%-5s %s"%(item['typename'],item['data'])
