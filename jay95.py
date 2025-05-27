import re
pattern="The"
text='''The rapid advancement of artificial intelligence (AI) is transforming industries, reshaping how humans interact with 
technology, and raising ethical concerns. From self-driving cars to intelligent virtual assistants, AI enhances efficiency 
and convenience in everyday life. However, its widespread adoption also sparks debates about job displacement, data privacy, 
and decision-making biases. While AI-powered automation improves productivity, it is crucial to implement regulations and 
ethical guidelines to ensure responsible development. As AI continues to evolve,
striking a balance between innovation and ethical considerations will be key to harnessing its full potential for societal benefit. 
'''
match=re.search(pattern,text)
print(match)