# Transformers

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def loadTokenizerModel(modelName="microsoft/DialoGPT-medium"):
    tokenizer = AutoTokenizer.from_pretrained(modelName)
    model = AutoModelForCausalLM.from_pretrained(modelName)
    print("finished learning model")
    return tokenizer, model

#if __name__=="__main__"#all function will be under this
tokenizer, model = loadTokenizerModel(modelName="microsoft/DialoGPT-medium")


def readInput(tokenizer):
    myInput = input("You: ")
    inputIDs = tokenizer.encode(myInput + tokenizer.eos_token, return_tensors='pt')

    return inputIDs

def generateResponse(tokenizer,model):
    inputIDs = readInput(tokenizer)
    chatOutput = model.generate(inputIDs,max_length=1250, pad_token_id = tokenizer.eos_token_id)
    chatOutputText = tokenizer.decode(chatOutput[:,inputIDs.shape[-1]:][0],skip_special_tokens=True)
    print("Model =",chatOutputText)

def generateResponseForRoundn(tokenizer,model,chatRound,chatHistory):
    inputIDs = readInput(tokenizer)

    allInputs = None
    if chatRound==0:
        allInputs = inputIDs
    else:
        allInputs = torch.cat([chatHistory,inputIDs],dim=1)

    allchatOutputsoFar = model.generate(allInputs,max_length=1250, pad_token_id = tokenizer.eos_token_id)
    chatOutputText = tokenizer.decode(allchatOutputsoFar[:,allInputs.shape[-1]:][0],skip_special_tokens=True)
    print("Model =",chatOutputText)
    return allchatOutputsoFar


def chatForNRounds(n=5):
    tokenizer, model = loadTokenizerModel(modelName="microsoft/DialoGPT-medium")
    chatHistory = None
    for chatRound in range(n):
        chatHistory = generateResponseForRoundn(tokenizer,model,chatRound,chatHistory)

#generateResponse(tokenizer,model)
chatForNRounds(n=5)
