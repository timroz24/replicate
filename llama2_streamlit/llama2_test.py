import os

os.environ["REPLICATE_API_TOKEN"] = "r8_dU2D4sim9RRc7yjhN2Zy4H0Wmqyoz3k2D51I5"

import replicate

pre_prompt = (
    "You are a helpful assistant, you are not the user, you only respond to the user"
)

prompt_input = "What is streamlit?"

output = replicate.run(
    "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
    input={
        "prompt": f" {pre_prompt}{prompt_input} Assistant:",
        "temperature": 0.1,
        "top_p": 0.9,
        "max_length": 128,
        "repetition_penalty": 1,
    },
)

full_response = ""

for item in output:
    full_response += item
print(full_response)
