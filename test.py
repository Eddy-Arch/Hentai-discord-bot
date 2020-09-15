time = "1m"
if "m" in time:
    print("inital time: " + time)
    bruhstr = time.replace("m", "")
    print(int(bruhstr))
    print(int(bruhstr) * 60)
    asyncio.sleep(int(bruhstr) * 60)
    print(time + "is up")
