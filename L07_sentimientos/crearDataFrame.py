from deep_translator import GoogleTranslator

# load dataset 
df = pd.read_csv(r'./data/1429_1.csv')
data = df[["id","reviews.text","reviews.rating"]]

## Seleccionar una muestra
data5 = data[data['reviews.rating']==5].sample(400,random_state=43)
data4 = data[data['reviews.rating']==4].sample(400,random_state=43)
data3 = data[data['reviews.rating']==3].sample(400,random_state=43)
data2 = data[data['reviews.rating']==2].sample(400,random_state=43)
data1 = data[data['reviews.rating']==1].sample(400,random_state=43)
# concat data sets
data = pd.concat([data5,data4,data3,data2,data1])
# - - Esta parte del código traduce únicamente un texto plano
def traductor_deep(texto):
    traductor = GoogleTranslator(source='es', target='en')
    resultado = traductor.translate(texto)
    return(resultado)

## Funcion chat gtp para consola.
#import os
#import openai
#openai.api_key = os.getenv("OPENAI_API_KEY")

#completion = openai.ChatCompletion.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    {"role": "user", "content": f"traduce el siguiente texto a español {}".(texto)}
#  ]
#)

print(completion.choices[0].message.content)

data["reviews.text_esp"]=["reviews.text"].apply(traductor_deep)
data.to_csv(r'./data/Amazon.csv')