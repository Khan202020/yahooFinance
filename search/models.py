from django.db import models

TICKER_LIST = (
    ('aapl','AAPL'),
    ('msft', 'MSFT'),
    ('goog','GOOG'),
    ('googl','GOOGL'),
    ('amzn','AMZN'),
    ('tsla','TSLA'),
)

# Create your models here.
class tickersymbol(models.Model):
    ticker = models.CharField(max_length=6, choices=TICKER_LIST, default='aapl')

    def get_absolute_url(self):
        return "tickersymbol/analysis"
