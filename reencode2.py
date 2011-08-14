blah=open("/Users/djethx/Downloads/meego-app-airsync_cn_SC.ts")

bloop=open("/Users/djethx/Downloads/meego-app-airsync_cn_SC2.ts", 'w')

bloop.write(unicode(blah.read(), 'gb18030').encode('utf8'))

bloop.close()
