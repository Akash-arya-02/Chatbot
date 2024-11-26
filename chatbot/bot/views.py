from django.shortcuts import render
from django.http import JsonResponse
from nltk.corpus import wordnet
import nltk
import re

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


def simple_tokenizer(text):
    return re.findall(r'\b\w+\b', text.lower())

def chatbot_response(user_input):
    tokens = simple_tokenizer(user_input.lower())

    
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!",
        "what is your name": "I am a food assistant bot! How can I help you?",
        "what do you do": "I can help you with food-related queries, like prices, recipes, and more!",
        "what is Indian food": "Indian food is a variety of dishes from India that are known for their rich flavors and use of spices like cumin, coriander, and turmeric.",
        "how do you make biryani": "Biryani is made by cooking rice with marinated meat or vegetables, spices, and often garnished with fried onions and boiled eggs.",
        "what is a recipe": "A recipe is a set of instructions for preparing a particular dish, including the ingredients needed.",
        "how do you make pizza": "To make pizza, you need dough, sauce, cheese, and toppings like pepperoni or vegetables. Then bake it in the oven.",
        "what is sushi": "Sushi is a Japanese dish consisting of vinegared rice combined with various ingredients like seafood, vegetables, and sometimes tropical fruits.",
        "what is pasta": "Pasta is an Italian dish made from durum wheat flour and water, usually in the form of noodles, and is often served with various sauces.",
        "food recipes": "I can suggest recipes for various types of food. What kind of recipe are you looking for?",
        "nutritional": "I can provide nutritional information for various foods. Please tell me the food you are interested in.",
        "food prices": "I can tell you the prices of various foods. What food's price would you like to know?",
        "food questions": "Ask me anything about food! I can answer a variety of food-related questions.",
        "food pairings": "I can help you with food pairings. For example, wine with cheese or meats with side dishes.",
        
        
        "what is dosa": "Dosa is a South Indian dish made from fermented rice and lentil batter, served with chutneys and sambar.",
        "how do you make samosa": "Samosas are made by filling a crispy pastry shell with spiced potatoes, peas, and sometimes meat, then deep-frying them.",
        "what is naan": "Naan is a type of Indian flatbread, typically cooked in a tandoor oven and served with curries.",
        "what is butter chicken": "Butter chicken, or murgh makhani, is a creamy, tomato-based curry made with grilled chicken pieces.",
        "how do you make masala chai": "Masala chai is a spiced tea made by brewing tea leaves with milk, sugar, and a mixture of spices like cinnamon, cardamom, and ginger.",
        "what is gulab jamun": "Gulab jamun is a popular Indian dessert made from deep-fried dough balls soaked in a sugary syrup flavored with rose water or cardamom.",
        "how do you make lassi": "Lassi is a traditional Indian yogurt-based drink, which can be either sweet or salty, often flavored with fruits or spices.",
        "what is chai tea": "Chai tea is a spiced tea beverage made with a blend of black tea, milk, sugar, and spices like cinnamon, cardamom, and cloves.",
        "how do you make pani puri": "Pani puri is a popular Indian street food made from hollow puris filled with spicy tamarind water, potatoes, and chickpeas.",
        "what is tandoori chicken": "Tandoori chicken is chicken marinated in yogurt and spices, then cooked in a tandoor, resulting in a smoky, flavorful dish.",
        "what is kulfi": "Kulfi is a traditional Indian ice cream made from milk, sugar, and various flavorings such as pistachio, mango, or rose.",
        "what is biryani": "Biryani is a flavorful rice dish made with marinated meat (or vegetables) and a blend of spices like saffron, cumin, and coriander.",
        "what is chole bhature": "Chole bhature is a popular North Indian dish consisting of spicy chickpeas (chole) served with deep-fried bread (bhature).",
        "what is pav bhaji": "Pav bhaji is a street food dish from Mumbai made of spiced mashed vegetables served with buttered bread rolls.",
        "what is aloo tikki": "Aloo tikki is a North Indian snack made from mashed potatoes seasoned with spices, shaped into patties, and shallow-fried.",
        "what is rasgulla": "Rasgulla is a Bengali sweet made from fresh cottage cheese (chhena) soaked in light syrup.",
        "what is kheer": "Kheer is a traditional Indian rice pudding made with milk, sugar, and flavored with cardamom, raisins, and nuts.",
        "what is mango lassi": "Mango lassi is a sweet yogurt drink made with fresh mangoes, yogurt, and sugar, often served chilled.",
        "what is ice cream": "Ice cream is a sweet frozen dessert made from milk, cream, sugar, and flavorings like vanilla, chocolate, or fruit.",
        "what is vanilla ice cream": "Vanilla ice cream is a classic ice cream flavor made with vanilla beans or vanilla extract, cream, and sugar.",
        "what is chocolate ice cream": "Chocolate ice cream is a rich and creamy frozen dessert flavored with cocoa or melted chocolate.",
        "what is jalebi": "Jalebi is a popular Indian sweet made by deep-frying batter in circular shapes and then soaking them in sugar syrup.",
        "what is ras malai": "Ras malai is a Bengali dessert made of soft, spongy milk-based dumplings soaked in sweetened milk cream.",
        "Vegthali": "A traditional Indian meal featuring a variety of flavorful vegetarian dishes served with rice, roti, and sides for a balanced feast.",
    }

    
    synonym_dict = {
        "hello": ["hi", "hey", "greetings", "howdy", "hola"],
        "how are you": ["how's it going", "how do you do", "how are you doing", "what's up", "how's life", "how are things"],
        "bye": ["goodbye", "see you", "take care", "bye bye", "later"],
        "what is your name": ["what's your name", "who are you", "what should I call you"],
        "what do you do": ["what can you do", "what is your job", "what's your purpose", "what's your function"],
        "what is Indian food": ["what is Indian cuisine", "tell me about Indian food", "what is food from India", "what is traditional Indian food", "what are Indian dishes"],
        "how do you make biryani": ["how is biryani made", "what is the recipe for biryani", "how do you prepare biryani", "how can I make biryani"],
        "what is a recipe": ["what does a recipe mean", "define recipe", "what is the meaning of a recipe"],
        "how do you make pizza": ["what's the recipe for pizza", "how can I make pizza", "how is pizza made", "tell me how to make pizza"],
        "what is sushi": ["tell me about sushi", "what is sushi made of", "explain sushi", "what does sushi mean"],
        "what is pasta": ["tell me about pasta", "what does pasta mean", "what is pasta made of", "how is pasta made"],
        "what is dosa": ["tell me about dosa", "what is dosa made of", "how is dosa made", "explain dosa"],
        "how do you make samosa": ["what's the recipe for samosa", "how to make samosa", "how do you prepare samosa"],
        "what is naan": ["tell me about naan", "what is naan made of", "what is naan bread"],
        "what is butter chicken": ["tell me about butter chicken", "what is butter chicken made of", "explain butter chicken"],
        "how do you make masala chai": ["what's the recipe for masala chai", "how to make masala chai", "what goes in masala chai"],
        "what is gulab jamun": ["tell me about gulab jamun", "what is gulab jamun made of", "what is gulab jamun's recipe"],
        "how do you make lassi": ["what is lassi made of", "what's the recipe for lassi", "how to prepare lassi"],
        "what is chai tea": ["tell me about chai tea", "what is chai tea made of", "how is chai tea prepared"],
        "how do you make pani puri": ["what is the recipe for pani puri", "how to make pani puri", "what's in pani puri"],
        "what is tandoori chicken": ["tell me about tandoori chicken", "what is tandoori chicken made of", "how do you prepare tandoori chicken"],
        "what is kulfi": ["tell me about kulfi", "what is kulfi made of", "how is kulfi prepared"],
        "what is biryani": ["tell me about biryani", "what is biryani made of", "how is biryani prepared"],
        "what is chole bhature": ["tell me about chole bhature", "what is chole bhature made of", "what is the recipe for chole bhature"],
        "what is pav bhaji": ["tell me about pav bhaji", "what is pav bhaji made of", "how is pav bhaji prepared"],
        "what is aloo tikki": ["tell me about aloo tikki", "how is aloo tikki made", "what is aloo tikki made of"],
        "what is rasgulla": ["tell me about rasgulla", "how is rasgulla made", "what is rasgulla's recipe"],
        "what is kheer": ["tell me about kheer", "what is kheer made of", "how is kheer prepared"],
        "what is mango lassi": ["tell me about mango lassi", "how is mango lassi made", "what goes in mango lassi"],
        "what is ice cream": ["tell me about ice cream", "what is ice cream made of", "how is ice cream prepared"],
        "what is vanilla ice cream": ["tell me about vanilla ice cream", "how is vanilla ice cream made", "what is the recipe for vanilla ice cream"],
        "what is chocolate ice cream": ["tell me about chocolate ice cream", "how is chocolate ice cream made", "what is the recipe for chocolate ice cream"],
        "what is jalebi": ["tell me about jalebi", "what is jalebi made of", "how is jalebi made"],
        "what is ras malai": ["tell me about ras malai", "how is ras malai made", "what is ras malai's recipe"],
        "recipes": ["recipe", "dish", "meal", "cook", "cooking"],
        "nutritional": ["nutrition", "calories", "nutrition facts", "health benefits"],
        "prices": ["price", "cost", "expense", "price list"],
        "questions": ["questions", "ask", "inquiries", "information", "details"],
        "pairings": ["pairing", "match", "combinations", "best food pairings"]
    }

   
    normalized_input = " ".join(tokens)

    if normalized_input in responses:
        return responses[normalized_input]
    
   
    for key, synonyms in synonym_dict.items():
        if any(synonym in normalized_input for synonym in synonyms):
            return responses[key]

   
    return "Sorry, I didn't understand that. Can you rephrase?"


def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        response = chatbot_response(user_input)
        return JsonResponse({"response": response})
    
    return render(request, "bot/chat.html")











