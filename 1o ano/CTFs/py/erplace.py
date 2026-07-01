tools = ["Wireshark", "Metasploit", "Nmap", "Burp Suite", "Snort", "OpenVAS", "Cuckoo Sandbox"]

upper = ''.join(tool.upper() for tool in tools)

subStr = upper[5:15]
reversedStr = subStr[::-1]

print(reversedStr)