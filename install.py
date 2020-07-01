import subprocess
try:
	subprocess.run(["pip install yagmail", ""])
	subprocess.run(["pip install pprint", ""])
	subprocess.run(["pip install IMAPClient", ""])
	subprocess.run(["pip install pyzmail36", ""])
	subprocess.run(["pip install objcrypt", ""])
except Exception as e:
	subprocess.run(["pip3 install yagmail", ""])
	subprocess.run(["pip3 install pprint", ""])
	subprocess.run(["pip3 install IMAPClient", ""])
	subprocess.run(["pip3 install pyzmail36", ""])
	subprocess.run(["pip3 install objcrypt", ""])