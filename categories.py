import random

class Categories:
    def __init__(self) :
        
        self.choices={
            1:{
            "easy": ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Audi', 'Tesla', 'Jaguar', 'Lexus', 'Porsche', 'Jeep', 'Cadillac', 'GMC', 'Mazda', 'Mini', 'Fiat', 'Bentley',
                     'Aston Martin', 'Bugatti', 'Rolls-Royce', 'McLaren', 'Lotus', 'Smart', 'Peugeot', 'Renault', 'Citroen', 'Opel', 'Skoda', 'Dacia'],
            "hard": {
                "Volkswagen": "German brand, translates to 'People's Car.'",
                "Nissan": "Japanese brand, known for the Z series and GT-R.",
                "Hyundai": "South Korean brand with the Sonata and Elantra models.",
                "Mercedes": "German luxury brand, known for the iconic three-pointed star.",
                "Audi": "German brand, part of the Volkswagen Group.",
                "Ferrari": "Italian luxury sports car manufacturer.",
                "Subaru": "Japanese brand with all-wheel-drive vehicles.",
                "Kia": "South Korean brand with the Optima and Sorento models.",
                "Volvo": "Swedish brand, known for safety features.",
                "Dodge": "American brand with the Charger and Challenger models.",
                "Buick": "American luxury brand, part of General Motors.",
                "Tesla": "American electric car manufacturer.",
                "Acura": "Japanese luxury brand, part of Honda.",
                "Land Rover": "British brand specializing in off-road vehicles.",
                "Alfa Romeo": "Italian luxury brand with a racing heritage.",
                "Maserati": "Italian luxury brand known for performance cars.",
                "Genesis": "South Korean luxury brand, part of Hyundai.",
                "Chrysler": "American brand, part of Stellantis.",
                "Ram": "American brand specializing in trucks.",
                "Infiniti": "Japanese luxury brand, part of Nissan.",
                "Mitsubishi": "Japanese brand with a focus on SUVs.",
                "Opel": "German brand, now part of the Stellantis group.",
                "Citroën": "French brand known for innovative designs.",
                "Skoda": "Czech brand, part of the Volkswagen Group.",
                "Dacia": "Romanian brand known for affordable vehicles."}},

            2:{
            'easy': ['Delhi', 'Mumbai', 'Jaipur', 'Goa', 'Bangalore', 'Agra', 'Chennai', 'Kolkata', 'Hyderabad', 'Kochi',
            'Pune', 'Lucknow', 'Ahmedabad', 'Amritsar', 'Bhopal', 'Indore', 'Vadodara', 'Coimbatore', 'Visakhapatnam', 'Nagpur',
            'Varanasi', 'Patna', 'Bhubaneswar', 'Ranchi', 'Surat'],
            'hard': {
            'Leh-Ladakh': 'A high-altitude desert region in Jammu and Kashmir known for its breathtaking landscapes.',
            'Rishikesh': 'A city in Uttarakhand known as the "Yoga Capital of the World" and a gateway to the Himalayas.',
            'Hampi': 'A UNESCO World Heritage Site in Karnataka known for its ancient ruins and temples.',
            'Khajuraho': 'A group of stunning temples in Madhya Pradesh known for intricate erotic sculptures.',
            'Gulmarg': 'A hill station in Jammu and Kashmir known for its skiing and panoramic views.',
            'Mahabalipuram': 'A town in Tamil Nadu known for its ancient rock-cut temples and Shore Temple.',
            'Udaipur': 'The "City of Lakes" in Rajasthan known for its palaces and vibrant cultural scene.',
            'Munnar': 'A hill station in Kerala known for its tea plantations and scenic landscapes.',
            'Agumbe': 'A village in Karnataka known for heavy rainfall, lush greenery, and the setting of "Malgudi Days."',
            'Ooty': 'A popular hill station in Tamil Nadu known for its gardens and pleasant weather.',
            'Ajanta Caves': 'Ancient Buddhist cave monuments in Maharashtra known for their exquisite sculptures.',
            'Rann of Kutch': 'A seasonal salt marsh in Gujarat known for its white desert landscape.',
            'Tawang': 'A town in Arunachal Pradesh known for its monasteries and natural beauty.',
            'Kumbhalgarh': 'A fortress in Rajasthan known for its walls that extend over 38 kilometers.',
            'Nanda Devi': 'The second-highest mountain in India, located in the state of Uttarakhand.',
            'Gangtok': 'The capital of Sikkim, known for its monasteries and views of the Himalayas.',
            'Jaisalmer': 'A city in Rajasthan known for its golden fort and desert surroundings.',
            'Halebidu': 'A town in Karnataka known for its Hoysala architecture and ancient temples.',
            'Dhanushkodi': 'A ghost town in Tamil Nadu, believed to be the place where Lord Rama built a bridge to Lanka.',
            'Jodhpur': 'The "Blue City" in Rajasthan known for its blue-painted houses and Mehrangarh Fort.',
            'Puducherry': 'A former French colony known for its colonial architecture and spiritual atmosphere.',
            'Majuli': 'The world\'s largest river island, located in the Brahmaputra River in Assam.',
            'Darjeeling': 'A hill station in West Bengal known for its tea gardens and views of Kanchenjunga.',
            'Kaziranga': 'A national park in Assam known for its one-horned rhinoceros population.'}
        
            },

            3:{
            "easy":['Harry', 'Ron', 'Hermione', 'Gryffindor', 'Hogwarts', 'Quidditch', 'Snape', 'Dumbledore', 'Magic', 'Wand', 'Spell', 'Owl', 'Broomstick',
                    'Platform', 'Invisibility', 'Phoenix', 'Chocolate', 'Patronus', 'Potion', 'Sorcerer', 'Muggle', 'Dragon', 'Mermaid', 'Mirror', 'Dobby'],

            "hard":{
            'Polyjuice Potion': 'A complex magical potion that allows the drinker to temporarily assume the appearance of another person.',
            'Horcrux': 'An object used to store a portion of a wizard or witch\'s soul, making them immortal as long as the Horcrux exists.',
            'Pensieve': 'A magical object used for reviewing and even entering memories.',
            'Thestrals': 'Invisible, winged horses that are visible only to those who have witnessed and accepted death.',
            'Dementor': '''Dark, hooded creatures that feed on human happiness and can perform a Dementor's Kiss, which sucks out the soul of the victim.''',
            'Portkey': 'A magical object that transports anyone touching it to a specific location when activated.',
            'Veela': 'Magical beings known for their beauty and ability to enchant men.',
            'Basilisk': 'A giant serpent that can kill with its gaze, and is often associated with Salazar Slytherin.',
            'Hippogriff': 'A magical creature with the front legs, wings, and head of an eagle and the body of a horse.',
            'Firebolt': 'A high-quality broomstick, known for its speed and agility.',
            'Floo Network': 'A magical transportation system connected by fireplaces.',
            'Gellert Grindelwald': 'A dark wizard and former friend of Albus Dumbledore, known for his pursuit of the Deathly Hallows.',
            'Mandrake': 'A magical plant with a humanoid appearance, used in potion-making.',
            'Triwizard Tournament': 'A magical competition held between three wizarding schools: Hogwarts, Beauxbatons, and Durmstrang.',
            'The Leaky Cauldron': 'A popular wizarding pub and inn located in London, serving as a gateway to Diagon Alley.',
            'Animagus': 'A wizard or witch who can transform into a specific animal at will.',
            'The Forbidden Forest': 'A dangerous forest on the Hogwarts grounds, inhabited by magical creatures and considered off-limits to students.',
            'Polyester Polyjuice': 'A humorous mispronunciation of Polyjuice Potion by Ron Weasley in the series.'}},
        
            4:{
            "easy":['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan',
                    'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand', 'United Kingdom', 'France',
                    'Tanzania', 'Italy', 'South Africa', 'Myanmar', 'Kenya', 'South Korea', 'Colombia', 'Spain', 'Uganda', 'Argentina', 'Algeria',
                    'Sudan', 'Ukraine', ],
            "hard":{'Iraq': "Known for its ancient history, including the Mesopotamian civilization. The Tigris and Euphrates rivers flow through this land.",
                        'Afghanistan': "Located in South Asia, often referred to as the 'Crossroads of Central Asia' due to its strategic location.",
                        'Poland': "Famous for its medieval architecture, this European country is home to the cities of Warsaw and Krakow.",
                        'Canada': "The second-largest country in the world, known for its vast landscapes, including the Rocky Mountains and Niagara Falls.",
                        'Morocco': "Situated in North Africa, this country offers a blend of Arab, Berber, and European cultural influences.",
                        'Saudi Arabia': "The largest country on the Arabian Peninsula, known for its deserts, including the Rub' al Khali, or Empty Quarter.",
                        'Uzbekistan': "This Central Asian country is famous for its ancient cities along the Silk Road, such as Samarkand and Bukhara.",
                        'Peru': "Home to the Inca Empire, this South American country features the iconic Machu Picchu and the Amazon Rainforest.",
                        'Angola': "Located in Southern Africa, this country has a diverse geography, including the coastal Namib Desert and the rainforests of Cabinda.",
                        'Malaysia': "This Southeast Asian country is known for its diverse culture, beautiful beaches, and the iconic Petronas Towers in Kuala Lumpur.",
                        'Mozambique': "Located on the southeastern coast of Africa, this country is known for its stunning coastline along the Indian Ocean.",
                        'Ghana': "A West African country with a rich history, known for the Ashanti Empire and as a major hub in the transatlantic slave trade.",
                        'Yemen': "Located on the Arabian Peninsula, this country has a rich cultural heritage and is home to ancient cities like Sana'a.",
                        'Nepal': "Nestled in the Himalayas, this South Asian country is known for Mount Everest, the world's highest peak.",
                        'Venezuela': "Situated in northern South America, this country has diverse landscapes, including the Andes Mountains and the Amazon Rainforest.",
                        'Madagascar': "An island nation in the Indian Ocean, known for its unique wildlife, including lemurs.",
                        'Cameroon': "Located in Central Africa, this country has a diverse landscape, including rainforests, savannas, and the active volcanic mountain, Mount Cameroon.",
                        'Ivory Coast': "A West African country known for its cocoa production and diverse landscapes.",
                        'North Korea': "Located on the Korean Peninsula, this country has a unique political system and is known for its closed-off nature.",
                        'Australia': "A continent and country, known for its unique wildlife, vast deserts, and iconic landmarks like the Sydney Opera House."}},       
            5:{
            'easy': ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye', 'Spider-Man', 'Black Panther', 'Ant-Man', 'Doctor Strange', 'Captain Marvel', 'Falcon', 'Winter Soldier', 'Scarlet Witch', 'Vision', 'Wasp', 'Star-Lord', 'Gamora', 'Drax', 'Rocket', 'Groot', 'Nebula'],
            'hard': {
                    'Thanos': 'Powerful villain seeking to collect all the Infinity Stones.',
                    'Loki': 'Trickster god and adopted brother of Thor.',
                    'Nick Fury': 'Director of S.H.I.E.L.D. and organizer of the Avengers.',
                    'Red Skull': 'Captain America\'s archenemy and Hydra leader.',
                    'Ultron': 'Artificial intelligence created by Tony Stark, turned antagonist.',
                    'Ronin': 'Alter ego of Hawkeye during certain story arcs.',
                    'Vision': 'Synthetic being with the Mind Stone embedded in his forehead.',
                    'Nebula': 'Adopted daughter of Thanos and sister to Gamora.',
                    'Winter Soldier': 'Bucky Barnes, best friend of Captain America, turned assassin.',
                    'Hela': 'Goddess of Death and sister to Thor in Norse mythology.',
                    'Doctor Strange': 'Sorcerer Supreme and master of the mystic arts.',
                    'Wanda Maximoff': 'Scarlet Witch, possessing reality-warping abilities.',
                    'T\'Challa': 'Black Panther, king of Wakanda.',
                'Gamora': 'Adopted daughter of Thanos and member of the Guardians of the Galaxy.',
                'Rocket': 'Raccoon and expert marksman from the Guardians of the Galaxy.',
                'Groot': 'Flora Colossus and companion to Rocket in the Guardians of the Galaxy.',
                'Captain Marvel': 'Carol Danvers, powerful superhero with cosmic abilities.',
                'Ant-Man': 'Scott Lang or Hank Pym, able to shrink or grow in size.',
                'Star-Lord': 'Peter Quill, leader of the Guardians of the Galaxy.',
                'Drax the Destroyer': 'Member of the Guardians of the Galaxy seeking vengeance.',
                'Mjolnir': 'Thor\'s enchanted hammer, granting him the power of the God of Thunder.'
            }}

                
                        }



    def choose_word(self, category, level):
        
        category_words = self.choices.get(category)
        if category_words:
            level_words = category_words.get(level)
            
            if level_words:
                chosen_word = random.choice(list(level_words))
                
                return chosen_word
        return None, None
 
   



# Get the category from tice!")
# else:
#     level_input = input("Enter the difficulty level (easy, hard): ")

#     if level_input == 'easy':
#         word = hangman_game.choose_word(category_input, level_input)

# category_input = int(input("Enter the category (1, 2, 3, 4, 5): "))
# if category_input > 5 or category_input < 1:
#     print("Invalid cho
#         if word:
#             print(f"Selected word: {word}")
    
#         else:
#             print("Invalid category or difficulty level.")
#     elif level_input == 'hard':
#         word = hangman_game.choose_word(category_input, level_input)
    
#         if word:
#             hints = hangman_game.choices[category_input][level_input][word]
#             print(f"Selected word: {word}")
#             print(f"Hints: {hints}")
#         else:
#             print("Invalid category or difficulty level.")
#     else:
#         print("Invalid difficulty chosen")