import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23909960"))
    API_HASH = os.environ.get("API_HASH", "20640a09707010d0f9766096804baaf2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8066679823:AAH_wO60kY1FF_DslNWgAyj7xG8DG_oYSNE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu15a_XS4H3rCasu9c16VJvRh3ybemCMVdJLp0drDTvI0ntpScG-tZPufGFfiNKIKXixjeZRCCjhjQMt5fi5aDiB_WoYfIlKJEIvhY-dHRkkEkXIwfF8XiBLbgytIDKiGM-PJIiR8DqdCmg5KGSssFU_-zAHQ5s33XFtomM61JEtUCSYdTGr9f13elgdhUws0z_EIsOeNHfXqpDL6vFIiOpBRvIHxN_BV0I5kOR5uDgDKIP1Ufi59JM90AviRarqtl3oI2Go42u07oXTaw5doM15LsdYum6G_eZeyO3DY0wl8mOXBZPp7alI7ANmPFHSmex_OyaCgwo0lH3dbwJgZPUI=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "saksokralibot")
    SUPPORT = os.environ.get("SUPPORT", "amigotukestestsaksosu") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "amigotukestestsaksosu1") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "8440907397")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
