from textblob import TextBlob
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras import Input
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

#removes all but latin leters
def filterNonLatin(myStr):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    answer = ''.join(filter(whitelist.__contains__, myStr))
    return answer


#read sample data into a dataframe
dfAngry = pd.read_csv("Anger/tweets.csv")
dfHappy = pd.read_csv("Happiness/tweets.csv")

happyTokens = []
angryTokens = []
lbls = []
for i in range (0, min(dfHappy.shape[0],dfAngry.shape[0])):
    noHash = (dfHappy["tweet"][i].replace("#happy","")).replace("#Happy", "")
    tb = TextBlob(filterNonLatin(noHash))
    happyTokens += [list(tb.words)]
    lbls += [0]
    noHash = (dfAngry["tweet"][i].replace("#angry","")).replace("#Angry", "")
    tb = TextBlob(filterNonLatin(noHash))
    angryTokens += [list(tb.words)]
    lbls += [1]

d = {"text": happyTokens + angryTokens, "lbls": lbls}
combinedDF = pd.DataFrame(data=d)
traindf = combinedDF.head(combinedDF.shape[0]*int(8/10))
testdf = combinedDF.tail(combinedDF.shape[0]*int(2/10))
train_data = tf.data.Dataset.from_tensor_slices(traindf)
test_data = tf.data.Dataset.from_tensor_slices(testdf)

model = keras.Sequential()
model.add(Input(shape=(1,), dtype="string"))
max_tokens = 1000
max_len = 100
vectorize_layer = TextVectorization(
  # Max vocab size. Any words outside of the max_tokens most common ones
  # will be treated the same way: as "out of vocabulary" (OOV) tokens.
  max_tokens=max_tokens,
  # Output integer indices, one per string token
  output_mode="int",
  # Always pad or truncate to exactly this many tokens
  output_sequence_length=max_len,
)
# Call adapt(), which fits the TextVectorization layer to our text dataset.
# This is when the max_tokens most common words (i.e. the vocabulary) are selected.
print(train_data)
#train_texts = train_data.map(lambda x: x)
# vectorize_layer.adapt(train_data["text"])
# model.add(vectorize_layer)














##IGNORE THIS SHITE LOL _---------------------------------------

# vocab = dict()
# count = 0

# happyInts = []
# #analyse with textblob
# for i in range (0, dfHappy.shape[0]):
#     noHash = (dfHappy["tweet"][i].replace("#happy","")).replace("#Happy", "")
#     tb = TextBlob(filterNonLatin(noHash))
#     wordTokens = tb.words
#     intTokens = []
#     #creating a map of integers to embed words
#     for word in wordTokens:
#         if not(word in vocab):
#             vocab.update({word : count}) 
#             count += 1
#             intTokens = intTokens + [count]
#         else:
#             intTokens += [vocab[word]]
#     happyInts += [intTokens]


# angryInts = []
# #analyse with textblob
# for i in range (0, dfAngry.shape[0]):
#     noHash = (dfAngry["tweet"][i].replace("#angry","")).replace("#Angry", "")
#     tb = TextBlob(filterNonLatin(noHash))
#     wordTokens = tb.words
#     intTokens = []
#     #creating a map of integers to embed words
#     for word in wordTokens:
#         if not(word in vocab):
#             vocab.update({word : count}) 
#             count += 1
#             intTokens = intTokens + [count]
#         else:
#             intTokens += [vocab[word]]
#     angryInts += [intTokens]