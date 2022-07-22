import requests
 
def main():
	res = requests.get("http://data.fixer.io/api/latest?access_key=dd44405658a1e71fd1d896a14a76f32d&base=EUR&symbols=CNY")
	if res.status_code != 200:
		raise Exception("ERROR: API rquest unsuccessful.")
	data = res.json()
	print(data)
 
if __name__ == "__main__":
	main()


