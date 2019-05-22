import dbl
import asyncio
import logging


class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot, token):
        self.bot = bot
        self.token = token  # set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """This function runs every 30 minutes to automatically
        update your server count"""

        while True:
            logger.info('attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('posted server count ({})'.format(
                    len(self.bot.guilds)))
            except Exception as e:
                logger.exception(
                    'Failed to post server count\n{}: {}'.format(
                        type(e).__name__, e))
            await asyncio.sleep(1800)