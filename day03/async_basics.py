import asyncio
import time
async def make_tea():
    print("water on...")
    await asyncio.sleep(3) 
    print("tean ready")
    return "tea"
async def toast():
    print("bread on toaster")    
    await asyncio.sleep(2)
    print("toast is ready")
    return "toast"
async def main():
    # start=time.time()
    # tea=await make_tea()
    # toaster=await toast()
    # print(tea,toaster)
    # print(f"Took {time.time() - start:.1f}s")
    start=time.time()
    tea ,toaster=await asyncio.gather( make_tea(), toast())
    print(tea,toaster)
    print(f"took {time.time()-start:.1f}")
asyncio.run(main())    