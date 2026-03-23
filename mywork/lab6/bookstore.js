// Task 2: use database
// use bookstore;

// Task 3: insert first author
// db.authors.insertOne({"name": “Jane Austen”, "nationality": “British”, "bio": {"short": "English novelist known for novels about the British landed gentry.", "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development.")

// Task 4: update to add birthday
// db.authors.updateOne({ name: "Jane Austen" }, { $set: { birthday: "1775-12-16" } })

// Task 5: insert four more authors
// db.authors.insertOne({"name": "Ernest Hemingway", "nationality": "American", "bio": {"short": "American journalist, novelist, and short story writer known for themes of betrayal and honor.", "long": "Ernest Hemingway was an American journalist, novelist, and short story writer known for his focus on masculinity, human endurance, and themes of betrayal and honor."}, "birthday": "1899-07-21"})
// db.authors.insertOne({"name": "Margaret Atwood", "nationality": "Canadian", "bio": {"short": "Canadian writer known for speculative fiction novels.", "long": "Margaret Atwood is a Canadian writer whose works are known for their feminist perspectives, sardonic tone, and themes of survival, dystopia, and religion. Her most popular works include The Handmaid's Tale, The Blind Assassin, and the MaddAddam trilogy."}, "birthday": "1939-11-18"})
// db.authors.insertOne({"name": "William Shakespeare", "nationality": "English", "bio": {"short": "English playwright known as the greatest writer in the English language.", "long": "William Shakespeare was an English playwright, poet, and actor credited with co-writing at least 39 plays and 154 sonnets, and is known for popularizing hundreds of words and phrases commonly used today. His most famous works include plays Hamlet and Macbeth."}, "birthday": "1564-04-23"})
// db.authors.insertOne({"name": "Leo Tolstoy", "nationality": "Russian", "bio": {"short": "Russian writer regarded as one of the greatest authors of all time.", "long": "Leo Tolstoy was a Russian writer known for his works of realist fiction, like War and Peace and Anna Karenina, that explore love, morality, and Russian society. He is also regarded as a moral philosopher and social reformer, influencing figures like MLK Jr. and Gandhi."}, "birthday": "1828-09-09"})

// Task 6: total count
// db.authors.countDocuments()

// Task 7: British authors, sorted by name
// db.authors.find({nationality: "British"}).sort({name:1})
