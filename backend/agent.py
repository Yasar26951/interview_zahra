
from typing import TypedDict, List, Dict
#from flask import Flask, request, jsonify
import torch
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict
from transformers import AutoTokenizer, AutoModelForCausalLM, 
from peft import PeftModel
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage,AIMessage
from transformers import pipeline
base_model = "Qwen/Qwen2.5-3B-Instruct"
adapter_repo = "Mohamed26/Qwen2.5-3B-Instruct-qlora-zahra"

tokenizer = AutoTokenizer.from_pretrained(base_model)
base = AutoModelForCausalLM.from_pretrained(base_model, device_map="auto")

model = PeftModel.from_pretrained(base, adapter_repo)
gen_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    temperature=0.7,
    do_sample=True,
)

from langchain_community.llms import HuggingFacePipeline


llm = HuggingFacePipeline(pipeline=gen_pipe)
class ChatState(TypedDict):
    history: List[BaseMessage]
    

def generate(state: ChatState) -> ChatState:
    h=state["history"][-1].content
    li=llm.invoke(f"""### instruction:
    you are a helpful interview assistant called zahra. help the student answer interview questions professionally and clearly.

### context:
{h}

### response:""")
    
    if li.find("\n### response:")!=-1:
        li=li[li.find("\n### response:")+len("\n### response:"):]
    if li.find("### context:")!=-1:
        li=li[:li.find("### context:")]
    if li.find("```")!=-1:
        li=li[:li.find("```")]
    state["history"].append(AIMessage(li))
    return state
sg = StateGraph(ChatState)
sg.add_node("generate", generate)
sg.set_entry_point("generate")
sg.add_edge("generate", END)
app1=sg.compile()