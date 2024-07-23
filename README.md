# ultraSmolLM
On the normal human benchmark models smaller than 500M parameters

<img src='https://huggingface.co/datasets/HuggingFaceTB/images/resolve/main/banner_smol.png' height=400>

works with Python 3.11+

required `llama-cpp-python` >= 0.2.83

```
pip install llama-cpp-python[server]==0.2.83 
pip instal tiktoken

mkdir models
```

Download the models below into the `models` directory

### Models with Chat Template

[MaziyarPanahi/SmolLM-360M-Instruct-GGUF 
](https://huggingface.co/MaziyarPanahi/SmolLM-360M-Instruct-GGUF/tree/main)

[MaziyarPanahi/SmolLM-135M-Instruct-GGUF](https://huggingface.co/MaziyarPanahi/SmolLM-135M-Instruct-GGUF/tree/main)


```
python SmolLM360MinstructCPPtextstream.py
```

Still under test OpenELM

### Models without a Chat Template

Based on the [Aira-2](https://huggingface.co/nicholasKluge/Aira-2-124M-DPO) series, nicholasKluge/Aira-2-124M-DPO
```
<|startofinstruction|>What is a language model?<|endofinstruction|>A language model is a probability distribution over a vocabulary.<|endofcompletion|>
```
#### Additional info
```
Model File: Aira-2-124M-DPO.Q8_0.gguf
───────────────────────────────────────────── Details ──────────────────────────────────────────────
Training Context Window: 1024
Stop Tokens: ['<|endofcompletion|>']
This model has Chat Template? False

 GGUF Repo: https://huggingface.co/Felladrin/gguf-Aira-2-124M-DPO
 Original Repo: https://huggingface.co/nicholasKluge/Aira-2-124M-DPO
 Model architecture: gpt2
 Number of parameters: 124M
```

Or to have the same number of parameters:
```
Model File: Aira-2-355M.Q6_K.gguf
───────────────────────────────────────────── Details ──────────────────────────────────────────────
Training Context Window: 1024
Stop Tokens: ['<|endoftext|>']
This model has Chat Template? False
────────────────────────────────────────────────────────────────────────────────────────────────────

 <|startofinstruction|>What is a language model?<|endofinstruction|>
 A language model is a probability distribution over a vocabulary.<|endofcompletion|>

 Recommended inference parameters
 penalty_alpha: 0.5
 top_k: 2
 repetition_penalty: 1.0016

────────────────────────────────────────────────────────────────────────────────────────────────────
 GGUF Repo: https://huggingface.co/Felladrin/gguf-Aira-2-355M/tree/main
 Original Repo: https://huggingface.co/nicholasKluge/Aira-2-355M
 Model architecture: gpt2
 Number of parameters: 355M
```


