import requests, asyncio

class DALLE:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://labs.openai.com/api/labs/tasks"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def generate(self, prompt: str):
        body = {
            "task_type": "text2im",
            "prompt": { "caption": prompt, "batch_size": 4 }
        }
        response = requests.post(self.base_url, headers=self.headers, json=body)
        
        if not response.ok:
            raise Exception("Unauthorized. Invalid unique session ID")
        
        data = response.json()
        taskId = data["id"]

        while True:
            response = requests.get(f"{self.base_url}/{taskId}", headers=self.headers)
            if not response.ok:
                raise Exception("Dall-E 2 couldn't generate images based upon your caption")
            data = response.json()
            if data["status"] == "rejected":
                return data["status_information"]
            elif data["status"] == "succeeded":
                return data["generations"]["data"]
            await asyncio.sleep(3)