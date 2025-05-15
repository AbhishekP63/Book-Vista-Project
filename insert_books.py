import sqlite3
books_data= {
        
    
    "Fiction": [
        {"title": "Project Hail Mary", "author": "Andy Weir", "rating": 4.9, "published_date": "2021", "description": "A gripping sci-fi adventure about a lone astronaut on a mission to save Earth."},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "rating": 4.9, "published_date": "1937", "description": "A fantasy adventure story."},
        {"title": "The Midnight Library", "author": "Matt Haig", "rating": 4.8, "published_date": "2020", "description": "A novel about a library between life and death, exploring infinite possibilities."},
        {"title": "Tomorrow, and Tomorrow, and Tomorrow", "author": "Gabrielle Zevin", "rating": 4.8, "published_date": "2022", "description": "A story about friendship, creativity, and the gaming industry."},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "rating": 4.8, "published_date": "1960", "description": "A novel about racial injustice in the Deep South."},
        {"title": "The Book Thief", "author": "Markus Zusak", "rating": 4.7, "published_date": "2005", "description": "A novel set during World War II."},
        {"title": "1984", "author": "George Orwell", "rating": 4.7, "published_date": "1949", "description": "A dystopian social science fiction novel."},
        {"title": "Lessons in Chemistry", "author": "Bonnie Garmus", "rating": 4.7, "published_date": "2022", "description": "A novel about a chemist-turned-TV host fighting societal norms."},
        {"title": "Where the Crawdads Sing", "author": "Delia Owens", "rating": 4.7, "published_date": "2018", "description": "A coming-of-age story intertwined with a murder mystery in the marshlands."},
        {"title": "Circe", "author": "Madeline Miller", "rating": 4.6, "published_date": "2018", "description": "A retelling of Greek mythology from the perspective of Circe, the enchantress."},
        {"title": "The Nightingale", "author": "Kristin Hannah", "rating": 4.6, "published_date": "2015", "description": "A historical novel about two sisters in Nazi-occupied France."},
        {"title": "The Alchemist", "author": "Paulo Coelho", "rating": 4.6, "published_date": "1988", "description": "A story about destiny and self-discovery."},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "rating": 4.6, "published_date": "1925", "description": "A novel about the American Dream and tragedy."},
        {"title": "Klara and the Sun", "author": "Kazuo Ishiguro", "rating": 4.6, "published_date": "2021", "description": "A dystopian novel about AI and human emotions."},
        {"title": "Brave New World", "author": "Aldous Huxley", "rating": 4.5, "published_date": "1932", "description": "A dystopian novel on society and technology."},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "rating": 4.5, "published_date": "1813", "description": "A classic romantic novel."},
        {"title": "A Man Called Ove", "author": "Fredrik Backman", "rating": 4.5, "published_date": "2015", "description": "A heartwarming story about a grumpy old man learning to live again."},
        {"title": "The Goldfinch", "author": "Donna Tartt", "rating": 4.5, "published_date": "2013", "description": "A Pulitzer Prize-winning novel about loss, art, and redemption."},
        {"title": "The Martian", "author": "Andy Weir", "rating": 4.8, "published_date": "2014", "description": "A thrilling sci-fi survival story about an astronaut stranded on Mars."},
        {"title": "All the Light We Cannot See", "author": "Anthony Doerr", "rating": 4.6, "published_date": "2014", "description": "A historical fiction novel set in World War II, following a blind French girl and a German soldier."},
        {"title": "The Night Circus", "author": "Erin Morgenstern", "rating": 4.6, "published_date": "2011", "description": "A beautifully written fantasy novel about a magical competition."},
        {"title": "Gone Girl", "author": "Gillian Flynn", "rating": 4.4, "published_date": "2012", "description": "A psychological thriller about marriage, lies, and mystery."},
        {"title": "Little Women", "author": "Louisa May Alcott", "rating": 4.4, "published_date": "1868", "description": "A story of four sisters growing up."},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "rating": 4.3, "published_date": "1951", "description": "A story about teenage rebellion."}
    ],
    
   "Non-Fiction": [
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "rating": 4.8, "published_date": "2011", "description": "A deep dive into the history of humankind, from the Stone Age to the modern era."},
    {"title": "Born a Crime", "author": "Trevor Noah", "rating": 4.8, "published_date": "2016", "description": "A memoir by comedian Trevor Noah about growing up in apartheid South Africa."},
    {"title": "Educated", "author": "Tara Westover", "rating": 4.7, "published_date": "2018", "description": "A memoir about a woman who escapes a strict and abusive upbringing to pursue education."},
    {"title": "The Glass Castle", "author": "Jeannette Walls", "rating": 4.7, "published_date": "2005", "description": "A memoir about growing up in a dysfunctional and unconventional family."},
    {"title": "Atomic Habits", "author": "James Clear", "rating": 4.7, "published_date": "2018", "description": "A practical guide to building good habits and breaking bad ones."},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "rating": 4.7, "published_date": "2020", "description": "Explores how emotions and psychology affect financial decisions."},
    {"title": "Why We Sleep", "author": "Matthew Walker", "rating": 4.7, "published_date": "2017", "description": "A scientific look at the impact of sleep on our health and well-being."},
    {"title": "Outliers: The Story of Success", "author": "Malcolm Gladwell", "rating": 4.6, "published_date": "2008", "description": "Examines what makes high-achievers different, exploring the role of culture, family, and opportunity."},
    {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot", "rating": 4.6, "published_date": "2010", "description": "The true story of a woman whose cancer cells led to groundbreaking medical discoveries."},
    {"title": "The Code Breaker", "author": "Walter Isaacson", "rating": 4.6, "published_date": "2021", "description": "Explores the life of Jennifer Doudna and the development of CRISPR gene editing."},
    {"title": "Breath: The New Science of a Lost Art", "author": "James Nestor", "rating": 4.6, "published_date": "2020", "description": "Investigates how proper breathing can improve health and performance."},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "rating": 4.6, "published_date": "2011", "description": "Explores human decision-making and the two systems of thinking: fast and slow."},
    {"title": "The Wright Brothers", "author": "David McCullough", "rating": 4.5, "published_date": "2015", "description": "A biography of the pioneers of aviation, Wilbur and Orville Wright."},
    {"title": "The Power of Habit", "author": "Charles Duhigg", "rating": 4.5, "published_date": "2012", "description": "Explores the science behind habits and how they shape our lives."},
    {"title": "Can't Hurt Me", "author": "David Goggins", "rating": 4.5, "published_date": "2018", "description": "A memoir about overcoming adversity and mental toughness."},
    {"title": "Dare to Lead", "author": "Brené Brown", "rating": 4.5, "published_date": "2018", "description": "A guide to courageous leadership and vulnerability in business."},
    {"title": "Greenlights", "author": "Matthew McConaughey", "rating": 4.5, "published_date": "2020", "description": "A memoir filled with life lessons and personal reflections."},
    {"title": "Into the Wild", "author": "Jon Krakauer", "rating": 4.4, "published_date": "1996", "description": "The true story of a young man who abandoned everything to live in the Alaskan wilderness."},
    {"title": "Caste: The Origins of Our Discontents", "author": "Isabel Wilkerson", "rating": 4.4, "published_date": "2020", "description": "Examines the hidden caste system in America and its effects on society."},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "rating": 4.4, "published_date": "2018", "description": "A self-improvement book about the power of waking up early."}
],

    "Science Fiction": [
    {"title": "Dune", "author": "Frank Herbert", "rating": 4.8, "published_date": "1965", "description": "A sci-fi epic set in a desert world."},
    {"title": "Ender's Game", "author": "Orson Scott Card", "rating": 4.8, "published_date": "1985", "description": "A young boy trained to fight in a space war."},
    {"title": "The Martian", "author": "Andy Weir", "rating": 4.8, "published_date": "2011", "description": "A stranded astronaut tries to survive on Mars."},
    {"title": "Project Hail Mary", "author": "Andy Weir", "rating": 4.8, "published_date": "2021", "description": "A gripping sci-fi adventure about a lone astronaut on a mission to save Earth."},
    {"title": "Hyperion", "author": "Dan Simmons", "rating": 4.7, "published_date": "1989", "description": "A space epic with multiple narrators."},
    {"title": "Foundation", "author": "Isaac Asimov", "rating": 4.7, "published_date": "1951", "description": "A series about the fall and rise of civilizations."},
    {"title": "The Three-Body Problem", "author": "Liu Cixin", "rating": 4.7, "published_date": "2008", "description": "A mind-bending story about first contact with an alien civilization."},
    {"title": "The Mountain in the Sea", "author": "Ray Nayler", "rating": 4.7, "published_date": "2022", "description": "A thought-provoking exploration of AI, intelligence, and the nature of consciousness."},
    {"title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "rating": 4.6, "published_date": "1969", "description": "A novel about gender and society on another planet."},
    {"title": "The Ministry for the Future", "author": "Kim Stanley Robinson", "rating": 4.6, "published_date": "2020", "description": "A near-future novel tackling climate change with sci-fi and political realism."},
    {"title": "Children of Time", "author": "Adrian Tchaikovsky", "rating": 4.6, "published_date": "2015", "description": "A story of evolution, survival, and alien intelligence."},
    {"title": "Neuromancer", "author": "William Gibson", "rating": 4.5, "published_date": "1984", "description": "A cyberpunk classic that introduced 'cyberspace'."},
    {"title": "Altered Carbon", "author": "Richard K. Morgan", "rating": 4.5, "published_date": "2002", "description": "A cyberpunk detective thriller."},
    {"title": "Sea of Tranquility", "author": "Emily St. John Mandel", "rating": 4.5, "published_date": "2022", "description": "A multiverse novel blending time travel, pandemics, and human connections."},
    {"title": "The War of the Worlds", "author": "H.G. Wells", "rating": 4.4, "published_date": "1898", "description": "A classic alien invasion story."},
    {"title": "Snow Crash", "author": "Neal Stephenson", "rating": 4.3, "published_date": "1992", "description": "A mix of sci-fi and cyberpunk ideas."},
    {"title": "The Space Between Worlds", "author": "Micaiah Johnson", "rating": 4.3, "published_date": "2020", "description": "A multiverse sci-fi thriller exploring identity and privilege."}
]
,
    
   "Romance": [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "rating": 4.8, "published_date": "1813", "description": "A timeless romance between Elizabeth Bennet and Mr. Darcy."},
    {"title": "It Ends with Us", "author": "Colleen Hoover", "rating": 4.7, "published_date": "2016", "description": "A deeply emotional love story tackling difficult themes."},
    {"title": "The Notebook", "author": "Nicholas Sparks", "rating": 4.7, "published_date": "1996", "description": "A beautiful tale of enduring love."},
    {"title": "Love and Other Words", "author": "Christina Lauren", "rating": 4.7, "published_date": "2018", "description": "A second-chance romance filled with nostalgia and deep emotions."},
    {"title": "People We Meet on Vacation", "author": "Emily Henry", "rating": 4.7, "published_date": "2021", "description": "A heartwarming romance between best friends over multiple summer vacations."},
    {"title": "Me Before You", "author": "Jojo Moyes", "rating": 4.6, "published_date": "2012", "description": "A heartwarming yet heartbreaking love story."},
    {"title": "The Hating Game", "author": "Sally Thorne", "rating": 4.6, "published_date": "2016", "description": "A witty enemies-to-lovers romance."},
    {"title": "Outlander", "author": "Diana Gabaldon", "rating": 4.6, "published_date": "1991", "description": "A historical romance with time travel elements."},
    {"title": "Red, White & Royal Blue", "author": "Casey McQuiston", "rating": 4.6, "published_date": "2019", "description": "A charming LGBTQ+ romance between a prince and the First Son of the USA."},
    {"title": "The Seven Husbands of Evelyn Hugo", "author": "Taylor Jenkins Reid", "rating": 4.6, "published_date": "2017", "description": "A glamorous and emotional novel about love and ambition."},
    {"title": "The Rosie Project", "author": "Graeme Simsion", "rating": 4.5, "published_date": "2013", "description": "A quirky romance about a genetics professor finding love."},
    {"title": "Beach Read", "author": "Emily Henry", "rating": 4.5, "published_date": "2020", "description": "A romance about two writers finding love."},
    {"title": "Book Lovers", "author": "Emily Henry", "rating": 4.5, "published_date": "2022", "description": "A clever and witty love story about two bookish rivals."},
    {"title": "Before We Were Strangers", "author": "Renée Carlino", "rating": 4.5, "published_date": "2015", "description": "A touching story about love, loss, and second chances."},
    {"title": "Every Summer After", "author": "Carley Fortune", "rating": 4.5, "published_date": "2022", "description": "A nostalgic childhood-friends-to-lovers romance."},
    {"title": "Twilight", "author": "Stephenie Meyer", "rating": 4.3, "published_date": "2005", "description": "A paranormal romance between a girl and a vampire."},
    {"title": "Eleanor & Park", "author": "Rainbow Rowell", "rating": 4.4, "published_date": "2013", "description": "A sweet first-love story with depth and emotion."},
    {"title": "The Love Hypothesis", "author": "Ali Hazelwood", "rating": 4.4, "published_date": "2021", "description": "A charming STEM-based romance between a PhD student and a professor."}
]
,

