CATALOG = {
"home": [
 {"title":"Minimal LED Ceiling Light","category":"lighting","platform":"IKEA","price":1299,"url":"https://www.ikea.com/in/en/search/?q=ceiling%20light"},
 {"title":"Modern 3-Seater Sofa","category":"furniture","platform":"Amazon","price":18999,"url":"https://www.amazon.in/s?k=3+seater+sofa"},
 {"title":"Wood Finish Study Table","category":"furniture","platform":"Amazon","price":6999,"url":"https://www.amazon.in/s?k=wood+study+table"},
 {"title":"Decorative Wall Mirror","category":"decor","platform":"IKEA","price":2499,"url":"https://www.ikea.com/in/en/search/?q=wall%20mirror"},
 {"title":"5-Star Ceiling Fan","category":"lighting","platform":"Amazon","price":2799,"url":"https://www.amazon.in/s?k=5+star+ceiling+fan"},
 {"title":"Dining Table Set","category":"furniture","platform":"IKEA","price":12999,"url":"https://www.ikea.com/in/en/search/?q=dining%20table"},
 {"title":"Ambient Table Lamp","category":"decor","platform":"Amazon","price":899,"url":"https://www.amazon.in/s?k=ambient+table+lamp"}],
"party": [
 {"title":"Party Catering Search","category":"food","platform":"Swiggy","price":6000,"url":"https://www.swiggy.com/"},
 {"title":"Restaurant & Catering Search","category":"food","platform":"Zomato","price":7000,"url":"https://www.zomato.com/"},
 {"title":"Event Venue Search","category":"venue","platform":"OYO","price":9000,"url":"https://www.oyorooms.com/"},
 {"title":"Birthday Decoration Package","category":"decoration","platform":"Amazon","price":1499,"url":"https://www.amazon.in/s?k=birthday+decoration+kit"},
 {"title":"Party Lights","category":"decoration","platform":"Amazon","price":999,"url":"https://www.amazon.in/s?k=party+lights"}],
"jewelry": [
 {"title":"Gold-Tone Jhumka Earrings","category":"earrings","platform":"Amazon","price":799,"url":"https://www.amazon.in/s?k=jhumka+earrings"},
 {"title":"Pearl Drop Earrings","category":"earrings","platform":"Flipkart","price":999,"url":"https://www.flipkart.com/search?q=pearl+drop+earrings"},
 {"title":"Minimal Pendant Necklace","category":"necklace","platform":"Amazon","price":1299,"url":"https://www.amazon.in/s?k=minimal+pendant+necklace"},
 {"title":"Statement Necklace Set","category":"necklace","platform":"Flipkart","price":1799,"url":"https://www.flipkart.com/search?q=statement+necklace"},
 {"title":"Bangle Set","category":"bangles","platform":"Amazon","price":699,"url":"https://www.amazon.in/s?k=bangle+set"}]}

def get_catalog(planner):
    return CATALOG.get(planner, [])
