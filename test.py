import os
import json
import time
class HandleWebHookEvents():
     def test(self):
         msg = "Invalid toolchainId: asdf-dfgh-wert-erty"
         rc = {"response": msg}
         return None, (rc, 400)

a=HandleWebHookEvents()

t,tt,ttt = a.test()

print t
print tt
print ttt
