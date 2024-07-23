# Chat with an intelligent assistant in your terminal  
# instruct template from official repo
# https://huggingface.co/nicholasKluge/Aira-2-124M-DPO
# THIS MODEL DOES NOT HAVE A CHAT TEMPLATE
import sys
from time import sleep
 

from llama_cpp import Llama
print("\033[95;3;6m")
print("1. Loading the model...")
print("2. DONE...")
print("\033[0m")  #reset all
llm = Llama(model_path="models\Aira-2-124M-DPO.Q8_0.gguf",
            verbose=False,
            n_ctx=1024)
print("\033[92;1m")
counter = 1
while True:  
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break
    print("\033[92;1m")
    prompt = f"<|startofinstruction|>{userinput}<|endofinstruction|>"
    completion = llm(prompt, stop=["<|endofcompletion|>"], temperature=0.25,
          repeat_penalty=1.55,
          max_tokens=500)["choices"][0]["text"]
    print(completion)
    print("\033[0m")  #reset all
    print('---')


"""
print("\033[95;3;6m")
print("1. Waiting 10 seconds for the API to load...")
sleep(10)
print("2. Connecting to the LlamaFile API...")
print("\033[0m")  #reset all

# Point to the local server
client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")


history = [
    {"role": "system", "content": "You are KS-AI, an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful. Always reply in the language of the instructions."},
    {"role": "user", "content": "Hi there!"},
    {"role": "assistant", "content": "Hi, I am KS-AI your intelligent assistant. How can I help you today?"}
]

#print(model("The quick brown fox jumps ", stop=["."])["choices"][0]["text"])
print("\033[92;1m")
counter = 1
while True:  
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break
    print("\033[92;1m")

    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.3,
        frequency_penalty  = 1.6,
        max_tokens = 600,
        stream=True,
        stop=['<|endoftext|>','</s>']
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content
    history.append(new_message)  
    counter += 1  

"""