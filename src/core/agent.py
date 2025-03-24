# agent.py
import openai
import logging


def run_agent(config):
    """
    Run a minimal agent that uses OpenAI's ChatCompletion API to verify the config works.
    """
    openai.api_key = config["openai"]["api_key"]

    try:
        logging.info("Testing a simple OpenAI ChatCompletion call...")

        # Use ChatCompletion with a system message and a user prompt.
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, GPT-4! Please say hello back."}
            ],
            max_tokens=50,
            temperature=0.7
        )

        # Extract the assistant's reply from the response.
        text = response.choices[0].message.content.strip()
        logging.info(f"OpenAI response: {text}")

    except Exception as e:
        logging.error(f"Error calling OpenAI API: {e}")
