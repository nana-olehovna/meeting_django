movies = [
    {
        "id": 1,
        "title": "Pulp Fiction",
        "year": 1994,
        "price": 79,
        "description": "A nonlinear crime story about intersecting lives of criminals in Los Angeles.",
        "rating": 8.5,
        "isInStock": True,
        "image": "shop/images/1.png"
    },
    {
        "id": 2,
        "title": "Kill Bill: Vol. 1",
        "year": 2003,
        "price": 69,
        "description": "A revenge-driven assassin embarks on a brutal mission against her former team.",
        "rating": 6.2,
        "isInStock": False,
        "image": "shop/images/2.png"
    },
    {
        "id": 3,
        "title": "The Hateful Eight",
        "year": 2015,
        "price": 89,
        "description": "Strangers trapped in a cabin during a blizzard reveal hidden motives and tensions.",
        "rating": 8.8,
        "isInStock": True,
        "image": "shop/images/3.png"
    },
    {
        "id": 4,
        "title": "Inglourious Basterds",
        "year": 2009,
        "price": 89,
        "description": "A group of Jewish-American soldiers plans to assassinate Nazi leaders in WWII France.",
        "rating": 10.0,
        "isInStock": True,
        "image": "shop/images/4.png"
    },
    {
        "id": 5,
        "title": "Django Unchained",
        "year": 2012,
        "price": 99,
        "description": "A freed slave teams up with a bounty hunter to rescue his wife from a plantation owner.",
        "rating": 9.5,
        "isInStock": True,
        "image": "shop/images/5.png"
    },

    {
        "id": 6,
        "title": "Lock, Stock and Two Smoking Barrels",
        "year": 1998,
        "price": 69,
        "description": "Four friends become entangled with gangsters after a high-stakes card game goes terribly wrong.",
        "rating": 8.2,
        "isInStock": True,
        "image": "shop/images/6.png"
    },
    {
        "id": 7,
        "title": "Snatch",
        "year": 2000,
        "price": 79,
        "description": "A stolen diamond, underground boxing, and colorful criminals collide in London.",
        "rating": 8.3,
        "isInStock": True,
        "image": "shop/images/7.png"
    },
    {
        "id": 8,
        "title": "RocknRolla",
        "year": 2008,
        "price": 75,
        "description": "A real estate scam draws criminals, politicians, and gangsters into a chaotic battle.",
        "rating": 7.2,
        "isInStock": False,
        "image": "shop/images/8.png"
    },
    {
        "id": 9,
        "title": "The Gentlemen",
        "year": 2019,
        "price": 99,
        "description": "An American drug lord tries to sell his cannabis empire, sparking a web of schemes and betrayals.",
        "rating": 7.8,
        "isInStock": True,
        "image": "shop/images/9.png"
    },
    {
        "id": 10,
        "title": "Sherlock Holmes",
        "year": 2009,
        "price": 85,
        "description": "Sherlock Holmes and Dr. Watson investigate a mysterious criminal conspiracy in Victorian London.",
        "rating": 7.6,
        "isInStock": False,
        "image": "shop/images/10.png"
    },

    {
        "id": 11,
        "title": "Memento",
        "year": 2000,
        "price": 79,
        "description": "A man with short-term memory loss searches for his wife's killer using notes and tattoos.",
        "rating": 8.4,
        "isInStock": True,
        "image": "shop/images/11.png"
    },
    {
        "id": 12,
        "title": "The Prestige",
        "year": 2006,
        "price": 89,
        "description": "Two rival magicians push obsession and sacrifice to dangerous extremes.",
        "rating": 8.5,
        "isInStock": False,
        "image": "shop/images/12.png"
    },
    {
        "id": 13,
        "title": "The Dark Knight",
        "year": 2008,
        "price": 99,
        "description": "Batman faces the Joker, a criminal mastermind determined to plunge Gotham into chaos.",
        "rating": 9.0,
        "isInStock": True,
        "image": "shop/images/13.png"
    },
    {
        "id": 14,
        "title": "Inception",
        "year": 2010,
        "price": 99,
        "description": "A skilled thief enters dreams to steal secrets but is offered one last impossible mission.",
        "rating": 8.8,
        "isInStock": True,
        "image": "shop/images/14.png"
    },
    {
        "id": 15,
        "title": "Interstellar",
        "year": 2014,
        "price": 109,
        "description": "A team of astronauts travels through a wormhole to find a new home for humanity.",
        "rating": 8.7,
        "isInStock": True,
        "image": "shop/images/15.png"
    }
]


top_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:6]

#HOME PAGE CONTENT
home_context = {
    "hero_title": "MEETING DJANGO",
    "hero_subtitle": "Rent iconic movies by Quentin Tarantino, Guy Ritchie, and Christopher Nolan in just one click",
    "description": "We bring together the best movies from three legendary directors of modern cinema. From Tarantino’s crime-driven masterpieces to Nolan’s mind-bending storytelling and Guy Ritchie’s stylish criminal comedies — everything is available for online rental."
}


#ABOUT PAGE CONTENT
about_info = {
    "title": "About Us",
    "intro": "We are an online movie rental platform focused on cult and auteur cinema. Our goal is to gather the best films of modern legendary directors in one place.",
    "mission": "Our mission is to make it easy for everyone to rewatch legendary films by Quentin Tarantino, Guy Ritchie, and Christopher Nolan without searching across multiple platforms.",
    "what_we_offer": [
            "Online movie rentals",
            "Curated director-based collections",
            "High-quality cult cinema",
            "Fast and simple access"
    ],
}

directors = [
    {
        "name": "Quentin Tarantino",
        "style": "Nonlinear storytelling, sharp dialogues, violence as art"
    },
    {
        "name": "Guy Ritchie",
        "style": "Crime comedies, fast editing, British storytelling style"
    },
    {
        "name": "Christopher Nolan",
        "style": "Complex structures, time manipulation, philosophy and scale"
    }
]


#CONTACTS_PAGE
contacts_info = {
    "subtitle": "We'd love to hear from you!",
    "description": "Whether you have a question about movie rentals, need technical support, or simply want to recommend your favorite film, our team is always happy to help.",
    "email": "support@meetingdjango.com",
    "phone": "+1 (555) 123-4567",
    "address": "221B Baker Street, London, United Kingdom",
    "working_hours": {
        "weekdays": "Monday – Friday: 9:00 AM – 8:00 PM",
        "weekends": "Saturday – Sunday: 10:00 AM – 6:00 PM"
    },
    "socials": {
        "instagram": "@meetingdjango",
        "facebook": "Meeting Django",
        "x": "@MeetingDjango"
    }
}


#USER INFO
user = {
    "name": "Lilia",
    "email": "lilia68@gmail.com",
    "phone": "420485935859",
    "password": "password",
    "balance": 200,
    
}