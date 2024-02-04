from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
url ='https://www.youtube.com/@JohnWatsonRooney/videos'

driver = webdriver.Chrome()
driver.get(url)

videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-rich-grid-row')
 
video_list = []

for video in videos:
    title = video.find_element(By.XPATH,'.//*[@id="video-title-link"]').text
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text

    vid_item = {
        'title' : title,
        'views' : views,
        'posted' : when

    }

    video_list.append(vid_item)

df = pd.DataFrame(video_list)
print(df)






