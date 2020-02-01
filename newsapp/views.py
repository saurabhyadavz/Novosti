from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):


    newsapi = NewsApiClient(api_key ='63665b97deb04425b289bcd1ede9eadb')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    pub=[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])
    mylist = zip(news, desc, img,pub)

    return render(request, 'index.html', context ={"mylist":mylist})
