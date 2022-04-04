from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import tickersymbol
from .forms import searchform
import yfinance as yf
import plotly.graph_objects as go
import plotly.offline as opy
import plotly.express as px

# Create your views here.
class TickerSearch(CreateView):
    model = tickersymbol
    template_name = 'search/searchPage.html'
    form_class = searchform


def Analysis(request):
    stock = tickersymbol.objects.last()
    yahoo_stock = yf.Ticker(stock.ticker)
    revenue = yahoo_stock.quarterly_earnings['Revenue']
    earnings = yahoo_stock.quarterly_earnings['Earnings']
    distribution = yahoo_stock.major_holders
    df =  yahoo_stock.history(period="1mo")
    old = df.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']: 
        old[i]  =  old[i].astype('float64')

    fig = go.Figure(data=[go.Candlestick(x=old['Date'],open=old['Open'],high=old['High'],low=old['Low'],close=old['Close'])])
    graph = opy.plot(fig, auto_open=False, output_type='div')
    linefig = px.line(old, x="Date", y="Open", title='Stock Prices')
    linegraph = opy.plot(linefig, auto_open=False, output_type='div')
    content = { 'ask' : yahoo_stock.info['ask'],
                'bid' : yahoo_stock.info['bid'],
                'spread' : round(yahoo_stock.info['ask'] - yahoo_stock.info['bid'],2),
                'name' : yahoo_stock.info['shortName'],
                'sector' : yahoo_stock.info['sector'],
                'employees' : yahoo_stock.info['fullTimeEmployees'],
                'description' : yahoo_stock.info['longBusinessSummary'],
                'pegratio' : yahoo_stock.info['pegRatio'],
                'pricetobook' : round(yahoo_stock.info['priceToBook'],2),
                'trailingpe' : round(yahoo_stock.info['trailingPE'],2),
                'forwardpe' : round(yahoo_stock.info['forwardPE'],2),
                's1' : distribution[0][0],
                's2' : distribution[0][1],
                's3' : distribution[0][2],
                's4' : distribution[0][3],
                's5' : distribution[1][0],
                's6' : distribution[1][1],
                's7' : distribution[1][2],
                's8' : distribution[1][3],
                'graph' : graph,
                'linegraph' : linegraph,
                'revenue' : '{:20,.2f}'.format(revenue[0] + revenue[1] + revenue[2] + revenue[3]),
                'earnings' : '{:20,.2f}'.format(earnings[0] + earnings[1] + earnings[2] + earnings[3])}
    return render(request, 'search/resultPage.html', content)




