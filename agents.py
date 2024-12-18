import dspy
import os
gpt4o = dspy.LM('openai/gpt-4o', api_key=os.getenv('OPENAI_API_KEY'), temperature=0.7)
dspy.configure(lm=gpt4o)




