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
<|startofinstruction|>What is a language model?<|endofinstruction|>
A language model is a probability distribution over a vocabulary.<|endofcompletion|>
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


### some text example for NlP operations
```
The quest for artificial general intelligence (AGI) has captured the attention of the research community for several decades now.
AGI refers to the ability of an AI system to perform a wide range of tasks that humans can do, without being explicitly programmed to do so. This means that we look for a system with the capacity to learn, reason, and adapt to new situations, much like a human being.
However, despite significant progress in the field, AGI remains an elusive goal, with most AI systems today still limited to narrow tasks and domains.
And why is that?
What AI is not good at
One of the major obstacles to AGI is the reliance of modern AI systems on memorization rather than reasoning. These systems, which we all know as Language Large Models (LLMs), are proficient at memorizing patterns in their training data and applying them in adjacent contexts.
However, they lack the ability to generate new reasoning based on new cases.
This limitation is due to the fact that LLMs rely heavily on memorization rather than reasoning, and they cannot generate new reasoning based on unusual or innovative situations.
Another issue is the inability of AI systems to generalize beyond their training data. For example, an AI system that has been trained to play chess may be able to beat humans at chess, but it would not be able to transfer its knowledge to other board games like Checkers or Go.
This failure to generalize is a major obstacle to achieving AGI, as it limits the system’s ability to apply its knowledge to new situations.
A new paradigm and a new benchmark
In 2019, François Chollet — creator of Keras, an open-source deep learning library adopted by over 2.5M developers, and Software Engineer & AI Researcher at Google — published the influential paper “On the Measure of Intelligence” where he introduced a benchmark to measure the efficiency of AI skill-acquisition on unknown tasks: Abstraction and Reasoning Corpus (ARC-AGI)
In the end, as every good Science should do, we must start from the definition. There is a general consensus about AGI defined as “a system that can automate the majority of economically valuable work”. While this can be indeed considered a useful goal... it is also an incorrect measure of intelligence.
To make deliberate progress toward more intelligent and human-like systems, we need to follow an appropriate feedback signal: we need to define and evaluate intelligence.
Measuring task-specific skill is not a good proxy for intelligence.
Skills, Memorization, and Intelligence
Skill is heavily influenced by prior knowledge and experience: unlimited priors or unlimited training data allows developers to “buy” levels of skill for a system. This masks a system’s own generalization power.
Modern AI (LLMs) have shown to be great memorization engines. They are able to memorize high-dimensional patterns in their training data and apply those patterns to adjacent contexts.
This is also how their apparent reasoning capability works. LLMs are not actually reasoning. Instead, they memorize reasoning patterns and apply those reasoning patterns to adjacent contexts. However, they cannot generate new reasoning based on new situations.
Intelligence, on the other end, lies in broad or general-purpose abilities; we have to adjust our definition of AGI considering it as a system that can efficiently acquire new skills outside of its training data: even better…
The intelligence of a system is a measure of its skill-acquisition efficiency over a scope of tasks, with respect to priors, experience, and generalization difficulty. — François Chollet, “On the Measure of Intelligence”
How can we measure this kind of Intelligence?
Most AI benchmarks measure skill. But skill is not intelligence, we just saw that right?
Born from the very same research in 2019, the Abstraction and Reasoning Corpus for Artificial General Intelligence (ARC-AGI) is considered the only formal benchmark of AGI.
The Abstraction and Reasoning Corpus (ARC) is a benchmark designed specifically to test the skill-acquisition efficiency over a scope of tasks by AI systems.
ARC-AGI consists of unique training and evaluation tasks. Each task contains input-output examples. The puzzle-like inputs and outputs present a grid where each square can be one of ten colors. A grid can be any height or width between 1x1 and 30x30.
an example of ARC-AGI task. To successfully solve a task, the test-taker must produce a pixel-perfect correct output grid for the final output. This includes picking the correct dimensions of the output grid.
As we can see it really looks like a collection of tasks involving images that require reasoning and abstraction to solve.
There is a clear intent here: to verify the ability of an AI system to learn from examples and apply that knowledge to solve new, unseen problems. This is a key aspect of human-like intelligence, often called “fluid intelligence.”
The ARC benchmark is significant because:
It challenges current machine learning methods that struggle with tasks requiring this kind of abstract reasoning.
It helps researchers develop AI systems that are closer to achieving human-level intelligence.
philosophers — Image by morhamedufmg from Pixabay
Multi-disciplinary approach
Progress toward artificial general intelligence (AGI) has stalled. LLMs are trained on unimaginably vast amounts of data, yet they remain unable to adapt to simple problems they haven’t been trained on, or make novel inventions, no matter how basic.
Chollet’s unbeaten 2019 Abstraction and Reasoning Corpus for Artificial General Intelligence (ARC-AGI) is the only formal benchmark of AGI.
It’s easy for humans, but hard for AI.
Recently Yann LeCun, Professor at NYU and Chief AI Scientist at Meta, openly stated that if we want to advance in AGI we should not work on LLMs…
I like the provocation, and I believe every AI researcher is well aware of this challenge. And I would say that University researchers are supposed to be a few steps ahead in this. The Academy is usually well versed in a multi-discipline approach to problems, but they lack the resources (money and computational power).
However, the current trend in AI research is moving towards closed-source research, which limits the sharing of ideas and knowledge. This trend is driven by the belief that “scale is all you need” and the desire to protect competitive advantages. This approach stifles innovation and limits the rate of progress towards AGI.
```
