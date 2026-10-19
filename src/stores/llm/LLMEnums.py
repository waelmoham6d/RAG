from enum import Enum


class LLMEnums(Enum):
    GEMINI='GEMINI'
    NVIDIA='NVIDIA'
    OPENAI='OPENAI'
    COHERE='COHERE'



class OpenAIEnums(Enum):
    SYSTEM='system'
    USER='user'
    ASSISTANT='assistant'



class GEMINIEnums(Enum):
    USER = 'user'
    ASSISTANT = 'model'

    DOCUMENT = 'RETRIEVAL_DOCUMENT'
    QUERY = 'RETRIEVAL_QUERY'
    
    
    
class CoHereEnums(Enum):
    SYSTEM='SYSTEM'
    USER='USER'
    ASSISTANT='CHATBOT'
    
    DOCUMENT='search_document'
    QUERY='search_query'



class DocumentTypeEnum(Enum):
    
    DOCUMENT='document'
    QUERY='query'
    
    




