"""
# Auggabe2:
Identification of Verifiable Rules from Legal Texts
-  review text (45_Visite.txt) and extract passages that define rules that can be checked based on invoice data.
-  Some rules can be verified using invoice attributes (e.g., checking the number of consultations per day).
-  Other rules cannot be verified if they require information that is not present in the invoice (e.g., checking what exactly happened during a consultation).

result :
List of rules that can be verified


Approach:
- Solution1 : AI Agent that get an access to our Rechnung Codebase and loop over the text chunks 
and return a list of rules that can be verified
- Solution2 : Simple LLM Call with a prompt listing these rules 
- solution3: Simple Regex Check with NLTK/Spacy
"""
from losung.utils import read_text_file, read_class_params_and_methods
from rechnungen.rechnung import Rechnung
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from loguru import logger
from typing import Literal
import sys
import os 

def task2():
    # 1- Read visite_45 file text
    logger.info("Reading visite_45")
    text = read_text_file("files/45_Visite.txt")
    if not text:
        logger.error("Error: Could not read the file. Please Check that assets/45_Visite.txt file exist ")
        return

    # 2- read our Rechnung class description (params, methods)
    logger.info("Reading Rechnung class description")
    class_data = read_class_params_and_methods(Rechnung) 
    class_description = f""" 
        params: {class_data.params}
        methods: {class_data.methods}
    """

    # 3- Extract rules from the text according to our Rechnung class description 
    logger.info("Extracting rules from the Visite text")
    rules = extract_rules_from_text(text, class_description)
    if not rules:
        logger.error("No verifiable rules found")
    
    logger.success(f"\n ✅ Found {len(rules)} verifiable rules:\n" + "\n".join([f"  - {rule}" for rule in rules]))

    return rules



def prepare_llm_chain(llm_type: Literal["google"] = "google"):
    """
    Prepare the LLM chain we are going to use to extract verifiable rules.
    """

    google_api_key = os.environ.get("GOOGLE_GEMINI_APIKEY", "")

    if not google_api_key:
        logger.error("GOOGLE_GEMINI_APIKEY not found in your .env")
        sys.exit(1)

    if llm_type == "google":
        try:
            llm = GoogleGenerativeAI(
                model="gemini-1.5-flash", 
                google_api_key=google_api_key, 
                temperature=0.7
            )
        except Exception as e:
            logger.error(f"Failed to initialize Google LLM: {str(e)}")
            sys.exit(1)
    else:
        logger.error("Invalid LLM type. Only 'google' is supported for now.")
        sys.exit(1)

    # This prompt could be improved and more dynamic
    template = """
        You are a legal German expert assistant tasked with extracting verifiable rules from the following legal text.
        A rule is verifiable if it can be confirmed using invoice params and attributes (e.g., date, number of consultations).
        Identify only the verifiable rules.

        NOTES:
        - Only extract rules that can be verified using invoice params and attributes.
        - Your output should be a list of rules in a comma-separated format.
        - Do not include anything other than the list of verifiable rules.
        - Sample output format: 'rule1', 'rule2', 'rule3', ...

        ----------
        Sample Invoice Params, data:
        {invoice_params}
        
        ---------
        Legal text:
        {legal_text}
        ---------

        Extracted List of Rules:
    """

    # Initialize the PromptTemplate using the template
    prompt = PromptTemplate.from_template(template)
    
    # Chain the prompt with LLM
    chain = prompt | llm
    return chain

def extract_rules_from_text(visite_text: str, class_description: str) -> list[str]:
    """
    Extract a list of verifiable rules from the provided legal text according to the class description.
    """
    
    # Get the LLM chain
    chain = prepare_llm_chain()  # Optionally, you can pass a custom llm_type here if needed
    
    # Prepare the input for the LLM
    input_data = {
        "invoice_params": class_description,
        "legal_text": visite_text
    }

    # Invoke the chain and extract the rules
    try:
        response = chain.invoke(input_data)
    except Exception as e:
        logger.error(f"Error invoking LLM chain: {str(e)}")
        return []

    # Ensure response is a comma-separated string
    if isinstance(response, str):
        # Parse the comma-separated list of rules
        rules = [rule.strip() for rule in response.split(',') if rule.strip()]
    else:
        logger.error("Unexpected response format from LLM chain")
        return []

    return rules