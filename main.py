from pytube import YouTube
from art import *
from Color_Console import ctext

def download (yt): 
  return yt.download()

def title(yt):
  return yt.title

def author(yt):
  return yt.author

def streams(yt):
  return yt.streams.filter(file_extension='mp4')

def length(yt):
  return round(yt.length / 60,ndigits=2)

def size(yt,itag):
  return yt.streams.get_by_itag(itag).filesize_mb

def resolutions(yt): 
  res = set([i.resolution for i in streams(yt)])
  arr = [int(i.replace("p","")) for i in res if i in ["1080p", "720p" , "360p", "480p","144p"]]
  arr.sort()
  return arr

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



# link = "https://www.youtube.com/watch?v=ly7OBjYt8s8"


Art=text2art("     OSOS\nVideo Downloader", font="cybermedium")
ctext(Art,"red","black")
ctext('=' * 70,"blue","black")
ctext("Made By: Ahmed Osama | FB:www.facebook.com/ahmed.osama.572","white","red")
ctext('=' * 70,"blue","black")

while(True):
  try:
    link = input("Plese Enter Video URL:")
    yt = YouTube(link,on_progress_callback=on_progress)
    break
  except:
    ctext("URL is Not Correct Check Again Please.","red","black")
    
ctext('=' * 70,"blue","black")
print("Video Name: ",end="")
ctext(f"{title(yt)}","green","black")
print("Video Length: ",end="")
ctext(f"{length(yt)} mins","green","black")
print("\bVideo Author: ",end="")
ctext(f"{author(yt)}","green","black")
ctext('=' * 70,"blue","black")
# https://www.youtube.com/watch?v=UYDw_627QLg&list=PLDlH6NfW8TnBaPG9R4-aLbeB8cvBVdTmD&index=7&t=5s&ab_channel=AhmedOsama
print("Available Resolutions:")
resolution = resolutions(yt)
for i in resolution: 
  if i !=  resolution[len(resolution) - 1]:
    print(f"{i}p | ",end="")
print(f"{resolution[len(resolution) - 1]}p")

while True:
  try:
      quality = int(input("Choose a Quality [ex: 720]: "))
      if(quality not in resolution):
        raise SyntaxError("Not Valid Value")
  except ValueError:
    ctext("Please Choose a Quality Number only like [720]", "red", "black")
  except SyntaxError:
      ctext("Please Choose a Quality From the list Above 👆", "red", "black")
  else :
    break

for i in streams(yt):
  if(f"{quality}p" == i.resolution and i.includes_video_track):
    video = i
    break
print("Video Size: ", end='')
ctext(f"{video.filesize_mb} MB","green","black")

choose = input("Are you sure to Download? [Y / N] ").upper()

if(choose == "Y"):
  try:
    video.download()
    ctext("Downloaded Successfully!","green","black")
    ctext("Thanks For Using Downloader 💘❤","white","blue")
  except:
    ctext("Failed to Download💥👎. Try again!","red","black")
else:
    ctext("Thanks For Using Downloader 💘❤","white","blue")

input()

