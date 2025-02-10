import asyncio
from bilibili_api import video, Credential
from bilibili_api import comment, sync
import pandas as pd
import time

SESSDATA = ""
BILI_JCT = ""
BUVID3 = ""



def get_bvid(url):
    
    str_ar = url.split('/')
    bvid_url = str_ar[4]
    alt_id = bvid_url.split('?')
    bvid_id = alt_id[0]
    
    return bvid_id

def get_website(url):
    
    str_ar = url.split('/')
    website = str_ar[2]
    return website
    

def is_bilibili(str):
    
    if(str == "www.bilibili.com"):
         return True
    else:
        return False


    
    
async def get_stats(id,cred,i,df):
    
    await asyncio.sleep(1) 
    
    vid_data = video.Video(bvid=id, credential=cred)
    
    try:
        vid_info = await vid_data.get_info()
    except:
        print("no data")
        stats = [{'view': 0,'like':0,'reply':0}]
    else:
        stats = vid_info['stat']
        df.loc[i,['views']] = stats['view']
        df.loc[i,['likes']] = stats['like']
        df.loc[i,['comments']] = stats['reply']
        print(stats['view'])
        
        
    return stats


  
    
async def main():
    
    
 df = pd.read_csv('newfile_updated_p3.csv')
 cred = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
 


 
 for i in range(0, len(df)):
     url = df.loc[i,"url"]
     web = get_website(url)
     
         
     if(is_bilibili(web) == True):
            
         id = get_bvid(url)
         print(id)
         await asyncio.sleep(1)
         stats = await asyncio.gather(get_stats(id,cred,i,df))
         print(stats)  
         time.sleep(3)
         print(df.loc[i])

 df.to_csv('singfake_updated.csv', index=False)         
         
             
    
    


asyncio.run(main())   
