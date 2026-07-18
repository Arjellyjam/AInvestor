from google import genai

client = genai.Client()

def aiInput(ticker, yahoo, live):
    respo = client.models.generate_content(
        model="gemini-3.5-flash",
        contents = f"using the ticker symbol, {ticker}, information about the ticker via {yahoo}, and online news via, {live}, generate a report on how the stock may perform and behave in the future. Do not make this financial advice"
    )
    return respo.text