"Fantasy": [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "rating": 4.9, "published_date": "1937", "description": "A classic fantasy adventure."},
    {"title": "Harry Potter and the Sorcerer’s Stone", "author": "J.K. Rowling", "rating": 4.9, "published_date": "1997", "description": "A young boy discovers he's a wizard."},
    {"title": "The House in the Cerulean Sea", "author": "TJ Klune", "rating": 4.9, "published_date": "2020", "description": "A heartwarming tale of found family and magic."},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "rating": 4.8, "published_date": "2007", "description": "A bard recounts his legendary life story."},
    {"title": "The Way of Kings", "author": "Brandon Sanderson", "rating": 4.8, "published_date": "2010", "description": "A high-fantasy tale of war and ancient secrets."},
    {"title": "A Court of Silver Flames", "author": "Sarah J. Maas", "rating": 4.8, "published_date": "2021", "description": "A powerful story of strength and healing in the ACOTAR universe."},
    {"title": "Fourth Wing", "author": "Rebecca Yarros", "rating": 4.8, "published_date": "2023", "description": "A thrilling fantasy set in a dragon-riding war academy."},
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "rating": 4.7, "published_date": "1996", "description": "A political fantasy epic with dragons and war."},
    {"title": "Mistborn: The Final Empire", "author": "Brandon Sanderson", "rating": 4.7, "published_date": "2006", "description": "A unique magic system and rebellion story."},
    {"title": "Iron Flame", "author": "Rebecca Yarros", "rating": 4.7, "published_date": "2023", "description": "A gripping sequel to Fourth Wing."},
    {"title": "Empire of the Vampire", "author": "Jay Kristoff", "rating": 4.7, "published_date": "2021", "description": "A dark and epic vampire fantasy."},
    {"title": "The Lies of Locke Lamora", "author": "Scott Lynch", "rating": 4.6, "published_date": "2006", "description": "A thrilling heist fantasy."},
    {"title": "American Gods", "author": "Neil Gaiman", "rating": 4.6, "published_date": "2001", "description": "A tale of old gods versus new in modern America."},
    {"title": "The Priory of the Orange Tree", "author": "Samantha Shannon", "rating": 4.5, "published_date": "2019", "description": "A standalone epic fantasy with dragons."},
    {"title": "The Poppy War", "author": "R.F. Kuang", "rating": 4.5, "published_date": "2018", "description": "A grimdark fantasy inspired by Chinese history."},
    {"title": "The Atlas Six", "author": "Olivie Blake", "rating": 4.5, "published_date": "2021", "description": "A dark academia fantasy about magical scholars."},
    {"title": "Eragon", "author": "Christopher Paolini", "rating": 4.4, "published_date": "2002", "description": "A young farm boy discovers a dragon egg."},
    {"title": "Legends & Lattes", "author": "Travis Baldree", "rating": 4.4, "published_date": "2022", "description": "A cozy fantasy about an orc opening a coffee shop."}
]
,

