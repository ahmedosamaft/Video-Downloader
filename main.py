# Import Modules
from pytube import YouTube
from art import *
from Color_Console import ctext
import datetime
# YouTube("https://www.youtube.com/watch?v=UYDw_627QLg&list=PLDlH6NfW8TnBaPG9R4-aLbeB8cvBVdTmD&index=7&t=2s").streams.get_lowest_resolution().download()

# Functions
def length(yt):
  return datetime.timedelta(seconds=yt.length)

def author(yt):
  return yt.author

def title(yt):
  return yt.title

def resolutions(yt):
  videos = yt.streams.filter(file_extension="mp4",only_video=True)
  resolutions = [video.resolution for video in videos]
  return resolutions

def streams(yt):
  return yt.streams.filter(file_extension="mp4",only_video=True)


def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')


# Credentials & Title
Art = text2art("     OSOS\nVideo Downloader", font="cybermedium")
ctext(Art,"red","black")
ctext('=' * 70,"blue","black")
ctext("Made By: Ahmed Osama | FB:www.facebook.com/ahmed.osama.572","white","red")
ctext('=' * 70,"blue","black")


# Prompt URL
while True:
  try: 
    link = input("Please Enter Video URL: ")
    yt = YouTube(link,on_progress)
  except: 
    ctext("URL is Not Correct Check Again Please.","red","black")
  else:
    break

# Show Video Data
ctext('=' * 70,"blue","black")
print("Video Name: ",end="")
ctext(title(yt),"green","black")
print("Video Length: ",end="")
ctext(length(yt),"green","black")
print("Video Author: ",end="")
ctext(author(yt),"green","black")
ctext('=' * 70,"blue","black")

# Show Video Resolutions
print("Available Resolutions: ", end="")
resolutionsList = resolutions(yt)
ctext(" | ".join(resolutionsList),"green","black")
ctext('=' * 70,"blue","black")

# Prompt Resolution
while True:
  try: 
    res = input("Choose a Quality [ex: 720p]: ").lower().strip()
    if(res not in resolutionsList):
      raise ValueError("Not Valid Value")
  except: 
    ctext("Please Choose a Quality From the list Above 👆","red","black")
  else:
    break

# Choose Specific Resolution
for video in streams(yt):
  if video.resolution == res:
    choose = video

# Show Video Size
print("Video Size: ", end='')
ctext(f"{choose.filesize_mb} MB","green","black")
ctext('=' * 70,"blue","black")

# Prompt If Agree On Download?
ch = input("Are you sure to Download? [Y / N] ").upper()

if(ch == "Y"):
  try:
      choose.download()
      ctext("Downloaded Successfully!","green","black")
      ctext("Thanks For Using Downloader 💘❤","white","blue")
  except:
    ctext("Failed to Download 💥👎. Try again!","red","black")
else:
  ctext("Thanks For Using Downloader 💘❤","white","blue")


# Pause Console
input()
