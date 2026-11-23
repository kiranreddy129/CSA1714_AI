
positive_words = ["good", "happy", "excellent", "great", "love"]
negative_words = ["bad", "sad", "poor", "worst", "hate"]

text = input("Enter a sentence: ")

words = text.lower().split()

positive = 0
negative = 0

for word in words:
    word = word.strip(".,!?")

    if word in positive_words:
        positive += 1
    elif word in negative_words:
        negative += 1

if positive > negative:
    print("Sentiment: Positive")
elif negative > positive:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
