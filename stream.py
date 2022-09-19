#!/usr/bin/python3

from twitty import *


bot = TwitterBot()


bot.clear_rules()
bot.add_rules('bounty live (defi OR bug OR "$" OR swap OR token OR eth OR nft OR dao OR dex OR finance) followers_count:20 -is:reply -is:retweet')
bot.add_rules('upgraded (defi OR bug OR "$" OR swap OR token OR eth OR nft OR dao OR dex OR finance) followers_count:20 -is:reply -is:retweet')
bot.stream_filter()
