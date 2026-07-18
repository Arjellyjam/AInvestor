from google import genai

client = genai.Client()

def aiInput(ticker, yahoo, live):
    respo = client.models.generate_content(
        model="gemini-3.5-flash",
        contents = f"using the ticker symbol, {ticker}, information about the ticker via {yahoo}, and online news via, {live}, generate a report on how the selected stock may advance, and add a summary as to what could happen to the stock over time, and make it informational enough to be of use and benefit to a stock trader. Finally, really limit the amount of words you put, dont regurgitate all the data you receive, and instead make it into facts, bullet points, and a summary that is breif but informational. Make your output format identical everytime. Put a disclaimer that this is not financial advice.")
    return respo.text