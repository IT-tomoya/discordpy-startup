from discord.ext import commands
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
    #url = "https://pubg.op.gg/user/" + arg
    
#     # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
#     instance = requests.get(url)  

#     # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
#     soup = BeautifulSoup(instance.text, "html.parser")

#     # CSSセレクターを使って指定した場所のtextを表示します
#     #ret_text1 = "KD:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.kd.stats-item.stats-top-graph > p").text
#     ret_text1 = "KD:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(1) > div:nth-child(2)").text
#     ret_text1 = "KD:" + soup.find_all("div", class_="link", href="/link")
    
#     ret_text1 = ret_text1.replace("\n", "")
#     #ret_text2 = "平均ダメージ:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.deals.stats-item.stats-top-graph > p").text 
    
#     ret_text2 = "平均ダメージ:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(2) > div:nth-child(2)").text
#     ret_text2 = ret_text2.replace("\n", "")
    
#     #ret_text3 = "ゲーム数:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.games.stats-item.stats-top-graph > p").text
#     ret_text3 = "ゲーム数:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > div > div:nth-child(2) > div:nth-child(1)").text
#     ret_text3 = ret_text3.replace("\n", "")
    
#     #ret_text4 = "最高キル:" + soup.select_one("#profile > div.profileContent.season-19.steam > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.mostkills.stats-item.stats-top-graph > p").text
#     ret_text4 = "最高キル:" + soup.select_one("#rankedStatsWrap > div.ranked-stats-wrapper__list > div:nth-child(95) > div > div:nth-child(3) > div > div > div > ul > li:nth-child(10) > div.ranked-stats__value").text
#     ret_text4 = ret_text4.replace("\n", "")

    
#     ret_text = ret_text1 + "\n" + ret_text2 + "\n" + ret_text3 + "\n" + ret_text4 
#     await ctx.send(ret_text.replace(" ", ""))

    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()
    options.binary_location = goole
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.set_headless(True)

    # ブラウザを起動する
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    # ブラウザでアクセスする
    driver.get(url)
    
    driver.findElements(By.xpath("//*[@id="profile"]/div[1]/div[1]/div/button")).click()	
    time.sleep(3)

    instance = requests.get(url)  

    # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    soup = BeautifulSoup(instance.text, "html.parser")
    
    # HTMLを文字コードをUTF-8に変換してから取得します。
    #html = driver.page_source.encode('utf-8')
    
    #soup = BeautifulSoup(html, "html.parser")

    ret_text1 = "KD:" + soup.find_all("div", class_="ranked-stats__value ranked-stats__value--imp ranked-stats__value--good").text
    
    await ctx.send(ret_text1.replace(" ", ""))

bot.run(token)