"Horror": [
    {"title": "The Shining", "author": "Stephen King", "rating": 4.8, "published_date": "1977", "description": "A family’s terrifying stay at a haunted hotel."},
    {"title": "The Only Good Indians", "author": "Stephen Graham Jones", "rating": 4.7, "published_date": "2020", "description": "A chilling tale of revenge and supernatural horror."},
    {"title": "Dracula", "author": "Bram Stoker", "rating": 4.6, "published_date": "1897", "description": "The classic vampire novel."},
    {"title": "The Exorcist", "author": "William Peter Blatty", "rating": 4.6, "published_date": "1971", "description": "A terrifying tale of demonic possession."},
    {"title": "The Haunting of Hill House", "author": "Shirley Jackson", "rating": 4.5, "published_date": "1959", "description": "A psychological horror classic."},
    {"title": "Frankenstein", "author": "Mary Shelley", "rating": 4.5, "published_date": "1818", "description": "A scientist creates a monster with tragic results."},
    {"title": "How to Sell a Haunted House", "author": "Grady Hendrix", "rating": 4.5, "published_date": "2023", "description": "A dark and eerie haunted house story with family drama."},
    {"title": "Sundial", "author": "Catriona Ward", "rating": 4.5, "published_date": "2022", "description": "A psychological horror novel about dark family secrets."},
    {"title": "The Cabin at the End of the World", "author": "Paul Tremblay", "rating": 4.5, "published_date": "2018", "description": "A home invasion thriller with apocalyptic stakes."},
    {"title": "House of Leaves", "author": "Mark Z. Danielewski", "rating": 4.4, "published_date": "2000", "description": "A unique horror story with a mysterious house."},
    {"title": "Carrie", "author": "Stephen King", "rating": 4.4, "published_date": "1974", "description": "A bullied girl develops telekinetic powers."},
    {"title": "Bird Box", "author": "Josh Malerman", "rating": 4.4, "published_date": "2014", "description": "A post-apocalyptic horror novel about unseen creatures."},
    {"title": "Mexican Gothic", "author": "Silvia Moreno-Garcia", "rating": 4.3, "published_date": "2020", "description": "A chilling gothic horror set in Mexico."},
    {"title": "The Final Girl Support Group", "author": "Grady Hendrix", "rating": 4.3, "published_date": "2021", "description": "A thrilling horror novel about slasher movie survivors."},
    {"title": "Hell House", "author": "Richard Matheson", "rating": 4.3, "published_date": "1971", "description": "A haunted house story like no other."},
    {"title": "The Hunger", "author": "Alma Katsu", "rating": 4.3, "published_date": "2018", "description": "A horror reimagining of the Donner Party tragedy."},
    {"title": "The Troop", "author": "Nick Cutter", "rating": 4.3, "published_date": "2014", "description": "A terrifying survival horror about a flesh-eating infection."},
    {"title": "The Book of Accidents", "author": "Chuck Wendig", "rating": 4.2, "published_date": "2021", "description": "A supernatural horror novel about trauma and family curses."}
]
,

    "Biography": [
    {"title": "Long Walk to Freedom", "author": "Nelson Mandela", "rating": 4.9, "published_date": "1994", "description": "The autobiography of Nelson Mandela."},
    {"title": "The Diary of a Young Girl", "author": "Anne Frank", "rating": 4.8, "published_date": "1947", "description": "The wartime diary of Anne Frank."},
    {"title": "Becoming", "author": "Michelle Obama", "rating": 4.8, "published_date": "2018", "description": "The memoir of former First Lady Michelle Obama."},
    {"title": "Leonardo da Vinci", "author": "Walter Isaacson", "rating": 4.8, "published_date": "2017", "description": "A detailed biography of Leonardo da Vinci."},
    {"title": "Steve Jobs", "author": "Walter Isaacson", "rating": 4.7, "published_date": "2011", "description": "A biography of Steve Jobs."},
    {"title": "Einstein: His Life and Universe", "author": "Walter Isaacson", "rating": 4.7, "published_date": "2007", "description": "A biography of Albert Einstein."},
    {"title": "Educated", "author": "Tara Westover", "rating": 4.7, "published_date": "2018", "description": "A memoir about a woman who escapes a strict upbringing."},
    {"title": "Elon Musk", "author": "Walter Isaacson", "rating": 4.7, "published_date": "2023", "description": "A biography of the tech entrepreneur Elon Musk."},
    {"title": "The Wright Brothers", "author": "David McCullough", "rating": 4.7, "published_date": "2015", "description": "A biography of the pioneers of flight."},
    {"title": "Alexander Hamilton", "author": "Ron Chernow", "rating": 4.6, "published_date": "2004", "description": "A biography of the American Founding Father."},
    {"title": "Caste: The Origins of Our Discontents", "author": "Isabel Wilkerson", "rating": 4.6, "published_date": "2020", "description": "A powerful examination of caste systems in history."},
    {"title": "The Glass Castle", "author": "Jeannette Walls", "rating": 4.5, "published_date": "2005", "description": "A memoir of resilience and survival."},
    {"title": "A Promised Land", "author": "Barack Obama", "rating": 4.5, "published_date": "2020", "description": "The memoir of former President Barack Obama."},
    {"title": "Born a Crime", "author": "Trevor Noah", "rating": 4.5, "published_date": "2016", "description": "A memoir about growing up in apartheid South Africa."},
    {"title": "The Code Breaker", "author": "Walter Isaacson", "rating": 4.5, "published_date": "2021", "description": "A biography of Nobel laureate Jennifer Doudna and gene editing."},
    {"title": "Hidden Valley Road", "author": "Robert Kolker", "rating": 4.4, "published_date": "2020", "description": "A family’s struggle with schizophrenia and mental health research."},
    {"title": "Shoe Dog", "author": "Phil Knight", "rating": 4.4, "published_date": "2016", "description": "A memoir by the founder of Nike."},
    {"title": "Spare", "author": "Prince Harry", "rating": 4.3, "published_date": "2023", "description": "A deeply personal memoir by Prince Harry, Duke of Sussex."}
]
,
    "Self-Help": [
    {"title": "Atomic Habits", "author": "James Clear", "rating": 4.9, "published_date": "2018", "description": "A guide to building good habits and breaking bad ones."},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "rating": 4.8, "published_date": "1989", "description": "A self-improvement guide on effective habits."},
    {"title": "The Four Agreements", "author": "Don Miguel Ruiz", "rating": 4.8, "published_date": "1997", "description": "A book on personal freedom and wisdom."},
    {"title": "The Mountain Is You", "author": "Brianna Wiest", "rating": 4.8, "published_date": "2020", "description": "A book on self-sabotage and personal transformation."},
    {"title": "Daring Greatly", "author": "Brené Brown", "rating": 4.7, "published_date": "2012", "description": "A book on vulnerability and courage."},
    {"title": "Grit", "author": "Angela Duckworth", "rating": 4.7, "published_date": "2016", "description": "A book on the power of perseverance."},
    {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "rating": 4.7, "published_date": "1936", "description": "A classic book on interpersonal skills."},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "rating": 4.7, "published_date": "2020", "description": "A book on financial behaviors and wealth mindset."},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "rating": 4.6, "published_date": "1997", "description": "A book on spiritual enlightenment and mindfulness."},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "rating": 4.6, "published_date": "1937", "description": "A book on personal development and success."},
    {"title": "You Are a Badass", "author": "Jen Sincero", "rating": 4.6, "published_date": "2013", "description": "A motivational book on achieving success."},
    {"title": "Can't Hurt Me", "author": "David Goggins", "rating": 4.6, "published_date": "2018", "description": "A book on mental toughness and resilience."},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "rating": 4.5, "published_date": "2016", "description": "A counterintuitive approach to living a good life."},
    {"title": "Make Your Bed", "author": "Admiral William H. McRaven", "rating": 4.5, "published_date": "2017", "description": "A book on discipline and small habits."},
    {"title": "The Courage to Be Disliked", "author": "Ichiro Kishimi & Fumitake Koga", "rating": 4.5, "published_date": "2013", "description": "A book based on Adlerian psychology for personal freedom."},
    {"title": "Ikigai: The Japanese Secret to a Long and Happy Life", "author": "Héctor García & Francesc Miralles", "rating": 4.5, "published_date": "2017", "description": "A book about finding your purpose and happiness."},
    {"title": "The Almanack of Naval Ravikant", "author": "Eric Jorgenson", "rating": 4.5, "published_date": "2020", "description": "A collection of wisdom from Naval Ravikant on wealth and happiness."},
    {"title": "100M Offers", "author": "Alex Hormozi", "rating": 4.4, "published_date": "2021", "description": "A book on creating compelling business offers."},
    {"title": "The Comfort Crisis", "author": "Michael Easter", "rating": 4.4, "published_date": "2021", "description": "A book on stepping out of comfort zones for personal growth."}
]
,
    "History": [
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "rating": 4.9, "published_date": "2011", "description": "A history of humankind from ancient to modern times."},    
    {"title": "Caste: The Origins of Our Discontents", "author": "Isabel Wilkerson", "rating": 4.8, "published_date": "2020", "description": "A book exploring caste systems and social hierarchies, particularly in the United States."},
    {"title": "The Rise and Fall of the Third Reich", "author": "William L. Shirer", "rating": 4.8, "published_date": "1960", "description": "A comprehensive history of Nazi Germany."},
    {"title": "1776", "author": "David McCullough", "rating": 4.8, "published_date": "2005", "description": "A history of the American Revolution."},
    {"title": "The Dead Are Arising: The Life of Malcolm X", "author": "Les Payne & Tamara Payne", "rating": 4.7, "published_date": "2020", "description": "An in-depth biography of Malcolm X based on decades of research."},
    {"title": "The Wright Brothers", "author": "David McCullough", "rating": 4.7, "published_date": "2015", "description": "A history of the inventors of flight."},
    {"title": "The Lessons of History", "author": "Will & Ariel Durant", "rating": 4.7, "published_date": "1968", "description": "A summary of history's key lessons."},
    {"title": "Genghis Khan and the Making of the Modern World", "author": "Jack Weatherford", "rating": 4.7, "published_date": "2004", "description": "A history of Genghis Khan’s influence."},
    {"title": "The Splendid and the Vile", "author": "Erik Larson", "rating": 4.7, "published_date": "2020", "description": "A gripping account of Winston Churchill’s leadership during World War II."},
    {"title": "Guns, Germs, and Steel", "author": "Jared Diamond", "rating": 4.7, "published_date": "1997", "description": "A book on the impact of geography on civilizations."},
    {"title": "The Silk Roads", "author": "Peter Frankopan", "rating": 4.6, "published_date": "2015", "description": "A new history of the world through trade routes."},
    {"title": "A People's History of the United States", "author": "Howard Zinn", "rating": 4.6, "published_date": "1980", "description": "A history book from the perspective of ordinary people."},
    {"title": "The Roman Empire: A History", "author": "Greg Woolf", "rating": 4.6, "published_date": "2012", "description": "A history of the rise and fall of Rome."},
    {"title": "The Warmth of Other Suns", "author": "Isabel Wilkerson", "rating": 4.6, "published_date": "2010", "description": "An epic history of the Great Migration of Black Americans."},
    {"title": "Empire of Pain: The Secret History of the Sackler Dynasty", "author": "Patrick Radden Keefe", "rating": 4.6, "published_date": "2021", "description": "A history of the opioid crisis and the family behind it."},
    {"title": "A Short History of Europe", "author": "Simon Jenkins", "rating": 4.5, "published_date": "2018", "description": "A concise history of Europe from its origins to modern times."},
    {"title": "The Bomber Mafia", "author": "Malcolm Gladwell", "rating": 4.5, "published_date": "2021", "description": "An exploration of the strategic bombing during WWII and its impact."},
    {"title": "The CIA Book Club: The Best-Kept Secret of the Cold War", "author": "Charlie English", "rating": 4.5, "published_date": "2025", "description": "An in-depth look at a secret CIA operation that spread banned books during the Cold War."}
]
,
    
    "Business & Finance": [
    {"title": "The Intelligent Investor", "author": "Benjamin Graham", "rating": 4.8, "published_date": "1949", "description": "A guide to value investing and financial wisdom."},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "rating": 4.8, "published_date": "2020", "description": "A book on personal finance and behavioral economics."},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "rating": 4.7, "published_date": "1997", "description": "A book about financial education and wealth-building mindset."},
    {"title": "Zero to One", "author": "Peter Thiel", "rating": 4.7, "published_date": "2014", "description": "A book about startups and building unique businesses."},
    {"title": "Principles", "author": "Ray Dalio", "rating": 4.7, "published_date": "2017", "description": "A book on decision-making and life principles."},
    {"title": "The Almanack of Naval Ravikant", "author": "Eric Jorgenson", "rating": 4.7, "published_date": "2020", "description": "A collection of insights on wealth, happiness, and life by Naval Ravikant."},
    {"title": "The Lean Startup", "author": "Eric Ries", "rating": 4.6, "published_date": "2011", "description": "A book on innovation and agile business practices."},
    {"title": "Good to Great", "author": "Jim Collins", "rating": 4.6, "published_date": "2001", "description": "A book analyzing what makes companies successful."},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "rating": 4.6, "published_date": "1937", "description": "A book about success principles and wealth-building strategies."},
    {"title": "The 4-Hour Workweek", "author": "Tim Ferriss", "rating": 4.5, "published_date": "2007", "description": "A guide to lifestyle design and time management."},
    {"title": "The Millionaire Fastlane", "author": "MJ DeMarco", "rating": 4.5, "published_date": "2011", "description": "A book about achieving financial freedom quickly."},
    {"title": "Your Next Five Moves", "author": "Patrick Bet-David", "rating": 4.5, "published_date": "2020", "description": "A strategic guide for business growth and leadership."},
    {"title": "The $100 Startup", "author": "Chris Guillebeau", "rating": 4.5, "published_date": "2012", "description": "A book about launching small businesses with minimal investment."},
    {"title": "Company of One", "author": "Paul Jarvis", "rating": 4.4, "published_date": "2019", "description": "A book about growing a small business without scaling up unnecessarily."},
    {"title": "The Millionaire Next Door", "author": "Thomas J. Stanley", "rating": 4.4, "published_date": "1996", "description": "A study of wealthy individuals and their habits."}
]
,
  "Comics & Graphic Novels": [
    {"title": "Maus", "author": "Art Spiegelman", "rating": 4.9, "published_date": "1991", "description": "A Pulitzer Prize-winning Holocaust memoir."},
    {"title": "Watchmen", "author": "Alan Moore", "rating": 4.9, "published_date": "1986", "description": "A deconstruction of the superhero genre."},
    {"title": "The Many Deaths of Laila Starr", "author": "Ram V", "rating": 4.9, "published_date": "2021", "description": "A philosophical exploration of death and humanity."},
    {"title": "The Sandman", "author": "Neil Gaiman", "rating": 4.8, "published_date": "1989", "description": "A blend of mythology, fantasy, and horror."},
    {"title": "Batman: The Killing Joke", "author": "Alan Moore", "rating": 4.8, "published_date": "1988", "description": "A psychological exploration of Batman and Joker."},
    {"title": "Monstress", "author": "Marjorie Liu", "rating": 4.8, "published_date": "2015", "description": "A fantasy steampunk world with deep lore and stunning art."},
    {"title": "Something is Killing the Children", "author": "James Tynion IV", "rating": 4.8, "published_date": "2019", "description": "A horror mystery about a town plagued by monsters."},
    {"title": "Immortal Hulk", "author": "Al Ewing", "rating": 4.8, "published_date": "2018", "description": "A horror-themed take on the Hulk's story."},
    {"title": "Batman: Year One", "author": "Frank Miller", "rating": 4.7, "published_date": "1987", "description": "An origin story of Batman’s early days."},
    {"title": "V for Vendetta", "author": "Alan Moore", "rating": 4.7, "published_date": "1988", "description": "A dystopian story about freedom and revolution."},
    {"title": "Persepolis", "author": "Marjane Satrapi", "rating": 4.7, "published_date": "2000", "description": "A memoir about growing up during the Iranian Revolution."},
    {"title": "Doomsday Clock", "author": "Geoff Johns", "rating": 4.7, "published_date": "2017", "description": "A sequel to Watchmen merging with DC’s main universe."},
    {"title": "Paper Girls", "author": "Brian K. Vaughan", "rating": 4.7, "published_date": "2015", "description": "A sci-fi adventure about a group of newspaper delivery girls."},
    {"title": "The Nice House on the Lake", "author": "James Tynion IV", "rating": 4.7, "published_date": "2021", "description": "A psychological horror about the end of the world."},
    {"title": "Superman: Red Son", "author": "Mark Millar", "rating": 4.6, "published_date": "2003", "description": "An alternate history where Superman lands in the USSR."},
    {"title": "Saga", "author": "Brian K. Vaughan", "rating": 4.6, "published_date": "2012", "description": "A space opera with deep storytelling."},
    {"title": "House of X / Powers of X", "author": "Jonathan Hickman", "rating": 4.6, "published_date": "2019", "description": "A revolutionary relaunch of the X-Men universe."},
    {"title": "Black Hammer", "author": "Jeff Lemire", "rating": 4.6, "published_date": "2016", "description": "A unique take on superhero mythology."},
    {"title": "Ms. Marvel (Kamala Khan)", "author": "G. Willow Wilson", "rating": 4.6, "published_date": "2014", "description": "A fresh and inspiring take on a teenage superhero."},
    {"title": "The Wicked + The Divine", "author": "Kieron Gillen", "rating": 4.6, "published_date": "2014", "description": "Gods reincarnated as pop stars in modern times."},
    {"title": "Batman: Three Jokers", "author": "Geoff Johns", "rating": 4.6, "published_date": "2020", "description": "A deep dive into the mystery of the Joker’s multiple identities."},
    {"title": "Spider-Man: Blue", "author": "Jeph Loeb", "rating": 4.5, "published_date": "2002", "description": "A heartfelt story about Peter Parker’s past love."},
    {"title": "Hawkeye (Matt Fraction & David Aja)", "author": "Matt Fraction", "rating": 4.5, "published_date": "2012", "description": "A stylish and witty take on Hawkeye’s life outside the Avengers."}
]
,

   "Mystery & Thriller": [
    {"title": "Sherlock Holmes: The Complete Collection", "author": "Arthur Conan Doyle", "rating": 4.9, "published_date": "1887", "description": "The famous detective's best cases."},
    {"title": "Gone Girl", "author": "Gillian Flynn", "rating": 4.7, "published_date": "2012", "description": "A psychological thriller about a missing wife."},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "rating": 4.6, "published_date": "2019", "description": "A psychological thriller about a woman who stops speaking."},
    {"title": "Big Little Lies", "author": "Liane Moriarty", "rating": 4.6, "published_date": "2014", "description": "A novel about secrets in a suburban town."},
    {"title": "Shutter Island", "author": "Dennis Lehane", "rating": 4.6, "published_date": "2003", "description": "A psychological thriller set in a mysterious mental institution."},
    {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "rating": 4.6, "published_date": "2005", "description": "A dark and gripping mystery novel."},
    {"title": "The Guest List", "author": "Lucy Foley", "rating": 4.6, "published_date": "2020", "description": "A thrilling mystery set during a wedding on a remote Irish island."},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "rating": 4.5, "published_date": "2003", "description": "A thriller based on historical conspiracies."},
    {"title": "Before I Go to Sleep", "author": "S.J. Watson", "rating": 4.5, "published_date": "2011", "description": "A thriller about a woman with memory loss."},
    {"title": "One of Us Is Lying", "author": "Karen M. McManus", "rating": 4.5, "published_date": "2017", "description": "A YA thriller about five students, one murder, and many secrets."},
    {"title": "The Reversal", "author": "Michael Connelly", "rating": 4.5, "published_date": "2010", "description": "A gripping legal thriller featuring lawyer Mickey Haller."},
    {"title": "The Woman in the Window", "author": "A.J. Finn", "rating": 4.3, "published_date": "2018", "description": "A psychological thriller with an unreliable narrator."},
    {"title": "The No. 1 Ladies' Detective Agency", "author": "Alexander McCall Smith", "rating": 4.3, "published_date": "1998", "description": "A charming detective story set in Botswana."},
    {"title": "The Chain", "author": "Adrian McKinty", "rating": 4.4, "published_date": "2019", "description": "A chilling thriller where victims must kidnap to save their own loved ones."},
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "rating": 4.4, "published_date": "2015", "description": "A psychological thriller about an unreliable witness to a crime."},
    {"title": "Saltwater", "author": "Katy Hays", "rating": 4.7, "published_date": "2025", "description": "A thrilling murder mystery set on the island of Capri."},
    {"title": "The Underground Man", "author": "Ross Macdonald", "rating": 4.6, "published_date": "1971", "description": "A private detective novel set against the backdrop of Los Angeles wildfires."},
    {"title": "Snowy Day and Other Stories", "author": "Lee Chang-dong", "rating": 4.5, "published_date": "2025", "description": "A collection of stories exploring themes of unknowability, family secrets, and societal paranoia in South Korea."}
]
   
    }

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

for category, books in books_data.items():
    for book in books:
        cursor.execute("""
            INSERT INTO books (title, author, category, rating, published_date, description)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            book["title"],
            book["author"],
            category,
            book["rating"],
            book["published_date"],
            book["description"]
        ))

conn.commit()
conn.close()

print("Books inserted successfully.")