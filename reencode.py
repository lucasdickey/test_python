blah=open("/Users/djethx/Downloads/meego-app-airsync_tw_TC.ts")

bloop=open("/Users/djethx/Downloads/meego-app-airsync_tw_TC2.ts", 'w')

bloop.write(unicode(blah.read(), 'gb18030').encode('utf8'))

bloop.close()
