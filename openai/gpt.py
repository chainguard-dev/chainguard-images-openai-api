from openai import OpenAI

with open('/run/secrets/openai_key') as key_file:
    KEY = key_file.read()


client = OpenAI(api_key=KEY.strip())

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poet and you write everything in iambic pentameter. You start every stanza with OH YEAH!"},
    {"role": "user", "content": "Tell us why Chainguard's container Images are super secure"}
  ]
)
print(completion.choices[0].message.content)
