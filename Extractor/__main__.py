import asyncio
import importlib
import traceback

from pyrogram import idle

from Extractor import app
from Extractor.modules import ALL_MODULES


async def sumit_boot():

    # Load all modules
    for all_module in ALL_MODULES:
        try:
            importlib.import_module(
                "Extractor.modules." + all_module
            )

            print(f"» Loaded module: {all_module} ✅")

        except Exception as e:
            print(f"» Failed to load module {all_module}: {e}")
            traceback.print_exc()
            raise

    print("» ᴍᴏᴅᴜʟᴇs ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")

    # -----------------------------------------
    # Start main bot
    # -----------------------------------------

    try:
        print("» Starting Telegram bot...")

        await asyncio.wait_for(
            app.start(),
            timeout=60
        )

        print("» Telegram connection established ✅")

    except Exception as e:
        print("» ❌ app.start() FAILED")
        print(f"» Error: {type(e).__name__}: {e}")
        traceback.print_exc()

        try:
            await app.stop()
        except Exception:
            pass

        raise

    # -----------------------------------------
    # Get bot information
    # -----------------------------------------

    try:
        print("» Checking bot account...")

        me = await asyncio.wait_for(
            app.get_me(),
            timeout=20
        )

        print(
            f"» ʙᴏᴛ sᴛᴀʀᴛᴇᴅ: "
            f"@{me.username or me.id} ✅"
        )

    except Exception as e:
        print("» ❌ get_me() FAILED")
        print(f"» Error: {type(e).__name__}: {e}")
        traceback.print_exc()

        try:
            await app.stop()
        except Exception:
            pass

        raise

    # -----------------------------------------
    # Keep bot alive
    # -----------------------------------------

    try:
        print("» Bot is now running... 🚀")
        await idle()

    finally:
        print("» Stopping bot...")

        try:
            await app.stop()
        except Exception:
            pass

        print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    asyncio.run(sumit_boot())
