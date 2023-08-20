#Import statements
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv

# load the Environment Variables. 
load_dotenv()

def getResponse(user_input):

    """
    This function takes the user response and returns the response from the LLM
    """

    #This function sets up the chain for use with the LLM, adapted from https://www.youtube.com/watch?v=XBVSve_SvNk
    def chain_setup():

        template = """<|prompter|>{question}<|endoftext|>
        <|assistant|>"""
        
        prompt = PromptTemplate(template=template, input_variables=["question"])

        llm=HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens":1200})

        llm_chain=LLMChain(
            llm=llm,
            prompt=prompt
        )
        return llm_chain


    # generate response
    def generate_response(question, llm_chain):
        response = llm_chain.run(question)
        return response

    ## load LLM
    llm_chain = chain_setup()

    #Get response
    response = generate_response(user_input, llm_chain)

    return response

if __name__ == '__main__':
    getResponse()