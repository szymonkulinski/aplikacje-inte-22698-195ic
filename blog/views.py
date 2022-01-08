from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import Post
from bs4 import BeautifulSoup
from lxml import html
import requests

def zajecia(request):
    #Przykład 1
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, "html.parser")

    all_h2_tags = []
    for element in soup.select("a"):
        all_h2_tags.append(element.text)

    pierwszy = all_h2_tags[0]
    trzeci = all_h2_tags[3]
    ostatni = len(all_h2_tags)
    #Przykład 2
    top_items = []

    products = soup.select("div.thumbnail")
    print("Liczba top items = ", len(products))
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)

    #Przykład 3
    # Create top_items as empty list
    image_data = []

    # Extract and store in top_items according to instructions on the left
    images = soup.select("img")
    print("Liczba obrazków =", len(images))
    for image in images:
        src = image.get("src")
        alt = image.get("alt")
        image_data.append({"src": src, "alt": alt})

    #Przykład 4
    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })

    return render(request,'blog/zajecia.html',{'pierwszy':pierwszy, 'trzeci':trzeci, 'ostatni':ostatni, 'top_items':top_items, 'image_data':image_data, 'all_products':all_products})
    
#

def webscrap(request):
    if request.method == "POST":
        url = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        source=requests.get(url).text 
        all_elements = []
        soup = BeautifulSoup(source, "html.parser")
        items = soup.find_all(element)
        amount = len(items)    
        index = 1 
        for i in items:
            # Szukanie klas
            find_class = i.get('class')
            if find_class is None:
                find_class = "Brak"   
            
            # Szukanie id
            find_id = i.get('id')
            find_id = find_id.strip() if find_id is not None else "Brak"

            # Szukanie linków
            find_href = i.get('href')
            find_href = find_href.strip() if find_href is not None else "Brak"

            # Szukanie tekstu
            get_text = i.text
            get_text = get_text.strip() if get_text is not None else "Brak"

            # Szukanie źródeł
            find_src = i.get('src')            
            if find_src is None:
                find_src = "Brak"
            # Szukanie atrybutu 'alt'
            find_alt = i.get('alt')
            find_alt = find_alt.strip() if find_alt is not None else "Brak"

            all_elements.append({"find_id": find_id, "find_class": find_class, "find_href": find_href, "get_text": get_text, 'find_alt':find_alt, 'find_src': find_src, 'index': index})
            index += 1
        
        return render(request, 'blog/webscrap.html', {'all_elements':all_elements, 'amount': amount, 'url': url, 'element':element})
    
    return render(request, 'blog/webscrap.html')

def xpath(request):
    
    # Szuaknie elementu przy pomocy xml
    # Szukanie elementu poprzez xPath
    url = 'https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna'    
    path = '/html/body/div[3]/div[3]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/p/b/a' 
    response = requests.get(url)
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxml1 = tree[0].text_content()
    
    # Szukanie elemntu przez nazwę klasy   
    url = 'https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna'    
    path = '//*[@class="mw-headline"]'    
    response = requests.get(url)    
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxml2 = tree[0].text_content()

    return render(request, 'blog/xpath.html', {'lxml1': lxml1,'lxml2': lxml2 })
