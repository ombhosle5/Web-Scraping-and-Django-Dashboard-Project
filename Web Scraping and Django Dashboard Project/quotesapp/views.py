from django.shortcuts import render
from .models import Quote

def quotes_list(request):
    quotes = Quote.objects.all()
    
     
    quotes_with_tags = []
    for quote in quotes:
        
        tags = [tag.strip() for tag in quote.tags.split(',') if tag.strip()] if quote.tags else []
        
        
        full_profile_url = f"https://quotes.toscrape.com{quote.author_profile}"
        
        quote_dict = {
            'quote': quote.quote,
            'author': quote.author,
            'tags': tags,
            'author_profile': full_profile_url,  
        }
        quotes_with_tags.append(quote_dict)
    
    context = {
        'quotes': quotes_with_tags,
        'total_quotes': len(quotes_with_tags),
    }
    return render(request, 'quotesapp/quotes_list.html', context)