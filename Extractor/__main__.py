import asyncio
import importlib

from pyrogram import idle

from Extractor import app
from Extractor.modules import ALL_MODULES


async def sumit_boot():

    # -----------------------------------------------------
    # Load all modules first
    # This registers all message/callback handlers
    # -----------------------------------------------------

    for all_module in ALL_MODULES:
        try:
            importlib.import_module(
                "Extractor.modules." + all_module
            )

            print(
                f"» Loaded module: {all_module} ✅"
            )

        except Exception as e:
            print(
                f"» Failed to load module "
                f"{all_module}: {e}"
            )
            raise

    print(
        "» ᴍᴏᴅᴜʟᴇs ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅"
    )

    # -----------------------------------------------------
    # Start bot after all handlers are registered
    # -----------------------------------------------------

    await app.start()

    me = await app.get_me()

    print(
        f"» ʙᴏᴛ sᴛᴀʀᴛᴇᴅ: "
        f"@{me.username or me.id} ✅"
    )

    # -----------------------------------------------------
    # Keep bot running
    # -----------------------------------------------------

    await idle()

    # -----------------------------------------------------
    # Stop bot cleanly
    # -----------------------------------------------------

    await app.stop()

    print(
        "» ɢᴏᴏᴅ ʙʏᴇ ! "
        "sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ."
    )


if __name__ == "__main__":
    asyncio.run(sumit_boot())
