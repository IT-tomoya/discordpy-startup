from discord.ext import commands
import discord
import os
import traceback
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
goole = os.environ['GOOGLE_CHROME_BIN']
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
    url = "https://dak.gg/profile/" + arg + "/pc-2018-04/steam"
    
    # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
    instance = requests.get(url)  

    # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    soup = BeautifulSoup(instance.text, "html.parser")

    # CSSセレクターを使って指定した場所のtextを表示します
    ret_text1 = "KD:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.kd.stats-item.stats-top-graph > p").text
    ret_text1 = ret_text1.replace("\n", "")
    ret_text2 = "平均ダメージ：" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.deals.stats-item.stats-top-graph > p").text
    ret_text2 = ret_text2.replace("\n", "")
    ret_text3 = "ゲーム数:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.games.stats-item.stats-top-graph > p").text
    ret_text3 = ret_text3.replace("\n", "")
    ret_text4 = "最高キル:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.mostkills.stats-item.stats-top-graph > p").text
    ret_text4 = ret_text4.replace("\n", "")

    #ret_text1 = "KD:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(1) > div:nth-child(2)").text
    #ret_text2 = "平均ダメージ：" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(2) > div:nth-child(2)").text
    #ret_text3 = "ゲーム数：" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > div > div:nth-child(2) > div:nth-child(1)").text
    #ret_text4 = "最高キル：" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(10) > div.ranked-stats__value").text
    
    ret_text = "プレイヤーネーム：" + arg + "\n" + ret_text1 + ret_text2 + "\n" + ret_text3 + ret_text4 
    await ctx.send(ret_text.replace(" ", ""))

    
    url2 = "https://pubg.op.gg/user/" + arg
    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()
    options.binary_location = goole
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.set_headless(True)

    # ブラウザを起動する
    driver = webdriver.Chrome(options=options)
    # ブラウザでアクセスする
    driver.get(url2)
    
    #driver.find_element_by_class_name("glyphicon glyphicon-refresh").click()
    await ctx.send("さつえいちゅうだよ！！")
    time.sleep(2)
    #driver.find_elements_by_xpath("//*[@id="profile"]/div[1]/div[1]/div/button").click()    
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    if driver.save_screenshot('screenshot.png'):
        #await ctx.send("./images/screenshot.png")
        await ctx.send('てすと', file=discord.File(goole + '/screenshot.png', 'ss.png'))
    else: 
        await ctx.send('さつえいしっぱい' + goole)
    
bot.run(token)
