from .LLMEnums import LLMEnums
from .providers import OpenAIProvider,CoHereProvider,GeminiProvider,NvidiaProvider


class LLMProviderFactory:
    def __init__(self,config: dict):
        self.config=config
        
    def create(self,Provider: str):
        if Provider==LLMEnums.OPENAI.value:
            return OpenAIProvider(
                api_key=self.config.OPENAI_API_KEY,
                api_url=self.config.OPENAI_API_URL,
                default_max_input_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generatoin_max_output_tokens=self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURE
            )
            
        if Provider==LLMEnums.NVIDIA.value:
            return NvidiaProvider(
                api_key=self.config.NVIDIA_API_KEY,
                api_url=self.config.NVIDIA_API_URL,
                default_max_input_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generatoin_max_output_tokens=self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURE
            )
            
        if Provider==LLMEnums.GEMINI.value:
            return GeminiProvider(
                api_key=self.config.GEMINI_API_KEY,
                api_url=self.config.GEMINI_API_URL,
                default_max_input_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generatoin_max_output_tokens=self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURE
            )
            
         
        if Provider==LLMEnums.COHERE.value:
            return CoHereProvider(
                api_key=self.config.COHERE_API_KEY,
                default_input_max_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens=self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURE
            )
            
            
        return None
