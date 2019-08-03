from urllib.request import urlopen
import re
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.veryfy_mode=ssl.CERT_NONE

url=input('Enter-')
html=urlopen(url,context=ctx).read().decode()
links=re.findall('href="(http[s]?://.*?)"',html)
print(links)