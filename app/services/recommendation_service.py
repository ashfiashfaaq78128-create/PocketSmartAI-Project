from .catalog import get_catalog
from .gemini_service import GeminiService

ai = GeminiService()

def fallback(planner, p):
    b = int(p["budget"]); c = get_catalog(planner)
    if planner == "home":
        alloc={"furniture":round(b*.5),"lighting":round(b*.2),"decor":b-round(b*.5)-round(b*.2)}
        order=["furniture","lighting","decor"]; summary=f"Starter home plan for {', '.join(p.get('rooms', ['Living Room']))}."
    elif planner == "party":
        alloc={"food":round(b*.5),"venue":round(b*.3),"decoration":b-round(b*.5)-round(b*.3)}
        order=["food","venue","decoration"]; summary=f"Balanced {p.get('event_type','event')} plan for {p.get('guests',1)} guests."
    else:
        alloc={"earrings":round(b*.45),"necklace":round(b*.35),"bangles":b-round(b*.45)-round(b*.35)}
        order=["earrings","necklace","bangles"]; summary=f"Coordinated {p.get('occasion','occasion')} jewelry plan."
    remaining=b; out=[]
    for cat in order:
        matches=[x for x in c if x["category"]==cat and x["price"]<=remaining]
        if matches:
            x=min(matches,key=lambda z:abs(z["price"]-alloc[cat]))
            out.append({**x,"estimated_price":x["price"],"quantity":1,"reason":f"Fits the {cat} portion of the budget."})
            remaining-=x["price"]
    return {"planner":planner,"budget":b,"budget_allocation":alloc,"summary":summary,
            "recommendations":out,"source_mode":"fallback",
            "notes":[f"Remaining budget: ₹{remaining:,}. Catalog entries are mock/search links, not live inventory."]}

def generate(planner, payload, image_bytes=None, mime_type=None):
    result=ai.recommend(planner,payload,get_catalog(planner),image_bytes,mime_type)
    return result if isinstance(result,dict) else fallback(planner,payload)
