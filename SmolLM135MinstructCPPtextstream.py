"""
llama_model_loader: loaded meta data with 37 key-value pairs and 272 tensors from models/SmolLM-135M-Instruct.Q8_0.gguf 
(version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Cosmo2 135M Webinst Sc2
llama_model_loader: - kv   3:                       general.organization str              = HuggingFaceTB
llama_model_loader: - kv   4:                           general.finetune str              = webinst-sc2
llama_model_loader: - kv   5:                           general.basename str              = cosmo2
llama_model_loader: - kv   6:                         general.size_label str              = 135M
llama_model_loader: - kv   7:                            general.license str              = apache-2.0
llama_model_loader: - kv   8:                          general.languages arr[str,1]       = ["en"]
llama_model_loader: - kv   9:                          llama.block_count u32              = 30
llama_model_loader: - kv  10:                       llama.context_length u32              = 2048

CHAT TEMPLATE = TRUE

llm_load_print_meta: model ftype      = Q8_0
llm_load_print_meta: model params     = 134.52 M
llm_load_print_meta: model size       = 136.40 MiB (8.51 BPW)
llm_load_print_meta: general.name     = Cosmo2 135M Webinst Sc2
llm_load_print_meta: BOS token        = 1 '<|im_start|>'
llm_load_print_meta: EOS token        = 2 '<|im_end|>'
llm_load_print_meta: UNK token        = 0 '<|endoftext|>'
llm_load_print_meta: PAD token        = 2 '<|im_end|>'
llm_load_print_meta: LF token         = 143 'Ä'
llm_load_print_meta: EOT token        = 0 '<|endoftext|>'
"""
import sys
from time import sleep
import datetime
import tiktoken
encoding = tiktoken.get_encoding("r50k_base") #context_count = len(encoding.encode(yourtext))

def writehistory(filename,text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')
    f.close()

modelname = 'SmolLM-135M-Instruct.Q8_0.gguf'
logfile = 'SmolLM-135M-Instruct_LOG.txt'
header = f"""CHAT LOG WITH {modelname}
================================================
TIMESTAMP: {datetime.datetime.now()}
------------------------------------------------

"""
writehistory(logfile,header)

from llama_cpp import Llama
print("\033[95;3;6m")
print(f"1. Loading the model {modelname}...")
print("2. DONE...")
print("\033[0m")  #reset all
llm = Llama(model_path=f"models/{modelname}",
            verbose=False,
            n_ctx=2048)
print("\033[92;1m")
counter = 1
history = []
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
    history.append({"role": "user", "content": userinput})
    new_message = {"role": "assistant", "content": ""}
    
    full_response = ""
    fisrtround = 0
    for chunk in llm.create_chat_completion(
        messages=history,
        temperature=0.25,
        repeat_penalty= 1.42,
        stop=['<|im_end|>'],
        max_tokens=450,
        stream=True,):
        try:
            if chunk["choices"][0]["delta"]["content"]:
                print(chunk["choices"][0]["delta"]["content"], end="", flush=True)
                full_response += chunk["choices"][0]["delta"]["content"]                              
        except:
            pass        
    new_message["content"] = full_response
    history.append(new_message)  
    counter += 1  

    print("\033[0m")  #reset all
    print('---')
    history.append({"role": "assistant", "content": full_response})
    kpis = f'''---
prompt tokens: {len(encoding.encode(userinput))}
generated tokens: {len(encoding.encode(full_response))}
---
'''
    header = f"""User: {userinput}
Assistant: {full_response}
{kpis}
------------------------------------------------
"""
    writehistory(logfile,header)  