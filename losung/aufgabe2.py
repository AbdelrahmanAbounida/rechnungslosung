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
    text = read_text_file("assets/45_Visite.txt")
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
    
    logger.success(f"""
                Found {len(rules)} verifiable rules: \n
                    {",".join(rules)}
                """)
    return rules



def prepare_llm_chain(llm_type: Literal["google"] = "google"):
    """
    Prepare the optimized LLM chain for rule extraction with enhanced reliability
    """
    google_api_key = os.environ.get("GOOGLE_GEMINI_APIKEY")
    
    if not google_api_key:
        logger.error("Missing GOOGLE_GEMINI_APIKEY in environment")
        sys.exit(1)

    llm = GoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=google_api_key,
        temperature=0.2,  # Lower temperature for more deterministic output
        max_output_tokens=1000
    )

    template = """Act as a German legal extraction expert. Analyze the legal text and extract ONLY concrete, verifiable rules that can be validated against invoice parameters.

Invoice Parameters Available:
{invoice_params}

Legal Text to Analyze:
{legal_text}

Formatting Rules:
- Return ONLY a comma-separated list
- Each rule must be a complete statement
- Use plain text without quotation marks
- Maximum 10 rules
- No explanatory text
- Must reference concrete invoice parameters

Examples of Valid Responses:
* Maximum 3 consultations per month,Consultation duration must not exceed 30 minutes,Invoice date must be within 30 days of service
* Night surcharge applies after 20:00,Weekend surcharge applies Saturday-Sunday,Emergency fee requires prior authorization

Extracted Rules:"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["invoice_params", "legal_text"]
    )
    
    chain = prompt | llm
    return chain

def extract_rules_from_text(visite_text: str, class_description: str) -> list[str]:
    """
    Robust rule extraction with validation
    """
    chain = prepare_llm_chain()
    response = chain.invoke({
        "invoice_params": class_description,
        "legal_text": visite_text
    })
    
    
    # Robust output cleaning
    clean_output = response.strip().replace("'", "").replace('"', '')
    return [rule.strip() for rule in clean_output.split(",") if rule.strip()]
