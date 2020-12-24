from django.shortcuts import render
import bs4
import requests
# Create your views here.

def home(request):
    name = []
    value = []
    response = requests.get("https://air-quality.com/place/india/gurugram/zh-Hans/aqi_us/d2853e61")
    data = bs4.BeautifulSoup(response.text, "html.parser")
    tags = data.find("div", class_="pollutants")
    p_name = list(tags.find_all(class_="name"))
    p_value = tags.find_all(class_="value")
    for n in p_name:
        a=n.get_text()
        name.append(a)
    for v in p_value:
        b=v.get_text()
        value.append(b)
    return render(request,'home.html',{'poll_name':name,'poll_value':value})

