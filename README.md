### Products Review Analysis using spaCy and SpacyTextBlob

**Description:**
This Python code analyzes product reviews using spaCy and SpacyTextBlob, providing insights into sentiment and similarity between reviews.

**Importance:**
In the modern era of e-commerce, understanding customer sentiment is crucial for businesses. This code allows for the efficient analysis of product reviews, aiding companies in gauging customer satisfaction and making data-driven decisions.

**Table of Contents:**
1. Introduction - Overview of the project and its significance.
2. Installation - Instructions for installing the necessary dependencies.
3. Usage - Guidelines on how to use the code with examples.
4. Authors - Information about the authors of the project.

**Installation:**
To run this code locally, follow these steps:
1. Install required dependencies: pandas, spacy, spacytextblob.

  pip install pandas spacy spacytextblob
  python -m spacy download en_core_web_md
3. Clone the repository and execute the code.
    
**Usage:**
The code focuses on analyzing sentiment and similarity in product reviews. It reads data from a CSV file ('amazon_product_reviews.csv') and processes reviews using spaCy and SpacyTextBlob.

**Examples:**
#### Process a single review
process_review(clean_data, 'reviews.text', 125)

#### Compare two reviews
process_review(clean_data, 'reviews.text', 200, 1500)

**Authors:**
Zinaida Liashenko

Feel free to contribute or provide feedback to enhance the functionality of this project. Happy analyzing!
