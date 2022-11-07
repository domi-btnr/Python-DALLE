<h1 align="center">Python DALL E</h1>

<div align="center">
<img src="https://img.shields.io/pypi/v/Python-DALLE.svg"/>
<img src="https://img.shields.io/pypi/dm/Python-DALLE.svg"/>
<img src="https://img.shields.io/pypi/pyversions/Python-DALLE.svg"/>
</div>

<p align="center">
Python library for interacting with <a href="https://openai.com/dall-e-2/">OpenAI's Dall-E 2 AI</a>
</p>

# Setup
To get access to Dall-E 2's API you need to join the waitlist and wait to be accepted which can be found [here](https://labs.openai.com/waitlist).

1. To get the your unique session key you need to go to [https://labs.openai.com/](https://labs.openai.com/).
2. Open the Network Tab in Developer Tools in your browser.
3. Send an image request in the input box.
4. In the network tab you'll find a POST request to [https://labs.openai.com/api/labs/tasks](https://labs.openai.com/api/labs/tasks).
5. In the POST request headers you'll find your session key in the "Authorization" header, it'll look something like "sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx".

# Usage
```python
import DALLE, asyncio

dalle = DALLE.DALLE("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
async def main():
    print("Generating images...")
    images = await dalle.generate("Kitten")
    print(images)

asyncio.run(main())
```
### Output
```
[
  {
    id: 'generation-QyXXdJP165TiSpSrzBqAo6IS',
    object: 'generation',
    created: 1659149946,
    generation_type: 'ImageGeneration',
    generation: {
      image_path: 'https://openailabsprodscus.blob.core.windows.net/private/...'
    },
    task_id: 'task-QCKmkq8rxg0ablIgiXizTn0y',
    prompt_id: 'prompt-IN4gE4yFBTi4MPlEG3GzCE4R',
    is_public: false
  },
  {
    id: 'generation-UNJiRu5dzbvJYo8FVnZs5SCS',
    object: 'generation',
    created: 1659149946,
    generation_type: 'ImageGeneration',
    generation: {
      image_path: 'https://openailabsprodscus.blob.core.windows.net/private/...'
    },
    task_id: 'task-QCKmkq8rxg0ablIgiXizTn0y',
    prompt_id: 'prompt-IN4gE4yFBTi4MPlEG3GzCE4R',
    is_public: false
  },
  {
    id: 'generation-XCqpvMF0araPjFczwwfDGHGv',
    object: 'generation',
    created: 1659149946,
    generation_type: 'ImageGeneration',
    generation: {
      image_path: 'https://openailabsprodscus.blob.core.windows.net/private/...'
    },
    task_id: 'task-QCKmkq8rxg0ablIgiXizTn0y',
    prompt_id: 'prompt-IN4gE4yFBTi4MPlEG3GzCE4R',
    is_public: false
  },
  {
    id: 'generation-sSo1TufL7d4OSGEBTwRTMtxv',
    object: 'generation',
    created: 1659149946,
    generation_type: 'ImageGeneration',
    generation: {
      image_path: 'https://openailabsprodscus.blob.core.windows.net/private/...'
    },
    task_id: 'task-QCKmkq8rxg0ablIgiXizTn0y',
    prompt_id: 'prompt-IN4gE4yFBTi4MPlEG3GzCE4R',
    is_public: false
  }
]
```
