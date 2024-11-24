AI-Powered Mental Health Assistant: MBTI Prediction and Sentiment Analysis

->This project is an AI-powered mental health assistant that uses natural language processing (NLP) and machine learning to predict Myers-Briggs Type Indicator (MBTI) personality types based on user text input. The assistant analyzes emotions and sentiment, and provides predictions on personality traits, helping users understand themselves better.

#Features:

*MBTI Personality Prediction: Predicts the user’s MBTI personality type (e.g., INTJ, ENFP) from text input.
*Sentiment Analysis: Identifies the user’s sentiment (positive, negative, or neutral) based on the input text.
*Emotion Detection: Detects specific emotions (e.g., happy, sad, stressed, etc.) from user inputs.
*Pre-trained BERT Model: Fine-tuned BERT model for improved accuracy on sentiment analysis tasks.
*Large Dataset: The model is trained on a diverse 50,000-entry dataset to ensure high accuracy and robust predictions.


#Project Overview:

Steps Involved:
*Dataset Preprocessing:
Clean the dataset by removing stop words, handling missing data, and normalizing text.
Tokenize the text data into individual words or subwords (tokens).

*Model Architecture:
BERT (Bidirectional Encoder Representations from Transformers) is used for deep learning-based text analysis. The model processes the text to capture the context of each word in a sentence.
The tokens are converted into input IDs using a tokenizer that converts each word/subword into a numerical format.
The CLS token represents the entire input sentence for classification tasks, and the SEP token is used to separate different sentences in tasks like question answering.

*Training the Model:
The pre-trained BERT model is fine-tuned on the 50,000-entry dataset for the task of sentiment analysis and MBTI prediction.
Logits are the raw prediction scores from the BERT model, and Softmax is used to convert these logits into probabilities, making them interpretable as predictions.

*Evaluation:
The model is evaluated using metrics like accuracy, F1 score, and confusion matrix to ensure its effectiveness.
Technologies Used:

*Python: The main programming language used for developing the model.
*TensorFlow/PyTorch: Libraries for building and training the machine learning model.
*Hugging Face Transformers: Pre-trained models and tokenizers for BERT and other NLP tasks.
*Scikit-learn: For evaluation metrics like F1 score and accuracy.


#How It Works:

*Input: The user provides a text input, such as "I am feeling blue."
*Preprocessing: The text is tokenized, stop words are removed, and it is converted into a format suitable for the BERT model.
*Model Inference: The BERT model processes the input and outputs a set of logits, which are converted into probabilities using the softmax function.
*Prediction: The model classifies the input text into one of the 16 MBTI personality types and/or detects the underlying sentiment and emotion.
*Example:

For a text input like:

"I am feeling blue."
(The model first processes this through tokenization and text preprocessing.
It then analyzes the sentiment (e.g., negative sentiment, sad emotion) and predicts the user's MBTI personality type based on the text pattern.
The output will provide the predicted MBTI type (e.g., INTJ, ENFP) and associated emotional state.)


#Steps to Run:

*Clone the Repository:
git clone https://github.com/yourusername/AI-Mental-Health-Assistant.git
cd AI-Mental-Health-Assistant


*Install Dependencies: Make sure you have Python installed, and then install the necessary libraries:
pip install -r requirements.txt


*Run the Model: You can test the model by running the following script:
python predict.py


*Input your Text: Enter your text in the command line or in the provided UI to see the sentiment and MBTI prediction.
Results:

#The model will output:

*Predicted Sentiment: (Positive, Negative, Neutral)
*Detected Emotion: (Sad, Happy, Angry, etc.)
*Predicted MBTI Type: One of the 16 personality types.
*Evaluation Metrics:


#The model is evaluated using:

*Accuracy: Percentage of correct predictions.
*F1 Score: A balance of precision and recall, important for imbalanced datasets.
*Confusion Matrix: Shows the performance of the classification model.


#Challenges Faced:

*Imbalanced Data: The dataset may have more entries for certain emotions or MBTI types, affecting model performance.
*Text Variability: User input can vary significantly, requiring extensive data augmentation and fine-tuning.


#Future Enhancements:

*Multilingual Support: Expand the assistant to support multiple languages.
*Voice Input: Integrate voice emotion recognition for an even richer user experience.
*User Feedback Loop: Continuously improve the model based on user feedback for better accuracy over time.
