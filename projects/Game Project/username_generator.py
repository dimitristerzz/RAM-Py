import random

nouns = ["people", "history", "way", "art", "world", "information", "map"]
adjectives = ["afraid", "brave", "calm", "fierce", "kind", "nice", "proud", "scary", "witty", "worried"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

random_username = random.choice(nouns) + random.choice(adjectives) + random.choice(numbers)