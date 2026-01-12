# import the necessary modules
import os
from pprint import pprint

import openai
from dotenv import load_dotenv, find_dotenv


def get_client() -> openai.OpenAI:
    # load .env file
    load_dotenv(find_dotenv())

    # get api key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set in environment.")
    return openai.OpenAI(api_key=api_key)


def print_section(title: str) -> None:
    print("\n" + "-" * 60)
    print(title)


def create_conversation(client: openai.OpenAI, metadata: dict, items: list):
    print_section("1. Create Conversation:")
    print(f"Topic: {metadata}")
    print(f"Items: {items}")

    # create conversation from OpenAI Conversations API with request parameters topic, type, role and content
    # POST https://api.openai.com/v1/conversations
    conversation = client.conversations.create(metadata=metadata, items=items)        

    # print conversation response
    print("\nAPI RESPONSE:")
    pprint(conversation)    
    return conversation

def list_conversation_items(client: openai.OpenAI, conversation_id: str, limit: int):
    print_section("2. List Items:")
    print(f"id: {conversation_id}")
    print(f"limit: {limit}")

    # get list items from OpenAI Conversations API with request parameters conversation id and limit
    list_items = client.conversations.items.list(conversation_id, limit=10)        
    
    # print conversation response
    print("\nAPI RESPONSE:")
    pprint(list_items.data)
    return list_items

def retrieve_conversation(client: openai.OpenAI, conversation_id: str):
    print_section("3. Retrieve Conversation:")
    print(f"id: {conversation_id}")
    
    # retrieve conversation from OpenAI Conversations API with request parameter conversation id
    retrieve = client.conversations.retrieve(conversation_id)     
    
    # print conversation response
    print("\nAPI RESPONSE:")
    pprint(retrieve)
    return retrieve

def update_conversation(client: openai.OpenAI, conversation_id: str, metadata: dict):
    print_section("4. Update Conversation:")
    print(f"id: {conversation_id}")
    print(f"Topic: {metadata}")
    
    # update conversation from OpenAI Conversations API with request parameters conversation id and metadata
    update = client.conversations.update(
      conversation_id,
      metadata=metadata
    )   
    
    # print conversation response
    print("\nAPI RESPONSE:")
    pprint(update)
    return update

def delete_conversation(client: openai.OpenAI, conversation_id: str):
    print_section("5. Delete Conversation:")
    print(f"id: {conversation_id}")
        
    # delete conversation from OpenAI Conversations API with request parameter conversation id
    delete = client.conversations.delete(conversation_id)  
    
    # print conversation response
    print("\nAPI RESPONSE:")
    pprint(delete)
    return delete

def main() -> None:
    client = get_client()
    metadata = {"topic": "model conversations"}
    items = [{"type": "message", "role": "user", "content": "Hello!"}]

    print("\nDEMO: OPENAI CONVERSATIONS API END-TO-END")
    
    # create conversation
    conversation = create_conversation(client, metadata, items)
    conversation_id = conversation.id

    print("\nCONVERSATION CREATED")
    print(f"CONVERSATION ID:{conversation_id}")
    
    # list items in existing conversation
    limit = 10
    conversation_list_items = list_conversation_items(client, conversation_id, limit)

    print("\nCONVERSATION LIST ITEMS")
    
    # retrieve full conversation details by conversation id
    retrieve = retrieve_conversation(client, conversation_id)
    print("\nCONVERSATION RETRIEVED")
    print(f"CONVERSATION ID:{conversation_id}")

    # update existing conversation metadata
    update_metadata={"topic": "updated model conversations"}
    updated = update_conversation(client, conversation_id, update_metadata)
    print("\nCONVERSATION UPDATED")    

    # delete conversation
    delete = delete_conversation(client, conversation_id)
    print("\nCONVERSATION DELETED")    
    print(f"CONVERSATION ID:{conversation_id}")


if __name__ == "__main__":
    main()
