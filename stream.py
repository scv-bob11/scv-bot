from twitty import *


bot = TwitterBot()


bot.add_rules('bounty live (defi OR bug OR "$" OR swap OR token OR eth OR nft OR dao OR dex OR finance) min_faves:5')
bot.stream_filter()
