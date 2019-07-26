from discord.ext import commands
import os
import traceback
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def pubg(ctx, arg):
    ret_text = ""
    # アクセスするURL
    #url = "https://dak.gg/profile/" + arg + "/pc-2018-04/steam"
    url = "https://pubg.op.gg/user/" + arg
    
    # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
    instance = requests.get(url)  

    # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    soup = BeautifulSoup(instance.text, "html.parser")

    # CSSセレクターを使って指定した場所のtextを表示します
    #ret_text1 = "KD:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.kd.stats-item.stats-top-graph > p").text
    ret_text1 = "KD:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(1) > div.ranked-stats__value.ranked-stats__value--imp.ranked-stats__value--good").text
    ret_text1 = ret_text1.replace("\n", "")
    #ret_text2 = "平均ダメージ:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.deals.stats-item.stats-top-graph > p").text 
    
    ret_text2 = "平均ダメージ:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(2) > div.ranked-stats__value.ranked-stats__value--imp.ranked-stats__value--good").text
    ret_text2 = ret_text2.replace("\n", "")
    
    #ret_text3 = "ゲーム数:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.games.stats-item.stats-top-graph > p").text
    ret_text3 = "ゲーム数:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > div > div.ranked-stats__summary > div.ranked-stats__games-count").text
    ret_text3 = ret_text3.replace("\n", "")
    
    #ret_text4 = "最高キル:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.mostkills.stats-item.stats-top-graph > p").text
    ret_text4 = "最高キル:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(10) > div.ranked-stats__value").text
    ret_text4 = ret_text4.replace("\n", "")
    
    ret_text = ret_text1 + "\n" + ret_text2 + "\n" + ret_text3 + "\n" + ret_text4 
    await ctx.send(ret_text.replace(" ", ""))
    await ctx.send(ret_text1.replace(" ", ""))
    await ctx.send(ret_text2.replace(" ", ""))
    await ctx.send(ret_text3.replace(" ", ""))
    await ctx.send(ret_text4.replace(" ", ""))

bot.run(token)
