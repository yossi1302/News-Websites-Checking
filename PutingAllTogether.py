import json
import GoogleAPI
import NewsScraping
import OpinionUnderstanding

def GetResults(topic, website):
    pos = 0
    neg = 0
    nt = 0
    total = 0
    biggest = 0
    GoogleAPI.ExecuteSearch(topic, website)
    with open("links.json") as r:
        items = json.load(r)
    for item in items:  
        try:
            text = NewsScraping.GetText(item["link"])
            analysis = OpinionUnderstanding.Analyze(text)
            if analysis == 1:
                pos = pos + 1
            if analysis == 0:
                nt = nt + 1
            if analysis == -1:
                neg = neg + 1
            total = total + 1
        except:
            print("couldn't get text")
    pos_precent = int((float(pos)/float(total))*100)
    neg_precent = int((float(neg)/float(total))*100)
    nt_precent = int((float(nt)/float(total))*100)
    if(pos_precent>=neg_precent and pos_precent >= nt_precent):
        return(f"{pos_precent}% of the articles about {topic} in {website} are positive")
    elif(pos_precent<=neg_precent and neg_precent >= nt_precent):
        return(f"{neg_precent}% of the articles about {topic} in {website} are negetive")
    else:
        return(f"{nt_precent}% of the articles about {topic} in {website} are nutral")
