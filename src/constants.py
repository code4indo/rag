#EMBEDDING_MODEL_PATH = "microsoft/mpnet-base"  # OR Path of local eg. "embedding_model/"" or the name of SentenceTransformer model eg. "sentence-transformers/all-mpnet-base-v2" from Hugging Face

#EMBEDDING_MODEL_PATH ="/home/jatnikonm/RAG/build_your_local_RAG_system/embedding_model/models--sentence-transformers--all-mpnet-base-v2/snapshots/9a3225965996d404b775526de6dbfe85d3368642"
EMBEDDING_MODEL_PATH ="sentence-transformers/all-mpnet-base-v2"





#/home/jatnikonm/RAG/build_your_local_RAG_system/embedding_model/


ASSYMETRIC_EMBEDDING = False  # Flag for asymmetric embedding
EMBEDDING_DIMENSION = 768  # Embedding model settings
TEXT_CHUNK_SIZE = 300  # Maximum number of characters in each text chunk for

OLLAMA_MODEL_NAME = (
    "modelv3"  # Name of the model used in Ollama for chat functionality
)

####################################################################################################
# Dont change the following settings
####################################################################################################

# Logging
LOG_FILE_PATH = "logs/app.log"  # File path for the application log file
# OpenSearch settings
OPENSEARCH_HOST = "172.16.20.185"  # Hostname for the OpenSearch instance
OPENSEARCH_PORT = 9200  # Port number for OpenSearch
OPENSEARCH_INDEX = "documents"  # Index name for storing documents in OpenSearch
