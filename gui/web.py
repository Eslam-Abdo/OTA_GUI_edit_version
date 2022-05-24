'''
resource : https://realpython.com/python-web-scraping-practical-introduction/
'''
from urllib.request import urlopen

def get_hex_code():
    url = "http://iot-arm.freevar.com/start_flash.php?config=allfile"
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    hex_list = html[1:-1].split('%')
    # print(hex_list)
    # print(len(hex_list))

    if len(hex_list) < 2: #no file found
        return None
    # hex_list.remove('')

    return hex_list

if __name__ == '__main__':

    hex_code = get_hex_code()
    # print(hex_code)
    if hex_code != None:
        for index,line in enumerate(hex_code):
            print(index,' ', line.encode("utf-8"))
    else:
        print("No Update Found now!")