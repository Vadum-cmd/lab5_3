from cache_webpage import WebPage
import time

webpage_trap = WebPage("http://www.fest.lviv.ua/uk/projects/uku/")
now = time.time()
content1 = webpage_trap.content
print(webpage_trap.lastupdatetime)
print(time.time() - now)
time.sleep(3)

print("**")
# now = time.time()
# if webpage_trap.lastupdatetime < (now - webpage_trap.refresh_interval):
content2 = webpage_trap.refresh
now = time.time()
print(webpage_trap.lastupdatetime)
print(time.time() - now)
print(content1 == content2)

time.sleep(3)
print("**")
# now = time.time()
# if webpage_trap.lastupdatetime < (now - webpage_trap.refresh_interval):
content3 = webpage_trap.refresh
now = time.time()
print(webpage_trap.lastupdatetime)
print(time.time() - now)
print(content2 == content3)
