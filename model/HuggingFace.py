from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1-Distill-Llama-8B")
model = ChatHuggingFace(llm=llm)
res = model.invoke("How are you?")
print(res.content)

