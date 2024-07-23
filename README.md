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
