from twitty import *


bot = TwitterBot()


bot.add_rules('bounty live (defi OR bug OR "$" OR swap OR token OR eth OR nft OR dao OR dex OR finance) followers_count:20')
bot.add_rules('upgraded (defi OR bug OR "$" OR swap OR token OR eth OR nft OR dao OR dex OR finance) followers_count:20')
bot.stream_filter()
