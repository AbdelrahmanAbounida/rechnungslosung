from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from dataclasses import  dataclass
from loguru import logger
import inspect
import os 

def read_text_file(file_path:str) -> list[Document]:
    """Reads a text file into langchain Document format"""

    if not os.path.isfile(file_path):
        logger.error(f"File '{file_path}' not found.")
        return ""
    loader = TextLoader(file_path)   
    return loader.load()


def read_class_params_and_methods(class_object: object) -> "ClassDescription":
    """ Read class parameters and methods from the class object 
       and its members params and methods

    Returns:
        ClassDescription: A ClassDescription object containing the class parameters and methods
    """
    class_params = list(inspect.signature(class_object).parameters.keys())
    
    # Get the methods of the class (excluding special methods)
    class_methods = [
        name
        for name, obj in inspect.getmembers(class_object)
        if not name.startswith('__') and inspect.isfunction(obj)
    ]
    members_data = [] # TODO:: do this with the all members too 
    return ClassDescription(params=class_params, methods=class_methods, members=members_data)


@dataclass
class ClassDescription:
    params: list[str] 
    methods: list[str]
    members: list["ClassDescription"]