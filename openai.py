import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: who are you?\n\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I need to do my homework but i am being lazy\nAI:\n\nThere's no need to be ashamed of being lazy - everyone feels that way sometimes! The important thing is to find a way to motivate yourself to do your homework. Perhaps you could set a goal for yourself, such as finishing your homework in a certain amount of time, or getting a certain grade on your next assignment. Once you have a goal in mind, it will be easier to push yourself to do your homework. Good luck!\nHuman: who created you?\nAI: OpenAI created me.\nHuman: who is elon musk?\n\nAI:\n\nAI: Elon Musk is the founder, CEO and CTO of SpaceX, co-founder of Tesla Motors, and chairman of SolarCity. He is also the founder of The Boring Company, a tunnel construction company.\nHuman: don't he own openai ?\nAI:\n\nI'm not sure - you would need to ask him!\nHuman: how can i contact him?\n\nAI:\n\nThere are many ways to contact Elon Musk - you could send him an email, tweet him, or even write him a letter. However, the best way to get in touch with him is probably through his companies. You could try reaching out to SpaceX, Tesla, or SolarCity. Thanks for asking!\nHuman: help me in finding the most popular places of the world",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)