import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob


'''
Products review analysis using spaCy and SpacyTextBlob

Description:
This code uses the spaCy model to process and analysis of product reviews.
This code prints sentiment for every review and the similarity for the two reviews.

Incoming Data:
- CSV 'amazon_product_reviews.csv', column 'reviews.text' with reviews text.

Output Data:
- Print the results of sentiment analysis and similarity of two reviews.

Dependencies:
- pandas, spacy, spacytextblob

Comments:
- analyze_sentiment returns sentiment and mood for review;
- analyze_similarity returns similarity_score and similarity for two reviews;
- clean_and_tokenize_text function uses spaCy to tokenize and clean text review;
- process_review provides all the functions to process the data and print the results.

Examples of usage:
process_review(125, 1025)
process_review(200, 1500)
process_review(0)
'''


# sentiment and mood of the review
def analyze_sentiment(doc):

    sentiment = doc._.blob.sentiment # sentiment

    # set the range for the mood of the review
    if sentiment.polarity > 0.5:
        mood = 'Positive'
    elif sentiment.polarity < -0.2:
        mood = 'Negative'
    else:
        mood = 'Neutral'

    return sentiment, mood


# similarity of 2 reviews
def analyze_similarity(doc1, doc2):

    similarity_score = doc1.similarity(doc2) # similarity

    # set the range for the similarity of the reviews
    if similarity_score > 0.65:
        similarity = 'Similar'
    else:
        similarity = 'Not similar'

    return similarity_score, similarity


# data preprocessing
def clean_and_tokenize_text(review):

    clean_review = (
        review.astype(str).str.lower() # lower register
        .replace(to_replace=r'(?i)(https?|www)\:\/\/[^\s]+', value='', regex=True) # delete web sites
        .replace(to_replace=r'[^\w\s]', value='', regex=True) # delete non-alphanumeric and non-whitespace characters
        .replace(to_replace=r'\d', value='', regex=True) # delete numbers
    )

    doc = nlp(str(clean_review)) # tokenization
    tokens = [token.text for token in doc if not token.is_stop] # delete stop words
    string = " ".join(tokens) # concatenate words in a string
    doc = nlp(string) # tokenization

    return doc


# call and print the necessary func to process one or two reviews
# add try-except in case of incorrect data passed to the function
def process_review(dataset, feature_name, review1, review2=None):

    try:
        if review2:
            # preprocessing and tokenization for both reviews
            doc1 = clean_and_tokenize_text(dataset.loc[[review1], feature_name])
            doc2 = clean_and_tokenize_text(dataset.loc[[review2], feature_name])
            # similarity analysis
            similarity_score, similarity = analyze_similarity(doc1, doc2) 
            # sentiment analysis
            sentiment1, mood1 = analyze_sentiment(doc1)
            sentiment2, mood2 = analyze_sentiment(doc2)

            # print similarity, sentiment1, sentiment2
            print('---------------------------------------------')
            print(f'Similarity for reviews {review1} and {review2}: {similarity_score} - {similarity}\n')
            print(f'Sentiment for review {review1} is {mood1}: {sentiment1}')
            print(f'Sentiment for review {review2} is {mood2}: {sentiment2}')
            print('---------------------------------------------')
            
        else:
            # preprocessing and tokenization for one review
            doc = clean_and_tokenize_text(dataset.loc[[review1], feature_name])
            # sentiment analysis
            sentiment, mood = analyze_sentiment(doc)

            # print sentiment
            print('---------------------------------------------')
            print(f'Sentiment for review {review1} is {mood}: {sentiment}')
            print('---------------------------------------------')
        
    except Exception as ex:
        # in case of the exception the message of the error is printed
        print('Please check your the parameters you pass to the function')
        print(f'An error occurred: {str(ex)}')
        return None    
        

if __name__ == "__main__":

    nlp = spacy.load('en_core_web_md') # implement a sentiment analysis model
    nlp.add_pipe('spacytextblob') # TextBlob extension to the spaCy pipeline
    data = pd.read_csv('amazon_product_reviews.csv', low_memory=False) # read the data, not using optimizations to reduce memory usage
    clean_data = data.dropna(subset=['reviews.text']) # delete missed values

    # examples
    process_review(clean_data, 'reviews.text', 125, 1025)
    process_review(clean_data, 'reviews.text', 200, 1500)
    process_review(clean_data, 'reviews.text', 0)