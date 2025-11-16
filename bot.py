"""Simple Discord bot that sends an @everyone ping when /깨우기 is used."""
from __future__ import annotations

import logging
import os
from typing import Final

import discord
from discord.ext import commands


LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

COMMAND_PREFIX: Final[str] = "/"
WAKE_COMMAND_NAME: Final[str] = "깨우기"


def build_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

    @bot.event
    async def on_ready() -> None:
        LOGGER.info("Logged in as %s (id=%s)", bot.user, bot.user and bot.user.id)

    @bot.command(name=WAKE_COMMAND_NAME)
    @commands.has_permissions(mention_everyone=True)
    async def wake(ctx: commands.Context[commands.Bot]) -> None:
        """Delete the invoking message and ping @everyone."""
        await ctx.message.delete()
        await ctx.send(
            "@everyone",
            allowed_mentions=discord.AllowedMentions(everyone=True),
        )

    @wake.error
    async def wake_error_handler(
        ctx: commands.Context[commands.Bot],
        error: commands.CommandError,
    ) -> None:
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                "@everyone 핑을 보낼 권한이 없어요!",
                delete_after=5,
            )
        else:
            LOGGER.exception("Unhandled error while running /%s", WAKE_COMMAND_NAME, exc_info=error)
            await ctx.send("명령 실행 중 문제가 발생했어요.", delete_after=5)

    return bot


def main() -> None:
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN 환경 변수를 설정해주세요.")

    bot = build_bot()
    bot.run(token)


if __name__ == "__main__":
    main()
