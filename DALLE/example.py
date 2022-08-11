import DALLE, asyncio

dalle = DALLE.DALLE("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
async def main():
    print("Generating images...")
    images = await dalle.generate("Kitten")
    print(images)

asyncio.run(main())