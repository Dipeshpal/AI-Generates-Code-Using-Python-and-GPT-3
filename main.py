from key import *
import glob
import openai
from gpt import GPT
from gpt import Example


openai.api_key = key
gpt = GPT(engine="davinci",
          temperature=0.5,
          output_prefix="Output: \n\n",
          max_tokens=100)

# add some code examples
for file in glob.glob("examples/*"):
    title = file.replace("_", " ")
    with open(f"{file}", "r") as f:
        code = f.read()
    gpt.add_example(Example(title, code))

# add some calculation examples
gpt.add_example(Example("add 3+5", "8"))
gpt.add_example(Example("add 8+5", "13"))
gpt.add_example(Example("add 50+25", "75"))

# Inferences
prompt = "sort list in python"
output = gpt.get_top_reply(prompt)
print(prompt, ":", output)
print("----------------------------------------")

prompt = "Code weather api in python"
output = gpt.get_top_reply(prompt)
print(prompt, ":", output)
print("----------------------------------------")

prompt = "What is 876+89"
output = gpt.get_top_reply(prompt)
print(prompt, ":", output)
print("----------------------------------------")

